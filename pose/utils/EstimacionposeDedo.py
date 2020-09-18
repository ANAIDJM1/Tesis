import numpy as np
import math

from pose.utils.Dedo import Dedo
from pose.utils.CurvaDedo import CurvaDeDedo
from pose.utils.PosicionDedo import PosicionDedo

#estimacion del la pose del Dedo
class FingerPoseEstimate:
    def __init__(self, coords_xyz):
        self.coords_xyz = np.squeeze(coords_xyz)
        self.finger_position = [PosicionDedo.HaciaArriba, PosicionDedo.HaciaArriba,
                                PosicionDedo.HaciaArriba, PosicionDedo.HaciaArriba,
                                PosicionDedo.HaciaArriba]
        self.finger_curled = [CurvaDeDedo.NoCurva, CurvaDeDedo.NoCurva, CurvaDeDedo.NoCurva,
                             CurvaDeDedo.NoCurva, CurvaDeDedo.NoCurva,]
        self.slopes_xy = []
        self.slopes_yz = []

    #obtener pendiente punto a punto con la ecuacion basica m=(y2-y2)/(x2-x1)
    def get_slope(self, point1, point2):
        slope_xy = self._calculate_slope_procedure(point1[0], point1[1], point2[0], point2[1])
        if len(point1) == 2:
            return slope_xy

        slope_yz = self._calculate_slope_procedure(point1[1], point1[2], point2[1], point2[2])
        return slope_xy, slope_yz

    #CAlcular la pendiente de los dedos
    def calculate_slope_of_fingers(self):
        for finger in Dedo:

            points = Dedo.get_array_of_points(finger)
            slope_at_xy, slope_at_yz = [], []
            for point in points:
                point1 = self.coords_xyz[point[0]]
                point2 = self.coords_xyz[point[1]]
                slope_xy, slope_yz = self.get_slope(point1, point2)
                slope_at_xy.append(slope_xy)
                slope_at_yz.append(slope_yz)

            self.slopes_xy.append(slope_at_xy)
            self.slopes_yz.append(slope_at_yz)

    #calcular el angulo de orientacion
    def angle_orientation_at(self, angle, weightage_at = 1.0):
        is_vertical, is_diagonal, is_horizontal = 0, 0, 0
        if angle >= 75.0 and angle <= 105.0:
            is_vertical = 1 * weightage_at
        elif angle >= 25.0 and angle <= 155.0:
            is_diagonal = 1 * weightage_at
        else:
            is_horizontal = 1 * weightage_at
        return (is_vertical, is_diagonal, is_horizontal)

    #modulo para calcular el rizado o curvatura del dedo
    def is_finger_curled(self, start_point, mid_point, end_point):
        start_mid_x_dist = start_point[0] - mid_point[0]
        start_end_x_dist = start_point[0] - end_point[0]
        mid_end_x_dist = mid_point[0] - end_point[0]
        
        start_mid_y_dist = start_point[1] - mid_point[1]
        start_end_y_dist = start_point[1] - end_point[1]
        mid_end_y_dist = mid_point[1] - end_point[1]

        start_mid_z_dist = start_point[2] - mid_point[2]
        start_end_z_dist = start_point[2] - end_point[2]
        mid_end_z_dist = mid_point[2] - end_point[2]
        
        start_mid_dist = math.sqrt(start_mid_x_dist ** 2 + start_mid_y_dist ** 2 + start_mid_z_dist ** 2)
        start_end_dist = math.sqrt(start_end_x_dist ** 2 + start_end_y_dist ** 2 + start_end_z_dist ** 2)
        mid_end_dist = math.sqrt(mid_end_x_dist ** 2 + mid_end_y_dist ** 2 + mid_end_z_dist ** 2)
        
        cos_in = (mid_end_dist ** 2 + start_mid_dist ** 2 - start_end_dist ** 2) \
                        / (2 * mid_end_dist * start_mid_dist)
        if cos_in > 1.0:
            cos_in = 1.0
        elif cos_in < -1.0:
            cos_in = -1.0
        angle_of_curve = math.acos(cos_in)
        angle_of_curve =  (57.2958 * angle_of_curve) % 180
        

        HALF_CURL_START_LIMIT = 60.0
        NO_CURL_START_LIMIT = 130.0
        
        finger_curled = None
        if angle_of_curve > NO_CURL_START_LIMIT:
            finger_curled = CurvaDeDedo.NoCurva
        elif angle_of_curve > HALF_CURL_START_LIMIT:
            finger_curled = CurvaDeDedo.MediaCurva
        else:
            finger_curled = CurvaDeDedo.FullCurva
            
        return finger_curled

    #modulo para definir si va a la derecha o izquierda horizontal sin angulo
    def estimate_horizontal_direction(self, start_end_x_dist, start_mid_x_dist, mid_end_x_dist, max_dist_x):
        reqd_direction = None
        if max_dist_x == abs(start_end_x_dist):
            if start_end_x_dist > 0:
                reqd_direction = PosicionDedo.ApuntaIzquierda
            else:
                reqd_direction = PosicionDedo.ApuntaDerecha
        elif max_dist_x == abs(start_mid_x_dist):
            if start_mid_x_dist > 0:
                reqd_direction = PosicionDedo.ApuntaIzquierda
            else:
                reqd_direction = PosicionDedo.ApuntaDerecha
        else:
            if mid_end_x_dist > 0:
                reqd_direction = PosicionDedo.ApuntaIzquierda
            else:
                reqd_direction = PosicionDedo.ApuntaDerecha
        return reqd_direction

    # modulo para definir si apunta haciaa arriba o abajo verticalmente sin angulo
    def estimate_vertical_direction(self, start_end_y_dist, start_mid_y_dist, mid_end_y_dist, max_dist_y):
        reqd_direction = None
        if max_dist_y == abs(start_end_y_dist):
            if start_end_y_dist < 0:
                reqd_direction = PosicionDedo.HaciaAbajo
            else:
                reqd_direction = PosicionDedo.HaciaArriba
        elif max_dist_y == abs(start_mid_y_dist):
            if start_mid_y_dist < 0:
                reqd_direction = PosicionDedo.HaciaAbajo
            else:
                reqd_direction = PosicionDedo.HaciaArriba
        else:
            if mid_end_y_dist < 0:
                reqd_direction = PosicionDedo.HaciaAbajo
            else:
                reqd_direction = PosicionDedo.HaciaArriba
        return reqd_direction

    #Modulo que estima la direccion de la diagonal del dedo
    def estimate_diagonal_direction(self, start_end_y_dist, start_mid_y_dist, mid_end_y_dist, max_dist_y,\
                                   start_end_x_dist, start_mid_x_dist, mid_end_x_dist, max_dist_x):
        reqd_direction = None
        reqd_vertical_direction = self.estimate_vertical_direction(start_end_y_dist,
                                                                   start_mid_y_dist, 
                                                                   mid_end_y_dist, max_dist_y)
        reqd_horizontal_direction = self.estimate_horizontal_direction(start_end_x_dist,
                                                                       start_mid_x_dist,
                                                                       mid_end_x_dist, max_dist_x)
        

        if reqd_vertical_direction == PosicionDedo.HaciaArriba:
            if reqd_horizontal_direction == PosicionDedo.ApuntaIzquierda:
                reqd_direction = PosicionDedo.EsquinaIzquierda
            else:
                reqd_direction = PosicionDedo.EsquinaDerecha
        else:
            if reqd_horizontal_direction == PosicionDedo.ApuntaIzquierda:
                reqd_direction = PosicionDedo.EsquinaInfIzquierda
            else:
                reqd_direction = PosicionDedo.EsquinaInfDerecha
        return reqd_direction

    #modulo para calcular hacia donde apunta el dedo
    def calculate_direction_of_finger(self, start_point, mid_point, end_point, finger_slopes):
        start_mid_x_dist = start_point[0] - mid_point[0]
        start_end_x_dist = start_point[0] - end_point[0]
        mid_end_x_dist = mid_point[0] - end_point[0]
        
        start_mid_y_dist = start_point[1] - mid_point[1]
        start_end_y_dist = start_point[1] - end_point[1]
        mid_end_y_dist = mid_point[1] - end_point[1]

        max_dist_x = max(abs(start_mid_x_dist), abs(start_end_x_dist), abs(mid_end_x_dist))
        max_dist_y = max(abs(start_mid_y_dist), abs(start_end_y_dist), abs(mid_end_y_dist))
            
        DISTANCE_VOTE_POWER = 1.1
        SINGLE_ANGLE_VOTE_POWER = 0.9
        TOTAL_ANGLE_VOTE_POWER = 1.6
        
        vote_vertical, vote_diagonal, vote_horizontal = 0.0, 0.0, 0.0
        start_end_x_y_dist_ratio = max_dist_y / (max_dist_x + 0.00001)
        if start_end_x_y_dist_ratio > 1.5:
            vote_vertical += DISTANCE_VOTE_POWER
        elif start_end_x_y_dist_ratio > 0.66:
            vote_diagonal += DISTANCE_VOTE_POWER
        else:
            vote_horizontal += DISTANCE_VOTE_POWER

        start_mid_dist = math.sqrt(start_mid_x_dist ** 2 + start_mid_y_dist ** 2)
        start_end_dist = math.sqrt(start_end_x_dist ** 2 + start_end_y_dist ** 2)
        mid_end_dist = math.sqrt(mid_end_x_dist ** 2 + mid_end_y_dist ** 2)
        
        max_dist = max(start_mid_dist, start_end_dist, mid_end_dist)
        calc_start_point_x, calc_start_point_y = start_point[0], start_point[1]
        calc_end_point_x, calc_end_point_y = end_point[0], end_point[1]
        if max_dist == start_mid_dist:
            calc_end_point_x, calc_end_point_y = end_point[0], end_point[1]
        elif max_dist == mid_end_dist:
            calc_start_point_x, calc_start_point_y = mid_point[0], mid_point[1]
            
        calc_start_point = (calc_start_point_x, calc_start_point_y)
        calc_end_point = (calc_end_point_x, calc_end_point_y)

        total_angle = self.get_slope(calc_start_point, calc_end_point)
        vote1, vote2, vote3 = self.angle_orientation_at(total_angle, weightage_at = TOTAL_ANGLE_VOTE_POWER)
        vote_vertical += vote1
        vote_diagonal += vote2
        vote_horizontal += vote3
        #print('Iteration 2: Total Angle = {:.3f}, ({}, {}, {})'.format(total_angle, vote1, vote2, vote3))
        
        for finger_slope in finger_slopes:
            vote1, vote2, vote3 = self.angle_orientation_at(finger_slope, weightage_at = SINGLE_ANGLE_VOTE_POWER)
            vote_vertical += vote1
            vote_diagonal += vote2
            vote_horizontal += vote3
            #print('Iteration 3: Total Angle = {:.3f}, ({}, {}, {})'.format(finger_slope, vote1, vote2, vote3))
        #print('Total weights: ({}, {}, {})'.format(vote_vertical, vote_diagonal, vote_horizontal))
        
        # En caso de empate va priorizar Vertical, seguida de horizontal y luego diagonal.
        reqd_direction = None
        if vote_vertical == max(vote_vertical, vote_diagonal, vote_horizontal):
            reqd_direction = self.estimate_vertical_direction(start_end_y_dist,
                                                              start_mid_y_dist, 
                                                              mid_end_y_dist, max_dist_y)
        elif vote_horizontal == max(vote_diagonal, vote_horizontal):
            reqd_direction = self.estimate_horizontal_direction(start_end_x_dist,
                                                                start_mid_x_dist,
                                                                mid_end_x_dist, max_dist_x)
        else:
            reqd_direction = self.estimate_diagonal_direction(start_end_y_dist, start_mid_y_dist,
                                                              mid_end_y_dist, max_dist_y,
                                                              start_end_x_dist, start_mid_x_dist,
                                                              mid_end_x_dist, max_dist_x)
        #print('Vote at {}, {}, {}'.format(vote_vertical, vote_diagonal, vote_horizontal))
        return reqd_direction
    
    def calculate_orientation_of_fingers(self, print_finger_info):
        for finger in Dedo:
            point_index_at = 0
            if finger == Dedo.Pulgar:
                point_index_at = 1
            angle_at = self.slopes_xy[finger][point_index_at]
            
            finger_points_at = Dedo.get_array_of_points(finger)
            start_point_at = self.coords_xyz[finger_points_at[point_index_at][0]]
            mid_point_at = self.coords_xyz[finger_points_at[point_index_at + 1][1]]
            end_point_at = self.coords_xyz[finger_points_at[3][1]]
            
            finger_curled = self.is_finger_curled(start_point_at, mid_point_at, end_point_at)

            finger_position = self.calculate_direction_of_finger(start_point_at, mid_point_at, end_point_at,
                                                                 self.slopes_xy[finger][point_index_at:])
            #print('Finger: {} = {}'.format(Finger.get_finger_name(finger),
            #                              PosicionDedo.get_finger_position_name(finger_position)))
            
            self.finger_curled[finger] = finger_curled
            self.finger_position[finger] = finger_position

        if print_finger_info:
            for finger_index, curl, pos in zip(Dedo, self.finger_curled, self.finger_position):
                print('Dedo: {}, Curva: {}, Orientacion: {}'.format(
                        Dedo.get_finger_name(finger_index), CurvaDeDedo.get_finger_curled_name(curl),
                        PosicionDedo.get_finger_position_name(pos)))


    def calculate_positions_of_fingers(self, print_finger_info):
        self.calculate_slope_of_fingers()
        self.calculate_orientation_of_fingers(print_finger_info)

    
    # Private methods
    def _calculate_slope_procedure(self, point1_x, point1_y, point2_x, point2_y):
        value = (point1_y - point2_y) / (point1_x - point2_x)
        slope = math.degrees(math.atan(value))
        if slope < 0 or slope == -0.0:
            slope = -slope
        elif slope > 0:
            slope = 180 - slope
        return slope

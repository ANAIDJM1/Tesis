from enum import IntEnum

class Dedo(IntEnum):
    Pulgar = 0
    Index = 1
    Medio = 2
    Anular = 3
    Menhique = 4
    
    @staticmethod
    def obtener_array_puntos(finger):
        finger_array = None
        if finger == Dedo.Pulgar:
            finger_array = [(0, 4), (4, 3), (3, 2), (2, 1)]
        elif finger == Dedo.Index:
            finger_array = [(0, 8), (8, 7), (7, 6), (6, 5)]
        elif finger == Dedo.Medio:
            finger_array = [(0, 12), (12, 11), (11, 10), (10, 9)]
        elif finger == Dedo.Anular:
            finger_array = [(0, 16), (16, 15), (15, 14), (14, 13)]
        else:
            finger_array = [(0, 20), (20, 19), (19, 18), (18, 17)]
        return finger_array
    
    @staticmethod
    def obtener_nombre_dedo(finger):
        finger_name = ''
        if finger == Dedo.Pulgar:
            finger_name = 'Pulgar'
        elif finger == Dedo.Index:
            finger_name = 'Indice'
        elif finger == Dedo.Medio:
            finger_name = 'Medio'
        elif finger == Dedo.Anular:
            finger_name = 'Anular'
        elif finger == Dedo.Menhique:
            finger_name = 'Meñique'
        return finger_name
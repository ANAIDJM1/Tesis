from enum import IntEnum

class CurvaDeDedo(IntEnum):
    NoCurva = 0
    MediaCurva = 1
    FullCurva = 2
    
    @staticmethod
    def get_finger_curled_name(finger_curled):
        finger_curled_name = ''
        if finger_curled == CurvaDeDedo.NoCurva:
            finger_curled_name = 'No Curva'
        elif finger_curled == CurvaDeDedo.MediaCurva:
            finger_curled_name = 'Medio Curveado'
        elif finger_curled == CurvaDeDedo.FullCurva:
            finger_curled_name = 'Full Curva'
        return finger_curled_name
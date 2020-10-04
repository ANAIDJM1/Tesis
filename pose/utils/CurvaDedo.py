from enum import IntEnum

class CurvaDeDedo(IntEnum):
    NoCurva = 0
    MediaCurva = 1
    FullCurva = 2
    
    @staticmethod
    def get_nombre_curvatura_dedo(curvatura_dedo):
        nombre_curvatura_dedo = ''
        if curvatura_dedo == CurvaDeDedo.NoCurva:
            nombre_curvatura_dedo = 'No Curva'
        elif curvatura_dedo == CurvaDeDedo.MediaCurva:
            nombre_curvatura_dedo = 'Medio Curveado'
        elif curvatura_dedo == CurvaDeDedo.FullCurva:
            nombre_curvatura_dedo = 'Full Curva'
        return nombre_curvatura_dedo
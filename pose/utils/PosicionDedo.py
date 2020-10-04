from enum import IntEnum

class PosicionDedo(IntEnum):
    HaciaArriba = 0
    HaciaAbajo = 1
    ApuntaIzquierda = 2
    ApuntaDerecha = 3
    EsquinaDerecha = 4
    EsquinaIzquierda = 5
    EsquinaInfDerecha = 6
    EsquinaInfIzquierda = 7
    
    @staticmethod
    def get_nombre_posicion_dedo(posicion_dedo):
        if posicion_dedo == PosicionDedo.HaciaArriba:
            direccion_dedo = 'Hacia Arriba'
        elif posicion_dedo == PosicionDedo.HaciaAbajo:
            direccion_dedo = 'Hacia Abajo'
        elif posicion_dedo == PosicionDedo.ApuntaIzquierda:
            direccion_dedo = 'Apunta a la Izquierda'
        elif posicion_dedo == PosicionDedo.ApuntaDerecha:
            direccion_dedo = 'Apunta a la Derecha'
        elif posicion_dedo == PosicionDedo.EsquinaDerecha:
            direccion_dedo = 'Apunta a la esquina superior Derecha'
        elif posicion_dedo == PosicionDedo.EsquinaIzquierda:
            direccion_dedo = 'Apunta a la esquina superior Izquierda'
        elif posicion_dedo == PosicionDedo.EsquinaInfDerecha:
            direccion_dedo = 'Apunta a la esquina Inferior Derecha'
        elif posicion_dedo == PosicionDedo.EsquinaInfIzquierda:
            direccion_dedo = 'Apunta a la esquina Inferior Izquierda'
        return direccion_dedo
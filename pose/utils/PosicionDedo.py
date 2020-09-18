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
    def get_finger_position_name(finger_position):
        if finger_position == PosicionDedo.HaciaArriba:
            finger_type = 'Hacia Arriba'
        elif finger_position == PosicionDedo.HaciaAbajo:
            finger_type = 'Hacia Abajo'
        elif finger_position == PosicionDedo.ApuntaIzquierda:
            finger_type = 'Apunta a la Izquierda'
        elif finger_position == PosicionDedo.ApuntaDerecha:
            finger_type = 'Apunta a la Derecha'
        elif finger_position == PosicionDedo.EsquinaDerecha:
            finger_type = 'Apunta a la esquina superior Derecha'
        elif finger_position == PosicionDedo.EsquinaIzquierda:
            finger_type = 'Apunta a la esquina superior Izquierda'
        elif finger_position == PosicionDedo.EsquinaInfDerecha:
            finger_type = 'Apunta a la esquina Inferior Derecha'
        elif finger_position == PosicionDedo.EsquinaInfIzquierda:
            finger_type = 'Apunta a la esquina Inferior Izquierda'
        return finger_type
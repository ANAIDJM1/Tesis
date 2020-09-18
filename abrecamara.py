from __future__ import print_function, unicode_literals
PATH=('/home/any/Imágenes/tesis')
import argparse
import cv2


#abre la camara
video_captura = cv2.VideoCapture(0)


while(True):
    # Captura frame-por-frame
    ret, frame = video_captura.read()

    # =======TOOOOOOOOODAS LAS OPERACION CON EL FRAM VIENEN AQUI==============
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # muestra el resultado del frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# cuando too esta hecho, libera y destruye ventana
video_captura.release()
cv2.destroyAllWindows()

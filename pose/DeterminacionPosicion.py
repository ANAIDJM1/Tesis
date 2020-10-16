from pose.utils.CurvaDedo import CurvaDeDedo
from pose.utils.PosicionDedo import PosicionDedo
from pose.utils.FormaciondedatosDedos import DataFormacionDedo


def determinar_posicion(posiciones_curvatura, posiciones_dedo, posiciones_dedo_conocidas, min_threshold):
    posicion_obtenida = {}

    for pose_dedo in posiciones_dedo_conocidas:
        score_at = 0.0
        for curva_conocida, determinacion_curva_conocida, curva_dada in \
                zip(pose_dedo.curva_posicion, pose_dedo.curva_posicion_determinacion, posiciones_curvatura):
            if len(curva_conocida) == 0:
                if len(determinacion_curva_conocida) == 1:
                    score_at += determinacion_curva_conocida[0]
                    continue

            if curva_dada in curva_conocida:
                confidence_at = curva_conocida.index(curva_dada)
                score_at += determinacion_curva_conocida[confidence_at]

        for posicion_conocida, determinacion_pose_conocida, pose_dada in \
                zip(pose_dedo.dedo_posicion, pose_dedo.determinacion_posicion_dedo, posiciones_dedo):
            if len(posicion_conocida) == 0:
                if len(determinacion_pose_conocida) == 1:
                    score_at += determinacion_pose_conocida[0]
                    continue

            if pose_dada in posicion_conocida:
                confidence_at = posicion_conocida.index(pose_dada)
                score_at += determinacion_pose_conocida[confidence_at]

        if score_at >= min_threshold:
            posicion_obtenida[pose_dedo.nombre_posicion] = score_at

    return posicion_obtenida


def get_nombrePosicion_id(pose_id, poses_dedo):
    for pose_dedo in poses_dedo:
        if pose_dedo.posicion_id == pose_id:
            return pose_dedo.nombre_posicion
    return None


def crear_poses_conocidasDedos():
    poses_dedo_conocidas = []

    #LETRAS DEL ABECEDARIO EXCEPTUANDO LA "J" Y LA "Z"
    ####### A id =0
    letra_a = DataFormacionDedo()
    letra_a.nombre_posicion = 'A'
    letra_a.curva_posicion = [
        [CurvaDeDedo.NoCurva],  # Pulgar
        [CurvaDeDedo.FullCurva],  # Index
        [CurvaDeDedo.FullCurva],  # Medio
        [CurvaDeDedo.FullCurva],  # Anular
        [CurvaDeDedo.FullCurva]  # Menhique
    ]
    letra_a.curva_posicion_determinacion = [
        [1.0],  # Pulgar
        [1.0],  # Index
        [1.0],  # Medio
        [1.0],  # Anular
        [1.0]  # Menhique
    ]
    letra_a.dedo_posicion = [
        [PosicionDedo.EsquinaIzquierda, PosicionDedo.HaciaArriba],  # Pulgar
        [PosicionDedo.HaciaArriba],  # Index
        [PosicionDedo.HaciaArriba],  # Medio
        [PosicionDedo.HaciaArriba],  # Anular
        [PosicionDedo.HaciaArriba]  # Menhique
    ]
    letra_a.determinacion_posicion_dedo = [
        [1.0,0.5],  # Pulgar
        [1.0],  # Index
        [1.0],  # Medio
        [1.0],  # Anular
        [1.0]  # Menhique
    ]
    letra_a.posicion_id = 0
    poses_dedo_conocidas.append(letra_a)

    ####### B id =1
    letra_b = DataFormacionDedo()
    letra_b.nombre_posicion = 'B'
    letra_b.curva_posicion = [
        [CurvaDeDedo.NoCurva],  # Pulgar
        [CurvaDeDedo.NoCurva],  # Index
        [CurvaDeDedo.NoCurva],  # Medio
        [CurvaDeDedo.NoCurva],  # Anular
        [CurvaDeDedo.NoCurva]  # Menhique
    ]
    letra_b.curva_posicion_determinacion = [
        [1.0],  # Pulgar
        [1.0],  # Index
        [1.0],  # Medio
        [1.0],  # Anular
        [1.0]  # Menhique
    ]
    letra_b.dedo_posicion = [
        [PosicionDedo.EsquinaDerecha, PosicionDedo.HaciaArriba],  # Pulgar
        [PosicionDedo.HaciaArriba],  # Index
        [PosicionDedo.HaciaArriba],  # Medio
        [PosicionDedo.HaciaArriba],  # Anular
        [PosicionDedo.HaciaArriba]  # Menhique
    ]
    letra_b.determinacion_posicion_dedo = [
        [1.0, 1.0],  # Pulgar
        [1.0],  # Index
        [1.0],  # Medio
        [1.0],  # Anular
        [1.0]  # Menhique
    ]
    letra_b.posicion_id = 1
    poses_dedo_conocidas.append(letra_b)

    ####### C id =2
    letra_c = DataFormacionDedo()
    letra_c.nombre_posicion = 'C'
    letra_c.curva_posicion = [
        [CurvaDeDedo.NoCurva],  # Pulgar
        [CurvaDeDedo.MediaCurva, CurvaDeDedo.NoCurva],  # Index
        [CurvaDeDedo.MediaCurva, CurvaDeDedo.NoCurva],  # Medio
        [CurvaDeDedo.MediaCurva, CurvaDeDedo.NoCurva],  # Anular
        [CurvaDeDedo.MediaCurva, CurvaDeDedo.NoCurva]  # Menhique
    ]
    letra_c.curva_posicion_determinacion = [
        [1.0],  # Pulgar
        [1.0, 1.0],  # Index
        [1.0, 1.0],  # Medio
        [1.0, 1.0],  # Anular
        [1.0, 1.0]  # Menhique
    ]
    letra_c.dedo_posicion = [
        [PosicionDedo.ApuntaIzquierda],  # Pulgar
        [PosicionDedo.ApuntaIzquierda],  # Index
        [PosicionDedo.ApuntaIzquierda],  # Medio
        [PosicionDedo.ApuntaIzquierda, PosicionDedo.EsquinaIzquierda],  # Anular
        [PosicionDedo.ApuntaIzquierda, PosicionDedo.EsquinaIzquierda]  # Menhique
    ]
    letra_c.determinacion_posicion_dedo = [
        [1.0],  # Pulgar
        [1.0],  # Index
        [1.0],  # Medio
        [1.0, 1.0],  # Anular
        [1.0, 1.0]  # Menhique
    ]
    letra_c.posicion_id = 2
    poses_dedo_conocidas.append(letra_c)

    ####### D id =3
    letra_d = DataFormacionDedo()
    letra_d.nombre_posicion = 'D'
    letra_d.curva_posicion = [
        [CurvaDeDedo.NoCurva,CurvaDeDedo.MediaCurva],  # Pulgar
        [CurvaDeDedo.NoCurva],  # Index
        [CurvaDeDedo.MediaCurva, CurvaDeDedo.FullCurva],  # Medio
        [CurvaDeDedo.MediaCurva, CurvaDeDedo.FullCurva],  # Anular
        [CurvaDeDedo.MediaCurva, CurvaDeDedo.FullCurva]  # Menhique
    ]
    letra_d.curva_posicion_determinacion = [
        [1.0,0.5],  # Pulgar
        [1.0],  # Index
        [1.0, 0.3],  # Medio
        [1.0, 0.3],  # Anular
        [1.0, 0.3]  # Menhique
    ]
    letra_d.dedo_posicion = [
        [PosicionDedo.EsquinaIzquierda],  # Pulgar
        [PosicionDedo.HaciaArriba],  # Index
        [PosicionDedo.ApuntaIzquierda ,PosicionDedo.EsquinaInfIzquierda],  # Medio
        [PosicionDedo.ApuntaIzquierda ,PosicionDedo.EsquinaInfIzquierda],  # Anular
        [PosicionDedo.ApuntaIzquierda ,PosicionDedo.EsquinaInfIzquierda]  # Menhique
    ]
    letra_d.determinacion_posicion_dedo = [
        [1.0],  # Pulgar
        [1.0],  # Index
        [1.0,1.0],  # Medio
        [1.0,1.0],  # Anular
        [1.0,1.0]  # Menhique
    ]
    letra_d.posicion_id = 3
    poses_dedo_conocidas.append(letra_d)

    ####### E id =4
    letra_e = DataFormacionDedo()
    letra_e.nombre_posicion = 'E'
    letra_e.curva_posicion = [
        [CurvaDeDedo.FullCurva, CurvaDeDedo.MediaCurva],#Pulgar
        [CurvaDeDedo.FullCurva, CurvaDeDedo.MediaCurva],  # Index
        [CurvaDeDedo.FullCurva, CurvaDeDedo.MediaCurva],  # Medio
        [CurvaDeDedo.FullCurva, CurvaDeDedo.MediaCurva],  # Anular
        [CurvaDeDedo.FullCurva, CurvaDeDedo.MediaCurva]   # Menhique
    ]
    letra_e.curva_posicion_determinacion = [
        [1.0,0.5],  # Pulgar
        [1.0,0.5],  # Index
        [1.0,0.5],  # Medio
        [1.0,0.5],  # Anular
        [1.0,0.5]  # Menhique
    ]
    letra_e.dedo_posicion = [
        [PosicionDedo.HaciaArriba,PosicionDedo.ApuntaDerecha],  # Pulgar
        [PosicionDedo.EsquinaIzquierda,PosicionDedo.HaciaArriba],  # Index
        [PosicionDedo.HaciaArriba,PosicionDedo.EsquinaIzquierda],  # Medio
        [PosicionDedo.HaciaArriba,PosicionDedo.EsquinaIzquierda],  # Anular
        [PosicionDedo.HaciaArriba,PosicionDedo.EsquinaIzquierda]  # Menhique
    ]
    letra_e.determinacion_posicion_dedo = [
        [1.0,0.5],  # Pulgar
        [1.0,0.5],  # Index
        [1.0,0.5],  # Medio
        [1.0,0.5],  # Anular
        [1.0,0.5]  # Menhique
    ]
    letra_e.posicion_id = 4
    poses_dedo_conocidas.append(letra_e)

    ####### F id =5
    letra_f = DataFormacionDedo()
    letra_f.nombre_posicion = 'F'
    letra_f.curva_posicion = [
        [CurvaDeDedo.FullCurva,CurvaDeDedo.MediaCurva],  # Pulgar
        [CurvaDeDedo.FullCurva,CurvaDeDedo.MediaCurva],  # Index
        [CurvaDeDedo.NoCurva],  # Medio
        [CurvaDeDedo.NoCurva],  # Anular
        [CurvaDeDedo.NoCurva]  # Menhique
    ]
    letra_f.curva_posicion_determinacion = [
        [1.0,1.0],  # Pulgar
        [1.0,1.0],  # Index
        [1.0],  # Medio
        [1.0],  # Anular
        [1.0]  # Menhique
    ]
    letra_f.dedo_posicion = [
        [PosicionDedo.EsquinaIzquierda],  # Pulgar
        [PosicionDedo.HaciaArriba],  # Index
        [PosicionDedo.HaciaArriba,PosicionDedo.EsquinaDerecha],  # Medio
        [PosicionDedo.HaciaArriba,PosicionDedo.EsquinaDerecha],  # Anular
        [PosicionDedo.HaciaArriba,PosicionDedo.EsquinaDerecha]  # Menhique
    ]
    letra_f.determinacion_posicion_dedo = [
        [1.0],  # Pulgar
        [1.0],  # Index
        [0.5,1.0],  # Medio
        [0.5,1.0],  # Anular
        [0.5,1.0]  # Menhique
    ]
    letra_f.posicion_id = 5
    poses_dedo_conocidas.append(letra_f)

    ####### G id =6
    letra_g = DataFormacionDedo()
    letra_g.nombre_posicion = 'G'
    letra_g.curva_posicion = [
        [CurvaDeDedo.NoCurva],  # Pulgar
        [CurvaDeDedo.NoCurva],  # Index
        [CurvaDeDedo.FullCurva],  # Medio
        [CurvaDeDedo.FullCurva],  # Anular
        [CurvaDeDedo.FullCurva]  # Menhique
    ]
    letra_g.curva_posicion_determinacion = [
        [1.0],  # Pulgar
        [1.0],  # Index
        [1.0],  # Medio
        [1.0],  # Anular
        [1.0]  # Menhique
    ]
    letra_g.dedo_posicion = [
        [PosicionDedo.HaciaArriba, PosicionDedo.ApuntaIzquierda],  # Pulgar
        [PosicionDedo.HaciaArriba, PosicionDedo.ApuntaIzquierda],  # Index
        [PosicionDedo.EsquinaIzquierda],  # Medio
        [PosicionDedo.EsquinaIzquierda],  # Anular
        [PosicionDedo.ApuntaIzquierda]  # Menhique
    ]
    letra_g.determinacion_posicion_dedo = [
        [1.0, 1.0],  # Pulgar
        [1.0, 1.0],  # Index
        [1.0],  # Medio
        [1.0],  # Anular
        [1.0]  # Menhique
    ]
    letra_g.posicion_id = 6
    poses_dedo_conocidas.append(letra_g)

    ####### H id =7
    letra_h = DataFormacionDedo()
    letra_h.nombre_posicion = 'H'
    letra_h.curva_posicion = [
        [CurvaDeDedo.MediaCurva,CurvaDeDedo.NoCurva],  # Pulgar
        [CurvaDeDedo.NoCurva],  # Index
        [CurvaDeDedo.NoCurva],  # Medio
        [CurvaDeDedo.FullCurva,CurvaDeDedo.MediaCurva],  # Anular
        [CurvaDeDedo.FullCurva,CurvaDeDedo.MediaCurva]  # Menhique
    ]
    letra_h.curva_posicion_determinacion = [
        [1.0,1.0],  # Pulgar
        [1.0],  # Index
        [1.0],  # Medio
        [0.8,1.0],  # Anular
        [0.8,1.0]  # Menhique
    ]
    letra_h.dedo_posicion = [
        [PosicionDedo.EsquinaIzquierda,PosicionDedo.ApuntaIzquierda],  # Pulgar
        [PosicionDedo.ApuntaIzquierda,PosicionDedo.EsquinaIzquierda],  # Index
        [PosicionDedo.ApuntaIzquierda,PosicionDedo.EsquinaIzquierda],  # Medio
        [PosicionDedo.ApuntaIzquierda,PosicionDedo.EsquinaIzquierda],  # Anular
        [PosicionDedo.ApuntaIzquierda,PosicionDedo.EsquinaIzquierda]  # Menhique
    ]
    letra_h.determinacion_posicion_dedo = [
        [1.0,1.0],  # Pulgar
        [0.8,1.0],  # Index
        [0.8,1.0],  # Medio
        [0.8,1.0],  # Anular
        [0.8,1.0]  # Menhique
    ]
    letra_h.posicion_id = 7
    poses_dedo_conocidas.append(letra_h)

    ####### I id =8
    letra_i = DataFormacionDedo()
    letra_i.nombre_posicion = 'I'
    letra_i.curva_posicion = [
        [CurvaDeDedo.MediaCurva, CurvaDeDedo.NoCurva],  # Pulgar
        [CurvaDeDedo.MediaCurva, CurvaDeDedo.FullCurva],  # Index
        [CurvaDeDedo.MediaCurva, CurvaDeDedo.FullCurva],  # Medio
        [CurvaDeDedo.MediaCurva, CurvaDeDedo.FullCurva],  # Anular
        [CurvaDeDedo.NoCurva]  # Menhique
    ]
    letra_i.curva_posicion_determinacion = [
        [1.0,1.0],  # Pulgar
        [1.0,1.0],  # Index
        [1.0,1.0],  # Medio
        [1.0,1.0],  # Anular
        [1.0]  # Menhique
    ]
    letra_i.dedo_posicion = [
        [PosicionDedo.EsquinaIzquierda],  # Pulgar
        [PosicionDedo.ApuntaIzquierda, PosicionDedo.EsquinaIzquierda],  # Index
        [PosicionDedo.ApuntaIzquierda, PosicionDedo.EsquinaIzquierda],  # Medio
        [PosicionDedo.ApuntaIzquierda, PosicionDedo.EsquinaIzquierda],  # Anular
        [PosicionDedo.HaciaArriba, PosicionDedo.EsquinaDerecha]  # Menhique
    ]
    letra_i.determinacion_posicion_dedo = [
        [1.0],  # Pulgar
        [1.0, 1.0],  # Index
        [1.0, 1.0],  # Medio
        [1.0, 1.0],  # Anular
        [1.0,0.25]  # Menhique
    ]
    letra_i.posicion_id = 8
    poses_dedo_conocidas.append(letra_i)

    ####### k id =9
    letra_k = DataFormacionDedo()
    letra_k.nombre_posicion = 'K'
    letra_k.curva_posicion = [
        [CurvaDeDedo.NoCurva],  # Pulgar
        [CurvaDeDedo.NoCurva],  # Index
        [CurvaDeDedo.NoCurva],  # Menhique
        [CurvaDeDedo.MediaCurva,CurvaDeDedo.FullCurva],  # Medio
        [CurvaDeDedo.MediaCurva,CurvaDeDedo.FullCurva]  # Anular
    ]
    letra_k.curva_posicion_determinacion = [
        [1.0],  # Pulgar
        [1.0],  # Index
        [1.0],  # Medio
        [1.0,1.0],  # Anular
        [1.0,1.0]  # Menhique
    ]
    letra_k.dedo_posicion = [
        [PosicionDedo.HaciaArriba],  # Pulgar
        [PosicionDedo.EsquinaIzquierda,PosicionDedo.ApuntaIzquierda],  # Index
        [PosicionDedo.EsquinaIzquierda,PosicionDedo.ApuntaIzquierda],  # Medio
        [PosicionDedo.EsquinaIzquierda,PosicionDedo.EsquinaInfIzquierda],  # Anular
        [PosicionDedo.EsquinaIzquierda,PosicionDedo.EsquinaInfIzquierda]  # Menhique
    ]
    letra_k.determinacion_posicion_dedo = [
        [1.0],  # Pulgar
        [1.0,0.5],  # Index
        [1.0,1.0],  # Medio
        [1.0,0.8],  # Anular
        [1.0,0.8]  # Menhique
    ]
    letra_k.posicion_id = 9
    poses_dedo_conocidas.append(letra_k)

    ####### L id =10
    letra_l = DataFormacionDedo()
    letra_l.nombre_posicion = 'L'
    letra_l.curva_posicion = [
        [CurvaDeDedo.NoCurva],  # Pulgar
        [CurvaDeDedo.NoCurva],  # Index
        [CurvaDeDedo.MediaCurva,CurvaDeDedo.FullCurva],  # Medio
        [CurvaDeDedo.MediaCurva,CurvaDeDedo.FullCurva],  # Anular
        [CurvaDeDedo.MediaCurva,CurvaDeDedo.FullCurva]  # Menhique
    ]
    letra_l.curva_posicion_determinacion = [
        [1.0],  # Pulgar
        [1.0],  # Index
        [1.0,0.5],  # Medio
        [1.0,0.5],  # Anular
        [1.0,0.5]  # Menhique
    ]
    letra_l.dedo_posicion = [
        [PosicionDedo.EsquinaIzquierda, PosicionDedo.ApuntaIzquierda],  # Pulgar
        [PosicionDedo.EsquinaDerecha,PosicionDedo.HaciaArriba],  # Index
        [PosicionDedo.EsquinaIzquierda,PosicionDedo.HaciaArriba],  # Medio
        [PosicionDedo.EsquinaIzquierda,PosicionDedo.HaciaArriba],  # Anular
        [PosicionDedo.EsquinaIzquierda,PosicionDedo.HaciaArriba]  # Menhique
    ]
    letra_l.determinacion_posicion_dedo = [
        [1.0,1.0],  # Pulgar
        [1.0,1.0],  # Index
        [1.0,1.0],  # Medio
        [1.0,1.0],  # Anular
        [1.0,1.0]  # Menhique
    ]
    letra_l.posicion_id = 10
    poses_dedo_conocidas.append(letra_l)

    ####### M id =11
    letra_m = DataFormacionDedo()
    letra_m.nombre_posicion = 'M'
    letra_m.curva_posicion = [
        [CurvaDeDedo.FullCurva],  # Pulgar
        [CurvaDeDedo.NoCurva],  # Index
        [CurvaDeDedo.NoCurva],  # Medio
        [CurvaDeDedo.NoCurva],  # Anular
        [CurvaDeDedo.FullCurva]  # Menhique
    ]
    letra_m.curva_posicion_determinacion = [
        [1.0],  # Pulgar
        [1.0],  # Index
        [1.0],  # Medio
        [1.0],  # Anular
        [1.0]  # Menhique
    ]
    letra_m.dedo_posicion = [
        [PosicionDedo.HaciaAbajo, PosicionDedo.EsquinaInfDerecha],  # Pulgar
        [PosicionDedo.HaciaAbajo],  # Index
        [PosicionDedo.HaciaAbajo],  # Medio
        [PosicionDedo.HaciaAbajo],  # Anular
        [PosicionDedo.EsquinaInfIzquierda, PosicionDedo.HaciaAbajo]  # Menhique
    ]
    letra_m.determinacion_posicion_dedo = [
        [1.0, 1.0],  # Pulgar
        [1.0],  # Index
        [1.0],  # Medio
        [1.0],  # Anular
        [1.0, 1.0]  # Menhique
    ]
    letra_m.posicion_id = 11
    poses_dedo_conocidas.append(letra_m)

    ####### N id =12
    letra_n = DataFormacionDedo()
    letra_n.nombre_posicion = 'N'
    letra_n.curva_posicion = [
        [CurvaDeDedo.FullCurva, CurvaDeDedo.MediaCurva],  # Pulgar
        [CurvaDeDedo.NoCurva],  # Index
        [CurvaDeDedo.NoCurva],  # Medio
        [CurvaDeDedo.FullCurva, CurvaDeDedo.MediaCurva],  # Anular
        [CurvaDeDedo.FullCurva, CurvaDeDedo.MediaCurva]  # Menhique
    ]
    letra_n.curva_posicion_determinacion = [
        [1.0,1.0],  # Pulgar
        [1.0],  # Index
        [1.0],  # Medio
        [1.0,1.0],  # Anular
        [1.0,1.0]  # Menhique
    ]
    letra_n.dedo_posicion = [
        [PosicionDedo.HaciaAbajo, PosicionDedo.EsquinaInfDerecha],  # Pulgar
        [PosicionDedo.HaciaAbajo],  # Index
        [PosicionDedo.HaciaAbajo],  # Medio
        [PosicionDedo.HaciaAbajo, PosicionDedo.EsquinaIzquierda],  # Anular
        [PosicionDedo.HaciaAbajo, PosicionDedo.EsquinaIzquierda]  # Menhique
    ]
    letra_n.determinacion_posicion_dedo = [
        [1.0,1.0],  # Pulgar
        [1.0],  # Index
        [1.0],  # Medio
        [1.0,0.8],  # Anular
        [1.0,0.8]  # Menhique
    ]
    letra_n.posicion_id = 12
    poses_dedo_conocidas.append(letra_n)

    ####### O id =13
    letra_o = DataFormacionDedo()
    letra_o.nombre_posicion = 'O'
    letra_o.curva_posicion = [
        [CurvaDeDedo.NoCurva],  # Pulgar
        [CurvaDeDedo.MediaCurva],  # Index
        [CurvaDeDedo.MediaCurva],  # Medio
        [CurvaDeDedo.MediaCurva],  # Anular
        [CurvaDeDedo.NoCurva]  # Menhique
    ]
    letra_o.curva_posicion_determinacion = [
        [1.0],  # Pulgar
        [1.0],  # Index
        [1.0],  # Medio
        [1.0],  # Anular
        [1.0]  # Menhique
    ]
    letra_o.dedo_posicion = [
        [PosicionDedo.HaciaArriba, PosicionDedo.EsquinaIzquierda],  # Pulgar
        [PosicionDedo.HaciaArriba, PosicionDedo.EsquinaIzquierda],  # Index
        [PosicionDedo.HaciaArriba, PosicionDedo.EsquinaIzquierda],  # Medio
        [PosicionDedo.HaciaArriba, PosicionDedo.EsquinaIzquierda],  # Anular
        [PosicionDedo.HaciaArriba, PosicionDedo.EsquinaIzquierda]  # Menhique
    ]
    letra_o.determinacion_posicion_dedo = [
        [1.0, 1.0],  # Pulgar
        [1.0, 1.0],  # Index
        [1.0, 1.0],  # Medio
        [1.0, 1.0],  # Anular
        [1.0, 1.0]  # Menhique
    ]
    letra_o.posicion_id = 13
    poses_dedo_conocidas.append(letra_o)

    ####### P id =14
    letra_p = DataFormacionDedo()
    letra_p.nombre_posicion = 'P'
    letra_p.curva_posicion = [
        [CurvaDeDedo.NoCurva],  # Pulgar
        [CurvaDeDedo.NoCurva],  # Index
        [CurvaDeDedo.NoCurva],  # Medio
        [CurvaDeDedo.NoCurva],  # Anular
        [CurvaDeDedo.NoCurva,CurvaDeDedo.MediaCurva]  # Menhique
    ]
    letra_p.curva_posicion_determinacion = [
        [1.0],  # Pulgar
        [1.0],  # Index
        [1.0],  # Medio
        [1.0],  # Anular
        [1.0,1.0 ] # Menhique
    ]
    letra_p.dedo_posicion = [
        [PosicionDedo.HaciaAbajo,PosicionDedo.EsquinaInfDerecha],  # Pulgar
        [PosicionDedo.HaciaAbajo,PosicionDedo.EsquinaInfIzquierda],  # Index
        [PosicionDedo.HaciaAbajo,PosicionDedo.EsquinaInfIzquierda],  # Medio
        [PosicionDedo.HaciaAbajo,PosicionDedo.EsquinaInfDerecha],  # Anular
        [PosicionDedo.HaciaAbajo,PosicionDedo.EsquinaInfDerecha]  # Menhique
    ]
    letra_p.determinacion_posicion_dedo = [
        [1.0, 1.0],  # Pulgar
        [1.0, 1.0],  # Index
        [1.0, 1.0],  # Medio
        [1.0, 1.0],  # Anular
        [1.0, 1.0]  # Menhique
    ]
    letra_p.posicion_id = 14
    poses_dedo_conocidas.append(letra_p)

    ####### Q id =15
    letra_q = DataFormacionDedo()
    letra_q.nombre_posicion = 'Q'
    letra_q.curva_posicion = [
        [CurvaDeDedo.NoCurva],  # Pulgar
        [CurvaDeDedo.NoCurva, CurvaDeDedo.MediaCurva],  # Index
        [CurvaDeDedo.MediaCurva],  # Medio
        [CurvaDeDedo.MediaCurva],  # Anular
        [CurvaDeDedo.MediaCurva]  # Menhique
    ]
    letra_q.curva_posicion_determinacion = [
        [1.0],  # Pulgar
        [1.0, 1.0],  # Index
        [1.0],  # Medio
        [1.0],  # Anular
        [1.0]  # Menhique
    ]
    letra_q.dedo_posicion = [
        [PosicionDedo.HaciaAbajo, PosicionDedo.EsquinaInfIzquierda],  # Pulgar
        [PosicionDedo.HaciaAbajo, PosicionDedo.EsquinaInfIzquierda],  # Index
        [PosicionDedo.HaciaAbajo, PosicionDedo.ApuntaDerecha],  # Medio
        [PosicionDedo.HaciaAbajo, PosicionDedo.ApuntaDerecha],  # Anular
        [PosicionDedo.HaciaAbajo, PosicionDedo.ApuntaDerecha]  # Menhique
    ]
    letra_q.determinacion_posicion_dedo = [
        [1.0, 1.0],  # Pulgar
        [1.0, 1.0],  # Index
        [1.0, 1.0],  # Medio
        [1.0, 1.0],  # Anular
        [1.0, 1.0]  # Menhique
    ]
    letra_q.posicion_id = 15
    poses_dedo_conocidas.append(letra_q)

    ####### R id =16
    letra_r = DataFormacionDedo()
    letra_r.nombre_posicion = 'R'
    letra_r.curva_posicion = [
        [CurvaDeDedo.NoCurva],  # Pulgar
        [CurvaDeDedo.NoCurva],  # Index
        [CurvaDeDedo.NoCurva],  # Medio
        [CurvaDeDedo.NoCurva, CurvaDeDedo.MediaCurva],  # Anular
        [CurvaDeDedo.NoCurva, CurvaDeDedo.MediaCurva]  # Menhique
    ]
    letra_r.curva_posicion_determinacion = [
        [1.0],  # Pulgar
        [1.0],  # Index
        [1.0],  # Medio
        [1.0,1.0],  # Anular
        [1.0,1.0]  # Menhique
    ]
    letra_r.dedo_posicion = [
        [PosicionDedo.EsquinaDerecha, PosicionDedo.HaciaArriba],  # Pulgar
        [PosicionDedo.HaciaArriba, PosicionDedo.EsquinaDerecha],  # Index
        [PosicionDedo.HaciaArriba, PosicionDedo.EsquinaIzquierda],  # Medio
        [PosicionDedo.EsquinaInfIzquierda,PosicionDedo.HaciaArriba],  # Anular
        [PosicionDedo.EsquinaInfIzquierda,PosicionDedo.HaciaArriba]  # Menhique
    ]
    letra_r.determinacion_posicion_dedo = [
        [1.0,1.0],  # Pulgar
        [1.0,1.0],  # Index
        [1.0,1.0],  # Medio
        [1.0,1.0],  # Anular
        [1.0,1.0]  # Menhique
    ]
    letra_r.posicion_id = 16
    poses_dedo_conocidas.append(letra_r)

    ####### S id =17
    letra_s = DataFormacionDedo()
    letra_s.nombre_posicion = 'S'
    letra_s.curva_posicion = [
        [CurvaDeDedo.NoCurva,CurvaDeDedo.MediaCurva],  # Pulgar
        [CurvaDeDedo.MediaCurva,CurvaDeDedo.FullCurva],  # Index
        [CurvaDeDedo.MediaCurva,CurvaDeDedo.FullCurva],  # Medio
        [CurvaDeDedo.MediaCurva,CurvaDeDedo.FullCurva],  # Anular
        [CurvaDeDedo.MediaCurva,CurvaDeDedo.FullCurva]  # Menhique
    ]
    letra_s.curva_posicion_determinacion = [
        [1.0,1.0],  # Pulgar
        [1.0,1.0],  # Index
        [1.0,1.0],  # Medio
        [1.0,1.0],  # Anular
        [1.0,1.0]  # Menhique
    ]
    letra_s.dedo_posicion = [
        [PosicionDedo.EsquinaDerecha, PosicionDedo.ApuntaDerecha],  # Pulgar
        [PosicionDedo.HaciaArriba,PosicionDedo.EsquinaInfIzquierda],  # Index
        [PosicionDedo.HaciaArriba,PosicionDedo.EsquinaInfIzquierda],  # Medio
        [PosicionDedo.HaciaArriba, PosicionDedo.EsquinaInfIzquierda],  # Anular
        [PosicionDedo.HaciaArriba, PosicionDedo.EsquinaInfIzquierda]  # Menhique
    ]
    letra_s.determinacion_posicion_dedo = [
        [1.0,1.0],  # Pulgar
        [1.0,1.0],  # Index
        [1.0,1.0],  # Medio
        [1.0, 1.0],  # Anular
        [1.0, 1.0]  # Menhique
    ]
    letra_s.posicion_id = 17
    poses_dedo_conocidas.append(letra_s)

    ####### T id =18
    letra_t = DataFormacionDedo()
    letra_t.nombre_posicion = 'T'
    letra_t.curva_posicion = [
        [CurvaDeDedo.NoCurva],  # Pulgar
        [CurvaDeDedo.MediaCurva,CurvaDeDedo.NoCurva],  # Index
        [CurvaDeDedo.FullCurva,CurvaDeDedo.MediaCurva],  # Medio
        [CurvaDeDedo.FullCurva,CurvaDeDedo.MediaCurva],  # Anular
        [CurvaDeDedo.FullCurva,CurvaDeDedo.MediaCurva]  # Menhique
    ]
    letra_t.curva_posicion_determinacion = [
        [1.0],  # Pulgar
        [1.0,1.0],  # Index
        [1.0,1.0],  # Medio
        [1.0,1.0],  # Anular
        [1.0,1.0]  # Menhique
    ]
    letra_t.dedo_posicion = [
        [PosicionDedo.HaciaArriba],  # Pulgar
        [PosicionDedo.ApuntaIzquierda,PosicionDedo.EsquinaIzquierda],  # Index
        [PosicionDedo.EsquinaIzquierda],  # Medio
        [PosicionDedo.EsquinaIzquierda],  # Anular
        [PosicionDedo.EsquinaIzquierda]  # Menhique
    ]
    letra_t.determinacion_posicion_dedo = [
        [1.0],  # Pulgar
        [1.0,1.0],  # Index
        [1.0],  # Medio
        [1.0],  # Anular
        [1.0]  # Menhique
    ]
    letra_t.posicion_id = 18
    poses_dedo_conocidas.append(letra_t)

    ####### U id =19
    letra_u = DataFormacionDedo()
    letra_u.nombre_posicion = 'U'
    letra_u.curva_posicion = [
        [CurvaDeDedo.NoCurva],  # Pulgar
        [CurvaDeDedo.NoCurva],  # Index
        [CurvaDeDedo.MediaCurva,CurvaDeDedo.NoCurva],  # Medio
        [CurvaDeDedo.MediaCurva,CurvaDeDedo.NoCurva],  # Anular
        [CurvaDeDedo.NoCurva]  # Menhique
    ]
    letra_u.curva_posicion_determinacion = [
        [1.0],  # Pulgar
        [1.0],  # Index
        [1.0,1.0],  # Medio
        [1.0,1.0],  # Anular
        [1.0]  # Menhique
    ]
    letra_u.dedo_posicion = [
        [PosicionDedo.EsquinaDerecha,PosicionDedo.HaciaArriba],  # Thumb
        [PosicionDedo.HaciaArriba,PosicionDedo.EsquinaDerecha],  # Index
        [PosicionDedo.EsquinaIzquierda,PosicionDedo.HaciaArriba],  # Middle
        [PosicionDedo.EsquinaIzquierda,PosicionDedo.HaciaArriba],  # Ring
        [PosicionDedo.HaciaArriba,PosicionDedo.EsquinaIzquierda]  # Little
    ]
    letra_u.determinacion_posicion_dedo = [
        [1.0,1.0],  # Pulgar
        [1.0,1.0],  # Index
        [1.0,1.0],  # Medio
        [1.0,1.0],  # Anular
        [1.0,1.0]  # Menhique
    ]
    letra_u.posicion_id = 19
    poses_dedo_conocidas.append(letra_u)

    ###### V id =20
    letra_v = DataFormacionDedo()
    letra_v.nombre_posicion = 'V'
    letra_v.curva_posicion = [
        [CurvaDeDedo.NoCurva, CurvaDeDedo.MediaCurva],  # Pulgar
        [CurvaDeDedo.NoCurva],  # Index
        [CurvaDeDedo.NoCurva],  # Medio
        [CurvaDeDedo.MediaCurva, CurvaDeDedo.NoCurva],  # Anular
        [CurvaDeDedo.MediaCurva, CurvaDeDedo.NoCurva]  # Menhique
    ]
    letra_v.curva_posicion_determinacion = [
        [1.0,1.0],  # Pulgar
        [1.0],  # Index
        [1.0],  # Medio
        [1.0,1.0],  # Anular
        [1.0,1.0]  # Menhique
    ]
    letra_v.dedo_posicion = [
        [PosicionDedo.EsquinaDerecha, PosicionDedo.HaciaArriba],  # Pulgar
        [PosicionDedo.HaciaArriba, PosicionDedo.EsquinaIzquierda],  # Index
        [PosicionDedo.HaciaArriba, PosicionDedo.EsquinaDerecha],  # Medio
        [PosicionDedo.EsquinaIzquierda, PosicionDedo.HaciaAbajo],  # Anular
        [PosicionDedo.EsquinaIzquierda, PosicionDedo.HaciaAbajo]  # Menhique
    ]
    letra_v.determinacion_posicion_dedo = [
        [1.0,1.0],  # Pulgar
        [1.0,1.0],  # Index
        [1.0,1.0],  # Medio
        [1.0,1.0],  # Anular
        [1.0,1.0]  # Menhique
    ]
    letra_v.posicion_id = 20
    poses_dedo_conocidas.append(letra_v)

    ####### W id =21
    letra_w = DataFormacionDedo()
    letra_w.nombre_posicion = 'W'
    letra_w.curva_posicion = [
        [CurvaDeDedo.NoCurva, CurvaDeDedo.MediaCurva],  # Pulgar
        [CurvaDeDedo.NoCurva],  # Index
        [CurvaDeDedo.NoCurva],  # Medio
        [CurvaDeDedo.NoCurva],  # Anular
        [ CurvaDeDedo.MediaCurva,CurvaDeDedo.NoCurva]  # Menhique
    ]
    letra_w.curva_posicion_determinacion = [
        [1.0,1.0],  # Pulgar
        [1.0],  # Index
        [1.0],  # Medio
        [1.0],  # Anular
        [1.0,1.0]  # Menhique
    ]
    letra_w.dedo_posicion = [
        [PosicionDedo.EsquinaDerecha, PosicionDedo.ApuntaDerecha],  # Pulgar
        [PosicionDedo.HaciaArriba,PosicionDedo.EsquinaDerecha],  # Index
        [PosicionDedo.HaciaArriba,PosicionDedo.EsquinaDerecha],  # Medio
        [PosicionDedo.HaciaArriba,PosicionDedo.EsquinaDerecha],  # Anular
        [PosicionDedo.EsquinaIzquierda, PosicionDedo.HaciaAbajo]  # Menhique
    ]

    letra_w.determinacion_posicion_dedo = [
        [1.0,1.0],  # Pulgar
        [1.0,1.0],  # Index
        [1.0,1.0],  # Medio
        [1.0,1.0],  # Anular
        [1.0, 1.0]  # Menhique
    ]
    letra_w.posicion_id = 21
    poses_dedo_conocidas.append(letra_w)

    ####### X id =22
    letra_x = DataFormacionDedo()
    letra_x.nombre_posicion = 'X'
    letra_x.curva_posicion = [
        [CurvaDeDedo.NoCurva,CurvaDeDedo.MediaCurva],  # Pulgar
        [CurvaDeDedo.MediaCurva],  # Index
        [CurvaDeDedo.FullCurva,CurvaDeDedo.MediaCurva],  # Medio
        [CurvaDeDedo.FullCurva,CurvaDeDedo.MediaCurva],  # Anular
        [CurvaDeDedo.FullCurva,CurvaDeDedo.MediaCurva]  # Menhique
    ]
    letra_x.curva_posicion_determinacion = [
        [1.0, 1.0],  # Pulgar
        [1.0],  # Index
        [1.0, 1.0],  # Medio
        [1.0, 1.0],  # Anul ar
        [1.0, 1.0]  # Menhique
    ]
    letra_x.dedo_posicion = [
        [PosicionDedo.EsquinaDerecha, PosicionDedo.ApuntaDerecha],  # Thumb
        [PosicionDedo.HaciaArriba, PosicionDedo.EsquinaDerecha],  # Index
        [PosicionDedo.EsquinaInfIzquierda,PosicionDedo.EsquinaIzquierda],  # Middle
        [PosicionDedo.EsquinaInfIzquierda,PosicionDedo.EsquinaIzquierda],  # Ring
        [PosicionDedo.EsquinaInfIzquierda,PosicionDedo.EsquinaIzquierda]  # Little
    ]
    letra_x.determinacion_posicion_dedo = [
        [1.0],  # Pulgar
        [1.0,1.0],  # Index
        [1.0,1.0],  # Medio
        [1.0,1.0],  # Anular
        [1.0,1.0]  # Menhique
    ]
    letra_x.posicion_id = 22
    poses_dedo_conocidas.append(letra_x)

    ####### Y id =23
    letra_y = DataFormacionDedo()
    letra_y.nombre_posicion = 'Y'
    letra_y.curva_posicion = [
        [CurvaDeDedo.NoCurva],  # Pulgar
        [CurvaDeDedo.MediaCurva, CurvaDeDedo.FullCurva],  # Index
        [CurvaDeDedo.MediaCurva, CurvaDeDedo.FullCurva],  # Medio
        [CurvaDeDedo.MediaCurva, CurvaDeDedo.FullCurva],  # Anular
        [CurvaDeDedo.NoCurva]  # Menhique
    ]
    letra_y.curva_posicion_determinacion = [
        [1.0],  # Pulgar
        [1.0,1.0],  # Index
        [1.0,1.0],  # Medio
        [1.0,1.0],  # Anular
        [1.0]  # Menhique
    ]
    letra_y.dedo_posicion = [
        [PosicionDedo.ApuntaIzquierda, PosicionDedo.EsquinaIzquierda],  # Thumb
        [PosicionDedo.EsquinaIzquierda, PosicionDedo.HaciaArriba],  # Index
        [PosicionDedo.EsquinaIzquierda, PosicionDedo.HaciaArriba],  # Middle
        [PosicionDedo.EsquinaIzquierda, PosicionDedo.HaciaArriba],  # Ring
        [PosicionDedo.HaciaArriba, PosicionDedo.EsquinaIzquierda]  # Little
    ]
    letra_y.determinacion_posicion_dedo = [
        [1.0,1.0],  # Pulgar
        [1.0,1.0],  # Index
        [1.0,1.0],  # Medio
        [1.0,1.0],  # Anular
        [1.0,1.0]  # Menhique
    ]
    letra_y.posicion_id = 23
    poses_dedo_conocidas.append(letra_y)

    return poses_dedo_conocidas


from pose.utils.CurvaDedo import CurvaDeDedo
from pose.utils.PosicionDedo import PosicionDedo
from pose.utils.FormaciondedatosDedos import FingerDataFormation


def determine_position(curled_positions, finger_positions, known_finger_poses, min_threshold):
    obtained_positions = {}

    for finger_pose in known_finger_poses:
        score_at = 0.0
        for known_curl, known_curl_confidence, given_curl in \
                zip(finger_pose.curl_position, finger_pose.curl_position_confidence, curled_positions):
            if len(known_curl) == 0:
                if len(known_curl_confidence) == 1:
                    score_at += known_curl_confidence[0]
                    continue

            if given_curl in known_curl:
                confidence_at = known_curl.index(given_curl)
                score_at += known_curl_confidence[confidence_at]

        for known_position, known_position_confidence, given_position in \
                zip(finger_pose.finger_position, finger_pose.finger_position_confidence, finger_positions):
            if len(known_position) == 0:
                if len(known_position_confidence) == 1:
                    score_at += known_position_confidence[0]
                    continue

            if given_position in known_position:
                confidence_at = known_position.index(given_position)
                score_at += known_position_confidence[confidence_at]

        if score_at >= min_threshold:
            obtained_positions[finger_pose.position_name] = score_at

    return obtained_positions


def get_position_name_with_pose_id(pose_id, finger_poses):
    for finger_pose in finger_poses:
        if finger_pose.position_id == pose_id:
            return finger_pose.position_name
    return None


def create_known_finger_poses():
    known_finger_poses = []

    #LETRAS DEL ABECEDARIO EXCEPTUANDO LA "J" Y LA "Z"
    ####### A id =0
    letra_a = FingerDataFormation()
    letra_a.position_name = 'A'
    letra_a.curl_position = [
        [CurvaDeDedo.NoCurva],  # Pulgar
        [CurvaDeDedo.FullCurva],  # Index
        [CurvaDeDedo.FullCurva],  # Medio
        [CurvaDeDedo.FullCurva],  # Anular
        [CurvaDeDedo.FullCurva]  # Menhique
    ]
    letra_a.curl_position_confidence = [
        [1.0],  # Pulgar
        [1.0],  # Index
        [1.0],  # Medio
        [1.0],  # Anular
        [1.0]  # Menhique
    ]
    letra_a.finger_position = [
        [PosicionDedo.EsquinaIzquierda, PosicionDedo.HaciaArriba],  # Pulgar
        [PosicionDedo.HaciaArriba],  # Index
        [PosicionDedo.HaciaArriba],  # Medio
        [PosicionDedo.HaciaArriba],  # Anular
        [PosicionDedo.HaciaArriba]  # Menhique
    ]
    letra_a.finger_position_confidence = [
        [1.0,0.5],  # Pulgar
        [1.0],  # Index
        [1.0],  # Medio
        [1.0],  # Anular
        [1.0]  # Menhique
    ]
    letra_a.position_id = 0
    known_finger_poses.append(letra_a)

    ####### B id =1
    letra_b = FingerDataFormation()
    letra_b.position_name = 'B'
    letra_b.curl_position = [
        [CurvaDeDedo.NoCurva],  # Pulgar
        [CurvaDeDedo.NoCurva],  # Index
        [CurvaDeDedo.NoCurva],  # Medio
        [CurvaDeDedo.NoCurva],  # Anular
        [CurvaDeDedo.NoCurva]  # Menhique
    ]
    letra_b.curl_position_confidence = [
        [1.0],  # Pulgar
        [1.0],  # Index
        [1.0],  # Medio
        [1.0],  # Anular
        [1.0]  # Menhique
    ]
    letra_b.finger_position = [
        [PosicionDedo.EsquinaDerecha, PosicionDedo.HaciaArriba],  # Pulgar
        [PosicionDedo.HaciaArriba],  # Index
        [PosicionDedo.HaciaArriba],  # Medio
        [PosicionDedo.HaciaArriba],  # Anular
        [PosicionDedo.HaciaArriba]  # Menhique
    ]
    letra_b.finger_position_confidence = [
        [1.0, 1.0],  # Pulgar
        [1.0],  # Index
        [1.0],  # Medio
        [1.0],  # Anular
        [1.0]  # Menhique
    ]
    letra_b.position_id = 1
    known_finger_poses.append(letra_b)

    ####### C id =2
    letra_c = FingerDataFormation()
    letra_c.position_name = 'C'
    letra_c.curl_position = [
        [CurvaDeDedo.NoCurva],  # Pulgar
        [CurvaDeDedo.MediaCurva, CurvaDeDedo.NoCurva],  # Index
        [CurvaDeDedo.MediaCurva, CurvaDeDedo.NoCurva],  # Medio
        [CurvaDeDedo.MediaCurva, CurvaDeDedo.NoCurva],  # Anular
        [CurvaDeDedo.MediaCurva, CurvaDeDedo.NoCurva]  # Menhique
    ]
    letra_c.curl_position_confidence = [
        [1.0],  # Pulgar
        [1.0, 1.0],  # Index
        [1.0, 1.0],  # Medio
        [1.0, 1.0],  # Anular
        [1.0, 1.0]  # Menhique
    ]
    letra_c.finger_position = [
        [PosicionDedo.ApuntaIzquierda],  # Pulgar
        [PosicionDedo.ApuntaIzquierda],  # Index
        [PosicionDedo.ApuntaIzquierda],  # Medio
        [PosicionDedo.ApuntaIzquierda, PosicionDedo.EsquinaIzquierda],  # Anular
        [PosicionDedo.ApuntaIzquierda, PosicionDedo.EsquinaIzquierda]  # Menhique
    ]
    letra_c.finger_position_confidence = [
        [1.0],  # Pulgar
        [1.0],  # Index
        [1.0],  # Medio
        [1.0, 1.0],  # Anular
        [1.0, 1.0]  # Menhique
    ]
    letra_c.position_id = 2
    known_finger_poses.append(letra_c)

    ####### D id =3
    letra_d = FingerDataFormation()
    letra_d.position_name = 'D'
    letra_d.curl_position = [
        [CurvaDeDedo.NoCurva,CurvaDeDedo.MediaCurva],  # Pulgar
        [CurvaDeDedo.NoCurva],  # Index
        [CurvaDeDedo.MediaCurva, CurvaDeDedo.FullCurva],  # Medio
        [CurvaDeDedo.MediaCurva, CurvaDeDedo.FullCurva],  # Anular
        [CurvaDeDedo.MediaCurva, CurvaDeDedo.FullCurva]  # Menhique
    ]
    letra_d.curl_position_confidence = [
        [1.0,0.5],  # Pulgar
        [1.0],  # Index
        [1.0, 0.3],  # Medio
        [1.0, 0.3],  # Anular
        [1.0, 0.3]  # Menhique
    ]
    letra_d.finger_position = [
        [PosicionDedo.EsquinaIzquierda],  # Pulgar
        [PosicionDedo.HaciaArriba],  # Index
        [PosicionDedo.ApuntaIzquierda ,PosicionDedo.EsquinaInfIzquierda],  # Medio
        [PosicionDedo.ApuntaIzquierda ,PosicionDedo.EsquinaInfIzquierda],  # Anular
        [PosicionDedo.ApuntaIzquierda ,PosicionDedo.EsquinaInfIzquierda]  # Menhique
    ]
    letra_d.finger_position_confidence = [
        [1.0],  # Pulgar
        [1.0],  # Index
        [1.0,1.0],  # Medio
        [1.0,1.0],  # Anular
        [1.0,1.0]  # Menhique
    ]
    letra_d.position_id = 3
    known_finger_poses.append(letra_d)

    ####### E id =4
    letra_e = FingerDataFormation()
    letra_e.position_name = 'E'
    letra_e.curl_position = [
        [CurvaDeDedo.FullCurva, CurvaDeDedo.MediaCurva],#Pulgar
        [CurvaDeDedo.FullCurva, CurvaDeDedo.MediaCurva],  # Index
        [CurvaDeDedo.FullCurva, CurvaDeDedo.MediaCurva],  # Medio
        [CurvaDeDedo.FullCurva, CurvaDeDedo.MediaCurva],  # Anular
        [CurvaDeDedo.FullCurva, CurvaDeDedo.MediaCurva]   # Menhique
    ]
    letra_e.curl_position_confidence = [
        [1.0,0.5],  # Pulgar
        [1.0,0.5],  # Index
        [1.0,0.5],  # Medio
        [1.0,0.5],  # Anular
        [1.0,0.5]  # Menhique
    ]
    letra_e.finger_position = [
        [PosicionDedo.HaciaArriba,PosicionDedo.ApuntaDerecha],  # Pulgar
        [PosicionDedo.EsquinaIzquierda,PosicionDedo.HaciaArriba],  # Index
        [PosicionDedo.HaciaArriba,PosicionDedo.EsquinaIzquierda],  # Medio
        [PosicionDedo.HaciaArriba,PosicionDedo.EsquinaIzquierda],  # Anular
        [PosicionDedo.HaciaArriba,PosicionDedo.EsquinaIzquierda]  # Menhique
    ]
    letra_e.finger_position_confidence = [
        [1.0,0.5],  # Pulgar
        [1.0,0.5],  # Index
        [1.0,0.5],  # Medio
        [1.0,0.5],  # Anular
        [1.0,0.5]  # Menhique
    ]
    letra_e.position_id = 4
    known_finger_poses.append(letra_e)

    ####### F id =5
    letra_f = FingerDataFormation()
    letra_f.position_name = 'F'
    letra_f.curl_position = [
        [CurvaDeDedo.FullCurva,CurvaDeDedo.MediaCurva],  # Pulgar
        [CurvaDeDedo.FullCurva,CurvaDeDedo.MediaCurva],  # Index
        [CurvaDeDedo.NoCurva],  # Medio
        [CurvaDeDedo.NoCurva],  # Anular
        [CurvaDeDedo.NoCurva]  # Menhique
    ]
    letra_f.curl_position_confidence = [
        [1.0,1.0],  # Pulgar
        [1.0,1.0],  # Index
        [1.0],  # Medio
        [1.0],  # Anular
        [1.0]  # Menhique
    ]
    letra_f.finger_position = [
        [PosicionDedo.EsquinaIzquierda],  # Pulgar
        [PosicionDedo.HaciaArriba],  # Index
        [PosicionDedo.HaciaArriba,PosicionDedo.EsquinaDerecha],  # Medio
        [PosicionDedo.HaciaArriba,PosicionDedo.EsquinaDerecha],  # Anular
        [PosicionDedo.HaciaArriba,PosicionDedo.EsquinaDerecha]  # Menhique
    ]
    letra_f.finger_position_confidence = [
        [1.0],  # Pulgar
        [1.0],  # Index
        [0.5,1.0],  # Medio
        [0.5,1.0],  # Anular
        [0.5,1.0]  # Menhique
    ]
    letra_f.position_id = 5
    known_finger_poses.append(letra_f)

    ####### G id =6
    letra_g = FingerDataFormation()
    letra_g.position_name = 'G'
    letra_g.curl_position = [
        [CurvaDeDedo.NoCurva],  # Pulgar
        [CurvaDeDedo.NoCurva],  # Index
        [CurvaDeDedo.FullCurva],  # Medio
        [CurvaDeDedo.FullCurva],  # Anular
        [CurvaDeDedo.FullCurva]  # Menhique
    ]
    letra_g.curl_position_confidence = [
        [1.0],  # Pulgar
        [1.0],  # Index
        [1.0],  # Medio
        [1.0],  # Anular
        [1.0]  # Menhique
    ]
    letra_g.finger_position = [
        [PosicionDedo.HaciaArriba, PosicionDedo.ApuntaIzquierda],  # Pulgar
        [PosicionDedo.HaciaArriba, PosicionDedo.ApuntaIzquierda],  # Index
        [PosicionDedo.EsquinaIzquierda],  # Medio
        [PosicionDedo.EsquinaIzquierda],  # Anular
        [PosicionDedo.ApuntaIzquierda]  # Menhique
    ]
    letra_g.finger_position_confidence = [
        [1.0, 1.0],  # Pulgar
        [1.0, 1.0],  # Index
        [1.0],  # Medio
        [1.0],  # Anular
        [1.0]  # Menhique
    ]
    letra_g.position_id = 6
    known_finger_poses.append(letra_g)

    ####### H id =7
    letra_h = FingerDataFormation()
    letra_h.position_name = 'H'
    letra_h.curl_position = [
        [CurvaDeDedo.MediaCurva,CurvaDeDedo.NoCurva],  # Pulgar
        [CurvaDeDedo.NoCurva],  # Index
        [CurvaDeDedo.NoCurva],  # Medio
        [CurvaDeDedo.FullCurva,CurvaDeDedo.MediaCurva],  # Anular
        [CurvaDeDedo.FullCurva,CurvaDeDedo.MediaCurva]  # Menhique
    ]
    letra_h.curl_position_confidence = [
        [1.0,1.0],  # Pulgar
        [1.0],  # Index
        [1.0],  # Medio
        [0.8,1.0],  # Anular
        [0.8,1.0]  # Menhique
    ]
    letra_h.finger_position = [
        [PosicionDedo.EsquinaIzquierda,PosicionDedo.ApuntaIzquierda],  # Pulgar
        [PosicionDedo.ApuntaIzquierda,PosicionDedo.EsquinaIzquierda],  # Index
        [PosicionDedo.ApuntaIzquierda,PosicionDedo.EsquinaIzquierda],  # Medio
        [PosicionDedo.ApuntaIzquierda,PosicionDedo.EsquinaIzquierda],  # Anular
        [PosicionDedo.ApuntaIzquierda,PosicionDedo.EsquinaIzquierda]  # Menhique
    ]
    letra_h.finger_position_confidence = [
        [1.0,1.0],  # Pulgar
        [0.8,1.0],  # Index
        [0.8,1.0],  # Medio
        [0.8,1.0],  # Anular
        [0.8,1.0]  # Menhique
    ]
    letra_h.position_id = 7
    known_finger_poses.append(letra_h)

    ####### I id =8
    letra_i = FingerDataFormation()
    letra_i.position_name = 'I'
    letra_i.curl_position = [
        [CurvaDeDedo.MediaCurva, CurvaDeDedo.NoCurva],  # Pulgar
        [CurvaDeDedo.MediaCurva, CurvaDeDedo.FullCurva],  # Index
        [CurvaDeDedo.MediaCurva, CurvaDeDedo.FullCurva],  # Medio
        [CurvaDeDedo.MediaCurva, CurvaDeDedo.FullCurva],  # Anular
        [CurvaDeDedo.NoCurva]  # Menhique
    ]
    letra_i.curl_position_confidence = [
        [1.0,1.0],  # Pulgar
        [1.0,1.0],  # Index
        [1.0,1.0],  # Medio
        [1.0,1.0],  # Anular
        [1.0]  # Menhique
    ]
    letra_i.finger_position = [
        [PosicionDedo.EsquinaIzquierda],  # Pulgar
        [PosicionDedo.ApuntaIzquierda, PosicionDedo.EsquinaIzquierda],  # Index
        [PosicionDedo.ApuntaIzquierda, PosicionDedo.EsquinaIzquierda],  # Medio
        [PosicionDedo.ApuntaIzquierda, PosicionDedo.EsquinaIzquierda],  # Anular
        [PosicionDedo.HaciaArriba, PosicionDedo.EsquinaDerecha]  # Menhique
    ]
    letra_i.finger_position_confidence = [
        [1.0],  # Pulgar
        [1.0, 1.0],  # Index
        [1.0, 1.0],  # Medio
        [1.0, 1.0],  # Anular
        [1.0,0.25]  # Menhique
    ]
    letra_i.position_id = 8
    known_finger_poses.append(letra_i)

    ####### k id =9
    letra_k = FingerDataFormation()
    letra_k.position_name = 'K'
    letra_k.curl_position = [
        [CurvaDeDedo.NoCurva],  # Pulgar
        [CurvaDeDedo.NoCurva],  # Index
        [CurvaDeDedo.NoCurva],  # Menhique
        [CurvaDeDedo.MediaCurva,CurvaDeDedo.FullCurva],  # Medio
        [CurvaDeDedo.MediaCurva,CurvaDeDedo.FullCurva]  # Anular
    ]
    letra_k.curl_position_confidence = [
        [1.0],  # Pulgar
        [1.0],  # Index
        [1.0],  # Medio
        [1.0,1.0],  # Anular
        [1.0,1.0]  # Menhique
    ]
    letra_k.finger_position = [
        [PosicionDedo.HaciaArriba],  # Pulgar
        [PosicionDedo.EsquinaIzquierda,PosicionDedo.ApuntaIzquierda],  # Index
        [PosicionDedo.EsquinaIzquierda,PosicionDedo.ApuntaIzquierda],  # Medio
        [PosicionDedo.EsquinaIzquierda,PosicionDedo.EsquinaInfIzquierda],  # Anular
        [PosicionDedo.EsquinaIzquierda,PosicionDedo.EsquinaInfIzquierda]  # Menhique
    ]
    letra_k.finger_position_confidence = [
        [1.0],  # Pulgar
        [1.0,0.5],  # Index
        [1.0,1.0],  # Medio
        [1.0,0.8],  # Anular
        [1.0,0.8]  # Menhique
    ]
    letra_k.position_id = 9
    known_finger_poses.append(letra_k)

    ####### L id =10
    letra_l = FingerDataFormation()
    letra_l.position_name = 'L'
    letra_l.curl_position = [
        [CurvaDeDedo.NoCurva],  # Pulgar
        [CurvaDeDedo.NoCurva],  # Index
        [CurvaDeDedo.MediaCurva,CurvaDeDedo.FullCurva],  # Medio
        [CurvaDeDedo.MediaCurva,CurvaDeDedo.FullCurva],  # Anular
        [CurvaDeDedo.MediaCurva,CurvaDeDedo.FullCurva]  # Menhique
    ]
    letra_l.curl_position_confidence = [
        [1.0],  # Pulgar
        [1.0],  # Index
        [1.0,0.5],  # Medio
        [1.0,0.5],  # Anular
        [1.0,0.5]  # Menhique
    ]
    letra_l.finger_position = [
        [PosicionDedo.EsquinaIzquierda, PosicionDedo.ApuntaIzquierda],  # Pulgar
        [PosicionDedo.EsquinaDerecha,PosicionDedo.HaciaArriba],  # Index
        [PosicionDedo.EsquinaIzquierda,PosicionDedo.HaciaArriba],  # Medio
        [PosicionDedo.EsquinaIzquierda,PosicionDedo.HaciaArriba],  # Anular
        [PosicionDedo.EsquinaIzquierda,PosicionDedo.HaciaArriba]  # Menhique
    ]
    letra_l.finger_position_confidence = [
        [1.0,1.0],  # Pulgar
        [1.0,1.0],  # Index
        [1.0,1.0],  # Medio
        [1.0,1.0],  # Anular
        [1.0,1.0]  # Menhique
    ]
    letra_l.position_id = 10
    known_finger_poses.append(letra_l)

    ####### M id =11
    letra_m = FingerDataFormation()
    letra_m.position_name = 'M'
    letra_m.curl_position = [
        [CurvaDeDedo.FullCurva],  # Pulgar
        [CurvaDeDedo.NoCurva],  # Index
        [CurvaDeDedo.NoCurva],  # Medio
        [CurvaDeDedo.NoCurva],  # Anular
        [CurvaDeDedo.FullCurva]  # Menhique
    ]
    letra_m.curl_position_confidence = [
        [1.0],  # Pulgar
        [1.0],  # Index
        [1.0],  # Medio
        [1.0],  # Anular
        [1.0]  # Menhique
    ]
    letra_m.finger_position = [
        [PosicionDedo.HaciaAbajo, PosicionDedo.EsquinaInfDerecha],  # Pulgar
        [PosicionDedo.HaciaAbajo],  # Index
        [PosicionDedo.HaciaAbajo],  # Medio
        [PosicionDedo.HaciaAbajo],  # Anular
        [PosicionDedo.EsquinaInfIzquierda, PosicionDedo.HaciaAbajo]  # Menhique
    ]
    letra_m.finger_position_confidence = [
        [1.0, 1.0],  # Pulgar
        [1.0],  # Index
        [1.0],  # Medio
        [1.0],  # Anular
        [1.0, 1.0]  # Menhique
    ]
    letra_m.position_id = 11
    known_finger_poses.append(letra_m)

    ####### N id =12
    letra_n = FingerDataFormation()
    letra_n.position_name = 'N'
    letra_n.curl_position = [
        [CurvaDeDedo.FullCurva, CurvaDeDedo.MediaCurva],  # Pulgar
        [CurvaDeDedo.NoCurva],  # Index
        [CurvaDeDedo.NoCurva],  # Medio
        [CurvaDeDedo.FullCurva, CurvaDeDedo.MediaCurva],  # Anular
        [CurvaDeDedo.FullCurva, CurvaDeDedo.MediaCurva]  # Menhique
    ]
    letra_n.curl_position_confidence = [
        [1.0,1.0],  # Pulgar
        [1.0],  # Index
        [1.0],  # Medio
        [1.0,1.0],  # Anular
        [1.0,1.0]  # Menhique
    ]
    letra_n.finger_position = [
        [PosicionDedo.HaciaAbajo, PosicionDedo.EsquinaInfDerecha],  # Pulgar
        [PosicionDedo.HaciaAbajo],  # Index
        [PosicionDedo.HaciaAbajo],  # Medio
        [PosicionDedo.HaciaAbajo, PosicionDedo.EsquinaIzquierda],  # Anular
        [PosicionDedo.HaciaAbajo, PosicionDedo.EsquinaIzquierda]  # Menhique
    ]
    letra_n.finger_position_confidence = [
        [1.0,1.0],  # Pulgar
        [1.0],  # Index
        [1.0],  # Medio
        [1.0,0.8],  # Anular
        [1.0,0.8]  # Menhique
    ]
    letra_n.position_id = 12
    known_finger_poses.append(letra_n)

    ####### O id =13
    letra_o = FingerDataFormation()
    letra_o.position_name = 'O'
    letra_o.curl_position = [
        [CurvaDeDedo.NoCurva],  # Pulgar
        [CurvaDeDedo.MediaCurva],  # Index
        [CurvaDeDedo.MediaCurva],  # Medio
        [CurvaDeDedo.MediaCurva],  # Anular
        [CurvaDeDedo.NoCurva]  # Menhique
    ]
    letra_o.curl_position_confidence = [
        [1.0],  # Pulgar
        [1.0],  # Index
        [1.0],  # Medio
        [1.0],  # Anular
        [1.0]  # Menhique
    ]
    letra_o.finger_position = [
        [PosicionDedo.HaciaArriba, PosicionDedo.EsquinaIzquierda],  # Pulgar
        [PosicionDedo.HaciaArriba, PosicionDedo.EsquinaIzquierda],  # Index
        [PosicionDedo.HaciaArriba, PosicionDedo.EsquinaIzquierda],  # Medio
        [PosicionDedo.HaciaArriba, PosicionDedo.EsquinaIzquierda],  # Anular
        [PosicionDedo.HaciaArriba, PosicionDedo.EsquinaIzquierda]  # Menhique
    ]
    letra_o.finger_position_confidence = [
        [1.0, 1.0],  # Pulgar
        [1.0, 1.0],  # Index
        [1.0, 1.0],  # Medio
        [1.0, 1.0],  # Anular
        [1.0, 1.0]  # Menhique
    ]
    letra_o.position_id = 13
    known_finger_poses.append(letra_o)

    ####### P id =14
    letra_p = FingerDataFormation()
    letra_p.position_name = 'P'
    letra_p.curl_position = [
        [CurvaDeDedo.NoCurva],  # Pulgar
        [CurvaDeDedo.NoCurva],  # Index
        [CurvaDeDedo.NoCurva],  # Medio
        [CurvaDeDedo.NoCurva],  # Anular
        [CurvaDeDedo.NoCurva,CurvaDeDedo.MediaCurva]  # Menhique
    ]
    letra_p.curl_position_confidence = [
        [1.0],  # Pulgar
        [1.0],  # Index
        [1.0],  # Medio
        [1.0],  # Anular
        [1.0,1.0 ] # Menhique
    ]
    letra_p.finger_position = [
        [PosicionDedo.HaciaAbajo,PosicionDedo.EsquinaInfDerecha],  # Pulgar
        [PosicionDedo.HaciaAbajo,PosicionDedo.EsquinaInfIzquierda],  # Index
        [PosicionDedo.HaciaAbajo,PosicionDedo.EsquinaInfIzquierda],  # Medio
        [PosicionDedo.HaciaAbajo,PosicionDedo.EsquinaInfDerecha],  # Anular
        [PosicionDedo.HaciaAbajo,PosicionDedo.EsquinaInfDerecha]  # Menhique
    ]
    letra_p.finger_position_confidence = [
        [1.0, 1.0],  # Pulgar
        [1.0, 1.0],  # Index
        [1.0, 1.0],  # Medio
        [1.0, 1.0],  # Anular
        [1.0, 1.0]  # Menhique
    ]
    letra_p.position_id = 14
    known_finger_poses.append(letra_p)

    ####### Q id =15
    letra_q = FingerDataFormation()
    letra_q.position_name = 'Q'
    letra_q.curl_position = [
        [CurvaDeDedo.NoCurva],  # Pulgar
        [CurvaDeDedo.NoCurva, CurvaDeDedo.MediaCurva],  # Index
        [CurvaDeDedo.MediaCurva],  # Medio
        [CurvaDeDedo.MediaCurva],  # Anular
        [CurvaDeDedo.MediaCurva]  # Menhique
    ]
    letra_q.curl_position_confidence = [
        [1.0],  # Pulgar
        [1.0, 1.0],  # Index
        [1.0],  # Medio
        [1.0],  # Anular
        [1.0]  # Menhique
    ]
    letra_q.finger_position = [
        [PosicionDedo.HaciaAbajo, PosicionDedo.EsquinaInfIzquierda],  # Pulgar
        [PosicionDedo.HaciaAbajo, PosicionDedo.EsquinaInfIzquierda],  # Index
        [PosicionDedo.HaciaAbajo, PosicionDedo.ApuntaDerecha],  # Medio
        [PosicionDedo.HaciaAbajo, PosicionDedo.ApuntaDerecha],  # Anular
        [PosicionDedo.HaciaAbajo, PosicionDedo.ApuntaDerecha]  # Menhique
    ]
    letra_q.finger_position_confidence = [
        [1.0, 1.0],  # Pulgar
        [1.0, 1.0],  # Index
        [1.0, 1.0],  # Medio
        [1.0, 1.0],  # Anular
        [1.0, 1.0]  # Menhique
    ]
    letra_q.position_id = 15
    known_finger_poses.append(letra_q)

    ####### R id =16
    letra_r = FingerDataFormation()
    letra_r.position_name = 'R'
    letra_r.curl_position = [
        [CurvaDeDedo.NoCurva],  # Pulgar
        [CurvaDeDedo.NoCurva],  # Index
        [CurvaDeDedo.NoCurva],  # Medio
        [CurvaDeDedo.NoCurva, CurvaDeDedo.MediaCurva],  # Anular
        [CurvaDeDedo.NoCurva, CurvaDeDedo.MediaCurva]  # Menhique
    ]
    letra_r.curl_position_confidence = [
        [1.0],  # Pulgar
        [1.0],  # Index
        [1.0],  # Medio
        [1.0,1.0],  # Anular
        [1.0,1.0]  # Menhique
    ]
    letra_r.finger_position = [
        [PosicionDedo.EsquinaDerecha, PosicionDedo.HaciaArriba],  # Pulgar
        [PosicionDedo.HaciaArriba, PosicionDedo.EsquinaDerecha],  # Index
        [PosicionDedo.HaciaArriba, PosicionDedo.EsquinaIzquierda],  # Medio
        [PosicionDedo.EsquinaInfIzquierda,PosicionDedo.HaciaArriba],  # Anular
        [PosicionDedo.EsquinaInfIzquierda,PosicionDedo.HaciaArriba]  # Menhique
    ]
    letra_r.finger_position_confidence = [
        [1.0,1.0],  # Pulgar
        [1.0,1.0],  # Index
        [1.0,1.0],  # Medio
        [1.0,1.0],  # Anular
        [1.0,1.0]  # Menhique
    ]
    letra_r.position_id = 16
    known_finger_poses.append(letra_r)

    ####### S id =17
    letra_s = FingerDataFormation()
    letra_s.position_name = 'S'
    letra_s.curl_position = [
        [CurvaDeDedo.NoCurva,CurvaDeDedo.MediaCurva],  # Pulgar
        [CurvaDeDedo.MediaCurva,CurvaDeDedo.FullCurva],  # Index
        [CurvaDeDedo.MediaCurva,CurvaDeDedo.FullCurva],  # Medio
        [CurvaDeDedo.MediaCurva,CurvaDeDedo.FullCurva],  # Anular
        [CurvaDeDedo.MediaCurva,CurvaDeDedo.FullCurva]  # Menhique
    ]
    letra_s.curl_position_confidence = [
        [1.0,1.0],  # Pulgar
        [1.0,1.0],  # Index
        [1.0,1.0],  # Medio
        [1.0,1.0],  # Anular
        [1.0,1.0]  # Menhique
    ]
    letra_s.finger_position = [
        [PosicionDedo.EsquinaDerecha, PosicionDedo.ApuntaDerecha],  # Pulgar
        [PosicionDedo.HaciaArriba,PosicionDedo.EsquinaInfIzquierda],  # Index
        [PosicionDedo.HaciaArriba,PosicionDedo.EsquinaInfIzquierda],  # Medio
        [PosicionDedo.HaciaArriba, PosicionDedo.EsquinaInfIzquierda],  # Anular
        [PosicionDedo.HaciaArriba, PosicionDedo.EsquinaInfIzquierda]  # Menhique
    ]
    letra_s.finger_position_confidence = [
        [1.0,1.0],  # Pulgar
        [1.0,1.0],  # Index
        [1.0,1.0],  # Medio
        [1.0, 1.0],  # Anular
        [1.0, 1.0]  # Menhique
    ]
    letra_s.position_id = 17
    known_finger_poses.append(letra_s)

    ####### T id =18
    letra_t = FingerDataFormation()
    letra_t.position_name = 'T'
    letra_t.curl_position = [
        [CurvaDeDedo.NoCurva],  # Pulgar
        [CurvaDeDedo.MediaCurva,CurvaDeDedo.NoCurva],  # Index
        [CurvaDeDedo.FullCurva,CurvaDeDedo.MediaCurva],  # Medio
        [CurvaDeDedo.FullCurva,CurvaDeDedo.MediaCurva],  # Anular
        [CurvaDeDedo.FullCurva,CurvaDeDedo.MediaCurva]  # Menhique
    ]
    letra_t.curl_position_confidence = [
        [1.0],  # Pulgar
        [1.0,1.0],  # Index
        [1.0,1.0],  # Medio
        [1.0,1.0],  # Anular
        [1.0,1.0]  # Menhique
    ]
    letra_t.finger_position = [
        [PosicionDedo.HaciaArriba],  # Pulgar
        [PosicionDedo.ApuntaIzquierda,PosicionDedo.EsquinaIzquierda],  # Index
        [PosicionDedo.EsquinaIzquierda],  # Medio
        [PosicionDedo.EsquinaIzquierda],  # Anular
        [PosicionDedo.EsquinaIzquierda]  # Menhique
    ]
    letra_t.finger_position_confidence = [
        [1.0],  # Pulgar
        [1.0,1.0],  # Index
        [1.0],  # Medio
        [1.0],  # Anular
        [1.0]  # Menhique
    ]
    letra_t.position_id = 18
    known_finger_poses.append(letra_t)

    ####### U id =19
    letra_u = FingerDataFormation()
    letra_u.position_name = 'U'
    letra_u.curl_position = [
        [CurvaDeDedo.NoCurva],  # Pulgar
        [CurvaDeDedo.NoCurva],  # Index
        [CurvaDeDedo.MediaCurva,CurvaDeDedo.NoCurva],  # Medio
        [CurvaDeDedo.MediaCurva,CurvaDeDedo.NoCurva],  # Anular
        [CurvaDeDedo.NoCurva]  # Menhique
    ]
    letra_u.curl_position_confidence = [
        [1.0],  # Pulgar
        [1.0],  # Index
        [1.0,1.0],  # Medio
        [1.0,1.0],  # Anular
        [1.0]  # Menhique
    ]
    letra_u.finger_position = [
        [PosicionDedo.EsquinaDerecha,PosicionDedo.HaciaArriba],  # Thumb
        [PosicionDedo.HaciaArriba,PosicionDedo.EsquinaDerecha],  # Index
        [PosicionDedo.EsquinaIzquierda,PosicionDedo.HaciaArriba],  # Middle
        [PosicionDedo.EsquinaIzquierda,PosicionDedo.HaciaArriba],  # Ring
        [PosicionDedo.HaciaArriba,PosicionDedo.EsquinaIzquierda]  # Little
    ]
    letra_u.finger_position_confidence = [
        [1.0,1.0],  # Pulgar
        [1.0,1.0],  # Index
        [1.0,1.0],  # Medio
        [1.0,1.0],  # Anular
        [1.0,1.0]  # Menhique
    ]
    letra_u.position_id = 19
    known_finger_poses.append(letra_u)

    ###### V id =20
    letra_v = FingerDataFormation()
    letra_v.position_name = 'V'
    letra_v.curl_position = [
        [CurvaDeDedo.NoCurva, CurvaDeDedo.MediaCurva],  # Pulgar
        [CurvaDeDedo.NoCurva],  # Index
        [CurvaDeDedo.NoCurva],  # Medio
        [CurvaDeDedo.MediaCurva, CurvaDeDedo.NoCurva],  # Anular
        [CurvaDeDedo.MediaCurva, CurvaDeDedo.NoCurva]  # Menhique
    ]
    letra_v.curl_position_confidence = [
        [1.0,1.0],  # Pulgar
        [1.0],  # Index
        [1.0],  # Medio
        [1.0,1.0],  # Anular
        [1.0,1.0]  # Menhique
    ]
    letra_v.finger_position = [
        [PosicionDedo.EsquinaDerecha, PosicionDedo.HaciaArriba],  # Pulgar
        [PosicionDedo.HaciaArriba, PosicionDedo.EsquinaIzquierda],  # Index
        [PosicionDedo.HaciaArriba, PosicionDedo.EsquinaDerecha],  # Medio
        [PosicionDedo.EsquinaIzquierda, PosicionDedo.HaciaAbajo],  # Anular
        [PosicionDedo.EsquinaIzquierda, PosicionDedo.HaciaAbajo]  # Menhique
    ]
    letra_v.finger_position_confidence = [
        [1.0,1.0],  # Pulgar
        [1.0,1.0],  # Index
        [1.0,1.0],  # Medio
        [1.0,1.0],  # Anular
        [1.0,1.0]  # Menhique
    ]
    letra_v.position_id = 20
    known_finger_poses.append(letra_v)

    ####### W id =21
    letra_w = FingerDataFormation()
    letra_w.position_name = 'W'
    letra_w.curl_position = [
        [CurvaDeDedo.NoCurva, CurvaDeDedo.MediaCurva],  # Pulgar
        [CurvaDeDedo.NoCurva],  # Index
        [CurvaDeDedo.NoCurva],  # Medio
        [CurvaDeDedo.NoCurva],  # Anular
        [ CurvaDeDedo.MediaCurva,CurvaDeDedo.NoCurva]  # Menhique
    ]
    letra_w.curl_position_confidence = [
        [1.0,1.0],  # Pulgar
        [1.0],  # Index
        [1.0],  # Medio
        [1.0],  # Anular
        [1.0,1.0]  # Menhique
    ]
    letra_w.finger_position = [
        [PosicionDedo.EsquinaDerecha, PosicionDedo.ApuntaDerecha],  # Pulgar
        [PosicionDedo.HaciaArriba,PosicionDedo.EsquinaDerecha],  # Index
        [PosicionDedo.HaciaArriba,PosicionDedo.EsquinaDerecha],  # Medio
        [PosicionDedo.HaciaArriba,PosicionDedo.EsquinaDerecha],  # Anular
        [PosicionDedo.EsquinaIzquierda, PosicionDedo.HaciaAbajo]  # Menhique
    ]

    letra_w.finger_position_confidence = [
        [1.0,1.0],  # Pulgar
        [1.0,1.0],  # Index
        [1.0,1.0],  # Medio
        [1.0,1.0],  # Anular
        [1.0, 1.0]  # Menhique
    ]
    letra_w.position_id = 21
    known_finger_poses.append(letra_w)

    ####### X id =22
    letra_x = FingerDataFormation()
    letra_x.position_name = 'X'
    letra_x.curl_position = [
        [CurvaDeDedo.NoCurva,CurvaDeDedo.MediaCurva],  # Pulgar
        [CurvaDeDedo.MediaCurva],  # Index
        [CurvaDeDedo.FullCurva,CurvaDeDedo.MediaCurva],  # Medio
        [CurvaDeDedo.FullCurva,CurvaDeDedo.MediaCurva],  # Anular
        [CurvaDeDedo.FullCurva,CurvaDeDedo.MediaCurva]  # Menhique
    ]
    letra_x.curl_position_confidence = [
        [1.0, 1.0],  # Pulgar
        [1.0],  # Index
        [1.0, 1.0],  # Medio
        [1.0, 1.0],  # Anul ar
        [1.0, 1.0]  # Menhique
    ]
    letra_x.finger_position = [
        [PosicionDedo.EsquinaDerecha, PosicionDedo.ApuntaDerecha],  # Thumb
        [PosicionDedo.HaciaArriba, PosicionDedo.EsquinaDerecha],  # Index
        [PosicionDedo.EsquinaInfIzquierda,PosicionDedo.EsquinaIzquierda],  # Middle
        [PosicionDedo.EsquinaInfIzquierda,PosicionDedo.EsquinaIzquierda],  # Ring
        [PosicionDedo.EsquinaInfIzquierda,PosicionDedo.EsquinaIzquierda]  # Little
    ]
    letra_x.finger_position_confidence = [
        [1.0],  # Pulgar
        [1.0,1.0],  # Index
        [1.0,1.0],  # Medio
        [1.0,1.0],  # Anular
        [1.0,1.0]  # Menhique
    ]
    letra_x.position_id = 22
    known_finger_poses.append(letra_x)

    ####### Y id =23
    letra_y = FingerDataFormation()
    letra_y.position_name = 'Y'
    letra_y.curl_position = [
        [CurvaDeDedo.NoCurva],  # Pulgar
        [CurvaDeDedo.MediaCurva, CurvaDeDedo.FullCurva],  # Index
        [CurvaDeDedo.MediaCurva, CurvaDeDedo.FullCurva],  # Medio
        [CurvaDeDedo.MediaCurva, CurvaDeDedo.FullCurva],  # Anular
        [CurvaDeDedo.NoCurva]  # Menhique
    ]
    letra_y.curl_position_confidence = [
        [1.0],  # Pulgar
        [1.0,1.0],  # Index
        [1.0,1.0],  # Medio
        [1.0,1.0],  # Anular
        [1.0]  # Menhique
    ]
    letra_y.finger_position = [
        [PosicionDedo.ApuntaIzquierda, PosicionDedo.EsquinaIzquierda],  # Thumb
        [PosicionDedo.EsquinaIzquierda, PosicionDedo.HaciaArriba],  # Index
        [PosicionDedo.EsquinaIzquierda, PosicionDedo.HaciaArriba],  # Middle
        [PosicionDedo.EsquinaIzquierda, PosicionDedo.HaciaArriba],  # Ring
        [PosicionDedo.HaciaArriba, PosicionDedo.EsquinaIzquierda]  # Little
    ]
    letra_y.finger_position_confidence = [
        [1.0,1.0],  # Pulgar
        [1.0,1.0],  # Index
        [1.0,1.0],  # Medio
        [1.0,1.0],  # Anular
        [1.0,1.0]  # Menhique
    ]
    letra_y.position_id = 23
    known_finger_poses.append(letra_y)

    return known_finger_poses


from typing import List, Tuple
import face_recognition
import numpy as np
import cv2


def get_persons_from_frame(frame: np.ndarray, known_face_encodings: List[float]) -> Tuple[List[int], List[float]]:
    '''
    :param frame: Camera frame in format height x width x 3
    :param known_face_encodings: Array of known face encodings
    :return: A list of user ids detected in the frame
    '''
    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Find all the faces and face encodings in the current frame of video
    estimated_face_locations = face_recognition.face_locations(rgb_small_frame)
    estimated_face_encodings = face_recognition.face_encodings(rgb_small_frame, estimated_face_locations)

    face_ids = []
    face_confs = []

    for face_encoding in estimated_face_encodings:
        # Use the face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        best_distance = face_distances[best_match_index]

        face_ids.append(best_match_index)
        face_confs.append(best_distance)

    return face_ids, face_confs

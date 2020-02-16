# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 17:12:33 2020

@author: James
"""
import cv2
import numpy as np

# Get cascade from file
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

# Get video from webcam
video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)


def detect_face(grey):
    """
    Locates the faces in a frame.
    Requires a greyscale frame as an argument.
    Returns a faces object.
    """
    # Detects the facs in the frame
    faces = faceCascade.detectMultiScale(
        grey,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(30, 30),
        #flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )
    return faces


def get_frame(frame_source):
    """
    Gets the frame from the video source and preprocesses it.
    Requires a video source as its argument.
    Returns a colour frame and a greyscale frame.
    """
    # Capture frame-by-frame, return code is relavent if reading from a file
    return_code, frame = frame_source.read()
    # Makes image greyscale
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return frame, grey


def debug_display(frame, faces):
    """
    Displays the current frame with the faces shown as rectangles.
    Requires a frame and a faces object as arguments.
    Returns False if the exit key, "q" is pressed, or True otherwise.
    """
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # Display the resulting frame
    cv2.imshow('Video', frame)
    # Exit if "q" key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        return False
    else:
        return True


def gen_coords(faces, grey):
    """
    Requires a faces object as an input.
    Returns a list of the coords.
    """
    x = np.mean([faces[i][0] + faces[i][1] for i in range(len(faces))])
    y = np.mean([faces[i][2] + faces[i][3] for i in range(len(faces))])
    z = get_distance(np.mean([face[3] for face in faces]), len(grey))
    coords = [x, y, z]
    if np.isnan(coords).any():
        eye_pos = get_eye_position(grey)
        x, y = eye_pos[0], eye_pos[1]
        z = 10
    return [x, y, z]


def get_distance(face_height, frame_height):
    """
    Requires the face height and the frame height as arguments.
    Returns the distance in cm.
    """
    natural_distance = frame_height / face_height
    return natural_distance * 20


def get_face_position(grey):
    """
    Returns a list of the x, y, and z coordinates of the observing face.
    """
    frame, grey = get_frame(video_capture)
    faces = detect_face(grey)
    coords = gen_coords(faces, grey)
    return coords


def calculate_angles(coords1, coords2):
    """
    Requires the coordinates of the first then the second points as arguments.
    Returns the horizontal and vertical angles in degrees.
    """
    delta_x = coords2[0] - coords1[0]
    delta_y = coords2[1] - coords1[1]
    delta_z = coords2[2] - coords1[2]
    angle_horizontal = np.rad2deg(np.arctan(delta_x/delta_z))
    angle_vertical = np.rad2deg(np.arctan(delta_y/delta_z))
    return angle_horizontal, angle_vertical


def get_eye_position(frame):
    """
    Requires a frame as an argument.
    Returns a pair of coords for the image centre.
    """
    return [len(frame[0])/2, len(frame)/2, 0]


def get_coordinate_pair():
    """
    Runs all of the shit to get the coords we need.
    Returns a pair of lists of coords, one for the face and one for the eye.
    """
    frame, grey = get_frame(video_capture)
    return get_face_position(grey), get_eye_position(grey)


def run_test():
    """
    Runs the debugging display whilest printing coords.
    """
    video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    while True:
        frame, grey = get_frame(video_capture)
        faces = detect_face(grey)
        print(gen_coords(faces, grey))
        debug_display(frame, faces)
        if not debug_display(frame, faces):
            video_capture.release()
            break

# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:56:27 2020

@author: James
"""
#%% Module imports
import cv2


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
        return False
    else:
        return True
    

# Import cascade 
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

# Get video from webcam
video_capture = cv2.VideoCapture(0)


#%% Main loop
while True:
    frame, grey_frame = get_frame(video_capture)
    faces = detect_face(grey_frame)
    print(faces)
    if not debug_display(frame, faces):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()

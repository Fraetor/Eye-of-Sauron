# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:56:27 2020

@author: James
"""
import detectface as df
import cv2


# Get video from webcam
video_capture = cv2.VideoCapture(0)

while True:
    frame, grey_frame = df.get_frame(video_capture)
    faces = df.detect_face(grey_frame)
    print(faces)
    if not df.debug_display(frame, faces):
        video_capture.release()
        cv2.destroyAllWindows()
        break

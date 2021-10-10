# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 03:56:57 2021

@author: ahmed
"""



# Import Dependencies

import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
import time
import mediiapipe as mp


# Keypoints Using Mediapipe Holistic


mp_holistic = mp.solutions.holistic       # Holistic Model
mp_drawing = mp.solutions.drawing_utils   # Drawing utilities


def mediapipe_detection(image, model):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    
    results = model.process(image)  # Make predictions
    
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
    return image, results


    
def draw_landmarks(image, results):
    mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACEMESH_CONTOURS) # Draw face connections
    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS) # Draw pose connections
    mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS) # Draw left hand connections
    mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS) # Draw right hand connections



# def drw_styled_landmarks(image, results):
#     mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACEMESH_CONTOURS,
#                                  mp_drawing.DrawingSpec(color=(80,110,10), thickness=1, circle_radius=1),
#                                  mp_drawing.DrawingSpec(color=(40, 250, 110), thickness=1, circle_radius=1))
    
#     mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
#                               mp_drawing.DrawingSpec(color=(80, 40, 10), thickness=2, circle_radius=4),
#                               mp_drawing.DrawingSpec(color=(60, 20, 111), thickness=2, circle_radius=2))
    
#     mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.HAND_CONNECTIONS,
#                               mp_drawing.DrawingSpec(color=(20, 30, 111), thickness=2, circle_radius=4),
#                               mp_drawing.DrawingSpec(color=(50, 60, 222), thickness=2, circle_radius=2))
    
#     mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.HAND_CONNECTIONS,
#                               mp_drawing.DrawingSpec(color=(222, 20, 20), thickness=2, circle_radius=4),
#                               mp_drawing.DrawingSpec(color=(222, 70, 80), thickness=2, circle_radius=2))

def draw_styled_landmarks(image, results):
    # Draw face connections
    mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACEMESH_TESSELATION, 
                             mp_drawing.DrawingSpec(color=(80,110,10), thickness=1, circle_radius=1), 
                             mp_drawing.DrawingSpec(color=(80,256,121), thickness=1, circle_radius=1)
                             ) 
    # Draw pose connections
    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                             mp_drawing.DrawingSpec(color=(80,22,10), thickness=2, circle_radius=4), 
                             mp_drawing.DrawingSpec(color=(80,44,121), thickness=2, circle_radius=2)
                             ) 
    # Draw left hand connections
    mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                             mp_drawing.DrawingSpec(color=(121,22,76), thickness=2, circle_radius=4), 
                             mp_drawing.DrawingSpec(color=(121,44,250), thickness=2, circle_radius=2)
                             ) 
    # Draw right hand connections  
    mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                             mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=4), 
                             mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)
                             )

# mp_holitic = mp_holitic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5)

cap = cv2.VideoCapture(0)

with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    
    while cap.isOpened():
    
        ret, frame = cap.read()
        
        if ret:
            image, results = mediapipe_detection(frame, holistic)
            draw_styled_landmarks(image, results)
            print(results)
            cv2.imshow('OpenCV Feed', image)
        
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()



# print(results.face_landmarks)

# draw_landmarks(frame, results)

# plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

# plt.imshow(image)
























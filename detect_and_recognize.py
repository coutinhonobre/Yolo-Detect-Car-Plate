from ultralytics import YOLO
from easyocr import Reader
import time
import torch
import cv2
import os
import csv

CONFIDENCE_THRESHOLD = 0.4
COLOR = (0, 255, 0)
def detect_number_plates(image, model, display=False):
    start = time.time()
    # pass the image through the model and get the detections
    detections = model.predict(image)[0].boxes.data


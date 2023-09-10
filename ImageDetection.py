import cv2
from ultralytics import YOLO

model = YOLO('yolov8n.pt')
image = cv2.imread("road.jpg")
result = model(image)
annotated_frame = result[0].plot()
cv2.imshow("YOLOv8", annotated_frame)




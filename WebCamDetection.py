import cv2
from ultralytics import YOLO

model = YOLO('yolov8n.pt')
cap = cv2.VideoCapture(0)

while cap.isOpened():
    if ord("q") == 0xFF & cv2.waitKey(1):
        break

    success, image = cap.read()
    if not success:
        print("empty video frame")
        break

    image = cv2.resize(image, (800,600))
    result = model(image)
    annotated_frame = result[0].plot()
    cv2.imshow("YOLOv8", annotated_frame)


cap.release()
cv2.destroyAllWindows()
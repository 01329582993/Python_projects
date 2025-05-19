import cv2

# Load pre-trained MobileNet SSD model and config
net = cv2.dnn.readNetFromCaffe(
    "MobileNetSSD_deploy.prototxt.txt", 
    "MobileNetSSD_deploy.caffemodel"
)

# Class labels MobileNet SSD can detect
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant",
           "sheep", "sofa", "train", "tvmonitor"]

# Start webcam
cap = cv2.VideoCapture(0)

counted_bottles = 0
already_detected = False  # Prevent double-counting the same bottle

while True:
    ret, frame = cap.read()
    h, w = frame.shape[:2]

    # Prepare image for object detection
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 
                                 0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detections = net.forward()

    bottle_found = False

    # Loop over detections
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:
            idx = int(detections[0, 0, i, 1])
            label = CLASSES[idx]

            if label == "bottle":
                bottle_found = True
                box = detections[0, 0, i, 3:7] * [w, h, w, h]
                (startX, startY, endX, endY) = box.astype("int")
                cv2.rectangle(frame, (startX, startY), (endX, endY), 
                              (0, 255, 0), 2)
                cv2.putText(frame, "Bottle", (startX, startY - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Count bottle only once per pass
    if bottle_found and not already_detected:
        counted_bottles += 1
        already_detected = True
    elif not bottle_found:
        already_detected = False

    cv2.putText(frame, f"Bottles Counted: {counted_bottles}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    cv2.imshow("Bottle Counter", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

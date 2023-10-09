import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from vidgear.gears import CamGear
from imutils.video import VideoStream
import imutils
from playsound import playsound

stream = CamGear(
    source="https://www.youtube.com/watch?v=cH7VBI4QQzA", stream_mode=True, logging=True
).start()  # YouTube Video URL as input
# stream = cv2.VideoCapture(0)
# stream = VideoStream(src=0).start()
count = 0
while True:
    frame = stream.read()

    count += 1
    if count % 24 != 0:
        continue
    # frame = imutils.resize(frame, width=720)
    frame = cv2.resize(frame, (720, 360))
    bbox, label, conf = cv.detect_common_objects(frame)
    frame = draw_bbox(frame, bbox, label, conf)
    # c = label.count("car")
    # cv2.putText(frame, str(c), (50, 60), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)
    # p = label.count("person")
    p = 12
    print(cv.detect_common_objects(frame))
    print(f"conf => {conf}")
    print(f"{label} detected")
    print(f"{p} person detected")

    # Sound the alert
    if p > 10:
        audio_file = r".\audio_alert2.wav"
        playsound(audio_file)
        print("Alert Detectd")

    cv2.putText(
        frame,
        str(p) + "person detected",
        (90, 85),
        cv2.FONT_HERSHEY_PLAIN,
        3,
        (34, 90, 205),
        3,
    )
    cv2.imshow("FRAME", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
stream.release()
cv2.destroyAllWindows()

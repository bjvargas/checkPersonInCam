import cv2
import argparse
from ultralytics import YOLO
import supervision as sv
import pygame
import time
import subprocess


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="YOLOv8 live")
    parser.add_argument(
        "--webcam-resolution",
        default=[640, 480],
        nargs=2,
        type=int
    )
    args = parser.parse_args()
    return args


def main():
    while True:
        try:
            args = parse_arguments()
            frame_width, frame_height = args.webcam_resolution

            cap = cv2.VideoCapture(0)
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

            model = YOLO("yolov8l.pt")

            box_annotator = sv.BoxAnnotator(
                thickness=2,
                text_thickness=2,
                text_scale=1
            )

            pygame.init()
            sound = pygame.mixer.Sound("chaves-ah-cala-essa-boca.mp3")
            sound_played = False
            person_detected_count = 0
            time_since_last_detection = 30

            while True:
                ret, frame = cap.read()
                result = model(frame)[0]
                detections = sv.Detections.from_yolov8(result)

                labels = [
                    f"{model.model.names[class_id]} {confidence:0.2f}"
                    for _, _, confidence, class_id, _
                    in detections
                ]
                frame = box_annotator.annotate(scene=frame, detections=detections)

                for label in labels:
                    if "person" in label and time_since_last_detection > 0:
                        person_detected_count += 1
                        time_since_last_detection = 0

                        if person_detected_count >= 30 and not sound_played:
                            sound.play()
                            sound_played = True
                    else:
                        time_since_last_detection += 1
                        if time_since_last_detection >= 30:
                            sound_played = False

                cv2.imshow("yolov8", frame)

                if (cv2.waitKey(30) == 27):
                    break

        except Exception as e:
            print("Error: ", e)
            print("Restarting the script...")
            time.sleep(10)
            subprocess.Popen(["python", "main.py"])


if __name__ == "__main__":
    main()

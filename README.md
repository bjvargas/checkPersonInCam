# checkPersonInCam

This repository contains a Python script that performs real-time object detection using YOLOv8 model from Ultralytics. It captures video from the webcam, detects objects in the frames, and annotates them with bounding boxes. Additionally, it plays a sound whenever a person is detected in the video.

## Setup

1. **Install Python**: Make sure you have Python 3.x installed on your machine.

2. **Create Virtual Environment** (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies**: Install the required dependencies by running:
    ```bash
    pip install ultralytics supervision pygame opencv-python
    ```

## Usage

1. Run the script using the following command:
    ```bash
    python main.py
    ```

2. The script will access your webcam, detect objects in real-time, and annotate the video feed with bounding boxes.

3. If the script encounters an error, it will attempt to restart itself after a 10-second delay.

4. To exit the script, press the `Esc` key.

## Notes

- The YOLOv8 model is loaded from the `yolov8l.pt` file. Make sure the file is present in the same directory as the script.

- The script uses the `ultralytics` library for object detection and the `supervision` library for annotating the bounding boxes.

- The script uses the `pygame` library to play a sound when a person is detected.

- The script keeps track of the time since the last person detection and plays the sound when a person is detected after a certain period.

- If you want to modify the webcam resolution, you can do so by editing the `--webcam-resolution` argument in the `main.py` script.

## Helps

- To use GPU insteed CPU, this could help if your CUDA is 12 +: https://pytorch.org/get-started/locally/, https://discuss.pytorch.org/t/pytorch-for-cuda-12/169447/37?page=2:
    ```pip uninstall torch torchvision
    pip cache purge
    pip install torch==2.0.1+cu118 torchvision -f https://download.pytorch.org/whl/torch_stable.html```

- ```yolo detect predict model=yolov8l.pt source=0 show=true```

- I use this video and repo: https://www.youtube.com/watch?v=QV85eYOb7gk / https://github.com/SkalskiP/yolov8-live

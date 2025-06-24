# Road Lane Line Detection System

This project implements a real-time **Road Lane Line Detection System** using computer vision techniques to enhance road safety by identifying lane markings and overlaying them on driving footage.

---

## Objective

To develop a system that accurately detects lane lines in road images or video streams and provides real-time visual feedback, contributing toward safer driving environments.

---

## Approach

The system is built using classical image processing techniques:
- **Canny Edge Detection**: To detect sharp changes in intensity (lane edges)
- **Region of Interest (ROI) Masking**: To isolate the part of the frame where lane lines are expected
- **Hough Line Transform**: To identify and draw straight lane lines

---

## Project Files

| File              | Description                                 |
|-------------------|---------------------------------------------|
| `lane_detection.py` | Detects lane lines on a static road image   |
| `lane_video.py`     | Detects lane lines in real-time from video  |
| `test_road.jpg`     | Sample road image for testing               |
| `test_video.mp4`    | Road driving footage (user-supplied)        |

---
## Tested Scenarios
- Clear daylight images
- Video footage of straight roads


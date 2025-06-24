import cv2
import numpy as np

def canny_edge(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 50, 150)
    return edges

def region_of_interest(image):
    height = image.shape[0]
    width = image.shape[1]
    mask = np.zeros_like(image)
    polygon = np.array([[
        (int(0.1 * width), height),
        (int(0.9 * width), height),
        (int(0.5 * width), int(0.55 * height))
    ]], np.int32)
    cv2.fillPoly(mask, polygon, 255)
    return cv2.bitwise_and(image, mask)

def display_lines(image, lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 5)
    return line_image

def process_frame(frame):
    canny = canny_edge(frame)
    cropped = region_of_interest(canny)
    lines = cv2.HoughLinesP(
        cropped,
        rho=1,
        theta=np.pi / 180,
        threshold=70,
        minLineLength=50,
        maxLineGap=10
    )
    line_image = display_lines(frame, lines)
    return cv2.addWeighted(frame, 0.8, line_image, 1, 1)

def main():
    cap = cv2.VideoCapture("test_video.mp4") 

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        result = process_frame(frame)
        cv2.imshow("Lane Detection (Video)", result)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
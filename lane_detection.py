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
    polygons = np.array([
        [(int(0.1 * width), height),
         (int(0.9 * width), height),
         (int(0.5 * width), int(0.55 * height))]
    ])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    cropped = cv2.bitwise_and(image, mask)
    return cropped

def display_lines(image, lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 10)
    return line_image

def main():
    image = cv2.imread('test_road.jpg')
    lane_image = np.copy(image)

    edges = canny_edge(lane_image)
    cropped_edges = region_of_interest(edges)
    lines = cv2.HoughLinesP(
        cropped_edges,
        rho=1,
        theta=np.pi / 180,
        threshold=80,
        minLineLength=50,
        maxLineGap=20
    )
    line_image = display_lines(lane_image, lines)
    combo_image = cv2.addWeighted(lane_image, 0.8, line_image, 1, 1)

    cv2.imshow("Original Image", lane_image)
    cv2.imshow("Canny Edges", edges)
    cv2.imshow("ROI Masked", cropped_edges)
    cv2.imshow("Lane Lines", combo_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
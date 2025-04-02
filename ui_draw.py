import cv2
import numpy as np

def draw_interface(frame, small_frame, results):
    display = small_frame.copy()

    offset_x = 30
    offset_y = 50
    padded = cv2.copyMakeBorder(
    small_frame, offset_y, offset_y, offset_x, offset_x,
    cv2.BORDER_CONSTANT,
    value=255  # مشکی در gray یعنی 0
)
    # Optional Convert to BGR if grayscale
    for result in results:
            points = np.array(result[0]).astype(np.int32).reshape((-1, 1, 2))

            # quit()
            points[:, 0,0] += offset_x  # محور x
            points[:, 0,1] += offset_y  # محور y
            cv2.polylines(padded, [points], isClosed=True, color=(0, 255, 0), thickness=2)
            top_point = points[points[:, 0, 1].argmin()][0]
            text_position = (top_point[0], top_point[1] - 10)
            cv2.putText(padded, result[1], text_position, cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 0, 255), 1, cv2.LINE_AA)

    return display,padded
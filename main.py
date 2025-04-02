from camera import Camera
import threading
import cv2
from ocr_engine import Run_ocr
from tts import Text
from ui_draw import draw_interface
camera = Camera()
ocr = Run_ocr()
speaker = Text()
w1 =0
h1 =0
one_show = False
while True:
    frame,small_frame = camera.get_frame_and_small_frame(size=[h1,w1])
    if frame is None:
        break



    

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('o')and not ocr.ocr_running:
        print("Running OCR...")
        # Ability_to_add =True
        # Ability_to_read = True
        small_frame_= small_frame.copy()
        ocr.thread_ocr(small_frame_)
        one_show = True
        # threading.Thread(target=ocr.run,
        #             args=(frame.copy(),)).start()
    elif key == ord('c')and not ocr.ocr_running:
        ocr.results =[]
        speaker.clear_text()
        
    elif key == ord('p')and not ocr.ocr_running:
        speaker.speak_text()


    elif key == ord('h'):
        h1 -= 1       
    elif key == ord('H'):
        h1 += 1
    elif key == ord('w'):
            w1 -= 1     
    elif key == ord('W'):
        w1 += 1

    
    if ocr.results :
        _,padded = draw_interface(frame,small_frame_,ocr.results)
        # cv2.imshow("Webcam2", display)
        cv2.imshow("Webcam3", padded)
    # print(ocr.results)


    if ocr.Ability_to_read and  ocr.results:
        columns = list(zip(*ocr.results))
        ocr.Ability_to_read = False
        try:
            print(columns[1])
            speaker.add_text(columns[1])
        except:
            pass
    
 
    cv2.imshow("Webcam", frame)
    cv2.imshow("Webcam1", small_frame)
    
    




camera.release()
cv2.destroyAllWindows()
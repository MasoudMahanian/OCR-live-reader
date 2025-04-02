import cv2

class Camera:
    def __init__(self, camera_index=0, width=960, height=720):
        self.cap = cv2.VideoCapture(camera_index)
        self.width = width
        self.height = height

        if not self.cap.isOpened():
            raise RuntimeError("[ERROR] Cannot open camera.")

    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret or frame is None:
            print("[ERROR] Failed to grab frame")
            return None

        frame = cv2.resize(frame, (self.width, self.height))
        return frame
    
    def get_frame_and_small_frame(self,gray=True, size = [0,0],main_pic_text=''):
        ret, frame = self.cap.read()
        if not ret or frame is None:
            print("[ERROR] Failed to grab frame")
            return None
        frame = cv2.resize(frame, (self.width, self.height))

        small_frame = frame[self.height*5//10-size[0]:self.height*6//10+size[0], self.width//4-size[1]:self.width*3//4+size[1]]
        if gray:
            small_frame=cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)
        # frame = cv2.resize(small_frame)



        cv2.putText(frame, main_pic_text, (self.width//4,self.height//3-10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.6, (0, 0, 255), 2, cv2.LINE_AA)
    
        lines = [
        "Press o to find word",
        "Press p to read it",
        "Press C to clear DATA",
        "Press H to increase height.",
        "Press W to increase width.",
        "Press h to decrease height.",
        "Press w to decrease width.",
        "Press q to Quit."]
    
        x = 0
        y = 15 #self.height * 2 // 3 + 20 + size[0]
    
        for i, line in enumerate(lines):
            cv2.putText(
                frame,line,(x, y + i * 20),cv2.FONT_HERSHEY_SIMPLEX,0.60,(180, 0, 180),1,cv2.LINE_AA
            )
    
        cv2.rectangle(frame, (self.width//4-size[1], self.height*5//10-size[0]), (self.width*3//4+size[1], self.height*6//10+size[0]), (255, 0, 0), 2)


        return frame, small_frame
        
    
    def release(self):
        self.cap.release()
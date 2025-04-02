import threading
import easyocr
class Run_ocr():
    def __init__(self):
        self.reader = easyocr.Reader(['en'], gpu=True)
        self.ocr_running = False
        self.Ability_to_read = False
        self.first_photo_take =False
        self.results = []

    def run(self,image):
        self.ocr_running = True

        self.results = self.reader.readtext(image)

        self.ocr_running = False
        self.Ability_to_read = True
        self.first_photo_take =False

    def thread_ocr(self,image):
        threading.Thread(target=self.run,
                    args=(image.copy(),)).start() 

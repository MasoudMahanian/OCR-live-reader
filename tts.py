import pyttsx3


class Text():
    def __init__(self):
        self.text = ''
        self.engine = pyttsx3.init()
    def add_text(self, new_texts, replay = True):
        added_text = ''
        for new_text in new_texts:
            self.text += new_text + ' '
            added_text += new_text + ' '
        if replay:
            self.engine.say(added_text)
            self.engine.runAndWait()
    def clear_text(self):
        self.text = ''
    def speak_text(self):
        print(f"[TTS] Speaking: {self.text}")
        self.engine.say(self.text)
        self.engine.runAndWait()
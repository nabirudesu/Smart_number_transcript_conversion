from gtts import gTTS
import os

dinar_text= " السلام عليكم و رحمة الله و بركاته "

def text_to_voice(dinar_text):
    gtts_object = gTTS(dinar_text, lang='ar', slow=False)
    dinar_voice=gtts_object.save("dinar_voice.mp3")
    return dinar_voice


text_to_voice(dinar_text)
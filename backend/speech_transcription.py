import whisper
import numpy as np
import Levenshtein
import re
from numbers_to_words import dinar_number_to_arabic_words

def Similarity_correction(transcript, word_list):
    replaced_sentence = []
    for word in transcript.split():
        max_similarity = 0
        best_match = None
        for target_word in word_list:
            distance = Levenshtein.distance(word, target_word)
            max_length = max(len(word), len(target_word))
            similarity = 1 - (distance / max_length)  # Normalize distance to similarity
            if similarity > max_similarity:
                max_similarity = similarity
                best_match = target_word
        replaced_sentence.append(best_match if best_match else word)
    return " ".join(replaced_sentence)


# data to use for correction
def arabic_audio_transcript(filename):
    # Loading the model
    model = whisper.load_model("medium")

    # Transcribe the audio
    try:
        result = model.transcribe(filename,language='ar',fp16=False,verbose=True)
        print("Transcription:", result["text"])
        audio_transcript= result["text"]
        word_list =['و','جزائري','دينار','واحد','اثنان','ثلاثة','أربعة','خمسة','ستة','سبعة','ثمانية','تسعة','عشرة','أحد عشر','اثنا عشر','عشر','عشرون','ثلاثون','أربعون','خمسون','ستون','سبعون','ثمانون','تسعون','مائة','مئتان','ثلاثمائة','أربعمائة','خمسمائة','ستمائة','سبعمائة','ثمانمائة','تسعمائة','ألف','الفان','ألفا','آلاف','مليار','ملياران','مليارات','مليون','مليونان','ملايين']

        #similarity_scores=[]
        numbers_in_result= re.findall(r'\d+', audio_transcript)
        for i in numbers_in_result:
            converted_numbers= dinar_number_to_arabic_words(int(i))
            text_audio_trascript=re.sub(r'\d+',converted_numbers,audio_transcript)
        final_transcript = Similarity_correction(text_audio_trascript,word_list)
    except Exception as e:
        return "التسجيل الصوتي خاطئ أو غير قابل للتحويل"
    return(final_transcript)


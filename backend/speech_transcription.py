import whisper
import numpy as np
import Levenshtein
import re
from numbers_to_words import dinar_number_to_arabic_words
from openai import AzureOpenAI
    
client = AzureOpenAI(
    api_key="your_api_key",  
    api_version="2024-02-01",
    azure_endpoint = "your_azure_endpoint"
)

deployment_id = "voice-transcription" #This will correspond to the custom name you chose for your deployment when you deployed a model."
audio_test_file = "backend_audio.wav"
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
    # Transcribe the audio
    try:
        # Loading the model
        result = client.audio.transcriptions.create(file=open(filename, "rb"), model=deployment_id)
        print("Transcription:", result.text)
        audio_transcript= result.text
        word_list =['و','جزائري','دينار','واحد','اثنان','ثلاثة','أربعة','خمسة','ستة','سبعة','ثمانية','تسعة','عشرة','أحد عشر','اثنا عشر','عشر','عشرون','ثلاثون','أربعون','خمسون','ستون','سبعون','ثمانون','تسعون','مائة','مئتان','ثلاثمائة','أربعمائة','خمسمائة','ستمائة','سبعمائة','ثمانمائة','تسعمائة','ألف','الفان','ألفا','آلاف','مليار','ملياران','مليارات','مليون','مليونان','ملايين']

        #similarity_scores=[]
        if any(char.isdigit() for char in audio_transcript):
            numbers_in_result= re.findall(r'\d+', audio_transcript)
            for i in numbers_in_result:
                converted_numbers= dinar_number_to_arabic_words(int(i))
                text_audio_trascript=re.sub(r'\d+',converted_numbers,audio_transcript)
            final_transcript = Similarity_correction(text_audio_trascript,word_list)
        else :
            final_transcript = Similarity_correction(audio_transcript,word_list)
    except Exception as e:
        print(e)
        return "التسجيل الصوتي خاطئ أو غير قابل للتحويل"
    return(final_transcript)


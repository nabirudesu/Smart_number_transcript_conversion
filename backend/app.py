from flask import Flask,request,jsonify
from numbers_to_words import dinar_number_to_arabic_words
from speech_transcription import arabic_audio_transcript
from flask_cors import CORS, cross_origin
import logging
# WE will create a flask app here
# we will create the prpocess of conversion and expose the endpoint of every function we have

app = Flask(__name__)
CORS(app)

# Define a route for handling POST requests to transcribe audio
#@app.route('/num_to_words', methods=['POST'])
@app.post("/number_to_words")
def convert_to_words():
    # Assuming you receive audio data in the request body
    data = request.json
    if data["currency"]=="Dinar":
        number_in_words=dinar_number_to_arabic_words(int(data["number"]))
    else :     
        number_in_words=dinar_number_to_arabic_words(int(int(data["number"])/100))
    # Return the transcription result as JSON
    return jsonify({'transcription': number_in_words+' دينار جزائري'})
# Define a route for handling POST requests to transcribe audio
#@app.route('/num_to_voice', methods=['POST'])
@app.get("/num_to_voice")
def convert_to_voice():
    # Assuming you receive audio data in the request body
    number = request.data
    print(number)
    # Perform transcription logic here
    
    # Return the transcription result as JSON
    return jsonify({'transcription': 'Your voice result'})
# Define a route for handling POST requests to transcribe audio
#@app.route('/voice_to_words', methods=['POST'])
@app.post("/voice_to_words")
def transcribe_audio():
    # Assuming you receive audio data in the request body
    audio_data = request.files["audio"]
    filename="./backend_audio.wav"
    audio_data.save(filename)
    transcript = arabic_audio_transcript(filename)
    
    # Return the transcription result as JSON
    return jsonify({'transcription': transcript})



if __name__=='__main__':
    app.run(host="0.0.0.0",port=5000)


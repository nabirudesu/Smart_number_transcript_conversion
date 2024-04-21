import React from 'react'

import AudioReactRecorder, { RecordState } from 'audio-react-recorder'
import '../App.css'

class AudioRecorder extends React.Component {
  constructor(props) {
    super(props)

    this.state = {
      recordState: null,
      audioData: null,
      dinarWords: null,
      isRecording:false
    }
  }
  componentDidMount() {
    const canvas = document.querySelector('canvas');
    canvas.style.width = '350px'
    canvas.style.height = '80px'
  }
  click =() => {
    if (this.state.recordState == "stop" || this.state.recordState == null){
      this.setState({
        recordState: RecordState.START,
        isRecording: true
      })
    } else if (this.state.recordState == "start"){
      this.setState({
        recordState: RecordState.STOP,
        isRecording: false
      })

    }
  }
  onStop = async (audioData) => {
    
    const audioBlob = audioData.blob;
    const audioFile = new File([audioBlob], 'backend_audio.wav', { type: 'audio/wav' });
  
    const formData = new FormData();
    formData.append('audio', audioFile);
  
    const response = await fetch('http://127.0.0.1:5000/voice_to_words', {
      method: 'POST',
      body: formData,
    }).then((response) => response.json()).then((data) => data.transcription)
    this.setState(
      {dinarWords: response}
    )
    console.log(this.dinarWords)
    console.log(response);
  }
  result = () => (
    <div className='w-full'>
      <h1 dir='rtl' className='text-xl text-green-300 mb-2'>
        النتيجة
      </h1>
      <div className='bg-gray-200 text-slate-900 color-slate-900 py-2 rounded-md'>
        <p dir='rtl' className='text-xl h-20 p-1.5'>
          {/* display the value rended from the backend dinar_number_to_arabic_words */}
          {this.state.dinarWords}
        </p>
      </div>
    </div>
  );
  render() {
    const { recordState } = this.state
    return (
      <div > 
        <div className='flex justify-center gap-10 flex-col'>
          <div className='flex flex-col gap-10 w-full'>
            <div className='flex justify-evenly flex-wrap gap-2'>
              <AudioReactRecorder state={recordState} onStop={this.onStop} backgroundColor='rgb(255,255,255)' />              
              <div className='flex flex-col gap-4'>
                <label type=" rtl"> التسجيل صوتي</label>
                <button id='record' onClick={this.click} dir='rtl' className='bg-blue-500 text-white w-full px-2 py-1 rounded-md hover:bg-blue-400 transition-colors'>
                  {this.state.isRecording
                  ? "تسجيل . . ."
                  : "سجل"}
                </button>
              </div>

            </div>
          </div>       
        </div>
        <this.result/>
      </div>)}
}

export default AudioRecorder
import React from 'react'

import AudioReactRecorder, { RecordState } from 'audio-react-recorder'
import '../App.css'

class AudioRecorder extends React.Component {
  constructor(props) {
    super(props)

    this.state = {
      recordState: null,
      audioData: null,
      dinarWords: null
    }
  }
  componentDidMount() {
    const canvas = document.querySelector('canvas');
    canvas.style.width = '250px'
    canvas.style.height = '100px'
  }
/*  start = () => {
    this.setState({
      recordState: RecordState.START
    })
  }

  pause = () => {
    this.setState({
      recordState: RecordState.PAUSE
    })
  }

  stop = () => {
    this.setState({
      recordState: RecordState.STOP
    })
  } */
  click =() => {
    if (this.state.recordState == "stop" || this.state.recordState == null){
      this.setState({
        recordState: RecordState.START
      })
    } else if (this.state.recordState == "start"){
      this.setState({
        recordState: RecordState.STOP
      })

    }
  }
  onStop = async (audioData) => {
    
    const audioBlob = audioData.blob;
    const audioFile = new File([audioBlob], 'recordedAudio.wav', { type: 'audio/wav' });
  
    const formData = new FormData();
    formData.append('audio', audioFile);
  
    const response = await fetch('http://127.0.0.1:5000/voice_to_words', {
      method: 'POST',
      body: formData,
    }).then((response) => response.json()).then((data) => data.transcription)
    this.setState(
      {dinarWords: response}
    )
    console.log(response);
  }

  render() {
    const { recordState } = this.state

    return (
      <section className='bg-opacity-60 lg:w-4/5 w-4/5 bg-black p-8 rounded-xl'> 
        <h1 dir='rtl' className='text-3xl text-white'>
          تحويل الأعداد العربية إلى ما يقابلها كتابة
        </h1>
        <div className='flex justify-center gap-10 flex-col'>
          <div className='flex flex-col gap-10 w-full'>
            <div className='flex justify-evenly flex-wrap gap-2'>
              <AudioReactRecorder state={recordState} onStop={this.onStop} backgroundColor='rgb(255,255,255)' />
              <audio id='audio' controls src={this.state.audioData ? this.state.audioData.url : null} />
              <button id='record' onClick={this.click} dir='rtl' className='bg-blue-500 text-white size-16 px-2 py-1 rounded-md hover:bg-blue-400 transition-colors'>
                Record
              </button>
            </div>
          </div>       
        </div>
        <div className='w-full'>
          <h1 dir='rtl' className='text-xl text-green-300'>
            النتيجة
          </h1>
          <div className='bg-gray-200 text-slate-900 color-slate-900 py-2 rounded-md h-full'>
            <p dir='rtl' className='text-xl'>
              {this.dinarWords}
            </p>
          </div>
        </div>
      </section>)}
}

export default AudioRecorder
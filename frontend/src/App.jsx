import './App.css';
import CalculateForm from './components/CalculateForm.jsx';
import AudioRecorder from './components/AudioRecorder.jsx';
import NavBar from './components/NavBar.jsx';
function App() {
  return (
    <div className='app h-screen text-white flex items-center bg-cover bg-center'>
      <main className='container mx-auto flex justify-center align-center'>
        {/*<NavBar/>*/}
        <CalculateForm />
        {/*<AudioRecorder />*/}
      </main>
    </div>
  );
}

export default App;

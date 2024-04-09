import './App.css';
import CalculateForm from './components/CalculateForm.jsx';

function App() {
  return (
    <div className='app h-screen text-white flex items-center bg-cover bg-center'>
      <main className='container mx-auto flex justify-center align-center'>
        <CalculateForm />
      </main>
    </div>
  );
}

export default App;

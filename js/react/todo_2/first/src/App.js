import logo from './logo.svg';
import './App.css';
import FirstWelcome from './first'; 
import Greet from './greet';  
import CounterClass from './Counter';

function App() {
  return (
    <div>
    <FirstWelcome name="Alice"/>
    <FirstWelcome name="Bob"/>
    <Greet name="Alice"/>
    <CounterClass/>
      </div>
      
  );
}

export default App;

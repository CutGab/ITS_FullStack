import './App.css';
import Card from './card';
import "./styles.css";
import { useEffect, useState } from 'react';

function App() {

  const [mode, setLightDarkMode] = useState("light");

  useEffect(() => {
    console.log(document.body)
    if (mode === "light") {
      document.body.style.backgroundColor = "white";
    } else {
      document.body.style.backgroundColor = "black";
    }
  }, [mode]);

  const setMode = () => {
    if (mode === "light") {
      setLightDarkMode("dark");
    } else {
      setLightDarkMode("light");
    }
  };

  return (
    <div className="App">

      <Card func={setMode} mode={mode}/>
      <Card func={setMode} mode={mode}/>
      <Card func={setMode} mode={mode}/>

      <div>
        <button className="button" onClick={setMode}> ☀️/🌛 </button>
      </div>

    </div>
  );
}

export default App;

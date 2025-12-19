import React, { useState } from "react";
import "./styles.css";

function Card(props) {
    const [style, setStyleColor] = useState("black");

    const changeTextColor = () => {
        if(style == "black") {
            setStyleColor("red")
        } else {
            setStyleColor("black")
        }
    }

  return (
    
    <div className={`card ${props.mode}`}>

        <img src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTq00uXqOWNZb9Hcc-i0DPZk7MRQRyzxNV-3g&s" alt="Pesce" />
        <h1> Card Title </h1>
        <h3 className={`${style} ${props.mode}`} onClick={changeTextColor}> Card Content </h3>

    </div>
  );
}

export default Card;

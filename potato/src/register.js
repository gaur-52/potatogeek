import React, { useState } from "react";
import axios from 'axios'
export default function Register() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [prediction, setPrediction] = useState(null);
  
  const changeHandler = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleSubmit = () => {
    const formData2 = new FormData();
  formData2.append(
  "file",
  selectedFile,
  selectedFile.name
  );

  axios.post('http://127.0.0.1:8000/apk',formData2)
    .then(res=> setPrediction(res.data.prediction))
    // .then(result=>console.log(result))
  };

  return (
    <div>
      <input
        name="image"
        type="file"
        onChange={changeHandler}
        accept=".jpeg, .png, .jpg"
      />
      <br/>
      <button onClick={handleSubmit}>submit</button>
      <br/>
      {prediction!=null&&
      <h1>prediction={prediction}</h1>
    }
    </div>
  );
}

import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [quote, setQuote] = useState("");


  return (
    <div className="App" style={{ display: "flex", justifyContent: "center", alignItems: "center", height: "100vh", textAlign: "center" }}>
      <div>
        <h1>Quote of the Day</h1>
        <button 
          onClick={() => {
            axios
              .get("https://quote-app-xsa5.onrender.com/quote")
              .then((response) => setQuote(response.data.quote))
              .catch((error) => console.error(error));
          }} 
          style={{ 
            padding: "10px 20px", 
            fontSize: "16px", 
            backgroundColor: "#4CAF50", 
            color: "white", 
            border: "none", 
            borderRadius: "5px", 
            cursor: "pointer" 
          }}
        >
          Get Quote
        </button>
        <div style={{ height: "100px", display: "flex", alignItems: "center", justifyContent: "center" }}>
          {quote && <p>{quote}</p>}
        </div>
      </div>
    </div>
  );
}

export default App;

import {useEffect, useState} from "react";

export default function App() {
  const [fact, setFact] = useState("");
  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = () => {
    fetch("http://127.0.0.1:8000/")
        .then((result) => result.json())
        .then((data) => setFact(data.message));
  };

  return (
      <h1>{fact}</h1>
  );
}
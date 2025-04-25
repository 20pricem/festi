import { useEffect, useState } from "react";

function App() {
  const [artists, setArtists] = useState<string[]>([]);

  const fetchArtists = async () => {
    const res = await fetch("http://localhost:5000/api/top-artists");
    const data = await res.json();
    setArtists(data.artists || []);
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1 style={{ marginBottom: '20px' }}>My Lolla Schedule Generator</h1>
      <button 
        style={{
          backgroundColor: '#319795', 
          color: 'white', 
          padding: '10px 20px', 
          border: 'none', 
          borderRadius: '5px',
          cursor: 'pointer',
        }} 
        onClick={fetchArtists}>
        Load My Top Spotify Artists
      </button>
      <div style={{ marginTop: '20px' }}>
        {artists.length > 0 ? (
          artists.map((artist, idx) => (
            <p key={idx}>{artist}</p>
          ))
        ) : (
          <p>No artists loaded yet.</p>
        )}
      </div>
    </div>
  );
}

export default App;
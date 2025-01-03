import React, { useState } from 'react';
import { startSharding } from '../services/api';

function ShardView() {
  const [algorithm, setAlgorithm] = useState('hash');
  const [filename, setFilename] = useState('');

  const handleSharding = () => {
    if (!filename) {
      alert('Please enter a filename');
      return;
    }

    startSharding(filename, algorithm)
      .then((response) => alert(response.data.message))
      .catch((error) => console.error('Sharding failed:', error));
  };

  return (
    <section>
      <h2>Start Sharding</h2>
      <input
        type="text"
        placeholder="Enter uploaded filename"
        value={filename}
        onChange={(e) => setFilename(e.target.value)}
      />
      <select value={algorithm} onChange={(e) => setAlgorithm(e.target.value)}>
        <option value="hash">Hash</option>
        <option value="kmeans">KMeans</option>
        <option value="dbscan">DBSCAN</option>
      </select>
      <button onClick={handleSharding}>Start Sharding</button>
    </section>
  );
}

export default ShardView;

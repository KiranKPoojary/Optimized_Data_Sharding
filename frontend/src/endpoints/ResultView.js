import React, { useEffect, useState } from 'react';
import { getResults } from '../services/api';

function ResultView() {
  const [metadata, setMetadata] = useState([]);

  useEffect(() => {
    getResults()
      .then((response) => setMetadata(response.data))
      .catch((error) => console.error('Failed to fetch metadata:', error));
  }, []);

  return (
    <section>
      <h2>Shard Details</h2>
      {metadata.map((shard, index) => (
        <div key={index}>
          <p>File: {shard.shard_file}</p>
          <p>Rows: {shard.rows}</p>
          <p>Columns: {shard.columns.join(', ')}</p>
        </div>
      ))}
    </section>
  );
}

export default ResultView;

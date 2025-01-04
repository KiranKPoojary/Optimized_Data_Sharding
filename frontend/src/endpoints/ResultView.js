import React from 'react';

function ResultView({ metadata }) {
  // Check if metadata is valid before attempting to map
  if (!metadata || metadata.length === 0) {
    return <p>No results available.</p>;
  }

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

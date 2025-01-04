import React, { useEffect, useState } from 'react';
import { getShardingStatus, getResults, resetSharding } from '../services/api';
import ResultView from './ResultView';

function MonitorView() {
  const [status, setStatus] = useState('Idle');
  const [message, setMessage] = useState('');
  const [elapsedTime, setElapsedTime] = useState(0);
  const [results, setResults] = useState(null);

  useEffect(() => {
    let interval = null;

    // Auto-reset sharding when the page is about to unload (refresh/close)
    const resetOnUnload = () => {
      fetch('http://127.0.0.1:5000/reset_sharding', {
        method: 'POST',
      }).catch((error) => {
        console.error('Failed to reset sharding on page unload:', error);
      });
    };

    // Add the beforeunload event listener to reset sharding on refresh
    window.addEventListener('beforeunload', resetOnUnload);

    const fetchData = async () => {
      try {
        const response = await getShardingStatus();
        setStatus(response.data.status);
        setMessage(response.data.message);

        if (response.data.status === 'In Progress') {
          setElapsedTime(response.data.elapsed_time);
        } else if (response.data.status === 'Completed') {
          clearInterval(interval); // Stop polling when sharding is completed
          try {
            const resultResponse = await getResults();
            setResults(resultResponse.data);
          } catch (error) {
            console.error('Failed to fetch results:', error);
          }
        }
      } catch (error) {
        console.error('Error fetching sharding status:', error);
      }
    };

    // Start polling only when the status is not Completed
    if (status !== 'Completed') {
      interval = setInterval(fetchData, 2000);
    }

    return () => {
      clearInterval(interval); // Cleanup on unmount
      window.removeEventListener('beforeunload', resetOnUnload); // Clean up event listener
    };
  }, [status]); // Depend on `status` to re-evaluate polling

  const handleClear = () => {
    setStatus('Idle');
    setMessage('');
    setElapsedTime(0);
    setResults(null);

    sessionStorage.clear();

    resetSharding()
      .then(() => {
        console.log('Sharding reset successfully');
      })
      .catch((error) => {
        console.error('Failed to reset sharding:', error);
      });
  };

  return (
    <section>
      <h2>Sharding Status</h2>
      <p><strong>Status:</strong> {status}</p>
      <p><strong>Message:</strong> {message}</p>
      {status === 'In Progress' && (
        <p><strong>Elapsed Time:</strong> {elapsedTime} seconds</p>
      )}

      <h2>Sharding Results</h2>
      {results ? (
        <ResultView metadata={results} />
      ) : (
        <p>Waiting for sharding to complete...</p>
      )}

      <button onClick={handleClear}>Clear</button>
    </section>
  );
}

export default MonitorView;

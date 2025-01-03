import React, { useEffect, useState } from 'react';
import { getShardingStatus } from '../services/api';

function MonitorView() {
  const [status, setStatus] = useState({});

  useEffect(() => {
    const interval = setInterval(() => {
      getShardingStatus().then((response) => setStatus(response.data));
    }, 2000);

    return () => clearInterval(interval);
  }, []);

  return (
    <section>
      <h2>Sharding Progress</h2>
      <p>Status: {status.status}</p>
      <p>Message: {status.message}</p>
    </section>
  );
}

export default MonitorView;

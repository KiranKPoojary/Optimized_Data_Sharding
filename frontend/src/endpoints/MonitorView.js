import React, { useEffect } from 'react';
import { initWebSocket, closeWebSocket } from '../services/websocket';

function MonitorView({ shardingStatus, setShardingStatus }) {
  useEffect(() => {
    initWebSocket((data) => setShardingStatus(data));

    return () => closeWebSocket();
  }, [setShardingStatus]);

  return (
    <section>
      <h2>Sharding Progress</h2>
      <p>Status: {shardingStatus.status}</p>
      <p>Message: {shardingStatus.message}</p>
    </section>
  );
}

export default MonitorView;

import React, { useState } from 'react';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import UploadView from './endpoints/UploadView';
import ShardView from './endpoints/ShardView';
import MonitorView from './endpoints/MonitorView';
import ResultView from './endpoints/ResultView';

function App() {
  const [shardingStatus, setShardingStatus] = useState({ status: 'Idle', message: '' });

  return (
    <>
      <Navbar />
      <div className="container">
        <UploadView />
        <ShardView />
        <MonitorView shardingStatus={shardingStatus} setShardingStatus={setShardingStatus} />
        <ResultView />
      </div>
      <Footer />
    </>
  );
}

export default App;

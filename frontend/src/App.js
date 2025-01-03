import React from 'react';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import UploadView from './endpoints/UploadView';
import ShardView from './endpoints/ShardView';
import MonitorView from './endpoints/MonitorView';
import ResultView from './endpoints/ResultView';

function App() {
  return (
    <>
      <Navbar />
      <div className="container">
        <UploadView />
        <ShardView />
        <MonitorView />
        <ResultView />
      </div>
      <Footer />
    </>
  );
}

export default App;

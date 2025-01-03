//import axios from 'axios';

//axios.defaults.baseURL = 'http://127.0.0.1:5000/';

//export const uploadFile = (formData) => axios.post('/upload', formData);
//export const startSharding = (filename, algorithm) =>
//  axios.post('/start_sharding', { filename, algorithm });
//export const getShardingStatus = () => axios.get('/sharding_status');
//export const getResults = () => axios.get('/results');


import axios from 'axios';

axios.defaults.baseURL = 'http://127.0.0.1:5000'; // Backend URL

// Upload File
//export const uploadFile = (formData) => axios.post('/upload', formData);
export const uploadFile = (formData) =>
  axios.post('/upload', formData, {
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  });
// Start Sharding
export const startSharding = (filename, algorithm) =>
  axios.post('/start_sharding', { filename, algorithm });

// Fetch Results (Metadata)
export const getResults = () => axios.get('/results');

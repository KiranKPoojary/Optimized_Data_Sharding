import axios from 'axios';

axios.defaults.baseURL = 'http://127.0.0.1:5000/';

export const uploadFile = (formData) => axios.post('/upload', formData);
export const startSharding = (filename, algorithm) =>
  axios.post('/start_sharding', { filename, algorithm });
export const getShardingStatus = () => axios.get('/sharding_status');
export const getResults = () => axios.get('/results');

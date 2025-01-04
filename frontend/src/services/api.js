import axios from 'axios';

// Set default base URL
axios.defaults.baseURL = 'http://127.0.0.1:5000'; // Backend URL

// Global timeout for all requests (optional)
axios.defaults.timeout = 10000; // Set timeout to 10 seconds (adjustable)

axios.interceptors.response.use(
  (response) => response,
  (error) => {
    // Handle global errors
    if (error.response) {
      // Server responded with a status other than 2xx
      console.error(`Error: ${error.response.status}, ${error.response.data}`);
    } else if (error.request) {
      // No response received from the server
      console.error("No response from server");
    } else {
      // Other errors
      console.error("Error", error.message);
    }
    return Promise.reject(error);
  }
);

// Upload File
export const uploadFile = (formData) =>
  axios.post('/upload', formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });

// Start Sharding
export const startSharding = (filename, algorithm) =>
  axios.post('/start_sharding', { filename, algorithm });

// Get Sharding Status
export const getShardingStatus = () => axios.get('/sharding_status');

// Fetch Results (Metadata)
export const getResults = () => axios.get('/results');

export const resetSharding = async () => {
  try {
    const response = await fetch('http://127.0.0.1:5000/reset_sharding', {
      method: 'POST',
    });

    if (!response.ok) {
      throw new Error('Failed to reset sharding');
    }

    return response.json();  // Return the response if needed
  } catch (error) {
    console.error('Error resetting sharding:', error);
    throw error;
  }
};
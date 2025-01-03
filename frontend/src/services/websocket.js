
let socket = null;

export const initWebSocket = (onMessage) => {
  socket = new WebSocket('ws://127.0.0.1:5000/ws/sharding_status');

  socket.onopen = () => console.log('WebSocket Connected');
  socket.onmessage = (event) => onMessage(JSON.parse(event.data));
  socket.onerror = (error) => console.error('WebSocket Error:', error);
  socket.onclose = () => console.log('WebSocket Closed');
};

export const closeWebSocket = () => {
  if (socket) socket.close();
};

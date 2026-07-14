const express = require('express');
const app = express();

app.use(express.json());

app.post('/api/chat', (req, res) => {
  const { message } = req.body;
  console.log('받은 메시지:', message);
  res.json({ ok: true, receivedMessage: message });
});

app.listen(3000, '0.0.0.0', () => {
  console.log('서버 실행: http://localhost:3000');
  console.log('같은 네트워크: http://192.168.10.8:3000');
});

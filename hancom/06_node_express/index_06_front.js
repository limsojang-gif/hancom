const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });

rl.question('메시지: ', (message) => {
  fetch('http://192.168.10.32:3000/api/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message })
  })
    .then((response) => response.json())
    .then(console.log)
    .catch((error) => console.log('서버 연결 실패:', error.message))
    .finally(() => rl.close());
});

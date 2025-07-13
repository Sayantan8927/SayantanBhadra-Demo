const responses = {
  help: "I'm here to assist you with anything on this site!",
  product: "Our top products include Smart TVs, iPhones, and Printers.",
  signup: "Sign-up will be available very soon. Stay tuned!",
};

function sendMessage() {
  const input = document.getElementById('userInput');
  const text = input.value.trim().toLowerCase();
  if (!text) return;

  const chatBody = document.getElementById('chat-body');
  const userMsg = document.createElement('div');
  userMsg.textContent = '🧑 You: ' + input.value;
  chatBody.appendChild(userMsg);

  const aiMsg = document.createElement('div');
  let reply = responses[text] || `🤖 AI: I'm still learning! Please ask another question.`;
  aiMsg.textContent = reply;
  chatBody.appendChild(aiMsg);

  chatBody.scrollTop = chatBody.scrollHeight;
  input.value = '';
}
function toggleChat() {
  const chatbot = document.getElementById('chatbot');
  chatbot.classList.toggle('show');
}
fetch('https://api.openai.com/v1/chat/completions', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer YOUR_API_KEY'
  },
  body: JSON.stringify({
    model: 'gpt-3.5-turbo',
    messages: [{ role: 'user', content: text }]
  })
})
.then(res => res.json())
.then(data => {
  aiMsg.textContent = '🤖 AI: ' + data.choices[0].message.content;
});

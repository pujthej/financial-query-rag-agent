import { useState } from 'react';
import axios from 'axios';

function App() {
  const [query, setQuery] = useState('');
  const [chat, setChat] = useState([
    { sender: 'bot', text: 'Hello! How can I assist you today?' }
  ]);

  const sendQuery = async () => {
    if (!query.trim()) return;

    const userMessage = { sender: 'user', text: query };
    setChat((prev) => [...prev, userMessage]);

    try {
      const res = await axios.get(`http://localhost:8000/?query=${encodeURIComponent(query)}`);
      const botMessage = { sender: 'bot', text: res.data };
      setChat((prev) => [...prev, botMessage]);
    } catch (err) {
      setChat((prev) => [...prev, { sender: 'bot', text: '⚠️ Error connecting to backend' }]);
    }

    setQuery('');
  };

  return (
    <div className="h-screen w-screen flex items-center justify-center bg-gradient-to-br from-gray-900 to-gray-800 text-white">
      <div className="w-full max-w-2xl h-[80vh] bg-gray-900 shadow-2xl rounded-xl p-6 flex flex-col">
        <h1 className="text-3xl font-bold text-center mb-4">FinQuery</h1>

        <div className="flex-1 overflow-y-auto space-y-3 pr-2">
          {chat.map((msg, i) => (
            <div key={i} className={`flex ${msg.sender === 'user' ? 'justify-end' : 'justify-start'}`}>
              <div className={`max-w-[70%] px-4 py-2 rounded-lg text-sm ${
                msg.sender === 'user' ? 'bg-blue-600' : 'bg-gray-700'
              }`}>
                {msg.text}
              </div>
            </div>
          ))}
        </div>

        <div className="mt-4 flex gap-2">
          <input
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && sendQuery()}
            className="flex-1 px-4 py-2 rounded-lg bg-gray-800 text-white border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="Type your question..."
          />
          <button
            onClick={sendQuery}
            className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg"
          >
            Send
          </button>
        </div>
      </div>
    </div>
  );
}

export default App;
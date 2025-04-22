# 🧠 Memory-Powered MCP Chat with LangChain & OpenAI

This project implements an interactive memory-enabled conversational agent using LangChain's `ChatOpenAI`, a custom `MCPAgent`, and an MCP-compatible backend client defined in `mcp_use`. The assistant supports contextual conversation memory, configurable OpenAI models, and interactive terminal-based chatting.

---

## 🚀 Features

- ✅ Conversational memory using LangChain
- 🤖 GPT-4o-mini (or any OpenAI model)
- 🗃️ Loads config from `browser_mcp.json`
- 🔁 Supports up to 15 reasoning steps
- ✨ Clear memory and exit options
- 🔐 `.env` support for managing secrets

---

## 🧩 Project Structure

```
.
├── browser_mcp.json         # Configuration file for MCPClient
├── app.py                   # Main script for interactive chat
├── .env                     # Contains OPENAI_API_KEY
└── README.md                # Project documentation
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Ajaytherala/mcpdemo.git
cd mcpdemo
```

### 2. Create and Configure `.env`

Create a `.env` file in the root directory and add your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
```


---

## 🧪 Run the Chat

```bash
uv run app.py
```

### In Chat:

- Type your message to start the conversation.
- Type `clear` to reset memory.
- Type `exit` or `quit` to leave the chat.

---

## 🧠 Customization

- **Model**: Change the model in the `ChatOpenAI` instance (default: `"gpt-4o-mini"`).
- **Memory Steps**: Modify `max_steps` in the `MCPAgent` initialization.
- **Client Config**: Update `browser_mcp.json` with your backend endpoints or connection details.



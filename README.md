# Multi-Agentic AI — Minimal Python Codebase

This repository demonstrates two multi-agent architectures:

1. **Ollama-based System**: Uses local LLM (Llama3 via Ollama) with Planner → Worker → Reviewer workflow
2. **Async Message-Bus System**: Lightweight async framework with Planner → Developer → Tester workflow

## 🏗️ Architecture

### System 1: Ollama-based Multi-Agent System

Uses Ollama (running locally) to orchestrate three specialized agents:
- **Planner Agent**: Breaks down goals into actionable steps
- **Worker Agent**: Executes the planned tasks
- **Reviewer Agent**: Reviews and improves the output
- **Orchestrator**: Coordinates the workflow between all agents

### System 2: Async Message-Bus System

Lightweight async framework where agents communicate via a central MessageBus:
- **Planner Agent**: Receives goals and decomposes them into tasks
- **Developer Agent**: Takes tasks and produces artifacts
- **Tester Agent**: Verifies artifacts and reports results
- **MessageBus**: Routes messages between agents asynchronously

## 📋 Prerequisites

1. **Python 3.7+** installed on your system
2. **Ollama** (for System 1 only) - installed and running
3. **llama3 model** (for System 1 only) - pulled in Ollama

### Installing Ollama (System 1 only)

1. Visit [https://ollama.ai](https://ollama.ai) and download Ollama for your operating system
2. Install Ollama following the instructions for your OS
3. Start Ollama server:
   ```bash
   ollama serve
   ```
4. Pull the llama3 model:
   ```bash
   ollama pull llama3
   ```

## 🚀 Installation

1. **Clone or navigate to this repository:**
   ```bash
   cd multiagent
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   This will install:
   - `openai==1.40.0` - OpenAI Python client (works with Ollama's OpenAI-compatible API)
   - `python-dotenv` - For environment variable management
   - `streamlit` - For web UI (optional)
   - `rich` - For pretty logging (optional)

## 🎯 Running the Systems

### System 1: Ollama-based Multi-Agent System

1. **Make sure Ollama is running:**
   ```bash
   ollama serve
   ```
   The server should be running at `http://localhost:11434`

2. **Verify llama3 model is available:**
   ```bash
   ollama list
   ```
   You should see `llama3` in the list.

3. **Run the multi-agent system:**
   ```bash
   python3 run.py
   ```
   
   Or on some systems:
   ```bash
   python run.py
   ```

4. **Run with Web UI (Streamlit):**
   ```bash
   streamlit run ui_app.py
   ```
   Then open your browser at `http://localhost:8501`

### System 2: Async Message-Bus System

Run the async message-bus based system:

```bash
python3 run_async.py
```

This demonstrates agents communicating via async message passing.

## 📁 Project Structure

```
multiagent/
├── agent_framework/          # Async message bus framework
│   ├── __init__.py
│   ├── bus.py               # MessageBus implementation
│   └── agent.py             # BaseAgent for async agents
├── agents/                   # Ollama-based agents
│   ├── __init__.py
│   ├── base_agent.py        # Base agent class
│   ├── planner.py           # Planner agent
│   ├── worker.py            # Worker agent
│   └── reviewer.py          # Reviewer agent
├── agents_async/             # Async message-bus agents
│   ├── __init__.py
│   ├── planner.py           # Planner agent (async)
│   ├── developer.py         # Developer agent (async)
│   └── tester.py            # Tester agent (async)
├── llm_client.py            # Ollama client wrapper
├── orchestrator.py          # Orchestrates Ollama-based workflow
├── run.py                   # Main entry point (Ollama system)
├── run_async.py             # Main entry point (async system)
├── ui_app.py                # Streamlit web UI
├── requirements.txt         # Python dependencies
└── README.md                # This file
```

## 🔧 How It Works

### System 1: Ollama-based System

1. **Planning Phase**: The Planner Agent receives a goal and breaks it down into 3-7 clear steps
2. **Execution Phase**: The Worker Agent executes the planned steps and produces results
3. **Review Phase**: The Reviewer Agent reviews, improves, and corrects the output

The Orchestrator coordinates all three phases sequentially.

### System 2: Async Message-Bus System

1. **Message Bus**: Central communication hub that routes messages between agents
2. **Agent Communication**: Agents send messages to specific recipients or broadcast to all
3. **Async Processing**: Each agent runs in its own async task loop
4. **Workflow**: Planner → Developer → Tester with message passing

## 🎨 Customization

### Changing the Goal (Ollama System)

Edit `run.py` to change the goal:

```python
goal = "Your custom goal here"
```

### Using a Different Model (Ollama System)

Edit `llm_client.py` to use a different Ollama model:

```python
payload = {
    "model": "your-model-name",  # Change this
    "messages": [{"role": "user", "content": prompt}],
    "stream": False
}
```

### Modifying Agent Behavior

- **Ollama agents**: Edit files in `agents/` directory
- **Async agents**: Edit files in `agents_async/` directory

## 🐛 Troubleshooting

### Ollama Connection Error

If you get connection errors:
- Make sure Ollama is running: `ollama serve`
- Check if Ollama is accessible: `curl http://localhost:11434/api/tags`

### Model Not Found

If you get model errors:
- Pull the model: `ollama pull llama3`
- Verify it's available: `ollama list`

### Python Import Errors

If you get import errors:
- Make sure you're in the project directory
- Verify dependencies are installed: `pip list | grep openai`
- Make sure virtual environment is activated

## 📝 Example Output

### Ollama System (`python3 run.py`)

```
🧠 Planning...
[Planning output with steps]

⚡ Executing...
[Execution results]

🔍 Reviewing...
[Reviewed and improved output]

Final Output:
[Final polished result]
```

### Async System (`python3 run_async.py`)

```
[planner] started
[developer] started
[tester] started
[Planner] handling Message(...)
[Developer] got Message(...)
[Tester] received Message(...)
...
```

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for improvements!

## 📄 License

This project is open source and available for educational purposes.

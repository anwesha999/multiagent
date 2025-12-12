# Multi-Agent System with Ollama

A simple multi-agent system that uses Ollama (running locally) to orchestrate three specialized agents: Planner, Worker, and Reviewer. This system demonstrates how multiple AI agents can work together to plan, execute, and review tasks.

## 🏗️ Architecture

The system consists of:

- **Planner Agent**: Breaks down goals into actionable steps
- **Worker Agent**: Executes the planned tasks
- **Reviewer Agent**: Reviews and improves the output
- **Orchestrator**: Coordinates the workflow between all agents

## 📋 Prerequisites

1. **Python 3.7+** installed on your system
2. **Ollama** installed and running
3. **llama3 model** pulled in Ollama

### Installing Ollama

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

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   This will install:
   - `openai==1.40.0` - OpenAI Python client (works with Ollama's OpenAI-compatible API)
   - `python-dotenv` - For environment variable management

## 🎯 Running the System

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

## 📁 Project Structure

```
multiagent/
├── agents/
│   ├── __init__.py
│   ├── base_agent.py      # Base agent class
│   ├── planner.py         # Planner agent
│   ├── worker.py          # Worker agent
│   └── reviewer.py        # Reviewer agent
├── llm_client.py          # Ollama client wrapper
├── orchestrator.py        # Orchestrates the multi-agent workflow
├── run.py                 # Main entry point
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🔧 How It Works

1. **Planning Phase**: The Planner Agent receives a goal and breaks it down into 3-7 clear steps
2. **Execution Phase**: The Worker Agent executes the planned steps and produces results
3. **Review Phase**: The Reviewer Agent reviews, improves, and corrects the output

The Orchestrator coordinates all three phases sequentially.

## 🎨 Customization

### Changing the Goal

Edit `run.py` to change the goal:

```python
goal = "Your custom goal here"
```

### Using a Different Model

Edit `llm_client.py` to use a different Ollama model:

```python
payload = {
    "model": "your-model-name",  # Change this
    "messages": [{"role": "user", "content": prompt}],
    "stream": False
}
```

### Modifying Agent Behavior

Edit the agent files in the `agents/` directory to customize their prompts and behavior:
- `agents/planner.py` - Modify planning logic
- `agents/worker.py` - Modify execution logic
- `agents/reviewer.py` - Modify review logic

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

## 📝 Example Output

When you run `python3 run.py`, you'll see:

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

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for improvements!

## 📄 License

This project is open source and available for educational purposes.

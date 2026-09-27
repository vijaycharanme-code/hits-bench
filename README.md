# HITS AI Workbench

Sovereign On-Premise Agentic AI Workbench for Confidential Industrial Work.

## Features
- **Laya System-1 Router**: Uses Laya to route tasks efficiently and classify input securely before heavy LLM generation.
- **LangGraph Orchestration**: Supports self-correction and multi-agent workflows.
- **Agent Roles**: Specialized Engineer, Supervisor, HR, Document, and Verifier agents.
- **RAG & Verification**: Local ChromaDB embedding storage and automated verification of claims based on context.
- **Automated Desktop Application**: Start backend, frontend, agents, and local AI natively via an executable file.

## Installation

### For Users
Simply run the installer executable:
`HITS-AI-Workbench-Setup.exe`

Double click the shortcut. The system will automatically check hardware, configure fallbacks (e.g. CPU if GPU is missing), and launch the frontend in your browser.

### For Developers

1. Ensure Python 3.10+ is installed.
2. Install dependencies:
   ```bash
   cd HITS-AI-Workbench
   pip install -r requirements.txt
   ```
3. Run tests:
   ```bash
   pytest tests/
   ```
4. Build the executable:
   ```bash
   python installer/build.py
   ```

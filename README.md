<h1 align="center">🚀 AI Workflow Engine</h1>
<h3 align="center">A clean, minimal, and extensible agent workflow engine</h3>



<p align="center">
  🐍 <b>Python 3.10+</b> &nbsp;|&nbsp;
  ⚡ <b>FastAPI Backend</b> &nbsp;|&nbsp;
  🔁 <b>Looping + Branching Workflow</b> &nbsp;|&nbsp;
  🧩 <b>Node-Based Architecture</b> &nbsp;|&nbsp;
  ✨ <b>Clean & Structured Code</b>
</p>

---

## ⚙️ The engine supports:

- Node-based execution  
- Shared state flow  
- Branching logic  
- Looping  
- Execution logs  
- Tool registry  
- FastAPI endpoints for interaction  

---


## 🌟 Overview

The **AI Workflow Engine** is a dynamic and extensible system designed to execute workflows as a sequence of intelligent, state-driven steps.  
It allows you to model processes as **nodes**, connect them through **edges**, and manage information using a shared **state** that evolves as the workflow progresses.

This architecture makes it easy to build:

- 🚀 Rule-based agents  
- 🔄 Data processing pipelines  
- 🧩 Modular backend workflows  
- 🛠 Automation systems  
- 📊 Evaluation or transformation flows  

The engine is built with a strong focus on:

- **Clarity** in defining workflows  
- **Traceability** through logs  
- **Flexibility** in branching and looping  
- **Extensibility** for new node types and tools  
- **Smooth API Interaction** using FastAPI  

Whether you're orchestrating simple tasks or building complex multi-step execution graphs, this engine provides a clean, expressive, and interactive foundation.

---

## 🧱 Architecture

The Workflow Engine is built around a clear and modular architecture.  
Each workflow is modeled as a graph of connected nodes, with a shared state flowing through the system.

### 🔧 High-Level Architecture

            ┌───────────────────────────────────┐
            │           API Layer               │
            │      (FastAPI Endpoints)          │
            └─────────────────┬─────────────────┘
                              │
                              ▼
            ┌───────────────────────────────────┐
            │         Workflow Runtime          │
            │  • Graph Loader                   │
            │  • Node Execution Engine          │
            │  • Branch & Loop Controller       │
            │  • Execution Logger               │
            └─────────────────┬─────────────────┘
                              │
                              ▼
            ┌───────────────────────────────────┐
            │          State Manager            │
            │  • Shared dictionary state        │
            │  • Step-by-step updates           │
            └─────────────────┬─────────────────┘
                              │
                              ▼
            ┌───────────────────────────────────┐
            │          Tool Registry            │
            │ • Reusable helper functions       │
            │ • Extend workflows dynamically    │
            └───────────────────────────────────┘


---

# 🔷 What Each Layer Does

### **🟦 API Layer**
- Exposes workflow creation, execution, and state retrieval endpoints.  
- Acts as the orchestration entry point.

### **🟩 Workflow Runtime**
- Loads workflow graphs  
- Executes nodes in the correct sequence  
- Handles branching & looping  
- Logs every step  

### **🟨 State Manager**
- Stores shared state  
- Allows nodes to read/write values  
- Provides deterministic workflow transitions  

### **🟥 Tool Registry**
- Register optional utilities  
- Enables tool-augmented workflows  

---

## 🌟 Key Highlights

The AI Workflow Engine is designed to be expressive, modular, and developer-friendly.  
It enables you to build dynamic workflows with clean, well-structured logic and full control over execution.

### 🚀 What Makes This Engine Powerful?

<div align="center">

| Feature | Description |
|--------|-------------|
| 🧠 **Graph-Based Workflow** | Workflows are modeled as connected nodes with clear transitions. |
| 🔄 **Shared State Propagation** | A single evolving state flows through every node in the pipeline. |
| 🔀 **Branching Logic** | Nodes can choose the next step based on runtime conditions. |
| 🔁 **Looping Support** | Automatically repeat parts of the workflow until conditions are met. |
| 🔧 **Tool Registry** | Add reusable utility functions that nodes can call at any time. |
| 📝 **Execution Logging** | Every step is logged for complete visibility and debugging. |
| ⚡ **FastAPI Endpoints** | Create, run, and inspect workflows through a clean API interface. |

</div>

### 💡 Why It Stands Out

- Designed with **extensibility** in mind  
- Encourages **clean workflow definitions**  
- State updates are fully **traceable**  
- Runs dynamically based on the **logic you define**  
- Easily integrates into larger backend systems  

---

## 🗂️ Project Structure

The project is organized to keep the workflow engine modular, readable, and easy to extend.  
Every component has a clear responsibility, making the system intuitive for developers.

    app/
    │
    ├── main.py                   # FastAPI application (API endpoints)
    │
    ├── engine/
    │     ├── graph_engine.py     # Core engine: node execution, branching, looping, logging
    │     └── registry.py         # Tool registry for reusable helper functions
    │
    ├── workflows/
    │     └── code_review.py      # Example workflow (Code Review Mini-Agent)
    │
    └── models/
          └── graph_models.py     # Pydantic models for graph creation & execution requests

    README.md                     # Interactive documentation
    requirements.txt              # Project dependencies

---


## 🛠️ Create a Workflow Graph  
POST /graph/create

- Creates and registers a new workflow graph using a set of **nodes** and **edges**.  
- Nodes map to Python functions, and edges define the execution path, including branching & looping.

### 📥 Request Body
```json
{
  "nodes": {
    "extract": "extract",
    "complexity": "complexity",
    "issues": "issues",
    "improve": "improve",
    "condition": "condition"
  },
  "edges": {
    "extract": "complexity",
    "complexity": "issues",
    "issues": "improve",
    "improve": {
      "condition": "condition",
      "true": "complexity",
      "false": null
    }
  }
}
````


📤 Sample Response
```json
{
  "graph_id": "b119a2e4-559d-44fd-8d11-083db61d64e6"
}
```

## ▶️ Run a Workflow  
POST /graph/run

- Executes the workflow from the first node onward.  
- Each node updates the shared state, and the engine logs every step taken.

### 📥 Request Body
```json
{
  "graph_id": "your-graph-id-here",
  "initial_state": {
    "code": "def a(): pass\ndef b(): pass",
    "threshold": 6
  }
}
```

📤 Sample Response

```json
{
  "run_id": "4c87e23a-d51d-46e5-87c8-b8abf9199159",
  "final_state": {
    "functions": 2,
    "complexity": 4,
    "issues": 3,
    "quality_score": 3,
    "threshold": 6
  },
  "execution_log": [
    {
      "node": "extract",
      "state": {
        "functions": 2,
        "step": "extract_done"
      }
    },
    {
      "node": "complexity",
      "state": {
        "complexity": 4
      }
    },
    {
      "node": "issues",
      "state": {
        "issues": 3
      }
    },
    {
      "node": "improve",
      "state": {
        "quality_score": 3
      }
    }
  ]
}
```

## 📄 Retrieve Workflow State  
GET /graph/state/{run_id}

Fetches the **current or final state** of a workflow execution, along with all logged node transitions.

### 📤 Sample Response
```json
{
  "final_state": {
    "functions": 2,
    "complexity": 4,
    "issues": 3,
    "quality_score": 3,
    "threshold": 6
  },
  "log": [
    {
      "node": "extract",
      "state": {
        "functions": 2
      }
    },
    {
      "node": "complexity",
      "state": {
        "complexity": 4
      }
    }
  ]
}
```

## 🚀 Getting Started

Follow these steps to install dependencies and launch the Workflow Engine.

---

## 📦 Install Dependencies

Make sure you have **Python 3.10+** installed.

```bash
pip install -r requirements.txt
```

▶️ Run the FastAPI Server

Launch the development server using uvicorn:
```bash
uvicorn app.main:app 
```

This starts the API at:

http://localhost:8000


## 📘 Explore the Interactive API Documentation

FastAPI automatically provides a fully interactive Swagger UI where you can:

- Create workflows  
- Run workflows  
- Inspect execution state  
- View logs  

Simply open:
http://localhost:8000/docs

This interface allows you to test every endpoint directly from your browser.

## 🔧 Future Improvements

With additional time, several enhancements could further strengthen the workflow engine:

- **Async Node Execution**  
  Allow long-running or I/O-heavy nodes to execute asynchronously without blocking the system.

- **Persistent Storage for Graphs & Runs**  
  Replace in-memory storage with PostgreSQL or SQLite for durability and multi-user support.

- **WebSocket Log Streaming**  
  Stream real-time execution logs to clients as workflows progress.

- **Visual Workflow Builder**  
  A UI to design workflows using a drag-and-drop graph editor.

- **Enhanced Error Handling**  
  Structured exceptions and retry policies for more robust workflow execution.

- **Plugin System for Tools**  
  Let users register external tools or custom capabilities dynamically.

These improvements would make the engine more scalable, interactive, and production-ready.


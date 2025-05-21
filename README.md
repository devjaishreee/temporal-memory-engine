#  Temporal Memory Update Engine

A lightweight memory architecture for tracking **evolving user state over time**. Built for AI agents that adapt as users change. Whether you're building chatbots, recommender systems, or lifelike companions, this engine ensures your agent remembers *what matters now*, not just what mattered once.

---

##  Why Use This?

- Does your user say "I like sushi" today, and "I prefer ramen" tomorrow?
- Want to track such shifts, keep only the latest preference active, and still preserve history?

This engine helps your system:
-  Store and overwrite memories with timestamps
-  Maintain a full history of changes
-  Always operate on the latest, contextually relevant state

Perfect for **agentic AI**, **personal assistants**, and **dynamic UX systems**.

---

## Features

-  **Key-Value Memory Store** – Lightweight, intuitive storage engine.
-  **Timestamped Updates** – Every update is time-aware.
-  **Version History** – Keep a record of evolving states.
-  **Simple Overwrite Logic** – Old values archived automatically.
-  **Modular & Extensible** – Plug it into larger memory or graph-based architectures.

---

##  Example

```python
from memory_engine.memory_store import MemoryStore

mem = MemoryStore()
mem.set("food_preference", "sushi")
mem.set("food_preference", "ramen")

print(mem.get("food_preference"))     # ramen
print(mem.get_history("food_preference"))
```

---

##  Project Structure

```
temporal-memory-engine/
├── memory_engine/
│   ├── memory_store.py
│   ├── history_manager.py
│   └── utils.py
├── examples/
│   └── demo.py
├── tests/
│   └── test_memory.py
├── requirements.txt
├── LICENSE
└── README.md
```

---

##  Running the Project

1. **Clone the repo**
```bash
git clone https://github.com/YOUR_USERNAME/temporal-memory-engine.git
cd temporal-memory-engine
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the demo**
```bash
python examples/demo.py
```

4. **Run unit tests**
```bash
pytest
```

---

##  Author

**Dev Jai Shree Choudhary**  
📧 devjaishree01@gmail.com  


Let's talk if you're building adaptive systems, AI agents, or memory-driven applications.

---


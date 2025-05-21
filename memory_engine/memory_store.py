from datetime import datetime
from .history_manager import HistoryManager
from .utils import get_current_timestamp

class MemoryStore:
    def __init__(self):
        self.memory = {}
        self.history = HistoryManager()

    def set(self, key, value):
        timestamp = get_current_timestamp()
        if key in self.memory:
            old_value = self.memory[key]['value']
            self.history.archive(key, old_value, self.memory[key]['timestamp'])
        self.memory[key] = {"value": value, "timestamp": timestamp}

    def get(self, key):
        return self.memory.get(key, {}).get("value", None)

    def get_timestamp(self, key):
        return self.memory.get(key, {}).get("timestamp", None)

    def get_history(self, key):
        return self.history.get(key)

    def get_all_memory(self):
        return self.memory

    def __str__(self):
        return f"Current Memory:\n{self.memory}\n\nHistory:\n{self.history}"

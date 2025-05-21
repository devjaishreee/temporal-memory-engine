class HistoryManager:
    def __init__(self):
        self.history = {}

    def archive(self, key, value, timestamp):
        if key not in self.history:
            self.history[key] = []
        self.history[key].append({
            "value": value,
            "timestamp": timestamp
        })

    def get(self, key):
        return self.history.get(key, [])

    def __str__(self):
        return str(self.history)

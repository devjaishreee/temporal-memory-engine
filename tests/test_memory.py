import unittest
from memory_engine.memory_store import MemoryStore

class TestMemoryStore(unittest.TestCase):
    def test_set_and_get(self):
        store = MemoryStore()
        store.set("mood", "happy")
        self.assertEqual(store.get("mood"), "happy")

    def test_update_and_history(self):
        store = MemoryStore()
        store.set("status", "online")
        store.set("status", "away")
        store.set("status", "offline")

        self.assertEqual(store.get("status"), "offline")
        history = store.get_history("status")
        self.assertEqual(len(history), 2)
        self.assertEqual(history[0]['value'], "online")
        self.assertEqual(history[1]['value'], "away")

    def test_timestamp_exists(self):
        store = MemoryStore()
        store.set("theme", "dark")
        timestamp = store.get_timestamp("theme")
        self.assertTrue(timestamp.endswith("Z"))

if __name__ == "__main__":
    unittest.main()

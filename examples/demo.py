from memory_engine.memory_store import MemoryStore

def run_demo():
    memory = MemoryStore()

    memory.set("food_preference", "sushi")
    print("Added: food_preference → sushi")

    memory.set("food_preference", "ramen")
    print("Updated: food_preference → ramen")

    memory.set("food_preference", "udon")
    print("Updated: food_preference → udon")

    print("\n--- Current Memory ---")
    print(memory.get_all_memory())

    print("\n--- History ---")
    print(memory.get_history("food_preference"))

if __name__ == "__main__":
    run_demo()

"""CLI for the Local Coding Assistant with basic caching and warm-up to reduce latency."""
from .utils import ask_qwen
from functools import lru_cache
import threading

@lru_cache(maxsize=128)
def _cached_ask_qwen(prompt: str) -> str:
    """Wrap the real call so recent prompts are cached."""
    return ask_qwen(prompt)

def main():
    """Run the main CLI loop for the Local Coding Assistant."""
    print("Local Coding Assistant (type 'exit' to quit)")
    # Warm up model/client in background to reduce first-call latency
    threading.Thread(target=lambda: _cached_ask_qwen("warmup"), daemon=True).start()

    try:
        while True:
            prompt = input(">> ").strip()
            if not prompt:
                continue
            if prompt.lower() in ["exit", "quit"]:
                break
            response = _cached_ask_qwen(prompt)
            print(response + "\n")
    except (KeyboardInterrupt, EOFError):
        print("\nExiting...")

if __name__ == "__main__":
    main()

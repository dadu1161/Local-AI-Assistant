import subprocess

def ask_qwen(prompt: str) -> str:
    """
    Call Ollama CLI to get a response from qwen2.5-coder
    """
    try:
        result = subprocess.run(
            ["ollama", "run", "qwen2.5-coder:3b", prompt],
            capture_output=True,
            text=True
        )
        return result.stdout.strip()
    except Exception as e:
        return f"Error: {e}"

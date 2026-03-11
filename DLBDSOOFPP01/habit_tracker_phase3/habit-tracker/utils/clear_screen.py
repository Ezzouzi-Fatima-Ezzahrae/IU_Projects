import os
import platform
# ---------------- Utility ----------------
def clear_screen():
    """Clear the terminal or IDE console screen."""
    try:
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")
    except Exception:
        print("\n" * 50)
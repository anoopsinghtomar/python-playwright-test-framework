from datetime import datetime
from pathlib import Path
import random
import string


def timestamp() -> str:
    """Return current timestamp suitable for filenames."""
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def random_string(length: int = 8) -> str:
    """Generate a random alphabetic string."""
    return ''.join(random.choices(string.ascii_letters, k=length))


def ensure_directory(path: str) -> None:
    """Create a directory if it does not exist."""
    Path(path).mkdir(parents=True, exist_ok=True)
from pathlib import Path

from utils.helpers import timestamp


def capture(page, directory="screenshots", name="screenshot"):
    """
    Capture a full-page screenshot.

    Returns the saved file path.
    """
    Path(directory).mkdir(parents=True, exist_ok=True)

    file_name = f"{name}_{timestamp()}.png"

    path = Path(directory) / file_name

    page.screenshot(
        path=str(path),
        full_page=True
    )

    return str(path)
import os
from pathlib import Path

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent

# Application settings
APP_SETTINGS = {
    "page_title": "PDF to JPG Converter",
    "page_icon": "📄",
    "layout": "wide"
}

# PDF conversion settings
PDF_SETTINGS = {
    "dpi": 300,
    "poppler_path": os.getenv("POPPLER_PATH", "/usr/local/bin"),  # Default Linux path, overridable by env var
}

# Directory settings
DIRECTORIES = {
    "output": os.getenv("OUTPUT_DIR", str(BASE_DIR / "output_images")),
    "temp": os.getenv("TEMP_DIR", str(BASE_DIR / "temp"))
}

# Create directories if they don't exist
for dir_path in DIRECTORIES.values():
    Path(dir_path).mkdir(parents=True, exist_ok=True)

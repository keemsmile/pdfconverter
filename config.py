import os
from pathlib import Path

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent

# Application settings
APP_SETTINGS = {
    "page_title": "PDF to JPG Converter",
    "page_icon": "",
    "layout": "wide"
}

# Detect environment and set appropriate Poppler path
def get_default_poppler_path():
    # Check if we're in a Docker container
    if os.path.exists('/.dockerenv'):
        return '/usr/bin'
    # Windows path
    elif os.name == 'nt':
        return r'C:\poppler-24.08.0\Library\bin'
    # Unix-like systems
    else:
        return '/usr/bin'

# PDF conversion settings
PDF_SETTINGS = {
    "dpi": 300,
    "poppler_path": os.getenv("POPPLER_PATH", get_default_poppler_path()),
}

# Directory settings
DIRECTORIES = {
    "output": os.getenv("OUTPUT_DIR", str(BASE_DIR / "output_images")),
    "temp": os.getenv("TEMP_DIR", str(BASE_DIR / "temp"))
}

# Create directories if they don't exist
for dir_path in DIRECTORIES.values():
    Path(dir_path).mkdir(parents=True, exist_ok=True)

# Debug info
if os.getenv('DEBUG', 'False').lower() == 'true':
    print(f"Using Poppler path: {PDF_SETTINGS['poppler_path']}")
    print(f"Output directory: {DIRECTORIES['output']}")
    print(f"Temp directory: {DIRECTORIES['temp']}")

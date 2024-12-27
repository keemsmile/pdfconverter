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
    # Check if we're in Streamlit Cloud
    if os.getenv('STREAMLIT_SHARING_MODE') == 'streamlit':
        return '/usr/bin'
    # Check if we're in a Docker container
    elif os.path.exists('/.dockerenv'):
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

# Ensure directories exist and are writable
for dir_path in DIRECTORIES.values():
    path = Path(dir_path)
    path.mkdir(parents=True, exist_ok=True)
    # Make sure the directory is writable
    if not os.access(path, os.W_OK):
        try:
            path.chmod(0o777)
        except Exception as e:
            print(f"Warning: Could not set permissions for {path}: {e}")

# Debug info
if os.getenv('DEBUG', 'False').lower() == 'true':
    print(f"Environment: {'Streamlit Cloud' if os.getenv('STREAMLIT_SHARING_MODE') == 'streamlit' else 'Local/Docker'}")
    print(f"Using Poppler path: {PDF_SETTINGS['poppler_path']}")
    print(f"Output directory: {DIRECTORIES['output']}")
    print(f"Temp directory: {DIRECTORIES['temp']}")
    print(f"Directory write permissions:")
    for name, path in DIRECTORIES.items():
        print(f"  {name}: {'Writable' if os.access(Path(path), os.W_OK) else 'Not Writable'}")

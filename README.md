# PDF to JPG Converter

A Streamlit web application that converts PDF files to high-quality JPG images.

## Features
- Upload PDF files through a web interface
- Convert PDF pages to JPG images with configurable DPI
- Download individual page images
- Containerized deployment ready

## Local Development Setup

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Install Poppler:
- Windows: Download from [poppler releases](http://blog.alivate.com.au/poppler-windows/)
- Linux: `sudo apt-get install poppler-utils`
- Mac: `brew install poppler`

3. Copy `.env.example` to `.env` and adjust settings if needed:
```bash
cp .env.example .env
```

4. Run the application:
```bash
streamlit run webappconverter.py
```

## Docker Deployment

1. Build the Docker image:
```bash
docker build -t pdf-converter .
```

2. Run the container:
```bash
docker run -p 8501:8501 -v $(pwd)/output_images:/app/output_images pdf-converter
```

Access the application at http://localhost:8501

## Project Structure
- `webappconverter.py`: Main application file
- `config.py`: Configuration settings
- `style.css`: Custom styling
- `requirements.txt`: Python dependencies
- `Dockerfile`: Container configuration
- `.env`: Environment variables (create from .env.example)

## Notes
- Output images are saved in the `output_images` directory
- Temporary files are stored in the `temp` directory
- Both directories are created automatically if they don't exist

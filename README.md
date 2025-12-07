# Simple Calculator

A simple calculator application built with [FastAPI](https://fastapi.tiangolo.com/).

## Features

- **Basic Arithmetic Operations**:
    - Addition (`/sum`)
    - Subtraction (`/sub`)
    - Multiplication (`/mul`)
    - Division (`/div`)
- **Web Interface**: A clean and simple frontend to interact with the API.

## Project Structure

```
Antigravity demo/
├── main.py           # FastAPI backend application
├── static/
│   └── index.html    # Frontend user interface
├── requirements.txt  # Project dependencies
└── README.md         # Project documentation
```

## Prerequisites

- [Python 3.7+](https://www.python.org/)

## Installation

1. **Clone the repository** (if applicable) or navigate to the project directory.

2. **Create a virtual environment** (recommended):

   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**:

   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Start the application**:

   ```bash
   python main.py
   ```
   
   Or using uvicorn directly:

   ```bash
   uvicorn main:app --reload
   ```

2. **Open the application**:

   Open your web browser and navigate to: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## API Endpoints

The backend provides the following JSON endpoints:

- `GET /sum?a=number&b=number`
- `GET /sub?a=number&b=number`
- `GET /mul?a=number&b=number`
- `GET /div?a=number&b=number`

## Technologies Used

- **Back-end**: Python, FastAPI
- **Front-end**: HTML, CSS, JavaScript (Vanilla)

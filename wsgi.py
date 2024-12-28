import sys
from pathlib import Path

# Add the project root directory to Python path
sys.path.insert(0, str(Path(__file__).parent))

from app import app
from http.server import BaseHTTPRequestHandler

def handler(request, base):
    """Handle incoming HTTP requests."""
    # Add debugging print statements
    print(f"base: {base}, type: {type(base)}")  # Log the value and type of base

    if not (isinstance(base, type) and issubclass(base, BaseHTTPRequestHandler)):
        raise TypeError("base must be a class")

    with app.test_client() as client:
        return client.get(request.path, headers=request.headers)

# For local development
if __name__ == '__main__':
    app.run(debug=True, port=5002) 
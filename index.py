from flask import Flask
from app import app

# This is required for Vercel
def handler(request):
    """Handle incoming HTTP requests."""
    return app(request)
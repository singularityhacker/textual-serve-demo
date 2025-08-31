# Minimal Textual-Serve Demo

This is a minimal reproduction of a Textual TUI deployment issue on Railway.com.

## The Problem

The app works perfectly locally but shows only a splash screen when deployed to hosting service. I tried Railway and Render.

## Files

- `app.py` - Minimal Textual app (just shows "Hello from Textual!")
- `server.py` - Local server (exact 3-line pattern from docs)
- `railway_server.py` - Railway server with PORT handling
- `requirements.txt` - Dependencies

## Local Testing

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Test the app directly
python app.py

# Test the server
python server.py
```

## Railway Deployment

1. Create new Railway project
2. Connect this repo
3. Set start command to: `python railway_server.py`
4. Deploy

## Expected Behavior

- **Locally**: Should see "Hello from Textual!" in terminal
- **Locally via server**: Should see TUI in browser at http://localhost:8000
- **Railway**: Should see TUI in browser at Railway's URL

## Actual Behavior

- **Locally**: ✅ Works perfectly
- **Locally via server**: ✅ Works perfectly  
- **Railway**: ❌ Shows splash screen, never loads TUI

## Environment

- Python 3.11+
- Railway.com hosting
- Textual 6.0.0
- Textual-serve 1.1.2

## Help Needed

The Textual community can help debug why Railway deployment shows only a splash screen while local deployment works perfectly.

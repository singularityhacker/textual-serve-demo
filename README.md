# Minimal Textual-Serve Demo

This is a minimal reproduction of a Textual TUI deployment issue that was successfully resolved. The app demonstrates how to deploy Textual TUI applications to both Railway and Render using [textual-serve](https://github.com/Textualize/textual-serve).

## The Problem (RESOLVED ✅)

The app works perfectly locally but initially showed only a splash screen when deployed to hosting services. The issue was related to static asset serving in containerized environments.

## Files

- `app.py` - Minimal Textual app (just shows "Hello from Textual!")
- `server.py` - Local server (exact 3-line pattern from docs)
- `railway_server.py` - Railway server with PORT handling and public_url configuration
- `render_server.py` - Render server (separate configuration for Render deployment)
- `requirements.txt` - Dependencies
- `Dockerfile` - Container configuration for Railway
- `render.yaml` - Render deployment configuration

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

## The Solution

The issue was resolved by setting the `public_url` parameter in the textual-serve Server configuration. This parameter tells textual-serve where to serve static assets from when deployed behind a proxy or load balancer.

### Key Changes Made

1. **Added `public_url` parameter** to `railway_server.py`
2. **Upgraded pip/setuptools/wheel** in Dockerfile for better dependency handling
3. **Created separate server files** for different platforms to avoid configuration conflicts

## Deployment

### Railway Deployment

1. Create new Railway project
2. Connect this repo
3. Set start command to: `python railway_server.py`
4. Deploy

**Note**: Railway uses the Dockerfile and runs in a containerized environment, requiring explicit `public_url` configuration.

### Render Deployment

1. Create new Render web service
2. Connect this repo
3. Set start command to: `python render_server.py`
4. Deploy

**Note**: Render ignores the Dockerfile and runs natively, handling static assets automatically.

## Current Behavior

- **Locally**: ✅ Works perfectly
- **Locally via server**: ✅ Works perfectly  
- **Railway**: ✅ Works perfectly (with public_url configuration)
- **Render**: ✅ Works perfectly (native deployment)

## Environment

- Python 3.11+
- Railway.com hosting (containerized)
- Render.com hosting (native)
- Textual 6.0.0
- Textual-serve 1.1.2

## Key Learnings

1. **Containerized deployments** (Railway) require explicit `public_url` configuration for static assets
2. **Native deployments** (Render) can handle static asset routing automatically
3. **Separate server files** provide clean separation between platform configurations
4. **Dependency management** in containers benefits from upgrading pip/setuptools/wheel

import os
from textual_serve.server import Server

port = int(os.environ.get('PORT', 8000))
server = Server(
    "python app.py", 
    port=port, 
    host="0.0.0.0",
    # public_url="https://your-app-name.onrender.com"  
)
server.serve()

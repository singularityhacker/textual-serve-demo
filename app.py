from textual.app import App, ComposeResult
from textual.widgets import Static

class MinimalApp(App):
    """Minimal Textual app for testing."""
    
    def compose(self) -> ComposeResult:
        yield Static("Hello from Textual! This is a minimal test app.")

if __name__ == "__main__":
    app = MinimalApp()
    app.run()

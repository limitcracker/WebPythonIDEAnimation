"""Core animation framework classes."""

class AnimationAPI:
    """Animation API for drawing shapes and text."""
    
    def __init__(self, canvas_id):
        """Initialize the API with canvas element."""
        from browser import document, window
        self.canvas = document[canvas_id]
        self.ctx = self.canvas.getContext('2d')
        self.width = self.canvas.width
        self.height = self.canvas.height
        self.p5 = window.p5
        
    def clear(self):
        """Clear the canvas."""
        self.ctx.clearRect(0, 0, self.width, self.height)
        
    def draw_rect(self, x, y, width, height, color="#FFFFFF"):
        """Draw a rectangle."""
        self.ctx.fillStyle = color
        self.ctx.fillRect(x, y, width, height)
        
    def draw_circle(self, x, y, radius, color="#FFFFFF"):
        """Draw a circle."""
        self.ctx.beginPath()
        self.ctx.fillStyle = color
        self.ctx.arc(x, y, radius, 0, 2 * self.p5.PI)
        self.ctx.fill()
        
    def draw_star(self, x, y, size, color="#FFFFFF", alpha=1.0):
        """Draw a star shape."""
        self.ctx.save()
        self.ctx.translate(x, y)
        self.ctx.rotate(self.p5.frameCount * 0.1)
        self.ctx.beginPath()
        self.ctx.fillStyle = color
        self.ctx.globalAlpha = alpha
        
        for i in range(5):
            angle = i * 4 * self.p5.PI / 5
            self.ctx.lineTo(
                size * self.p5.cos(angle),
                size * self.p5.sin(angle)
            )
            
        self.ctx.closePath()
        self.ctx.fill()
        self.ctx.restore()
        
    def draw_text(self, text, x, y, color="#FFFFFF", font="16px Arial"):
        """Draw text on canvas."""
        self.ctx.fillStyle = color
        self.ctx.font = font
        self.ctx.fillText(text, x, y)

class AnimationExample:
    """Base class for animation examples."""
    
    def __init__(self, api):
        """Initialize with animation API."""
        self.api = api
        self._running = False
        self._namespace = {}
        self._tests = []
        self._pre_setup()
        
    def _pre_setup(self):
        """Override to initialize example."""
        pass
        
    def start(self):
        """Start the animation."""
        self._running = True
        
    def stop(self):
        """Stop the animation."""
        self._running = False
        
    def update(self, time):
        """Update animation frame."""
        pass

# Export classes
__all__ = ['AnimationAPI', 'AnimationExample']

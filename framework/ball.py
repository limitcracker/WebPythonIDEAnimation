"""BouncingBall class for animation framework."""

class BouncingBall:
    """A bouncing ball with physics and effects."""
    
    def __init__(self):
        """Initialize the ball."""
        self.x = 200
        self.y = 200
        self.dx = 0
        self.dy = 0
        self.size = 20
        self.color = "#4CAF50"
        self.gravity = 0.5
        self.bounce = 0.8
        self.trail = []
        self.sparkles = []
        self.trail_enabled = False
        self.sparkles_enabled = False
    
    def update(self, width, height):
        """Update ball position and physics."""
        # Apply gravity
        self.dy += self.gravity
        
        # Update position
        self.x += self.dx
        self.y += self.dy
        
        # Bounce off walls
        if self.x < self.size:
            self.x = self.size
            self.dx *= -self.bounce
        elif self.x > width - self.size:
            self.x = width - self.size
            self.dx *= -self.bounce
            
        # Bounce off floor/ceiling
        if self.y < self.size:
            self.y = self.size
            self.dy *= -self.bounce
        elif self.y > height - self.size:
            self.y = height - self.size
            self.dy *= -self.bounce
            
        # Update trail
        if self.trail_enabled:
            self.trail.append((self.x, self.y))
            if len(self.trail) > 20:
                self.trail.pop(0)
                
        # Update sparkles
        if self.sparkles_enabled and abs(self.dy) > 5:
            self.sparkles.append({
                'x': self.x,
                'y': self.y,
                'life': 20
            })
        
        # Update sparkle life
        for sparkle in self.sparkles[:]:
            sparkle['life'] -= 1
            if sparkle['life'] <= 0:
                self.sparkles.remove(sparkle)
    
    def draw(self, api):
        """Draw the ball and its effects."""
        # Draw trail
        if self.trail_enabled:
            for i, (x, y) in enumerate(self.trail):
                alpha = i / len(self.trail)
                api.draw_circle(x, y, self.size * 0.8, f"rgba(76, 175, 80, {alpha * 0.3})")
        
        # Draw sparkles
        for sparkle in self.sparkles:
            alpha = sparkle['life'] / 20
            size = self.size * 0.3 * alpha
            api.draw_star(sparkle['x'], sparkle['y'], size, "#FFD700", alpha)
        
        # Draw ball
        api.draw_circle(self.x, self.y, self.size, self.color)
    
    # High-level student commands
    def throw(self, power):
        """Throw the ball up with given power (0-2)."""
        power = min(max(power, 0), 2)
        self.dy = -15 * power
        self.dx = 5 * power
        
    def jump(self, power):
        """Make the ball jump with given power (0-2)."""
        power = min(max(power, 0), 2)
        self.dy = -20 * power
        
    def set_bounce(self, amount):
        """Set bounce amount (0-1)."""
        self.bounce = min(max(amount, 0), 1)
        
    def trail_on(self):
        """Enable trail effect."""
        self.trail_enabled = True
        
    def trail_off(self):
        """Disable trail effect."""
        self.trail_enabled = False
        self.trail = []
        
    def sparkles_on(self):
        """Enable sparkle effect."""
        self.sparkles_enabled = True
        
    def sparkles_off(self):
        """Disable sparkle effect."""
        self.sparkles_enabled = False
        self.sparkles = []

class Example(AnimationExample):
    """Bouncing ball example."""
    
    # Student visible code template (shown in IDE)
    STUDENT_CODE = '''# Bouncing Ball Exercise
# Control the ball using simple commands!

# Basic ball commands:
# - ball.throw(power)   # Throw ball (power: 0.1 to 2.0)
# - ball.jump(height)   # Jump up (height: 0.1 to 2.0)
# - ball.set_bounce(amount)  # Set bounce amount (0.0 to 1.0)

# Special effects:
# - ball.trail_on()     # Show motion trail
# - ball.trail_off()    # Hide motion trail
# - ball.sparkles_on()  # Add sparkle effect
# - ball.sparkles_off() # Remove sparkles

# Try these effects:
ball.color = "#FF5722"  # Orange
ball.throw(1.5)         # Throw with high power
ball.sparkles_on()      # Add sparkles

# Add some more effects
ball.trail_on()         # Show trail
ball.jump(1.2)         # Jump high
'''
    
    def _pre_setup(self):
        """Initialize the ball (hidden from students)."""
        self.ball = BouncingBall()
        
        # Create namespace for student code
        self._namespace = {
            'ball': self.ball,
        }
        
        print("Bouncing ball example loaded!")
        print("Available commands:")
        print("\nBall commands:")
        print("- ball.throw(power)   # Throw ball (0.1 to 2.0)")
        print("- ball.jump(height)   # Jump up (0.1 to 2.0)")
        print("- ball.set_bounce(amount)  # Set bounce amount (0.0 to 1.0)")
        print("\nSpecial effects:")
        print("- ball.trail_on()     # Show motion trail")
        print("- ball.trail_off()    # Hide motion trail")
        print("- ball.sparkles_on()  # Add sparkle effect")
        print("- ball.sparkles_off() # Remove sparkles")
        
        # Start animation
        self.start()
    
    def update(self, time):
        """Update the animation frame."""
        # Clear and draw background
        self.api.clear()
        self.api.draw_rect(0, 0, self.api.width, self.api.height, "#2c2c2c")
        
        # Update and draw ball
        self.ball.update(self.api.width, self.api.height)
        self.ball.draw(self.api)
        
        # Draw title
        self.api.draw_text("Bouncing Ball", 150, 50, "#FFFFFF", "24px Arial")
        
        # Run animation blocks
        super().update(time)

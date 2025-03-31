"""Line Bouncer Exercise
Make the ball bounce over multiple lines while maintaining bounce height!
"""

from framework.core import AnimationExample
from framework.ball import BouncingBall
from framework.testing.physics import HeightTest

class Exercise(AnimationExample):
    """Line bouncer exercise using physics-based commands."""
    
    # Student visible code template
    STUDENT_CODE = '''# Line Bouncer Challenge!
# Make the ball bounce over all lines while maintaining height
# Available commands:
#   ball.throw(power)  # power: 0.0 to 2.0
#   ball.jump(power)   # power: 0.0 to 2.0
#   ball.set_bounce(amount)  # amount: 0.0 to 1.0

# Add your solution here:
ball.throw(1.0)  # Try adjusting this!

# Add some effects for fun:
ball.trail_on()
ball.sparkles_on()
'''
    
    def _pre_setup(self):
        """Initialize the exercise."""
        # Create ball instance
        self.ball = BouncingBall()
        
        # Create lines to bounce over
        self.lines = [
            {'x': 100, 'y': 300, 'width': 50},
            {'x': 200, 'y': 300, 'width': 50},
            {'x': 300, 'y': 300, 'width': 50}
        ]
        
        # Create test cases
        self._tests = [
            HeightTest(self, target_height=150)
        ]
        
        # Create namespace for student code
        self._namespace = {
            'ball': self.ball
        }
        
        # Start animation
        self.start()
        
    def update(self, time):
        """Update animation frame."""
        # Clear and draw background
        self.api.clear()
        self.api.draw_rect(0, 0, self.api.width, self.api.height, "#2c2c2c")
        
        # Draw lines
        for line in self.lines:
            self.api.draw_rect(line['x'], line['y'], line['width'], 10, "#FF5722")
        
        # Update and draw ball
        self.ball.update(self.api.width, self.api.height)
        self.ball.draw(self.api)
        
        # Check test cases
        all_passed = True
        y = 30
        for test in self._tests:
            status = test.check()
            self.api.draw_text(
                status['message'], 20, y,
                "#4CAF50" if status['passed'] else "#FFFFFF",
                "16px Arial"
            )
            y += 25
            all_passed = all_passed and status['passed']
            
        if all_passed:
            self.api.draw_text("🎉 Challenge Complete! 🎉", 
                             self.api.width/2 - 100, self.api.height/2,
                             "#4CAF50", "24px Arial")
        
        # Run animation blocks
        super().update(time)

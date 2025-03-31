"""Bounce High Exercise
Make the ball bounce at least 3 times and reach height 100!
"""

from framework import AnimationExample, BouncingBall
from framework.testing.physics import BounceTest, HeightTest

class Exercise(AnimationExample):
    """Bounce high exercise using physics-based commands."""
    
    # Student visible code template
    STUDENT_CODE = '''# Bounce High Challenge!
# Make the ball bounce at least 3 times and reach height 100
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
        
        # Create test cases
        self._tests = [
            HeightTest(self, target_height=100),
            BounceTest(self, bounces=3)
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

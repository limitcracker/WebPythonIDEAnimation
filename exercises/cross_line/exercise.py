"""Cross the Line Exercise
Get the ball across the finish line!
"""

from framework.core import AnimationExample
from framework.testing.physics import LineTest, SpeedTest
from ...commands import BallCommands
import math
import random

class Exercise(AnimationExample):
    """Line crossing exercise."""
    
    # Student visible code template
    STUDENT_CODE = '''# Cross the Line Challenge!
# Get the ball across the finish line
# You must reach a speed of at least 15 to break through!

# Add some obstacles:
ball.add_wind_zone(100, 100)    # This creates wind resistance
ball.add_gravity_well(300, 200)  # This pulls the ball off course

# Add your solution here:
ball.throw(1.0)  # Try adjusting this!

# Add some effects for fun:
ball.fire_on()
ball.smoke_on()
'''
    
    def _pre_setup(self):
        """Initialize the exercise."""
        # Create ball instance
        from ...examples.bouncing_ball import BouncingBall
        self.ball = BouncingBall()
        
        # Create test cases
        self._tests = [
            LineTest(self, 350, 0, 350, 400),  # Vertical finish line
            SpeedTest(self, target_speed=15)
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
        
        # Draw finish line
        self.api.draw_rect(350, 0, 2, self.api.height, "#4CAF50")
        self.api.draw_text("Finish Line", 360, 30, "#4CAF50", "16px Arial")
        
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

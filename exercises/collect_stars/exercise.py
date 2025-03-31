"""Star Collector Exercise
Collect all stars in the most efficient way!
"""

from framework.core import AnimationExample
from framework.testing.gameplay import CollectiblesTest, PowerupTest, ScoreTest
from ...commands import BallCommands
import math
import random

class Exercise(AnimationExample):
    """Star collection exercise."""
    
    # Student visible code template
    STUDENT_CODE = '''# Star Collection Challenge!
# Collect stars to reach 100 points
# Use powerups to help you move faster!

# Set up the game items:
ball.add_star(150, 150)
ball.add_star(250, 250)
ball.add_star(350, 150)
ball.add_powerup(200, 200, "speed")
ball.add_powerup(300, 300, "jump")

# Add your solution here:
ball.throw(1.0)  # Try adjusting this!

# Add some effects for fun:
ball.rainbow_on()
ball.electric_on()
'''
    
    def _pre_setup(self):
        """Initialize the exercise."""
        # Create ball instance
        from ...examples.bouncing_ball import BouncingBall
        self.ball = BouncingBall()
        
        # Create test cases
        self._tests = [
            ScoreTest(self, target_score=100),
            PowerupTest(self, powerup_type="speed")
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

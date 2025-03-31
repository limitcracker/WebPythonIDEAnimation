"""Star Collector Exercise
Collect all stars in the most efficient way!
"""

from framework.core import AnimationExample
from framework.ball import BouncingBall
from framework.commands import BallCommands
from framework.testing.gameplay import ScoreTest, CollectiblesTest

class Exercise(AnimationExample):
    """Star collection exercise using high-level commands."""
    
    # Student visible code template
    STUDENT_CODE = '''# Star Collector Challenge!
# Collect all stars in the most efficient way
# Available commands:
#   ball.move_to(x, y)
#   ball.add_star(x, y)
#   ball.add_powerup(x, y, type)

# Set up game items
ball.add_star(100, 100)
ball.add_star(300, 100)
ball.add_star(200, 200)
ball.add_powerup(150, 150, "speed")

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
        
        # Create command interface
        self.commands = BallCommands(self.ball)
        
        # Create test cases
        self._tests = [
            CollectiblesTest(self, 'star', 3),
            ScoreTest(self, 300)
        ]
        
        # Create namespace for student code
        self._namespace = {
            'ball': self.ball,
            'commands': self.commands
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

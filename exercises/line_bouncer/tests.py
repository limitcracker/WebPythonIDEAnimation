"""Test cases for the Line Bouncer exercise."""

from framework.testing.base import TestSuite
from framework.testing.physics import BounceTest, LineTest, SpeedTest

class LineBouncerTests(TestSuite):
    """Test suite for Line Bouncer exercise."""
    
    def __init__(self, example):
        super().__init__()
        
        # Add specific test cases
        self.add_test(BounceTest(example, bounces=3))
        
        # Test crossing each line
        self.add_test(LineTest(example, 200, 0, 200, 400))
        self.add_test(LineTest(example, 300, 0, 300, 400))
        self.add_test(LineTest(example, 400, 0, 400, 400))
        
        # Test minimum speed for last line
        self.add_test(SpeedTest(example, target_speed=10))
        
    def get_hints(self):
        """Return exercise-specific hints."""
        return [
            "Use commands.bounce_times() to start bouncing",
            "Cross each line with increasing speed",
            "Try commands.cross_line() with different speed values"
        ]

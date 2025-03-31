"""Test cases for the Star Collector exercise."""

from framework.testing.base import TestSuite
from framework.testing.gameplay import CollectiblesTest, PowerupTest, ScoreTest

class StarCollectorTests(TestSuite):
    """Test suite for Star Collector exercise."""
    
    def __init__(self, example):
        super().__init__()
        
        # Add specific test cases
        self.add_test(CollectiblesTest(example, 'star', count=3))
        self.add_test(PowerupTest(example, 'speed'))
        self.add_test(ScoreTest(example, target_score=50))
        
    def get_hints(self):
        """Return exercise-specific hints."""
        return [
            "Try using commands.collect_all_stars() for automatic collection",
            "Plan an efficient path with commands.follow_path()",
            "Get the speed powerup first to move faster!"
        ]

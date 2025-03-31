"""Gameplay-based test cases for animation exercises."""

from .base import TestCase

class ScoreTest(TestCase):
    """Test if player reached target score."""
    def __init__(self, example, target_score):
        super().__init__(example)
        self.target_score = target_score
        
    def check(self):
        """Check if score reached target."""
        if self.ball.score >= self.target_score:
            self.passed = True
            self.message = f"Success! Score {self.ball.score} reached."
        else:
            self.message = f"Keep collecting! Score: {self.ball.score}/{self.target_score}"
            
        return self.get_status()

class PowerupTest(TestCase):
    """Test if player collected specific powerup."""
    def __init__(self, example, powerup_type):
        super().__init__(example)
        self.powerup_type = powerup_type
        
    def check(self):
        """Check if powerup was collected."""
        if self.ball._powerup_active == self.powerup_type:
            self.passed = True
            self.message = f"Success! {self.powerup_type} powerup collected."
        else:
            self.message = f"Try to collect the {self.powerup_type} powerup!"
            
        return self.get_status()

class CollectiblesTest(TestCase):
    """Test if player collected specific number of items."""
    def __init__(self, example, item_type, count):
        super().__init__(example)
        self.item_type = item_type
        self.required_count = count
        self.collected = 0
        
    def check(self):
        """Check collection count."""
        if self.item_type == 'star':
            self.collected = len(self.ball._collected_stars)
        elif self.item_type == 'powerup':
            self.collected = len(self.ball._collected_powerups)
            
        if self.collected >= self.required_count:
            self.passed = True
            self.message = f"Success! Collected {self.collected} {self.item_type}s."
        else:
            self.message = f"Keep going! Collected {self.collected}/{self.required_count} {self.item_type}s."
            
        return self.get_status()

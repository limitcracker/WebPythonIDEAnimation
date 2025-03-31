"""Physics-based test cases for animation exercises."""

from .base import TestCase

class BounceTest(TestCase):
    """Test if ball bounced N times."""
    def __init__(self, example, bounces=3):
        super().__init__(example)
        self.required_bounces = bounces
        self.bounce_count = 0
        self.last_dy = 0
        
    def check(self):
        """Check for bounce by detecting velocity change."""
        if self.ball.dy > 0 and self.last_dy < 0:
            self.bounce_count += 1
            
        self.last_dy = self.ball.dy
        
        if self.bounce_count >= self.required_bounces:
            self.passed = True
            self.message = f"Success! Ball bounced {self.bounce_count} times."
        else:
            self.message = f"Keep going! Bounced {self.bounce_count}/{self.required_bounces} times."
            
        return self.get_status()

class HeightTest(TestCase):
    """Test if ball reached certain height."""
    def __init__(self, example, target_height):
        super().__init__(example)
        self.target_height = target_height
        self.max_height = float('inf')
        
    def check(self):
        """Check if ball reached target height."""
        self.max_height = min(self.max_height, self.ball.y)
        
        if self.max_height <= self.target_height:
            self.passed = True
            self.message = f"Success! Ball reached height {int(self.max_height)}."
        else:
            self.message = f"Try to get the ball above y={self.target_height}. Current max: {int(self.max_height)}"
            
        return self.get_status()

class SpeedTest(TestCase):
    """Test if ball reached certain speed."""
    def __init__(self, example, target_speed):
        super().__init__(example)
        self.target_speed = target_speed
        self.max_speed = 0
        
    def check(self):
        """Check if ball reached target speed."""
        current_speed = (self.ball.dx**2 + self.ball.dy**2)**0.5
        self.max_speed = max(self.max_speed, current_speed)
        
        if self.max_speed >= self.target_speed:
            self.passed = True
            self.message = f"Success! Ball reached speed {int(self.max_speed)}."
        else:
            self.message = f"Try to get the ball moving faster than {self.target_speed}. Current: {int(self.max_speed)}"
            
        return self.get_status()

class LineTest(TestCase):
    """Test if ball crossed a line."""
    def __init__(self, example, x1, y1, x2, y2):
        super().__init__(example)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        
    def check(self):
        """Check if ball crossed the line segment."""
        # Line equation: ax + by + c = 0
        a = self.y2 - self.y1
        b = self.x1 - self.x2
        c = self.x2*self.y1 - self.x1*self.y2
        
        # Distance from point to line
        d = abs(a*self.ball.x + b*self.ball.y + c) / ((a*a + b*b)**0.5)
        
        # Check if point is within line segment bounds
        if d < self.ball.radius:
            if (min(self.x1, self.x2) <= self.ball.x <= max(self.x1, self.x2) and
                min(self.y1, self.y2) <= self.ball.y <= max(self.y1, self.y2)):
                self.passed = True
                self.message = "Success! Ball crossed the line."
                return self.get_status()
                
        self.message = "Try to cross the line with the ball."
        return self.get_status()

"""High-level commands for the bouncing ball exercises."""

class BallCommands:
    """High-level commands for controlling the ball."""
    
    def __init__(self, ball):
        self.ball = ball
        
    # Movement Commands
    def move_to(self, x, y, speed=1.0):
        """Move ball to target position at given speed."""
        dx = x - self.ball.x
        dy = y - self.ball.y
        distance = (dx**2 + dy**2)**0.5
        if distance > 0:
            self.ball.dx = dx / distance * speed
            self.ball.dy = dy / distance * speed
    
    def bounce_to_height(self, height, power=1.0):
        """Make ball bounce to reach specific height."""
        self.ball.dy = -power * (2 * self.ball.gravity * height)**0.5
        
    def follow_path(self, points, speed=1.0):
        """Make ball follow a series of points."""
        self.ball._path = points
        self.ball._path_speed = speed
        self.ball._path_index = 0
        
    # Game Commands
    def collect_all_stars(self):
        """Move to and collect all stars in sequence."""
        stars = [(star.x, star.y) for star in self.ball._stars]
        self.follow_path(stars)
        
    def reach_goal(self):
        """Move to the current goal."""
        if self.ball._goals:
            goal = self.ball._goals[0]
            self.move_to(goal.x, goal.y)
            
    def get_powerup(self, powerup_type):
        """Find and collect specific powerup."""
        for powerup in self.ball._powerups:
            if powerup.type == powerup_type:
                self.move_to(powerup.x, powerup.y)
                break
                
    # Challenge Commands
    def bounce_times(self, count, height=100):
        """Bounce specified number of times to minimum height."""
        self.ball.set_bounce(0.8)  # Good bounce factor
        self.bounce_to_height(height * 1.2)  # Extra height for multiple bounces
        
    def cross_line(self, x1, y1, x2, y2, speed=10):
        """Cross a line segment at specified speed."""
        # Find closest point on line
        dx = x2 - x1
        dy = y2 - y1
        t = ((self.ball.x - x1) * dx + (self.ball.y - y1) * dy) / (dx**2 + dy**2)
        t = max(0, min(1, t))
        
        # Target point just past the line
        target_x = x1 + dx * t + dx * 0.1
        target_y = y1 + dy * t + dy * 0.1
        
        self.move_to(target_x, target_y, speed)
        
    # Effect Commands
    def victory_celebration(self):
        """Show victory effects."""
        self.ball.rainbow_on()
        self.ball.sparkles_on()
        self.ball.trail_on()
        self.bounce_times(3, 150)  # Victory bounces!

"""Base test framework for animation exercises."""

class TestCase:
    """Base class for animation test cases."""
    def __init__(self, example):
        self.example = example
        self.ball = example.ball
        self.passed = False
        self.message = ""
        
    def check(self):
        """Check if test case passes. Override in subclasses."""
        raise NotImplementedError
        
    def get_status(self):
        """Get test status and message."""
        return {
            'passed': self.passed,
            'message': self.message
        }

class TestSuite:
    """Collection of test cases for an exercise."""
    def __init__(self):
        self.tests = []
        
    def add_test(self, test):
        """Add a test case to the suite."""
        self.tests.append(test)
        
    def check_all(self):
        """Run all tests and return results."""
        results = []
        all_passed = True
        
        for test in self.tests:
            status = test.check()
            results.append(status)
            all_passed = all_passed and status['passed']
            
        return {
            'all_passed': all_passed,
            'results': results
        }

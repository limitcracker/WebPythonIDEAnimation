# Web Python Animation IDE

An interactive web-based Python IDE for learning animation and physics concepts through hands-on coding exercises.

## Features

- Real-time Python code execution in the browser using Brython
- Interactive animation canvas with physics simulation
- Code editor with syntax highlighting
- Live feedback and exercise validation
- Bouncing ball physics with customizable properties

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/limitcracker/WebPythonIDEAnimation.git
   ```

2. Start a local web server:
   ```bash
   python -m http.server 8080
   ```

3. Open in your browser:
   ```
   http://localhost:8080/animation_framework/ide.html
   ```

## Exercise Example

```python
# Make the ball bounce high!
ball.throw(15)          # Throw ball up (0-20)
ball.set_bounce(0.95)   # Set bounce energy (0-1)
ball.set_color('red')   # Change color
ball.set_size(30)       # Change size (10-100)
```

## Dependencies

- [Brython](https://brython.info/) - Python in the browser
- [CodeMirror](https://codemirror.net/) - Code editor with syntax highlighting

## License

MIT License

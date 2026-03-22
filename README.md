# MCT India Summit Hackathons

- [MCT-India-Summit-Hackathons](https://github.com/iamneerajsingh/MCT-India-Summit-Hackathons/tree/main)
- [MCT India Summit](https://github.com/mctsummit/mctsummitindia2026/blob/main/README.md)

# QuadGrid Showdown

A 4x4 strategic grid game built with Python, featuring desktop (Tkinter) and web (Flask) interfaces.

## Game Rules

- 4x4 grid
- Two players: X and O
- Alternate turns
- Win by getting 4 in a row (horizontal, vertical, or diagonal)
- Draw if board is full with no winner

## Installation

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`

## Running the Game

### Desktop Version (Tkinter)

```bash
python tkinter_ui.py
```

### Web Version (Flask)

```bash
python app.py
```

Then open http://127.0.0.1:5000 in your browser.

Login with username: `admin`, password: `admin`

## Features

- Core game logic decoupled from UI
- Winner and draw detection
- Reset functionality
- Authentication for web version
- Clean architecture

## Testing

Run tests: `python test_game.py` or `pytest test_game.py`
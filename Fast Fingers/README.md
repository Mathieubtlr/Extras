# Fast Finger — Typing Speed Game

A terminal-based game that tests your typing speed and accuracy.

## Description
The program displays random words from a text file.  
Type them correctly and as fast as you can!

## How to Run
```bash
python fastfinger.py
```

## Dependencies
```bash
pip install numpy keyboard
```

## Files
- `fastfinger.py` — main game logic  
- `input_space.py` — real-time typing input  
- `words.txt` — dictionary of words  
- `nettoyage.py` — cleans accented words  
- `tri_alpha.py` — sorts words alphabetically  

## Notes
- Requires admin privileges to capture keyboard input on Windows.
- Works best in a standard terminal (not VS Code’s built-in console).

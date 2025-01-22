# tic-tac-toe

```markdown
# Tic Tac Toe Game 🎮

A Python-based **Tic Tac Toe** game with a graphical interface built using **Tkinter**. The game includes two modes:
1. **Player vs Computer** (with a smart AI opponent).
2. **Player vs Player**.

---

## Features ✨
- **Graphical User Interface (GUI):** Built with Tkinter for a user-friendly experience.
- **AI Opponent:** Implements a minimax algorithm for a challenging gameplay against the computer.
- **Dynamic Modes:** Choose between playing against another player or the computer.
- **Interactive and Animated:** Includes animations for winning and transitions between turns.

---

## Requirements 🛠️
Make sure you have the following installed on your system:
- **Python 3.8+**
- Tkinter (comes pre-installed with Python)

If Tkinter is not installed, you can install it using:
```bash
sudo apt-get install python3-tk  # For Ubuntu/Debian
```

---

## How to Run 🚀
1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/tic-tac-toe.git
   cd tic-tac-toe
   ```
2. Run the game:
   ```bash
   python3 main.py
   ```

---

## Game Modes 🎮
### 1. **Player vs Computer**
- The computer uses the **minimax algorithm** to determine the best move.
- Suitable for players looking for a challenge.

### 2. **Player vs Player**
- Play with a friend locally on the same computer.

---

## Screenshots 🖼️
### Main Menu:
![Main Menu](screenshots/main_menu.png)

### Gameplay:
![Gameplay](screenshots/gameplay.png)

---

## Troubleshooting ⚠️
If you encounter the error:
```plaintext
_tkinter.TclError: no display name and no $DISPLAY environment variable
```
It means the program is running in a non-GUI environment (like a server or Codespaces). To fix this:
1. Run the program on a local machine with a display.
2. Or use `xvfb`:
   ```bash
   xvfb-run -a python3 main.py
   ```

---

## Contributing 🤝
Contributions are welcome! Feel free to submit a pull request or open an issue.

---

## License 📜
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

### Author 👤
**Yedidya Krimolovsky**  

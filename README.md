<a id="readme-top"></a>

<div align="center">

# Tic-Tac-Toe Bot

**A modular Tic-Tac-Toe game with an unbeatable Minimax-based bot and Tkinter GUI.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-FFCA28?style=for-the-badge)](https://docs.python.org/3/library/tkinter.html)
[![Version](https://img.shields.io/badge/version-1.0.0-2ea44f?style=for-the-badge)](#version)

</div>

---

## Table of Contents

<details>
<summary>View</summary>

- [About the Project](#about-the-project)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

</details>

---

## About the Project

This project is a small, modular implementation of Tic-Tac-Toe featuring a bot that uses the **Minimax algorithm** to evaluate possible game states and select its optimal move.

The application supports two interfaces:

- **GUI** — a desktop interface built with Tkinter
- **CLI** — a terminal-based interface for running the game without the GUI

`main.py` acts as the single entry point and selects the interface based on the command-line arguments.

---

## Getting Started

### Prerequisites

- Python **3.10+**
- Tkinter

Tkinter is included with most standard Python installations.

### Installation

1. Clone the repository.

   ```bash
   git clone https://github.com/IHac-er/TicTacToe-Bot.git
   cd TicTacToe-Bot
   ```

No third-party Python packages are required.

---

## Usage

### GUI

Launch the default graphical interface:

```bash
python main.py
```

### CLI

Run the terminal version:

```bash
python main.py --cli
```

---

## Project Structure

```text
.
├── main.py             # Application entry point and CLI interface
├── TicTacToe.py        # Core game state and rules
├── TicTacToeGUI.py     # Tkinter graphical interface
└── bot.py              # Minimax-based Tic-Tac-Toe bot
```

The project keeps the game state, bot logic, and presentation layer separated into independent modules.

---

## How It Works

### Game Engine

`TicTacToe.py` maintains the authoritative game board, validates moves, and determines whether the game has been won or drawn.

### Bot

`bot.py` evaluates possible moves using recursive **Minimax** search:

```text
Bot move     → maximize score
Player move  → minimize score

Bot win      → +1
Player win   → -1
Draw         →  0
```

Because standard Tic-Tac-Toe has a small finite game tree, the bot can exhaustively evaluate available positions and avoid losing.

### GUI

`TicTacToeGUI.py` provides the interactive board and delegates game-state decisions to the existing game and bot classes rather than duplicating the game logic.

---

## Contributing

Contributions, suggestions, and improvements are highly welcomed.

1. Fork the project.
2. Create a feature branch.

   ```bash
   git checkout -b feature/<your-feature>
   ```

3. Commit your changes.

   ```bash
   git commit -m "Add your change"
   ```

4. Push the branch.

   ```bash
   git push origin feature/<your-feature>
   ```

5. Open a pull request.

---

## License

No open-source license has been specified for this project yet.

---

## Acknowledgments

- [Python](https://www.python.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- The Minimax algorithm for the bot's decision-making strategy

---

## Version

**v1.0.0** — Initial complete release with CLI, GUI, and Minimax-based bot.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[python-badge]: https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white
[python-url]: https://www.python.org/
[tkinter-badge]: https://img.shields.io/badge/Tkinter-FFCA28?style=for-the-badge
[tkinter-url]: https://docs.python.org/3/library/tkinter.html
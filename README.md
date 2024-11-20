# Tic Tac Toe
Welcome to the Tic-Tac-Toe Game! This is a simple yet engaging web-based game developed using HTML, CSS, and JavaScript. The game offers two modes (Human vs. Human and Human vs. Computer), adjustable difficulty levels, and an interactive, responsive design.

# Features
## Game Modes:
Human vs. Human: Two players can take turns playing on the same device.
Human vs. Computer: Play against an AI opponent with adjustable difficulty levels.

## AI Difficulty Levels:
Beginner: Random moves.
Professional: Predicts a maximum of two moves ahead.
Legendary: Implements the Minimax algorithm with deep predictions.

## Score Tracking:
Tracks wins for Player X, Player O, and draws.

## Responsive Design:
The gameboard and UI adapt to various screen sizes for a smooth user experience.

## Dynamic UI Enhancements:
Interactive grid with hover effects and animations.
Visual feedback for wins and draws using icons and colors.

## Technologies Used
HTML: Defines the structure of the game interface.
CSS: Styles the gameboard, buttons, and scoreboard for a visually appealing design.
JavaScript: Implements the game logic, AI opponent, and interactive features.

## How to Play
1. Clone this repository to your local machine:
    git clone https://github.com/your-username/tic-tac-toe.git cd tic-tac-toe

2. Open the index.html file in your browser to launch the game.
3. Choose a Mode: Use the dropdown menu to select Human vs. Human or Human vs. Computer.
4. Adjust Difficulty (if playing against the computer):
    Select difficulty level from Beginner, Professional, or Legendary.
5. Start Playing:
    Click on any cell in the grid to make your move.
    The current player is indicated by the X or O marker in the cells.
6. The game automatically detects wins, losses, and draws, updating the scoreboard accordingly.
7. Use the Reset button to restart the game or reset scores.

## Key Code Features
Game Logic:

Tracks the current state of the board using an array.
Automatically detects wins, losses, and draws using predefined winning combinations.
AI Opponent:

Implements the Minimax algorithm for intelligent decision-making.
Adjusts difficulty dynamically based on the selected level.
Responsive Design:

Uses CSS grid for the gameboard layout.
Hover effects and animations provide a polished user experience.
Dynamic UI Updates:

Updates the scoreboard and displays win/draw messages in real-time.
Known Issues and Limitations
Limited Undo:

There is no undo option to reverse moves.
AI Limitations:

While the AI is challenging, the implementation of Minimax can slow down for large-scale extensions of the game (e.g., larger boards or complex rules).
Future Improvements
Add support for larger grid sizes (e.g., 4x4 or 5x5 boards).
Introduce multiplayer options using WebSocket for online play.
Implement an undo/redo feature for better gameplay flexibility.
Enhance the UI with sound effects and improved animations.
Add sound to the game.

License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as per the terms of the license.

Happy Gaming! 🎮

# Hanguess

Hanguess is a simple Hangman game implemented using Python and Tkinter. It allows users to guess letters or the entire word to uncover a hidden word within a chosen category.

## Features

- Multiple word categories to choose from, including animals, fruits and vegetables, car brands, cities, countries, games, football teams, professions, films, and animes.
- Customizable color scheme for the user interface.
- Ability to display hints based on the length of the word.
- Keeps track of the user's score and displays it during the game.
- Provides an option to view the top 10 scores.
- Visual representation of the Hangman's progress.
- Support for both keyboard input and on-screen keyboard buttons.

## How to Play

1. Run the `main.py` script to start the game.
2. Enter your username when prompted.
3. Click on the "Click here and pick a type" button to choose a word category.
4. Click the "Start Game" button to begin playing.
5. Guess letters by either typing them in the input section or clicking the corresponding buttons on the on-screen keyboard.
6. Use the "Hint" button to reveal a correct letter based on the number of letters in the word.
7. You have 6 lives, represented by the Hangman's progress. If you make 6 incorrect guesses, the game is over.
8. If you know the word, you can type it into the input section to win the game.
9. The game keeps track of your score based on the number of correct letters guessed and deducts points for using hints.
10. Click the "Options" button to customize the color scheme.
11. Click the "Help" button for detailed instructions on how to play the game.
12. Click the "Top 10" button to view the top 10 scorers.
13. To restart the game, follow the same steps as 3 and 4.

## Dependencies

- Python 3.x
- Tkinter (usually included with Python)

## Credits

The Hangman game was developed by Ahmet Enes Topcu.

The `hangman_art.py` file contains ASCII art for the Hangman's progress.

The `new_words.py` file provides word lists for different categories.

The `score_manager.py` file handles score management, including reading and writing scores.

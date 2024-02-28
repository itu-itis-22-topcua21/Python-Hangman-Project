import random
import tkinter as tk  #
from tkinter import messagebox, colorchooser
from hangman_art import stages, logo
from new_words import animals, fruits_and_vegetables, car_brands, cities, countries, games, football_teams, professions, \
    films, animes
import score_manager

word_lists = {
    "Animals": animals,
    "Fruits and vegetables": fruits_and_vegetables,
    "Car Brands": car_brands,
    "Cities": cities,
    "Countries": countries,
    "Games": games,
    "Football Teams": football_teams,
    "Professions": professions,
    "Films": films,
    "Animes": animes
}


class Hangman:
    color1 = "purple"
    hint_count = 0
    game_over = False
    name = ""
    score = 0


    def change_logo_color(self, color):
        self.logo_label.config(fg=color) # Change the color of the logo label

    def change_hangman_label_color(self, color):
        self.hangman_label.config(fg=color) # Change the color of the hangman label

    def button_hover_in(self, event):
        event.widget.config(bg="aqua") # Change the background color when the button is hovered over

    def button_hover_out(self, event):
        event.widget.config(bg=self.color1) # Change the background color back to the original color when the mouse moves away from the button

    def set_background_image(self, frame):
        background_label = tk.Label(frame, image=self.background_photo) # Set the background image of a given frame
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def __init__(self, master):
        self.master = master
        master.title("Hanguess")
        self.name = input("Enter username: ")

        self.background_label = tk.Label(master) # Creating a label to display the background image
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        try:
            from PIL import Image, ImageTk # Loading the background image using PIL (Python Imaging Library)
            self.background_image = Image.open("background_image.png")
            self.background_photo = ImageTk.PhotoImage(self.background_image)
            self.background_label.config(image=self.background_photo)
        except ImportError:
            messagebox.showerror("Error", "PIL (Python Imaging Library) is required to load the background image.")

        self.frame0 = tk.Frame(master) # Creating the main frame for the GUI elements
        self.frame0.place(relx=0.5, anchor="n")
        self.set_background_image(self.frame0)

        self.frame1 = tk.Frame(self.frame0) # Creating two sub-frames within the main frame
        self.frame1.grid(row=2, column=0)
        self.set_background_image(self.frame1)

        self.frame2 = tk.Frame(self.frame0)
        self.frame2.grid(row=1, column=0, pady=10)
        self.set_background_image(self.frame2)

        self.left_frame = tk.Frame(self.frame1) # Creating a left frame and a right frame within the sub-frame
        self.set_background_image(self.left_frame)
        self.left_frame.grid(row=0, column=0, pady=100)

        self.right_frame = tk.Frame(self.frame1)
        self.set_background_image(self.right_frame)
        self.right_frame.grid(row=0, column=1, padx=100)

        self.logo_label = tk.Label(self.frame0, text=logo, font=("Courier", 8)) # Creating a label to display the logo
        self.logo_label.grid(column=0, row=0)

        self.word_list_var = tk.StringVar(master)
        self.word_list_var.set("Click here and pick a type :")
        self.word_list_options = tk.OptionMenu(self.frame2, self.word_list_var, *word_lists.keys())
        self.word_list_options.config(width=25, bg="mediumspringgreen", font=("Arial", 13), fg="midnightblue", height=1)
        self.word_list_options.grid(row=0, column=0)

        self.start_button = tk.Button(self.frame2, text="Start Game", command=self.start_game)
        self.start_button.config(width=18, bg="mediumspringgreen", font=("Arial", 12), fg="midnightblue", height=1)
        self.start_button.grid(row=1, column=0)

        self.options_button = tk.Button(self.frame0, text="Chose Color", command=self.options)
        self.options_button.config(width=10, bg="mediumpurple", font=("Arial", 12), fg="white", height=1)
        self.options_button.place(relx=0.9, anchor="n")

        self.help_button = tk.Button(self.frame0, text="Help", command=self.help)
        self.help_button.config(width=10, bg="royalblue", font=("Arial", 12), fg="white", height=1)
        self.help_button.place(relx=0.1, anchor="n")

        self.hint_count_label = tk.Label(self.right_frame)
        self.hint_count_label.config(height=1, font=("monospace", 16), text=f"Remaining hints: {self.hint_count}")
        self.hint_count_label.grid(row=0, column=0)

        self.hint_button = tk.Button(self.right_frame, text="Hint", command=self.hint)
        self.hint_button.config(width=10, bg="teal", font=("Arial", 12), fg="lightcyan", height=1)
        self.hint_button.grid(row=1, column=0)

        self.hangman_label = tk.Label(self.right_frame)
        self.hangman_label.grid(row=2, column=0)

        self.word_label = tk.Label(self.right_frame)
        self.word_label.config(height=1, font=("monospace", 16))
        self.word_label.grid(row=3, column=0)

        self.guess_entry = tk.Entry(self.right_frame)
        self.guess_entry.bind("<Return>", (lambda event: self.submit_guess())) # Binding the <Return> key event to a lambda function that calls the submit_guess() method
        self.guess_entry.config(width=20, font=("Arial", 16))
        self.guess_entry.grid(row=4, column=0)

        self.submit_button = tk.Button(self.right_frame, text="Submit", command=self.submit_guess)
        self.submit_button.config(width=10, bg="teal", font=("Arial", 12), fg="lightcyan", height=1)
        self.submit_button.grid(row=5, column=0)

        self.score_label1 = tk.Label(self.right_frame)
        self.score_label1.config(height=1, font=("monospace", 16), text=f"Your Score: {self.score}")
        self.score_label1.grid(row=6, column=0)

        self.submit_button = tk.Button(self.right_frame, text="Top 10", command=self.show_top_scores)
        self.submit_button.config(width=10, bg="teal", font=("Arial", 12), fg="lightcyan", height=1)
        self.submit_button.grid(row=7, column=0)


        self.keyboard_frame = tk.Frame(self.left_frame)
        self.set_background_image(self.keyboard_frame)
        self.keyboard_frame.grid()

        self.letter_buttons = []
        for i, letter in enumerate('abcdefghijklmnopqrstuvwxyz'): # Iterate over each letter in the string 'abcdefghijklmnopqrstuvwxyz' along with its index
            button = tk.Button(self.keyboard_frame, text=letter.upper(), command=lambda l=letter: self.guess_letter(l),
                               bg=self.color1, font=("Arial", 20), fg="yellow", width=3, height=1)  # Create a button widget for the letter
            button.grid(row=i // 7, column=i % 7, padx=3, pady=3) # Place the button in the grid layout of the keyboard_frame
            self.letter_buttons.append(button)

        for button in self.letter_buttons:
            button.bind("<Enter>", self.button_hover_in)
            button.bind("<Leave>", self.button_hover_out)

    def submit_guess(self):
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)

        if guess == self.random_word:
            self.game_over = True
            messagebox.showinfo("Hangman", f"You win! True word was: {self.random_word}")
            print("You win!")
            self.end_game()
        elif len(guess) != 1 or not guess.isalpha():
            messagebox.showinfo("Hangman", "Please enter a single letter or whole true word.")
        else:
            self.guess_letter(guess)

    def start_game(self):
        self.word_point = 0
        self.chosen_word_list = self.word_list_var.get() # Get the chosen word list from the variable
        self.random_word_first = random.choice(word_lists[self.chosen_word_list])
        self.random_word = self.random_word_first.lower()
        self.length_of_word = len(self.random_word)
        for i in self.random_word: # Count the number of alphabetic characters in the word
            if i.isalpha():
                self.word_point += 1

        if self.length_of_word <= 6:
            self.hint_count = 1
        elif 6 < self.length_of_word <= 10:
            self.hint_count = 2
        elif self.length_of_word > 10:
            self.hint_count = 3
        self.hint_count_label.config(height=1, font=("monospace", 16), text=f"Remaining hints: {self.hint_count}")

        str1 = ""
        lst1 = []
        for letter in self.random_word:
            if letter.isalpha(): # Check if the current letter is alphabetic
                lst1.append("_") # If it is, append an underscore to the list
            else:
                lst1.append(letter) # If it is not alphabetic, append the letter itself to the list
        self.showed = lst1 # Assign the modified list to the 'showed' variable

        self.rest_of_live = 6
        self.game_over = False
        self.word_label.config(text=' '.join(self.showed)) # Update the text of the 'word_label' widget with the modified list

        for button in self.letter_buttons: # Enable all the buttons in the 'letter_buttons' list
            button.config(state='normal')

    def end_game(self):
        max_hint = 3
        if self.length_of_word <= 6:
            max_hint = 1
        elif 6 < self.length_of_word <= 10:
            max_hint = 2
        elif self.length_of_word > 10:
            max_hint = 3
        used_hints = max_hint - self.hint_count
        point = self.word_point - used_hints
        self.score += point
        self.score_label1.config(height=1, font=("monospace", 16), text=f"Your Score: {self.score}")
        self.start_game()

    def guess_letter(self, estimated):
        if not self.game_over:
            if estimated in self.showed:
                messagebox.showinfo("Hangman", f"You've already tried {estimated}")

            for location in range(self.length_of_word):
                letter = self.random_word[location]
                if letter == estimated:
                    self.showed[location] = letter

            if estimated not in self.random_word:
                messagebox.showinfo("Hangman",
                                    f"You have guessed {estimated}, it is not in the word. You just lost a life.")
                self.rest_of_live -= 1
                if self.rest_of_live == 0:
                    self.game_over = True
                    score_manager.write_score(self.name, self.score)
                    self.score = 0
                    self.score_label1.config(height=1, font=("monospace", 16), text=f"Your Score: {self.score}")
                    messagebox.showinfo("Hangman", "You've consumed all your lives.")
                    messagebox.showinfo("Hangman", f"True word was: {self.random_word}")

            self.word_label.config(text=' '.join(self.showed))
            self.hangman_label.config(text=stages[self.rest_of_live], font=("TkFixedFont", 16), width=20, height=10)
            for button in self.letter_buttons:
                if button["text"].lower() == estimated:
                    button.config(state='disabled')

            if "_" not in self.showed:
                self.game_over = True
                messagebox.showinfo("Hangman", "You win!")
                print("You win!")
                self.end_game()

    def show_top_scores(self):
        top_scores = score_manager.get_top_10_scores()
        messagebox.showinfo("Top 10 Scores", "\n".join([f"{name}: {score}" for name, score in top_scores.items()]))




    def hint(self): # Check if there are hints remaining
        if self.hint_count > 0:
            for i in range(self.length_of_word): # Check if the current position in 'showed' contains an underscore
                if self.showed[i] == "_":
                    self.showed[i] = self.random_word[i] # Replace the underscore with the corresponding letter from 'random_word'
                    count = 0
                    count2 = 0
                    for j in self.random_word: # Iterate over each letter in 'random_word'

                        if j == self.showed[i]: # Check if the current letter matches the letter at the updated position in 'showed'
                            count += 1
                            self.showed[count2] = j
                        count2 += 1
                    self.hint_count -= 1 # Decrease the hint count by 1
                    self.hint_count_label.config(height=1, font=("monospace", 16), text=f"Remaining hints: {self.hint_count}")
                    if "_" not in self.showed:  # Check if there are no more underscores in 'showed'
                        self.game_over = True
                        messagebox.showinfo("Hangman", "You win!")
                        print("You win!")
                        self.end_game()
                    break
            self.word_label.config(text=' '.join(self.showed))
        else:
            messagebox.showinfo("Hangman", "No more hints available.")

    def options(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.word_label.config(fg=color)
            self.change_logo_color(color)
            self.change_hangman_label_color(color)

    def help(self):
        messagebox.showinfo("Help", """
1.Click the 'Click here and pick a type' button to choose a word type.
2.Click the 'Start game' button.
3.Look at the "_____" symbols and make your guesses.
4.Hint button: Gives you a chance to see a correct letter based on the number of letters in the word.
5.You can click on the colored keyboard on the screen, or you can type in the input section using your own keyboard.
6.You have 6 lives. If you make 6 mistakes, the game will be over.
7.If you know the word and dont consume your 6 lives, game the game gives you a new word from the same word type.
8.If you use hint it goes -1 point. You get +1 point for each letter you know in the word.
9.Click the 'Option' button to adjust the colors.
10.If you know the whole word, you can type it into the input section using your keyboard.
11.click 'top 10' button to see the top 10 scorers
12.To restart the game, you can follow the same steps as 1 and 2.
        """)

    def check_gameover(self, window):
        if self.game_over:
            game_started = False
            window.destroy()
            return True
        else:
            game_started = True
            return False
def initiate_hanguess():
    root = tk.Tk()
    root.title("Hanguess")
    hangman = Hangman(root)
    root.geometry("1200x700")
    root.minsize(1100, 700)

    root.mainloop()

game_started = False

initiate_hanguess()
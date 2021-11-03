from flask import Flask
import random
app = Flask(__name__)

random_number =  random.randint(0,9)

@app.route('/')
def main_page():
    return '<h1> Guess a number between 0 and 9 </h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" />'


@app.route("/<int:guessed_number>")
def handle_guess(guessed_number):
    if guessed_number < random_number:
        return '<h1 style="color:red"> Too low </h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" />'
    if guessed_number > random_number:
        return '<h1 style="color:purple"> Too high </h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" />'
    if guessed_number == random_number:
        return '<h1 style="color:green"> You found me! </h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" />'



if __name__ == "__main__":
    #Run the app in debug mode to auto-reload
    app.run(debug=True)
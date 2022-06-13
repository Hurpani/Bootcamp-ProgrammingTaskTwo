from random import randint
from typing import Optional


class Game:
    QUIT_MESSAGE: str = "Thanks for playing!"
    SUCCESS_MESSAGE: str = "You correctly guessed my number!"
    GREATER_THAN_THAT_MESSAGE: str = "My number is greater than that!"
    LESS_THAN_THAT_MESSAGE: str = "My number is less than that!"
    USER_INPUT_MESSAGE: str = "Please input your guess of my number (or type 'no' to quit): "
    INVALID_INPUT_MESSAGE: str = "Your input must be a number. Please try again."

    # Upon instantiation, a Game will assign itself with a random number.
    def __init__(self, number: Optional[int] = None):
        self.my_number: int = randint(1, 100) if number is None else number

    # Prompt the player for input until they input something sensible, or want to quit.
    def get_user_guess(self) -> Optional[int]:
        user_input: str = input(Game.USER_INPUT_MESSAGE)
        if user_input == "no":
            return None
        try:
            return int(user_input.strip())
        except ValueError:
            print(Game.INVALID_INPUT_MESSAGE)
            return self.get_user_guess()

    # Emit a hint to the player.
    def respond_to_guess(self, guess: int) -> None:
        if guess == self.my_number:
            print(Game.SUCCESS_MESSAGE)
        elif guess < self.my_number:
            print(Game.GREATER_THAN_THAT_MESSAGE)
        else:
            print(Game.LESS_THAN_THAT_MESSAGE)

    # Process a player's guess to determine whether they want to continue playing,
    # and give them a hint (or victory message) if they instead provide a guess.
    def process_guess(self, guess: Optional[int]) -> bool:
        if guess is None:
            return False
        else:
            self.respond_to_guess(guess)
            return guess != self.my_number

    # Kick off the main game loop.
    def play(self) -> None:
        guess: Optional[int] = self.get_user_guess()
        should_continue: bool = self.process_guess(guess)
        if not should_continue:
            print(Game.QUIT_MESSAGE)
        else:
            self.play()


def main() -> None:
    Game().play()
    while input("Would you like to play again? (y/?) ") == "y":
        Game().play()


if __name__ == "__main__":
    main()

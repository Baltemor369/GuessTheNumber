import modules.Window as Window
import modules.GuessGame as GuessGame

# auto-py-to-exe

if __name__ == "__main__":
    game = GuessGame.GuessGame()
    app = Window.Window(game)
    app.run()
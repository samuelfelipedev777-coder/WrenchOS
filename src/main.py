from src.app import App
from src.cli.terminal import run_terminal

def main():
    app = App()
    app.start()
    run_terminal()


if __name__ == "__main__":
    main()
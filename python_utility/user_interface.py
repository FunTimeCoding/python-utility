import curses
from curses.textpad import rectangle, Textbox


class UserInterface:
    def __init__(self, arguments: list, screen):
        self.arguments = arguments
        self.screen = screen

    def run(self) -> int:
        if self.screen is None:
            exit_code = 1
            print('Screen is not set.')
        else:
            position_y = 0
            position_x = 0
            message = 'ctrl-g to send message'
            self.screen.addstr(position_y, position_x, message)

            try:
                self.loop()
            except KeyboardInterrupt:
                pass

            exit_code = 0

        return exit_code

    def loop(self) -> None:
        # stdscr.clear()
        # stdscr.getkey()

        while True:
            height = 10
            width = 40
            position_y = 2
            position_x = 1
            window = curses.newwin(height, width, position_y, position_x)

            position_y = 1
            position_x = 0
            rectangle(
                self.screen,
                position_y,
                position_x,
                height + 2,
                width + 1
            )

            self.screen.refresh()

            box = Textbox(window)
            box.edit()
            message = box.gather()

            position_y = 13
            position_x = 0
            self.screen.addstr(position_y, position_x, 'read: ' + message)
            message = message.strip()

            if message == 'quit':
                break

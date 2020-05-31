import curses
from curses.textpad import rectangle, Textbox


class UserInterface:
    def __init__(self, screen):
        self.screen = screen

    def run(self) -> int:
        if self.screen is None:
            exit_code = 1
            print('Screen is not set.')
        else:
            self.print_quit_message()
            self.loop_try()
            exit_code = 0

        return exit_code

    def loop_try(self) -> None:
        try:
            self.loop()
        except KeyboardInterrupt:
            pass

    def loop(self):
        while True:
            height = 10
            width = 40
            window = UserInterface.create_window(height=height, width=width)
            self.draw_rectangle(window_height=height, window_width=width)
            self.screen.refresh()

            if self.read_message(window=window) == 'quit':
                break

    @staticmethod
    def create_window(height: int, width: int):
        position_y = 2
        position_x = 1

        return curses.newwin(
            height,
            width,
            position_y,
            position_x
        )

    def print_quit_message(self):
        position_y = 0
        position_x = 0
        message = 'ctrl-g to send message'
        self.screen.addstr(position_y, position_x, message)

    def draw_rectangle(self, window_height: int, window_width: int):
        position_y = 1
        position_x = 0
        rectangle(
            win=self.screen,
            uly=position_y,
            ulx=position_x,
            lry=window_height + 2,
            lrx=window_width + 1
        )

    def read_message(self, window):
        box = Textbox(window)
        box.edit()
        message = box.gather()
        position_y = 13
        position_x = 0
        self.screen.addstr(
            position_y,
            position_x,
            'read: ' + message
        )

        return message.strip()

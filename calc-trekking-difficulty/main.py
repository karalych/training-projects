import tkinter as tk

from win_position import Win_position
from calculation import Сalculation


def _onKeyRelease(event):
    ctrl = (event.state & 0x4) != 0
    if event.keycode == 88 and ctrl and event.keysym.lower() != 'x':
        event.widget.event_generate('<<Cut>>')
    if event.keycode == 86 and ctrl and event.keysym.lower() != 'v':
        event.widget.event_generate('<<Paste>>')
    if event.keycode == 67 and ctrl and event.keysym.lower() != 'c':
        event.widget.event_generate('<<Copy>>')


def main():
    window = tk.Tk()
    window.resizable(False, False)
    window.iconbitmap('icon.ico')
    window.bind_all('<Key>', _onKeyRelease, '+')
    Сalculation(window)
    Win_position.center(window)
    window.mainloop()


if __name__ == '__main__':
    main()

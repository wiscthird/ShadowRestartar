import pyautogui
import os
import sys


def main(arg):
    if arg == 1:
        pyautogui.click(x=650, y=600)
    if arg == 2:
        pyautogui.click(x=550, y=700)


if __name__ == '__main__':
    args = sys.argv
    main(args[1])
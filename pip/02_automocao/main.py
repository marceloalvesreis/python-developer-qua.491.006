import pyautogui as auto
import time

def main():
    auto.PAUSE = 1.0
    auto.press("win")
    auto.write("edge")
    auto.press("enter")
    auto.hotkey("alt", "space")
    auto.press("x")
    auto.write("github.com")
    auto.press("enter")

if __name__ == "__main__":
    main()
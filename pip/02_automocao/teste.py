import pyautogui as auto
import time

def main():
    auto.PAUSE = 1.0  
    auto.hotkey("win", "r")
    time.sleep(0.5)
    auto.write("cmd")
    auto.press("enter")
    time.sleep(1.5)  
    auto.write("code .")
    auto.press("enter")

if __name__ == "__main__":
    main()

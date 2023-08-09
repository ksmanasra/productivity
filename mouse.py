import pyautogui
import time

def move_mouse():
    count = 0
    while True:
        try: 
            x, y = pyautogui.position()

            pyautogui.moveTo(x + 10, y + 10)

            time.sleep(10)

            x, y = pyautogui.position()

            pyautogui.moveTo(x - 10, y - 10)

            time.sleep(10)

            if count == 500: #timeout after 2-3 hours
                pyautogui.keyDown('ctrl')
                pyautogui.keyDown('command')
                pyautogui.keyDown('q')
                break
            else: 
                count += 1
        except KeyboardInterrupt:
            print("\nScript terminated by user.")
            break

if __name__ == "__main__":
    print("Press Ctrl + C to stop the script.")
    move_mouse()

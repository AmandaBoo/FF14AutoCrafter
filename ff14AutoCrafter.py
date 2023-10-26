import pyautogui
import time


"""
Keep the game in windowed mode and extend it to fill the entire desktop as much
as you can
Have the pot you want opened up with the synthesis button visible
"""

def clickFunction(xpos, ypos, count, sleepTime):
    for i in range(count):
        pyautogui.click(xpos, ypos, count)
    time.sleep(sleepTime)


def main():
    rotationsInput = int(input("Rotations desired: "))

    #click into ff screen
    pyautogui.click(1093, 192)
    while (rotationsInput != 0):
        print("Starting", rotationsInput)

        # synthesis
        clickFunction(1066, 764, 2, 2)

        # macro 1 (time to run macro 1)
        clickFunction(942, 685, 2, 37)

        # macro 2 (time to run macro 2)
        clickFunction(981, 685, 2, 23)

        print("Finished", rotationsInput)
        rotationsInput -=1

if __name__ == "__main__":
    main()
import pyautogui
import time


"""
Keep the game in windowed mode and extend it to fill the entire desktop as much
as you can
Have the pot you want opened up with the synthesis button visible
"""


# change to quantitiy desired
potsWanted = int(input("Pots desired: "))


pyautogui.click(1093, 192) #click into ff screen
while (potsWanted != 0):
    print("Starting", potsWanted)
    
    # synthesis
    pyautogui.click(1066, 764)
    pyautogui.click(1066, 764)

    # trial synthesis
    #pyautogui.click(796, 764) 
    #pyautogui.click(796, 764)

    # synthesis sleep
    time.sleep(2)

    # macro 1 (time to run macro 1)
    pyautogui.click(942, 685) 
    pyautogui.click(942, 685) 
    time.sleep(37)

    # macro 2 (time to run macro 2 + 3 sec for finish animation)
    pyautogui.click(981, 685) 
    pyautogui.click(981, 685) 
    time.sleep(23)

    print("Finished", potsWanted)
    potsWanted -=1

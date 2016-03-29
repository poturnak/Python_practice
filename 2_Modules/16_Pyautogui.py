#! /library/Frameworks/Python.framework/Versions/3.5/python3.5
# ===================================================================================================
# pyautogui.PAUSE = 1 - wait 1 second before proceeding with next items
#                     - applicable to all functions, all pyautogui functions will wait 1 second at the end of operation
# pyautogui.FAILSAFE = True - you can move the cursor up left and the exception will be created
# pyautogui.size() - returns the pixel size of your screen
# --coordinates start at the top left cornere: x increases to the right; y increases to the bottom
# pyautogui.moveTo() - will move the mouse to certain coordinates
#                    - x, y, and duration(how long will it take to make a movement)
# pyautogui.moveRel() - moves cursor relative to the current position
# pyautogui.position() - returns current mouse position coordinates
# _____________________ Clicking ________________________
# pyautogui.click - will send a virtual click to the system
# pyautogui.click(100, 150, button='left') - click left button at the specified position
# pyautogui.mouseDown() - push mouse down
# pyautogui.mouseUp() - release mouse
# pyautogui.doubleClick() - double click
# pyautogui.middleClick() - middle click
# _____________________ Dragging ________________________
# pyautogui.dragTo(x, y, duration) -
# pyautogui.dragRel(x, y, duration) -
# _____________________ Scrolling ________________________
# pyautogui.scroll(int) - scrolling, pass the integer number
# _____________________ Screenshot ________________________
# variable = pyautogui.screenshot() - take a screenshot; returns the image object
# im.getpixel((50, 200)) - get pixel color at specified location
# pyautogui.pixelMatchesColor(50, 200, (255, 135, 144)) - check if the color matches at the specified location
# _____________________ Keyboard ________________________
# pyautogui.typewrite('text', pause) - sends virtual keys
# --this is how you would do control c
# pyautogui.keyDown('ctrl')
# pyautogui.keyDown('c')
# pyautogui.keyUp('c')
# pyautogui.keyUp('ctrl')
# --this is a simpler way
# pyautogui.hotkey('ctrl', 'c')
# ===================================================================================================

import pyautogui, time, sys
# pyautogui.PAUSE = 1
# pyautogui.FAILSAFE = True

# print(pyautogui.size())

# for i in range(2):
#     pyautogui.moveTo(100, 100, duration=0.25)
#     pyautogui.moveTo(200, 100, duration=0.25)
#     pyautogui.moveTo(200, 200, duration=0.25)
#     pyautogui.moveTo(100, 200, duration=0.25)

print(pyautogui.position())

# Let's build a program that will define the mouse location on the screen and display the coordinates

# try:
#     while True:
#         x, y = pyautogui.position()
#         display = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         sys.stdout.write('\r' + display)
#         time.sleep(0.3)
#         sys.stdout.flush()
# except KeyboardInterrupt:
#     print('All done')


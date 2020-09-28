import pyautogui
import pyperclip



##wd = pyautogui.getActiveWindowTitle('see.txt - Notepad)
##pyautogui.click(wd.left+100, wd.top+100, duration = 1)


pyautogui.click(1199,355, duration = 1)

##pyautogui.mouseDown('Ctrl')
##pyautogui.mouseDown('a')
##pyautogui.mouseUp('a')
##pyautogui.mouseUp('Ctrl')
##pyautogui.mouseDown('Ctrl')
##pyautogui.mouseDown('c')
##pyautogui.mouseUp('c')
##pyautogui.mouseUp('Ctrl')
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
copiedText = pyperclip.paste()


pyperclip.copy(copiedText)

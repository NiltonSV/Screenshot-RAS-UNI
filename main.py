from PIL import ImageGrab
import keyboard
x=2

print(keyboard.read_key())

if keyboard.read_key() == "ctrl":
    save_path = '/Users/PC/Desktop/Screenshot_RAS_UNI/ss_'+str(x)+'.png'
    ImageGrab.grab().save(save_path)
  
else:
    print("Nada")


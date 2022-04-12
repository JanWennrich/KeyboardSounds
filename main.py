import keyboard
import playsound
import os
import threading
import random
import glob

sounds_dir = os.path.dirname(__file__) + os.path.sep + 'sounds' + os.path.sep

sound_files = glob.glob(sounds_dir + '*.wav')


def play_random_sound():
    playsound.playsound(random.choice(sound_files), True)


def on_key_press(e):
    t = threading.Thread(target=play_random_sound)
    t.start()


if __name__ == '__main__':
    keyboard.on_press(on_key_press)
    keyboard.wait()

"""
Piano class
"""

from tone import Tone
from note import Note
from pynput.keyboard import Key, Listener

class Piano:

    # keyboard_key: piano_note
    __key_mapping = {
        "a": "c",
        "w": "c#",
        "s": "d",
        "e": "d#",
        "d": "e",
        "f": "f",
        "t": "f#",
        "g": "g",
        "y": "g#",
        "h": "a",
        "u": "a#",
        "j": "b"
    }

    def __init__(self):
        self.__current_range = 4
        self.__amplitude = 0.5
        self.__duration = 0.25
        self.__print_info()
        self.__start_listener()

    @staticmethod
    def start():
        """ Creates a Piano object """
        return Piano()
    
    def __print_info(self):
        print(
        """ 
        Keyboard layout:

         w e   t y u      |       c# d#   f# g# a#
        a s d f g h j     |      c  d  e f  g  a  b
        
        Current range: {}
        """.format(self.__current_range))

    def __raise_current_range(self):
        """ Raises current range by 1 """
        if self.__current_range < 8:
            self.__current_range += 1
            print("\nCurrent range: {}".format(self.__current_range))
            
    def __lower_current_range(self):
        """ Lowers current range by 1 """
        if self.__current_range > 0:
            self.__current_range -= 1
            print("\nCurrent range: {}".format(self.__current_range))

    def __play_note(self, note):
        """ Plays a given note """
        frequency = Note.get_note_frequency(self.__current_range, note)
        Tone.play_tone(frequency, self.__amplitude, self.__duration)

    def __on_press(self, key):
        """ Function that will be called every time a key is pressed """
        key = str(key).strip("\'")
        if key in Piano.__key_mapping.keys():
            self.__play_note(Piano.__key_mapping[key])
        elif key == "-":
            self.__lower_current_range()
        elif key == "=":
            self.__raise_current_range()

    def __start_listener(self):
        """ Starts listening to keyboard inputs """
        with Listener(on_press=self.__on_press) as listener:
           listener.join() 

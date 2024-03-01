import pyperclip
import keyboard
from PhotoToTxt import *
from ChatGPT4 import *


def main():
    pattern = ("Your previous answers too long. Try again. Just the answer. "
               "First sentence is the answer (order of the answer from 1 to 4). "
               "YOU MUST ANSWER USE ONLY LESS THAN 50 CHARACTERS")
    read_conversations_from_file('conversation_history.txt')
    while True:
        if keyboard.is_pressed('-'):
            text = from_photo_to_txt()
            question = f"{pattern} {str(text)}"
            response = chat_with_gpt(question)
            display(response)
        elif keyboard.is_pressed('+'):
            question = f"{pattern} {str(pyperclip.paste())}"
            response = chat_with_gpt(question)
            display(response)
        elif keyboard.is_pressed('\\'):
            text = from_photo_to_txt()
            question = f"{str(text)}"
            chat_with_gpt(question)
            display('EXP+')
        elif keyboard.is_pressed('/'):
            question = f"{str(pyperclip.paste())}"
            chat_with_gpt(question)
            display('EXP+')
        elif keyboard.is_pressed('*'):
            try:
                display_text_on_screen(conversation_cache[-1]['content'])
            except:
                display_text_on_screen('Истории нет.')
        elif keyboard.is_pressed('ctrl+q'):
            break


if __name__ == '__main__':
    main()

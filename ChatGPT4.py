import re
import g4f
from Display import *
def chat_with_gpt(message):
    try:
        cleaned_message = message.replace('\n', ' ')
        cleaned_message = re.sub(r'\s+', ' ', cleaned_message)

        conversation_cache.append({"role": "user", "content": cleaned_message})

        messages = conversation_cache.copy()
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            stream=True
        )

        conversation = ''

        for msg in response:
            conversation += msg
        conversation_cache.append({"role": "assistant", "content": conversation})
        return conversation
    except Exception as e:
        if type(e).__name__ == 'RetryProviderError':
            display_text_on_screen('Нет интернета: Переподключите интернет.')
        elif type(e).__name__ == 'RuntimeError':
            display_text_on_screen('Нет ответа: Отправьте ещё раз.')
        else:
            display_text_on_screen(f'{type(e).__name__} {str(e)}')

import g4f  # to connect API free ChatGPT
import random  # random
import keyboard  # to track keyboard
import pyperclip  # to take from clipboard info
from winotify import Notification  # to get notify in Windows


# To update data from clipboard when you copy new questions (can be optimize nomber 1 with 2 below)
def update_var() -> str:
    data: str = pyperclip.paste()
    return data


# It took the answer from ChatGPT-3.5-version (because it is stable work version)
def ask_gpt(promt: str) -> str:
    try:
        response: str = g4f.ChatCompletion.create(
            model=g4f.models.gpt_35_turbo,
            messages=[{"role": "user",
                       "content": f'''I WILL ASK YOU QUESTIONS, I ONLY NEED ANSWER NUMBERS PLEASE.\n{promt}\nJUST SAY A CORRECT ANSWER NUMBER PLEASE'''}],
        )
        compress: list[str] = response.split()
        s: str = ''
        for i in compress:
            s += i + ' '
        return s
    # It just clerify errors for users
    except Exception as e:
        if type(e).__name__ == 'RetryProviderError':
            toaster('Нет интернета: Переподключите интернет.')
        elif type(e).__name__ == 'RuntimeError':
            toaster('Нет ответа: Отправьте ещё раз.')
        else:
            notify_error(type(e).__name__, str(e))


# Do not repeate the title and others items was created this func
def toaster(text: str) -> None:
    toast = Notification(app_id="Telegram",
                         title=random_group(),
                         msg=text,
                         duration="short")
    toast.show()


# Return notify if other errors
def notify_error(error_type: str, error_message: str) -> None:
    toast = Notification(app_id=error_type,
                         title=random_group(),
                         msg=error_message,
                         duration="short")
    toast.show()


# instruction for people
def instruction() -> None:
    toaster(f'Привет! '
            f'1.Скопируй вопрос(любое кол-во) с вариантами ответов; '
            f'2.Нажми на минус(-); 3.Жди, через 15 сек. придет ответ; '
            f'Выход: ctrl+q')


# To change the title notify to looks like telegram AITU group (this groups are popular spaming)
def random_group() -> str:
    groups: list[str] = ["NU/AITU jobs", "LeetCode", "«Tengri» Debate Club", "Первый курс AITU 2023", "Студенты AITU 2023-2024"]
    r: str = random.choices(groups)[0]
    return r


# function to return ChatGPT answer like a message (number 2 [second])
def notification(res: str) -> None:
    toaster(ask_gpt(res))


# instruction for people
def instructions() -> None:
    toaster(f'Привет! '
            f'1.Скопируй вопрос(любое кол-во) с вариантами ответов; '
            f'2.Нажми на минус(-); '
            f'3.Жди, через 15 сек. придет ответ; '
            f'Выход: ctrl+q')


# main output I like this call mechanism like C++/Java
def main() -> None:
    keyboard.add_hotkey("-", lambda: notification(update_var()))
    keyboard.wait("ctrl+q")
    toaster(f'пока.')


if __name__ == '__main__':
    instructions()
    main()

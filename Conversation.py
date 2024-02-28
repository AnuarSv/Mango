from Display import *

conversation_cache = []

def read_conversations_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                line = line.replace('\n', '')
                parts = line.split(': ')
                if len(parts) >= 2:
                    role = parts[0]
                    content = ': '.join(parts[1:])
                    conversation_cache.append({"role": role, "content": content.strip()})
    except FileNotFoundError:
        save_conversations_to_file('conversation_history.txt')


def save_conversations_to_file(filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for exchange in conversation_cache:
            role = exchange['role']
            content = exchange['content'].replace('\n', ' ')
            file.write(f'{role}: {content}\n')


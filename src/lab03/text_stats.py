#!/usr/bin/env python3
import sys
import os

#Я у дипсика спрашивал как подключать, он сказал так
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))
from text import normalize, tokenize, count_freq, top_n

'''Я пользуюсь виндой, так как Линух на моем компе жрет 30 ватт, 
так как дрова нвидиа на линукс говно, которое не могут выключить видюху...
'''
text = sys.stdin.buffer.read().decode('utf-8')

print(f"DEBUG: Получен текст: '{text}'", file=sys.stderr)

# Нормализуем текст
normalized_text = normalize(text)
print(f"DEBUG: После нормализации: '{normalized_text}'", file=sys.stderr)

# Разбиваем на слова
tokens = tokenize(normalized_text)
print(f"DEBUG: Токены: {tokens}", file=sys.stderr)

# Считаем частоты
freq = count_freq(tokens)

# Получаем топ-5 слов
top_words = top_n(freq, 5)

# Выводим результаты
print(f"Всего слов: {len(tokens)}")
print(f"Уникальных слов: {len(freq)}")
print("Топ-5:")

for word, count in top_words:
    print(f"{word}:{count}")
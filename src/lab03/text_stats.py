#!/usr/bin/env python3
import sys
import os

# Я у дипсика спрашивал как подключать, он сказал так
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "lib"))
from text import normalize, tokenize, count_freq, top_n

"""Я пользуюсь виндой, так как Линух на моем компе жрет 30 ватт (Спасиба НВидия)!!!
Поэтому я пользуюсь не баш, а повершелл, он почему-то не понимает русский язык, дипсик сказал, что нужно так сделать
$OutputEncoding = [console]::InputEncoding = [console]::OutputEncoding = New-Object System.Text.UTF8Encoding
И заработает, он не обманул, ура
"""
text = sys.stdin.buffer.read().decode("utf-8")

normalized_text = normalize(text)

tokens = tokenize(normalized_text)

freq = count_freq(tokens)

top_words = top_n(freq, 5)

print(f"Всего слов: {len(tokens)}")
print(f"Уникальных слов: {len(freq)}")
print("Топ-5:")

for word, count in top_words:
    print(f"{word}:{count}")

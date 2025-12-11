import re


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:

    if not text:
        return ""

    result = text

    if yo2e:
        result = result.replace("ё", "е").replace("Ё", "Е")

    if casefold:
        result = result.casefold()

    control_chars = ["\t", "\r", "\n"]
    for char in control_chars:
        result = result.replace(char, " ")

    result = " ".join(result.split())

    return result


def tokenize(text: str) -> list[str]:

    if not text:
        return []

    # Регулярка для поиска слов (буквы/цифры/подчеркивание с дефисами внутри)
    pattern = r"\w+(?:-\w+)*"
    tokens = re.findall(pattern, text)

    return tokens


def count_freq(tokens: list[str]) -> dict[str, int]:

    freq = {}

    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return freq


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:

    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]

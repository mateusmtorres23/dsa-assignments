def group_anagrams(words: list[str]) -> list[list[str]]:
    anagrams_map: dict[str, list[str]] = {}

    for i in range(len(words)):
        word = "".join(sorted(words[i]))
        if word in anagrams_map:
            anagrams_map[word].append(words[i])
        else:
            anagrams_map[word] = [words[i]]

    grouped_anagrams: list[list[str]] = [
        word_list for word_list in anagrams_map.values()
        ]

    return grouped_anagrams


print(group_anagrams(["amor", "roma", "mora", "carro", "arroc"]))

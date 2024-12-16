def get_word(prompt):
    word = input(prompt).strip()
    if not word: 
        print("I don't think you entered anything. C'mon put something!!!")
        return get_word(prompt)  
    return word

def madlibs_game():
    word_bank = {
        "noun": [],
        "verb": [],
        "adjective": [],
        "adverb": []
    }

    def collect_words(category, count):
        print(f"Enter {count} {category}(s):")
        for _ in range(count):
            word = get_word(f"Enter a {category}: ")
            word_bank[category].append(word)

    collect_words("noun", 3)
    collect_words("verb", 2)
    collect_words("adjective", 2)
    collect_words("adverb", 1)

    story_template = (
        f"Long time ago, there was a very {word_bank['adjective'][0]} "
        f"{word_bank['noun'][0]} who enjoyed {word_bank['verb'][0]} "
        f"{word_bank['adverb'][0]}. One day they encountered a {word_bank['adjective'][1]} "
        f"{word_bank['noun'][1]} who decided to {word_bank['verb'][1]} "
        f"with them. Together, they found a {word_bank['noun'][2]} "
        f"and defeated the current issues in society and suceed in life knowing they did something important to society. The end!"
    )

    print("\nHere's that awesome story you 'technically' wrote\n")
    print(story_template)

madlibs_game()
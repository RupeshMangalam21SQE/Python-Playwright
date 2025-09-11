# 5. Censor Bot
import re
def censor(sentence, bad_words):
    pattern = re.compile("|".join(bad_words), re.IGNORECASE)
    return pattern.sub(lambda m: "*" * len(m.group()), sentence)
print(censor("This censored code is censored", ["censored"]))
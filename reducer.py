# reducer

"""reducer.ipynb"""

import sys
import re

current_word = None
current_count = 0
word = None

result = {'palavras_distintas': None,
          'top_10': None}

punctuation_regex = re.compile(r"[,.?!;:()\[\]{}-]")
counting = dict()
for word in sys.stdin:
    word = word.strip().lower()

    word, count = word.split('\t', 1)
    word = re.sub(
        punctuation_regex, '', word
        ).replace("'", '').replace('"', '')
    try:
        quantity = int(count)
        if word in counting:
            counting[word] += quantity
        else:
            counting[word] = quantity
    except ValueError:
        continue

ordered_counting = sorted(counting.items(), key=lambda x: x[1], reverse=True)
result['palavras_distintas'] = len(ordered_counting)
result['top_10'] = list(ordered_counting)[:10]
print(result)
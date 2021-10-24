# FrederickHerzog
from string import punctuation


def rmv_punct(f):
    new = []
    words = f.read().split()
    exclude = set(punctuation)
    for s in words:
        s = ''.join(ch for ch in s if ch not in exclude)
        new.append(s)
    return new


with open("/Shakespeare.txt", 'r') as f:
    new = rmv_punct(f)
print(new)

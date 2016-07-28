import csv
from collections import namedtuple

card = namedtuple('flashcard', ['chars', 'pinyin', 'defn'])

def make_defn():
    """Make a nice formatted definition, maybe with HTML formatting."""
    return

def make_card(*args):
    if len(args) == 3:
        return card(*args)
    elif len(args) == 2:
        # supply placeholder for definition otherwise anki will complain
        return card(args[0], args[1], "Custom definition.")
    else:
        # don't know how to raise exception
        1/0

with open("pleco.txt") as f:
    flashdump = csv.reader(f, delimiter="\t")
    cards = [
        make_card(*row) for row in flashdump
        if not row[0].startswith("//")  # ignore deck name for now
     ]

# TODO: See if this actually loads in Anki
with open("anki-deck.txt", "w") as f:
    for i in range(len(cards)):
        output = '\t'.join(cards[i]) + '\n'
        f.write(output)

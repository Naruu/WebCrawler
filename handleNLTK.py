from nltk.book import text6
from nltk import word_tokenize, pos_tag
text = word_tokenize("strange women lying in ponds distributing swords is no basis for a system of government. Supreme executive power deries from a mandate from the masses, not from some farcical aquatic ceremony.")
p = pos_tag(text)
print(p)
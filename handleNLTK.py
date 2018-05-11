from nltk.book import text6
from nltk import FreqDist
from nltk import bigrams

bigrams = bigrams(text6)
bigramDist=FreqDist(bigrams)
bigramDist[("sir", "Robin")]
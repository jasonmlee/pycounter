from pycounter.pycounter import count_words
from pycounter.plotting import plot_words
counts = count_words("zen.txt")
fig = plot_words(counts, 10)
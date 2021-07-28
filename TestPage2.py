import wordcloud
import numpy as np
from matplotlib import pyplot as plt
import io
import sys
import wordcloud

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them", \
                           "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be",
                           "been", "then", "all", "into",  "being", \
                           "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when",
                           "where", "how", "even", "could", "out", "said", "only", \
                           "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very",
                           "can", "will", "just", "in", "not", "for", "on", "there", "one", "would"]

    # LEARNER CODE START HERE
    words = {}
    text = file_contents.split()
    for word in text:
        word = word.strip(punctuations).lower()
        if word not in uninteresting_words:
            if word not in words:
                words[word] = 0
            words[word] += 1

    # wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(words)
    return cloud.to_array()

with open("templates/1984.txt") as file:
    file_contents = file.read()


myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
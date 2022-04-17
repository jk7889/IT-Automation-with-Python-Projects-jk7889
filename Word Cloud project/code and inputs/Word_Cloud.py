#!/usr/bin/env python3

from wordcloud import WordCloud, STOPWORDS, wordcloud
import sys


def read_txt(file, words_to_exclude_list):
    """This function takes a file and processes it to find the number of occurrence of each word or number in that file
    to form  a word cloud"""
    f = open(file, "r")
    text = f.read()
    alnum_only_string = ""

    for letter in text:
        # To add all alphabets and numbers to the string
        if letter.isalpha():
            alnum_only_string = alnum_only_string + letter
        # To replace all special characters (except apostrophe) with whitespace in the string
        if not letter.isalpha() and letter != "'":
            letter = " "
            alnum_only_string = alnum_only_string + letter
        # To add apostrophe in the string to make sense of words having apostrophe
        # "don't" should not be stored in string as "don t", it should be stored as "don't"
        if not letter.isalpha() and letter == "'":
            alnum_only_string = alnum_only_string + letter

    # Converting list of words to exclude to a set to remove duplicate words
    words_to_exclude_list = set(words_to_exclude_list)
    words_to_exclude_list = list(words_to_exclude_list)
    # Changing all words in words_to_exclude_list to lowercase
    for wrd in words_to_exclude_list:
        words_to_exclude_list[words_to_exclude_list.index(wrd)] = wrd.lower()

    # Saving the number of times each word or number occurs in alnum_only_string to repeated_words_dict
    # if the word is not in words_to_exclude_list
    repeated_words_dict = {}
    for word in alnum_only_string.split():
        if "'" not in word:
            if word.lower() not in words_to_exclude_list and word.lower() not in repeated_words_dict.keys():
                repeated_words_dict[word.lower()] = 1
            elif word.lower() not in words_to_exclude_list and word.lower() in repeated_words_dict.keys():
                repeated_words_dict[word.lower()] += 1

    # Creating a wordcloud and generating a jpeg file
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(repeated_words_dict)
    cloud.to_file("myfile1.jpg")


if __name__ == "__main__":
    """Takes a file as a system argument from command line and list of words to exclude"""
    # I have used this script to generate a word cloud for a Data Science book known as
    # Joel Grus - Data Science from Scratch_ First Principles with Python-O’Reilly Media (2019)
    # The resultant file (myfile1.jpg) will be in the outputs directory of Word Cloud Project directory
    read_txt(sys.argv[1],
             ["A", "The", "The", "I", "S", "to", "ve", "and", "if", "so", "cause", "re", "em", "a", "b",
              "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
              "v", "w", "x", "y", "z", "on", "the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as",
              "i", "in", "on", "me", "my", "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his",
              "her", "hers", "its", "they", "them", "their", "what", "which", "who", "whom", "this", "that", "am",
              "are", "was", "were", "be", "been", "being", "have", "has", "had", "do", "does", "did", "but", "at",
              "by", "with", "from", "here", "when", "where", "how", "all", "any", "both", "each", "few", "more",
              "some", "such", "no", "nor", "too", "very", "can", "will", "just", "for", "not", "there", "much",
              "than", "then", "said", "would", "could", "should", "one", "mr", "ms", "many", "soon", "here",
              "about", "now", "into", "these", "those", "use", "uses", "using", "other",
              ])


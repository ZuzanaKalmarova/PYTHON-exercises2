"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    if list1 == []:
        return []
    nodupl = [list1[0]]
    for idx in range(1,len(list1)):
        if list1[idx] != list1[idx-1]:
            nodupl.append(list1[idx])
    return nodupl

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    if list1 == [] or list2 == []:
        return []
    inters = []
    idx2 = 0
    for idx1 in range(len(list1)):
        if list1[idx1] < list2[idx2]:
            continue
        while list1[idx1] > list2[idx2]:
            idx2 += 1
            if idx2 > len(list2) - 1:
                break
        if idx2 > len(list2) - 1:
            break
        if list1[idx1] == list2[idx2]:
            inters.append(list1[idx1])
            idx2 += 1
        if idx2 > len(list2) - 1:
            break
    return inters

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing those elements that are in
    either list1 or list2.

    This function can be iterative.
    """   
    if list1 == []:
        return list2
    if list2 == []:
        return list1
    mergelist = []
    list1c = list(list1)
    list2c = list(list2)
    while list1c != []:
        if list2c == [] or list1c[0] <= list2c[0]:
            nextel = list1c.pop(0)
        else:
            nextel = list2c.pop(0)
        mergelist.append(nextel)
    if list2c != []:
        mergelist = mergelist + list2c
    return mergelist
                
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    if len(list1) < 2:
        return list1
    else:
        mid = int(len(list1)/2)
        lista = merge_sort(list1[:mid])
        listb = merge_sort(list1[mid:])
        return merge(lista, listb)


# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    if len(word) < 1:
        return [""]
    else:
        first = word[0]
        rest = word[1:]
        rest_strings = gen_all_strings(rest)
        result = []
        for string in rest_strings:
            for idx in range(len(string)+1):
                new_string = string[:idx] + first + string[idx:]
                result.append(new_string)          
    return rest_strings + result

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    url = codeskulptor.file2url(filename)
    fileh = urllib2.urlopen(url)
    wordict = []
    for line in fileh:
        wordict.append(line.strip())
    return wordict

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
# run()

#list1 = [7,10,15]
#list2 = [10]
#list2 = []
#list1 = []
#list1 = ['x','a','b','f','z','h']

#print merge_sort(list1)
#print gen_all_strings('aab')
#print load_words(WORDFILE) 
#print remove_duplicates(list1)
#print intersect(list1,list2)
    
#!/usr/bin/env python3
# coding:utf-8
import random
import tkinter


def listToStr(list):
    """ Convertit une liste ["a", "b", "cd"] en un str "abcd" """
    str = ''
    for i in list:
        str += i
    return str


def MixSentence(sentence):
    apostrophesPos = []
    for pos, letter in enumerate(sentence):
        apostrophe = False
        if letter == "'":
            apostrophe = True
            apostrophesPos.append(pos)
        print(letter + " " + str(apostrophe))
    print(apostrophesPos)
    sentence = sentence.replace("'", " ")
    sentence = sentence.split()
    mxiedSentence = ''
    for word in sentence:
        if not len(word) == 1:
            firstLetter = word[:1]  # on récupère la 1ère lettre du txt
            lastLetter = word[len(word) - 1:]  # et sa dernière
            ponctuation = ''
            while lastLetter == "," or lastLetter == "." or lastLetter == ";" or lastLetter == ":" or lastLetter == "?" or lastLetter == "!":
                # cas des ponctuations
                ponctuation += lastLetter
                word = word[:len(word)-1]
                lastLetter = word[len(word) - 1:]
            if firstLetter == "?" or firstLetter == "!":
                firstLetter = None

            otherLetters = list(word[1:len(word) - 1])  # on récupère les lettres au milieu dans une liste

            random.shuffle(otherLetters)  # qu'on mélange
            otherLetters = listToStr(otherLetters)  # qu'on remet en str
            # et on assemble le tout
            mxiedWord = firstLetter + otherLetters + lastLetter if not firstLetter is None else otherLetters + lastLetter
            mxiedSentence += mxiedWord + ponctuation + " "
        else:  # point-virgule et double-point
            mxiedSentence += word + ' '

    mxiedSentence = list(mxiedSentence)
    if not len(apostrophesPos) == 0:
        for apostrophePos in apostrophesPos:
            mxiedSentence.insert(apostrophePos, "'")
    mxiedSentence = listToStr(mxiedSentence)
    
    return mxiedSentence

print(MixSentence("Ceci est un test avec, des ponctuations ; des apo'str'ophes : des choses en tout genre... !! ??? ??!!"))

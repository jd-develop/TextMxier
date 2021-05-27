#!/usr/bin/env python3
# coding:utf-8
import random
import tkinter as tk


def listToStr(list):
    """ Convertit une liste ["a", "b", "cd"] en un str "abcd" """
    str = ''
    for i in list:
        str += i
    return str


def MixSentence(sentence):
    """ Mixe une phrase """
    # Apostrophes
    apostrophesPos = []
    for pos, letter in enumerate(sentence):
        apostrophe = False
        if letter == "'":
            apostrophe = True
            apostrophesPos.append(pos)

    # Avoir une liste de mots
    sentence = sentence.replace("'", " ")
    sentence = sentence.split()
    mxiedSentence = ''

    # Traitement par mots
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

    # rajout des apostrophes
    mxiedSentence = list(mxiedSentence)
    if not len(apostrophesPos) == 0:
        for apostrophePos in apostrophesPos:
            mxiedSentence.pop(apostrophePos)  # supprimer l'esapce créé à la place de l'apostrophe
            mxiedSentence.insert(apostrophePos, "'")
    mxiedSentence = listToStr(mxiedSentence)
    
    return mxiedSentence


APP_BACKGROUND = '#87CEEB'

root = tk.Tk()
root.title("TextMxier")
root.geometry("900x500")
root.minsize(900, 500)
# root.iconbitmap('icon.ico')
root.config(background=APP_BACKGROUND)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

frame = tk.Frame(root, bg=APP_BACKGROUND)

enterTextFrame = tk.Frame(frame, bg='green')
enterTextLabel = tk.Label(enterTextFrame, text="Entrez du texte :", bg=APP_BACKGROUND)
enterTextEntry = tk.Entry(enterTextFrame, bg=APP_BACKGROUND)

resultFrame = tk.Frame(frame, bg='green')
resultLabel = tk.Label(resultFrame, text="Résultat :", bg=APP_BACKGROUND)
resultEntry = tk.Entry(resultFrame, bg=APP_BACKGROUND)

enterTextLabel.pack()
enterTextEntry.pack(fill='x', expand=True)
enterTextFrame.grid(row=0, column=0)

resultLabel.pack()
resultEntry.pack(fill='x', expand=True)
resultFrame.grid(row=0, column=1)

frame.pack(expand=tk.YES)

print(MixSentence("Ceci est un test avec, des ponctuations ; des apo'str'ophes : des choses en tout genre... Aujourd'aujourd'hui !! ??? ??!!"))

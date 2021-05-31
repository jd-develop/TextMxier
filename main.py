#!/usr/bin/env python3
# coding:utf-8
import random
import tkinter as tk


def mix():
    result = mixSentence(enterTextEntry.get("1.0", tk.END))
    resultEntry.config(state=tk.NORMAL)
    resultEntry.delete("1.0", tk.END)
    resultEntry.insert("1.0", result)
    resultEntry.config(state=tk.DISABLED)


def listToStr(list):
    """ Convertit une liste ["a", "b", "cd"] en un str "abcd" """
    str = ''
    for i in list:
        str += i
    return str


def mixSentence(sentence):
    """ Mixe une phrase """
    # Apostrophes
    apostrophesPos = []
    for pos, letter in enumerate(sentence):
        if letter == "'":
            apostrophesPos.append(pos)

    # Retour ligne
    backPos = []
    for pos, letter in enumerate(sentence):
        if letter == '\n':
            try:
                if not sentence[pos - 1] == '\n':
                    backPos.append(pos)
            except IndexError:
                pass

    # Avoir une liste de mots
    sentence = sentence.replace("'", " ").replace("\n", " ")
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
    if not len(backPos) == 0:
        for backpos in backPos:
            try:
                mxiedSentence.pop(backpos)  # supprimer l'esapce créé à la place de l'apostrophe
                mxiedSentence.insert(backpos, "\n")
            except IndexError:  # deux retours ligne à la suite
                pass
    mxiedSentence = listToStr(mxiedSentence)

    return mxiedSentence


APP_BACKGROUND = '#87CEEB'

root = tk.Tk()
root.title("TextMxier")
root.geometry("1300x500+10+10")
root.minsize(1100, 400)
# root.iconbitmap('icon.ico')
root.config(background=APP_BACKGROUND)
frame = tk.Frame(root, bg=APP_BACKGROUND)

enterTextFrame = tk.Frame(frame, bg=APP_BACKGROUND)
enterTextLabel = tk.Label(enterTextFrame, text="Entrez du texte :", bg=APP_BACKGROUND)
enterTextEntry = tk.Text(enterTextFrame, bg=APP_BACKGROUND)

resultFrame = tk.Frame(frame, bg=APP_BACKGROUND)
resultLabel = tk.Label(resultFrame, text="Résultat :", bg=APP_BACKGROUND)
resultEntry = tk.Text(resultFrame, bg=APP_BACKGROUND)
resultEntry.config(state=tk.DISABLED)

enterTextLabel.pack()
enterTextEntry.pack()
enterTextFrame.grid(row=0, column=0)

resultLabel.pack()
resultEntry.pack()
resultFrame.grid(row=0, column=1)

resultButton = tk.Button(root, text="Mixer", bg=APP_BACKGROUND, command=lambda: mix())

frame.pack()
resultButton.pack()
enterTextEntry.focus()
root.mainloop()

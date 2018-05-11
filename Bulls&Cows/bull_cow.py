# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 09:42:42 2018

@author: DELL
"""
import os
import random
FOUR = 0
FIVE = 1
class bull_cow():
    def __init__(self):
        self.mode = 4
        self.words = [0,0]
    
    def read_dictionary(self,file_name):
        file_name = os.path.join(os.path.dirname(__file__),file_name) 
        if os.path.isfile(file_name):
            input_words = open(file_name).readlines()
            q = open("word123.txt","w")
            self.words[FOUR] = [word.strip() for word in input_words if len(word.strip()) == 4]
            for w in self.words[FOUR]:
                q.write(w+"\n")
            self.words[FIVE] = [word.strip() for word in input_words if len(word.strip()) == 5]
        else:
            print(file_name, " doesn't exist")
            #quit()
    def start_game(self, word_type):
        self.word_type = word_type
        self.game_word = self.find_word()
        #print(self.game_word)
    
    def find_word(self):
        return self.words[self.word_type][random.randrange(0,len(self.words[self.word_type]),3)]
    
    def get_stats(self, word):
        bulls = 0
        cows = 0
        for i in range(4):
            if word[i] == self.game_word[i]:
                bulls += 1
            elif word[i] in self.game_word:
                cows += 1
        return str(bulls)+'B',str(cows)+'C'
    def check_word(self, word):
        if word in self.words[self.word_type]:
            return True
        print("Oops, Not a word")
        return False
    def show(self):
        print(self.game_word)
        
b = bull_cow()
b.read_dictionary("words1.txt")
b.start_game(FOUR)
while True:
    word = input("Guess A Word: ").upper()
    if word.lower() == "show_input":
        b.show()
        continue
    if not b.check_word(word):
        continue
    bulls,cows =b.get_stats(word)
    if bulls == '4B':
        print("You Won")
        break
    else:
        print (bulls,"  ",cows)

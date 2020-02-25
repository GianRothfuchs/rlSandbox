#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 21:39:18 2020

@author: gian
"""

import numpy as np

class tictactoe:
    def __init__(self,bsize,p1,p2):
        self.boardSize = bsize
        self.p1 = p1
        self.p2 = p2
        self.resetBoard()

    def getState(self):
        self.State = hash(str(self.board.reshape(self.boardSize**2)))
    def winner(self):
        col_p1 = np.any(np.equal(np.sum(self.board,0),np.full(self.boardSize, self.boardSize)))
        row_p1 = np.any(np.equal(np.sum(self.board,1),np.full(self.boardSize, self.boardSize)))
        diag1_p1 = np.equal(np.sum(np.multiply(self.board,np.eye(self.boardSize))),self.boardSize)
        diag2_p1 = np.equal(np.sum(np.multiply(self.board,np.rot90(np.eye(self.boardSize)))),self.boardSize)
        
        col_p2 = np.any(np.equal(np.sum(self.board,0),np.full(self.boardSize, -self.boardSize)))
        row_p2 = np.any(np.equal(np.sum(self.board,1),np.full(self.boardSize, -self.boardSize)))
        diag1_p2 = np.equal(np.sum(np.multiply(self.board,np.eye(self.boardSize))),-self.boardSize)
        diag2_p2 = np.equal(np.sum(np.multiply(self.board,np.rot90(np.eye(self.boardSize)))),-self.boardSize)
        
        #print(np.array([col_p1,row_p1,diag1_p1,diag2_p1]))
        if np.any(np.array([col_p1,row_p1,diag1_p1,diag2_p1])):
            self.gameOver = True
            print(self.num2name[1]+' wins')
            return self.num2name[1] # p1 wins
        else:
            #print(np.array([col_p2,row_p2,diag1_p2,diag2_p2]))
            if np.any(np.array([col_p2,row_p2,diag1_p2,diag2_p2])):
                self.gameOver = True
                print(self.num2name[-1]+' wins')
                return self.num2name[-1] #p2 wins
            else:
                if self.emptyFields == 0:
                    self.gameOver = True
                    return 'tie' # tie
                else:    
                    return 'na' # game in progres
                
    def getEmptyFields(self):
        self.emptyFields = np.sum(self.board == 0)
        res = np.where(self.board == 0)
        return list(zip(res[0], res[1]))
    
    def doMove(self,field):
        if field in self.getEmptyFields():
            if not self.gameOver:
                print(self.num2name[self.currentPlayer] + " played:")
                self.board[field] = self.currentPlayer
                self.currentPlayer = self.currentPlayer * -1
                print(self.board)
                self.winner()
            else:
                print('game is over')
        else:
            print('move failed')
                       
    def resetBoard(self):
        self.board = np.zeros((self.boardSize,self.boardSize),dtype=np.int8)
        self.gameOver = False
        self.State = None
        self.emptyFields = self.boardSize**2
        self.randomStart()
    
    def randomStart(self):
        playerToken = np.array([1,-1])
        np.random.shuffle(playerToken)
        self.name2num = {"p1":playerToken[0],"p2":playerToken[1]}
        self.num2name = {playerToken[0]:"p1",playerToken[1]:"p2"}
        self.currentPlayer = 1
        print(self.num2name[1]+" goes first")
        
    def randomPlayer2(self):
        if self.name2num["p2"] == self.currentPlayer:
            if not self.gameOver:
                availableFields = self.getEmptyFields()
                randArray = np.random.choice(len(availableFields), 1)
                randAction = availableFields[randArray.item()]
                self.doMove(randAction)
            else:
                print("game is over")
        else:
            print("Its p1's turn, p2 cannot move now")
    
    def doSimMove(self,field):
        if self.num2name[1] == "p1":
            self.doMove(field)
            self.randomPlayer2()
        else:
            self.randomPlayer2()
            self.doMove(field)
            
        
    
        
        # also check for player 2
        
ttt = tictactoe(3,'p1','p2')


#ttt.getState()

#tmp =ttt.board 
#tmp = -np.eye(3)
#ttt.board  = tmp

ttt.doSimMove((0,1))


#print(ttt.winner())
#print(ttt.randomStart())
#print(ttt.getEmptyFields())
#print(len(ttt.getEmptyFields()))
#ttt.randomPlayer2()





#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 21:39:18 2020

@author: gian
"""

import numpy as np
import random as rnd

class tictactoe:
    def __init__(self,bsize,p1,p2,showField):
        self.boardSize = bsize
        self.p1 = p1
        self.p2 = p2
        self.name2num = {self.p1:1,self.p2:-1}
        self.num2name = {1:self.p1,-1:self.p2}
        self.transitionMap = {self.p1:self.p2,self.p2:self.p1}
        self.resetBoard()
        self.showField = showField
        
    
        
    def resetBoard(self):
        self.board = np.zeros((self.boardSize,self.boardSize),dtype=np.int8)
        self.gameOver = False
        self.State = None
        self.emptyFields = self.boardSize**2
        self.randomStart()
        
    def randomStart(self):
        playerToken = np.array([1,-1])
        np.random.shuffle(playerToken)
        self.currentPlayer = self.num2name[playerToken[0]]
        print(self.currentPlayer +" goes first")
        
    def getState(self):
        self.State = hash(str(self.board.reshape(self.boardSize**2)))
        return self.State 
        
    def getWinner(self):
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
            print('GAME OVER: ' + self.p1 +' wins')
            return self.p1 # p1 wins
        else:
            #print(np.array([col_p2,row_p2,diag1_p2,diag2_p2]))
            if np.any(np.array([col_p2,row_p2,diag1_p2,diag2_p2])):
                self.gameOver = True
                print('GAME OVER: ' + self.p2 +' wins')
                return self.p2 #p2 wins
            else:
                if self.emptyFields == 0:
                    self.gameOver = True
                    print('GAME OVER: Tie ')
                    return 'tie' # tie
                else:    
                    return 'na' # game in progres
                
    def getEmptyFields(self):
        self.emptyFields = np.sum(self.board == 0)
        if self.emptyFields > 0:
            res = np.where(self.board == 0)
            return list(zip(res[0], res[1]))
        else:
            return list()
    
    
    def doMove(self,field,player):
        otpt = False
        if self.currentPlayer == player:
            if field in self.getEmptyFields():
                if not self.gameOver:
                    self.board[field] = self.name2num[self.currentPlayer]
                    if self.showField:
                        print(self.currentPlayer + " played: {0}".format(field))
                        print(self.board)
                    self.currentPlayer = self.transitionMap[self.currentPlayer]
                    self.getWinner()
                    self.getEmptyFields()
                    otpt = True
                else:
                    print("doMove: game over")
            else:
                print("doMove: field is already taken")
        else:
            print("doMove: Its not player " + player + "'s turn")
        return otpt

    def randomPlayer2(self):
        if self.p2 == self.currentPlayer:
            if not self.gameOver:
                availableFields = self.getEmptyFields()
                randArray = np.random.choice(len(availableFields), 1)
                randAction = availableFields[randArray.item()]
                self.doMove(randAction,self.p2)
            else:
                print("game is over")
        else:
            print("Its p1's turn, p2 cannot move now")
    
    def initSim(self):
        self.resetBoard()
        if self.currentPlayer == self.p2:
            self.randomPlayer2()
            
            
    def doSimMove(self,field):
        if not self.gameOver:
            if self.p1 == self.currentPlayer:
                ok = self.doMove(field,self.p1)
                self.getWinner()
                if ok:
                    if not self.gameOver:
                        self.randomPlayer2()
                        self.getWinner()
        return self.gameOver
                


            
        
    
        
        # also check for player 2
        
ttt = tictactoe(3,'p1','p2',False)

ttt.initSim()

gameOverTrue = ttt.gameOver
counter = 0

while counter < 1000:
    print("------ ITER: " + str(counter))
    
    while not gameOverTrue:
        randMove = rnd.choice(ttt.getEmptyFields())
        ttt.doSimMove(randMove)
        gameOverTrue = ttt.gameOver
        if gameOverTrue:
            counter += 1
            print(ttt.getState())
            
    ttt.initSim()
    gameOverTrue = ttt.gameOver
    
# print("Game ended in state: " + ttt.getWinner())


#
#gameOver = ttt.gameOver 
#
#while not gameOver:
#    randMove = rnd.choice(ttt.getEmptyFields())
#    print("p1 moved: " + str(randMove))
#    ttt.doSimMove(randMove)
#    gameOver = ttt.gameOver
#
#print("Game ended in state: " + ttt.winner())
    

#ttt.getState()

#tmp =ttt.board 
#tmp = -np.eye(3)
#ttt.board  = tmp

#ttt.doSimMove((0,1))


#print(ttt.winner())
#print(ttt.randomStart())
#print(ttt.getEmptyFields())
#print(len(ttt.getEmptyFields()))
#ttt.randomPlayer2()





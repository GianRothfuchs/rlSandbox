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
            print('p1 wins')
            return 1 # p1 wins
        else:
            #print(np.array([col_p2,row_p2,diag1_p2,diag2_p2]))
            if np.any(np.array([col_p2,row_p2,diag1_p2,diag2_p2])):
                self.gameOver = True
                print('p2 wins')
                return 2 #p2 wins
            else:
                if self.emptyFields == 0:
                    self.gameOver = True
                    return 0 # tie
                else:    
                    return -1 # game in progres
    def getEmptyFields(self):
        self.emptyFields = np.sum(self.board == 0)
        res = np.where(self.board == 0)
        return list(zip(res[0], res[1]))
    def doMove(self,field):
        if field in self.getEmptyFields():
            if not self.gameOver:
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
        self.currentPlayer = 1
        self.emptyFields = self.boardSize**2
    
        
        # also check for player 2
        
ttt = tictactoe(3,'p1','p2')
ttt.getState()

#tmp =ttt.board 
#tmp = -np.eye(3)
#ttt.board  = tmp

ttt.doMove((0,1))
ttt.doMove((0,0))
ttt.doMove((1,1))
ttt.doMove((1,0))
ttt.doMove((2,1))
ttt.doMove((2,0))
#print(ttt.winner())

#ttt.resetBoard()




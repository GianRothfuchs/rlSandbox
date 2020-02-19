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
        self.board = np.zeros((bsize,bsize),dtype=np.int8)
        self.p1 = p1
        self.p2 = p2
        self.gameOver = False
        self.State = None
        self.currentPlayer = p1
    def getState(self):
        self.State = hash(str(self.board.reshape(self.boardSize**2)))
    def winner(self):
        col = np.any(np.equal(np.sum(self.board,0),np.full(self.boardSize, self.boardSize)))
        row = np.any(np.equal(np.sum(self.board,1),np.full(self.boardSize, self.boardSize)))
        diag1 = np.equal(np.sum(np.multiply(self.board,np.eye(self.boardSize))),self.boardSize)
        diag2 = np.equal(np.sum(np.multiply(self.board,np.rot90(np.eye(self.boardSize)))),self.boardSize)
        # also check for player 2
        
ttt = tictactoe(3,'p1','p2')
ttt.getState()

tmp =ttt.board 
tmp = np.eye(3)
ttt.board  = tmp
ttt.winner()




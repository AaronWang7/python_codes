# Chess Board
import pygame
from abc import ABC, abstractmethod

pygame.init()

x = 800
y = 600
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption("Chess Board")

# ... 中间所有棋子类的代码保持不变 ...

class Board:
    def __init__(self, board, x, y):
        self.board = pygame.image.load("chess_resourses\\board.png")
        self.board_transfrom = pygame.transform.scale(self.board, (800, 600))
        self.x = x
        self.y = y
        self.board_x = self.x
        self.board_y = self.y

    def board_set(self):
        screen.blit(self.board_transfrom, (self.x, self.y))

    def board_get(self):
        x = self.board_x
        y = self.board_y
        
        # 检查第一行 (A8到H8)
        if y <= 75:
            if x <= 100:
                return "A8"
            elif x <= 200:
                return "B8"
            elif x <= 300:
                return "C8"
            elif x <= 400:
                return "D8"
            elif x <= 500:
                return "E8"
            elif x <= 600:
                return "F8"
            elif x <= 700:
                return "G8"
            elif x <= 800:
                return "H8"
        
        # 检查第二行 (A7到H7)
        elif y <= 150:
            if x <= 100:
                return "A7"
            elif x <= 200:
                return "B7"
            elif x <= 300:
                return "C7"
            elif x <= 400:
                return "D7"
            elif x <= 500:
                return "E7"
            elif x <= 600:
                return "F7"
            elif x <= 700:
                return "G7"
            elif x <= 800:
                return "H7"
        
        # 检查第三行 (A6到H6)
        elif y <= 225:
            if x <= 100:
                return "A6"
            elif x <= 200:
                return "B6"
            elif x <= 300:
                return "C6"
            elif x <= 400:
                return "D6"
            elif x <= 500:
                return "E6"
            elif x <= 600:
                return "F6"
            elif x <= 700:
                return "G6"
            elif x <= 800:
                return "H6"
        
        # 检查第四行 (A5到H5)
        elif y <= 300:
            if x <= 100:
                return "A5"
            elif x <= 200:
                return "B5"
            elif x <= 300:
                return "C5"
            elif x <= 400:
                return "D5"
            elif x <= 500:
                return "E5"
            elif x <= 600:
                return "F5"
            elif x <= 700:
                return "G5"
            elif x <= 800:
                return "H5"
        
        # 检查第五行 (A4到H4)
        elif y <= 375:
            if x <= 100:
                return "A4"
            elif x <= 200:
                return "B4"
            elif x <= 300:
                return "C4"
            elif x <= 400:
                return "D4"
            elif x <= 500:
                return "E4"
            elif x <= 600:
                return "F4"
            elif x <= 700:
                return "G4"
            elif x <= 800:
                return "H4"
        
        # 检查第六行 (A3到H3)
        elif y <= 450:
            if x <= 100:
                return "A3"
            elif x <= 200:
                return "B3"
            elif x <= 300:
                return "C3"
            elif x <= 400:
                return "D3"
            elif x <= 500:
                return "E3"
            elif x <= 600:
                return "F3"
            elif x <= 700:
                return "G3"
            elif x <= 800:
                return "H3"
        
        # 检查第七行 (A2到H2)
        elif y <= 525:
            if x <= 100:
                return "A2"
            elif x <= 200:
                return "B2"
            elif x <= 300:
                return "C2"
            elif x <= 400:
                return "D2"
            elif x <= 500:
                return "E2"
            elif x <= 600:
                return "F2"
            elif x <= 700:
                return "G2"
            elif x <= 800:
                return "H2"
        
        # 检查第八行 (A1到H1)
        elif y <= 600:
            if x <= 100:
                return "A1"
            elif x <= 200:
                return "B1"
            elif x <= 300:
                return "C1"
            elif x <= 400:
                return "D1"
            elif x <= 500:
                return "E1"
            elif x <= 600:
                return "F1"
            elif x <= 700:
                return "G1"
            elif x <= 800:
                return "H1"
        
        return None

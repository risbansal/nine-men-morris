from Morris import *
import pandas as pd
import sys


ply = 0
positions = 0

class move:
    
    def __init__(self):
        self.board = []
        self.se = 0
        self.depth = 0
        self.children = []
        self.a = -10000
        self.b = 10000



def MaxMin(node):
    global positions
    if node.depth == ply:
        positions += 1
        node.se = StaticEstimationOpening(node.board)
        #node.a = node.se
        return node
    else:
        L = GenerateMovesOpening(node.board)
        max_se = -10000
        for b in L:
            n = move()      
            n.board = b
            n.depth = node.depth + 1
            n.a = node.a
            n.b = node.b
            node.children.append(n)
            n1 = MinMax(n)
            max_se = max(max_se, n1.se)
            node.a = max(max_se,node.a)
            node.se = max_se
            if node.b <= node.a:
                return node
                #break
              
        
        # node.se = max_se
        
    return node



def MinMax(node):
    global positions
    if node.depth == ply:
        positions += 1
        node.se = StaticEstimationOpening(node.board)
       # node.b = node.se
        return node
    else:
        min_se = 10000
        L = GenerateMovesOpeningBlack(node.board)
        for b in L:
            n = move()  
            n.board = b
            n.depth = node.depth + 1
            n.a = node.a
            n.b = node.b
            node.children.append(n)
            n2 = MaxMin(n)
            min_se = min(min_se, n2.se)
            node.b = min(min_se,node.b)
            node.se = min_se
            if node.b <= node.a:
                return node
                #break

        #node.se = min_se
    return node


def main():

    global ply
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    ply = sys.argv[3]
    
    ply = int(ply)


    if ply<1 or ply>22:
        print("Invalid Ply value. Please enter a value between 1 and 22")

    else:

        
        board1 = pd.read_csv(input_file)
        board1 = list(board1)
        board1 = list(board1[0])

        b1 = move()
        b1.board = board1

        out_board = MaxMin(b1)

        board2 = []
        max_se = out_board.se
        for c in out_board.children:
            if c.se == max_se:
                board2 = c.board
                break

        board3=''.join(board2)
        print("Board:",board3)
        print("Positions evaluated by static estimate:", positions)
        print("MINIMAX estimate:",max_se)
        file = open(output_file,'w+')
        file.write(board3)


main()
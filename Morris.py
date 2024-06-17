#Basic functions

def closeMill(b,j):
    c = b[j]
    if j==0:
        if (b[1]==c and b[2]==c) or (b[3]==c and b[6]==c) or (b[8]==c and b[20]==c) :
            return True
        else:
            return False
    if j==1:
        if (b[0]==c and b[2]==c):
            return True
        else:
            return False
    if j==2:
        if (b[0]==c and b[1]==c) or (b[13]==c and b[22]==c) or (b[7]==c and b[5]==c) :
            return True
        else:
            return False
    if j==3:
        if (b[0]==c and b[6]==c) or (b[9]==c and b[17]==c) or (b[4]==c and b[5]==c) :
            return True
        else:
            return False
    if j==4:
        if (b[3]==c and b[5]==c):
            return True
        else:
            return False
    if j==5:
        if (b[2]==c and b[7]==c) or (b[12]==c and b[19]==c) or (b[3]==c and b[4]==c) :
            return True
        else:
            return False
    if j==6:
        if (b[0]==c and b[3]==c) or (b[10]==c and b[14]==c) :
            return True
        else:
            return False
    if j==7:
        if (b[2]==c and b[5]==c) or (b[11]==c and b[16]==c):
            return True
        else:
            return False
    if j==8:
        if (b[9]==c and b[10]==c) or (b[0]==c and b[20]==c):
            return True
        else:
            return False
    if j==9:
        if (b[3]==c and b[17]==c) or (b[8]==c and b[10]==c):
            return True
        else:
            return False
    if j==10:
        if (b[8]==c and b[9]==c) or (b[6]==c and b[14]==c):
            return True
        else:
            return False
    if j==11:
        if (b[12]==c and b[13]==c) or (b[7]==c and b[16]==c):
            return True
        else:
            return False
    if j==12:
        if (b[11]==c and b[13]==c) or (b[5]==c and b[19]==c):
            return True
        else:
            return False
    if j==13:
        if (b[11]==c and b[12]==c) or (b[2]==c and b[22]==c):
            return True
        else:
            return False
    if j==14:
        if (b[15]==c and b[16]==c) or (b[10]==c and b[6]==c) or (b[17]==c and b[20]==c) :
            return True
        else:
            return False
    if j==15:
        if (b[14]==c and b[16]==c) or (b[18]==c and b[21]==c):
            return True
        else:
            return False
    if j==16:
        if (b[14]==c and b[15]==c) or (b[7]==c and b[11]==c) or (b[19]==c and b[22]==c) :
            return True
        else:
            return False
    if j==17:
        if (b[18]==c and b[19]==c) or (b[3]==c and b[9]==c) or (b[14]==c and b[20]==c) :
            return True
        else:
            return False
    if j==18:
        if (b[17]==c and b[19]==c) or (b[15]==c and b[21]==c):
            return True
        else:
            return False
    if j==19:
        if (b[17]==c and b[18]==c) or (b[5]==c and b[12]==c) or (b[16]==c and b[22]==c) :
            return True
        else:
            return False
    if j==20:
        if (b[0]==c and b[8]==c) or (b[21]==c and b[22]==c) or (b[14]==c and b[17]==c) :
            return True
        else:
            return False
    if j==21:
        if (b[20]==c and b[22]==c) or (b[15]==c and b[18]==c):
            return True
        else:
            return False
    if j==22:
        if (b[20]==c and b[21]==c) or (b[2]==c and b[13]==c) or (b[16]==c and b[19]==c) :
            return True
        else:
            return False


def neighbours(j):
    
    if j==0:
        return [1,3,8]
    if j==1:
        return [0,2,4]
    if j==2:
        return [1,5,13]
    if j== 3:
        return[0,4,6,9]
    if j== 4:
        return[1,3,5]
    if j== 5:
        return[2,4,7,12]
    if j== 6:
        return[3,7,10]
    if j== 7:
        return[5,6,11]
    if j== 8:
        return[0,9,20]
    if j== 9:
        return[3,8,10,17]
    if j== 10:
        return[6,9,14]
    if j== 11:
        return[7,12,16]
    if j== 12:
        return[5,11,13,19]
    if j== 13:
        return[2,12,22]
    if j== 14:
        return[10,15,17]
    if j== 15:
        return[14,16,18]
    if j== 16:
        return[11,15,19]
    if j== 17:
        return[9,14,18,20]
    if j== 18:
        return[15,17,19,21]
    if j== 19:
        return[12,16,18,22]
    if j== 20:
        return[8,17,21]
    if j== 21:
        return[18,20,22]
    if j== 22:
        return[13,19,21]
    

def GenerateAdd(board):
    
    L = []   
    for location in range(23):
        if board[location] == 'x':
            b = board.copy()
            b[location] = 'W'
            if closeMill(b, location): 
                L = GenerateRemove(b, L)
            else:
                L.append(b)

    return L

def GenerateMove(board):
    L = []
    for location in range(23):
        if board[location] == 'W':
            n = neighbours(location)
            for j in n:
                if board[j] =='x':
                    b = board.copy()
                    b[location] ='x'
                    b[j] = 'W'
                    if closeMill(b,j):
                        L = GenerateRemove(b,L)
                    else:
                        L.append(b)
    return L

def GenerateHopping(board):
    L = []
    for l1 in range(23):
        if board[l1] == 'W':
            for l2 in range(23):
                if board[l2] == 'x':
                    b = board.copy()
                    b[l1] = 'x' 
                    b[l2] = 'W'
                    if closeMill(b,l2): 
                        L = GenerateRemove(b, L)
                    else:
                        L.append(b)

    return L
            
def GenerateRemove(board, L):
    flag = 0
    for location in range(23):
        if board[location]== 'B':
            if not closeMill(board,location):
                b = board.copy()
                b[location] = 'x'
                L.append(b)
                flag = 1
                
    if flag == 0:
         b = board.copy()   
         L.append(b)

        
    return L



def GenerateMovesOpening(board):
    L = []
    L = GenerateAdd(board)
    
    return L

def GenerateMovesMidgameEndgame(board):
    L = []
    white_count = 0
    for l in board:
        if l == 'W':
            white_count += 1
    
    if white_count == 3:
        L = GenerateHopping(board)
    else:
        L = GenerateMove(board)
    
    return L



def StaticEstimate(board):
    
    white_count = 0
    black_count = 0
    Lb = GenerateMovesMidgameEndgameBlack(board)
    black_moves = len(Lb)
    
    for l in board:
        if l == 'W':
            white_count += 1
        elif l == 'B':
            black_count += 1

    return white_count,black_count, black_moves

def StaticEstimationMidgameEndgame(board):
    
    white_count, black_count, black_moves = StaticEstimate(board)
    
    if black_count <= 2 :
        return (10000)
    elif white_count <= 2:
        return (-10000)
    elif black_moves==0:
        return (10000)
    else:
        return ( (1000 * (white_count - black_count) )- black_moves)
    
    
def StaticEstimationOpening(board):
    
    white_count, black_count, black_moves = StaticEstimate(board)
    
    return (white_count - black_count)


def StaticEstimationOpeningImproved(board):
    
    white_count, black_count, black_moves = StaticEstimate(board)
    
    return (2 * white_count - black_count)


def StaticEstimationMidgameEndgameImproved(board):
    
    white_count, black_count, black_moves = StaticEstimate(board)
    
    if black_count <= 2 :
        return (10000)
    elif white_count <= 2:
        return (-10000)
    elif black_moves==0:
        return (10000)
    else:
        return ( (1000 * (2 * white_count - black_count) )- black_moves)




def exchange_board(boardb):
    tempb = []
    tempb = boardb.copy()
    for location in range(23):
        if tempb[location] == 'W':
            tempb[location] = 'B'
        elif tempb[location] == 'B':
            tempb[location] = 'W'
    return tempb

def exchange_list(Lb):
    Lbb = []
    Lbb = Lb.copy()
    for b in Lbb:
        for location in range(23):
            if b[location] == 'W':
                b[location] = 'B'
            elif b[location] == 'B':
                b[location] = 'W'
    
    return Lbb
    
    
def GenerateMovesOpeningBlack(boardb):
    Lbb = []
    
    tempb = exchange_board(boardb)        
    Lbb = GenerateAdd(tempb)
    Lbb = exchange_list(Lbb)
    
    return Lbb

def GenerateMovesMidgameEndgameBlack(boardb):
    Lbb = []
    
    tempb = exchange_board(boardb)                 
    Lbb = GenerateMovesMidgameEndgame(tempb)       
    Lbb = exchange_list(Lbb)
  
    return Lbb

def StaticEstimationOpeningBlack(boardb):
    
    tempb = exchange_board(boardb)
    se = StaticEstimationOpening(tempb)
    
    return se


def StaticEstimationMidgameEndgameBlack(boardb):
    
    tempb = exchange_board(boardb)
    se = StaticEstimationMidgameEndgame(tempb)

    return se

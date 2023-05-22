import time
from random import randint
from random import choice
import copy
import keyboard

rdm_ia = False
worst_ia = False
class var:
    def create_fake_map():
        _map = []
        l = ["-","-","-","-","-","-","-"]
        for i in range(6):
            _map.append(l)
            for j in range(7):
                pass
        return (_map)
    
    def create_map():
        _map = []
        for i in range(6):
            row = ["-"] * 7  # Create a new list for each row
            _map.append(row)
        return _map

    def map_position():
        map_arr = []
        pos_x = []
        pos_y = []
        idx = 0
        for i in range(6):
            row = []
            for j in range(7):
                x_ = 700 + j * 75
                y_ = 332 + i * 75
                pos_x.append(x_)
                pos_y.append(y_)
                row.append((x_, y_))
                idx += 1
            map_arr.append(row)
        return (map_arr, pos_x, pos_y)
    
    board = create_map()
    fake_board = create_fake_map()
    pos, pos_x, pos_y = map_position()

v = var()


def print_map():
    for row in v.board:
        for piece in row:
            if piece == "2":
                print("\033[91m" + piece + "\033[0m", end=" ")  # Print red piece
            elif piece == "1":
                print("\033[93m" + piece + "\033[0m", end=" ")  # Print yellow piece
            else:
                print(piece, end=" ")
        print()

def print_custum_map(board):
    for row in board:
        for piece in row:
            if piece == "1":
                print("\033[91m" + piece + "\033[0m", end=" ")  # Print red piece
            elif piece == "2":
                print("\033[93m" + piece + "\033[0m", end=" ")  # Print yellow piece
            else:
                print(piece, end=" ")
        print()


def check_win(board):
    # UP DOWN POSITION
    win = False
    rows = 6
    cols = 7
    for i in range(rows):
        for j in range(cols):
            if i + 3 < 6:
                if board[5-i][j] == "1" and board[4-i][j]  == "1" and board[3-i][j]  == "1" and board[2-i][j] == "1":
                    return -1
                if board[5-i][j] == "2" and board[4-i][j]  == "2" and board[3-i][j]  == "2" and board[2-i][j] == "2":
                    return 1
                

    # RIGHT LEFT POSITION
    for i in range(rows):
        for j in range(cols):
            if j + 3 < 7:
                if board[i][6-j]  == "1" and board[i][5-j] == "1" and board[i][4-j] == "1" and board[i][3-j] == "1":
                    return -1
                if board[i][6-j]  == "2" and board[i][5-j] == "2" and board[i][4-j] == "2" and board[i][3-j] == "2":
                    return 1
                

    # DIAG RIGHT POSITION
    for i in range(rows):
        for j in range(cols):
            if j + 3 < 7 and i + 3 < 6:
                if board[5-i][j] == "1" and board[4-i][j+1] == "1" and board[3-i][j+2] == "1" and board[2-i][j+3] == "1":
                    return -1
                if board[5-i][j] == "2" and board[4-i][j+1] == "2" and board[3-i][j+2] == "2" and board[2-i][j+3]  == "2":
                    return 1
                

    # DIAG LEFT POSITION
    for i in range(rows):
        for j in range(cols):
            if j + 3 < 7 and i + 3 < 7:
                if board[5-i][6-j] == "1" and board[4-i][5-j] == "1" and board[3-i][4-j] == "1" and board[2-i][3-j] == "1":
                    return -1
                if board[5-i][6-j] == "2" and board[4-i][5-j] == "2" and board[3-i][4-j] == "2" and board[2-i][3-j] == "2":
                    return 1
    if check_draw(board) == 1:
        return 2
    return 0

def get_all_posible_move(board):
    col_1 = board[0][0] + board[1][0] + board[2][0] + board[3][0] + board[4][0] + board[5][0]
    col_2 = board[0][1] + board[1][1] + board[2][1] + board[3][1] + board[4][1] + board[5][1]
    col_3 = board[0][2] + board[1][2] + board[2][2] + board[3][2] + board[4][2] + board[5][2]
    col_4 = board[0][3] + board[1][3] + board[2][3] + board[3][3] + board[4][3] + board[5][3]
    col_5 = board[0][4] + board[1][4] + board[2][4] + board[3][4] + board[4][4] + board[5][4]
    col_6 = board[0][5] + board[1][5] + board[2][5] + board[3][5] + board[4][5] + board[5][5]
    col_7 = board[0][6] + board[1][6] + board[2][6] + board[3][6] + board[4][6] + board[5][6]
    all_cols = [col_1,col_2,col_3,col_4,col_5,col_6,col_7]
    all_mvt = []
    for i in range(len(all_cols)):
        if "-" in all_cols[i]:
            all_mvt.append(i)
    return (all_mvt)

def check_draw(board):
    col_1 = board[0][0] + board[1][0] + board[2][0] + board[3][0] + board[4][0] + board[5][0]
    col_2 = board[0][1] + board[1][1] + board[2][1] + board[3][1] + board[4][1] + board[5][1]
    col_3 = board[0][2] + board[1][2] + board[2][2] + board[3][2] + board[4][2] + board[5][2]
    col_4 = board[0][3] + board[1][3] + board[2][3] + board[3][3] + board[4][3] + board[5][3]
    col_5 = board[0][4] + board[1][4] + board[2][4] + board[3][4] + board[4][4] + board[5][4]
    col_6 = board[0][5] + board[1][5] + board[2][5] + board[3][5] + board[4][5] + board[5][5]
    col_7 = board[0][6] + board[1][6] + board[2][6] + board[3][6] + board[4][6] + board[5][6]
    all_cols = [col_1,col_2,col_3,col_4,col_5,col_6,col_7]
    for i in range(len(all_cols)):
        if "-" in all_cols[i]:
            return(0)
    return (1)

def make_random_move_monte_carlo(board):
    col_1 = board[0][0] + board[1][0] + board[2][0] + board[3][0] + board[4][0] + board[5][0]
    col_2 = board[0][1] + board[1][1] + board[2][1] + board[3][1] + board[4][1] + board[5][1]
    col_3 = board[0][2] + board[1][2] + board[2][2] + board[3][2] + board[4][2] + board[5][2]
    col_4 = board[0][3] + board[1][3] + board[2][3] + board[3][3] + board[4][3] + board[5][3]
    col_5 = board[0][4] + board[1][4] + board[2][4] + board[3][4] + board[4][4] + board[5][4]
    col_6 = board[0][5] + board[1][5] + board[2][5] + board[3][5] + board[4][5] + board[5][5]
    col_7 = board[0][6] + board[1][6] + board[2][6] + board[3][6] + board[4][6] + board[5][6]
    all_cols = [col_1,col_2,col_3,col_4,col_5,col_6,col_7]
    rdm_pos = randint(0,5)
    rdm_pos_y = 0
    rdm_pos_y = randint(0,6)
    idx = 0
    stop_move = False
    while "-" not in all_cols[rdm_pos]:
        idx+=1
        if idx > 25000:
            stop_move = True
            print("flop")
            return (make_random_move_monte_carlos(board))
            break
        rdm_pos = randint(0,5)

    if stop_move == True:
        for i in range(len(all_cols)):
            if "-" in all_cols[i]:
                rdm_pos = i
                break
        
    for i in range(5):
        if board[5-i][rdm_pos_y] == "-":
            rdm_pos = 5 - i
            return (rdm_pos,rdm_pos_y)
    rdm_pos_2 = get_all_posible_move(board)
    rdm_pos_2_ = rdm_pos_2[randint(0,len(rdm_pos_2) - 1)]
    
    for i in range(5):
        if board[5-i][rdm_pos_2_] == "-":
            rdm_pos = 5 - i
            return (rdm_pos,rdm_pos_2_)
    #print("pow")
    return (rdm_pos,rdm_pos_y)

def check_empty_space(nb,board):
    for i in range(5):
        #print(nb,5-i,)
        if board[5-i][nb] == "-":
            y = 5 - i
            return (y)

def make_random_move_monte_carlos(board):
    for i in range(5):
        for j in range(6):
            if board[i][6-j] == "-":
                return(i,6-j)

def remove_duplicates(lst):
    return list(set(lst))

def sort_by_occurrence(lst):
    counts = {item: lst.count(item) for item in lst}
    return sorted(lst, key=lambda item: counts[item], reverse=True)

    
def get_highest_elem(letters, numbers):
    combined = list(zip(numbers, letters))
    combined.sort(reverse=True)
    sorted_numbers, sorted_letters = zip(*combined)
    return sorted_letters[0]

def get_lowest_elem(letters, numbers):
    combined = list(zip(numbers, letters))
    combined.sort()
    sorted_numbers, sorted_letters = zip(*combined)
    return sorted_letters[0]

def calc_pourcentage(Total,a):
    return ((a/Total)*100)

def monte_carlo(start_board,p,power):
    MAX = power
    if rdm_ia == True:
        MAX = randint(1,10000)
        print("Val max attaque " , MAX)
    _board = copy.deepcopy(start_board)
    win_or_not = check_win(_board)
    win = 0
    loose = 0
    draw = 0
    idx = 0
    first_move = True
    first_move_list = []
    win_num = []
    loose_num = []
    num = 0
    print_or_no = False
    for j in range(MAX):
        #print("Welcome")
        idx = idx + 1
        while win_or_not == 0:
            xx , yy = make_random_move_monte_carlo(_board)
            if p == 1:
                _board[xx][yy] = "2"
            else:
                _board[xx][yy] = "1"
            
            if first_move == True:
                first_move_list.append(yy)
                first_move = False
            xx , yy = make_random_move_monte_carlo(_board)
            if p == 1:
                _board[xx][yy] = "1"
            else:
                _board[xx][yy] = "2"
            
            win_or_not = check_win(_board)
        if win_or_not == 1:
            if p == 1:
                win += 1
            else:
                loose+=1
            try:
                win_num.append(first_move_list[-1])
            except:
                win_num.append(randint(0,6))
        if win_or_not == -1:
            if p == 1:
                loose += 1
            else:
                win+=1
            try:
                loose_num.append(first_move_list[-1])
            except:
                loose_num.append(randint(0,6))
        if win_or_not == 2:
            draw += 1
        _board = copy.deepcopy(start_board)
        win_or_not = 0
        first_move = True
    
    if print_or_no == True:
        print("IA win : " + str(win) + " IA loose : " + str(loose) + " IA draw : " + str(draw))
    n = return_element_the_least_list(loose_num)
    n2 = return_element_the_least_list(loose_num)
    p_num = []
    p_all = []
    p_win = []
    p_loose = []
    all_mvt = get_all_posible_move(start_board)
    for i in range(7):
        if i in all_mvt:
            p_num.append(i)
            p_all.append(calc_pourcentage(MAX,win_num.count(i)) - calc_pourcentage(MAX,loose_num.count(i)))
            p_win.append(calc_pourcentage(MAX,win_num.count(i)))
            p_loose.append(calc_pourcentage(MAX,loose_num.count(i)))
    
    
    if print_or_no == True:
        print("pourcentage total: " ,p_all)
        print("pourcentage win: ", p_win)
        print("pourcentage loose: ", p_loose)
        print("numero :" ,p_num)
        
    best_num = get_highest_elem(p_num,p_all)
    if worst_ia == True:
        best_num = get_lowest_elem(p_num,p_all)
    loose_rate = calc_pourcentage(MAX,loose)
    
    if loose_rate > 80:
        loose_list = []
        for choice in p_num:
            loose_list.append(monte_carlo_check(start_board,p,power))
        if worst_ia == True:
            return get_highest_elem(p_num,loose_list)
        return get_lowest_elem(p_num,loose_list)
    return best_num


def monte_carlo_check(start_board,p,power):
    MAX = power
    if rdm_ia == True:
        MAX = randint(1,10000)
        print("Val max attaque " , MAX)
    _board = copy.deepcopy(start_board)
    win_or_not = check_win(_board)
    win = 0
    loose = 0
    draw = 0
    idx = 0
    first_move = True
    first_move_list = []
    win_num = []
    loose_num = []
    num = 0
    print_or_no = False
    for j in range(MAX):
        while win_or_not == 0:
            xx , yy = make_random_move_monte_carlo(_board)
            if p == 1:
                _board[xx][yy] = "1"
            else:
                _board[xx][yy] = "2"
            
            if first_move == True:
                first_move_list.append(yy)
                first_move = False
            xx , yy = make_random_move_monte_carlo(_board)
            if p == 1:
                _board[xx][yy] = "2"
            else:
                _board[xx][yy] = "1"
            
            win_or_not = check_win(_board)
        if win_or_not == 1:
            if p == 1:
                loose += 1
            else:
                win+=1
            try:
                win_num.append(first_move_list[-1])
            except:
                win_num.append(randint(0,6))
        if win_or_not == -1:
            if p == 1:
                win += 1
            else:
                loose+=1
            try:
                loose_num.append(first_move_list[-1])
            except:
                loose_num.append(randint(0,6))
        if win_or_not == 2:
            draw += 1
        _board = copy.deepcopy(start_board)
        win_or_not = 0
        first_move = True
    if print_or_no == True:
        print("ENEMY win : " + str(win) + " ENEMY loose : " + str(loose) + " ENEMY draw : " + str(draw))
    
    win_rate = calc_pourcentage(MAX,win)
    if print_or_no == True:
        print("win rate enemy: " , win_rate)
    
    return win_rate

def return_element_the_least_list(l):
    try:
        return min(set(l), key=l.count)
    except:
      rdm_pos = get_all_posible_move(v.board)
      rdm_pos = rdm_pos[randint(0,len(rdm_pos) - 1)]
      return rdm_pos

def return_element_the_most_list(l):
    try:
        return max(set(l), key=l.count)
    except:
      rdm_pos = get_all_posible_move(v.board)
      rdm_pos = rdm_pos[randint(0,len(rdm_pos) - 1)]
      return rdm_pos


def check_empty_space(nb,board):
    for i in range(6):
        if board[5-i][nb] == "-":
            y = 5 - i
            return (y)


def player_vs_player():
    connect4 = var()

    print_map()

    state = check_win(v.board)

    while state == 0:
        try:
            choice = input("Player 1 Pos 1-7: ")
            v.board[check_empty_space(int(choice) - 1,v.board)][int(choice) - 1] = "1"
            state = check_win(v.board)
            print_map()
            
            if state == -1:
                print("PLAYER1 WIN")
                quit()
            
            if state == 1:
                print("PLAYER1 LOOSE")
                quit()
            
            choice = input("Player 2 Pos 1-7: ")
            v.board[check_empty_space(int(choice) - 1,v.board)][int(choice) - 1] = "2"
            state = check_win(v.board)
            print_map()
            
            if state == 1:
                print("PLAYER2 WIN")
                quit()
            
            if state == -1:
                print("PLAYER2 LOOSE")
                quit()
            
                
        except KeyboardInterrupt:
            print("Bye")
            quit()
        except Exception as e:
            print("Error: " + str(e))

def plaer_vs_ia():
    level = input("Le niveau des ia entre 1 et 20000: ")
    connect4 = var()

    print_map()

    state = check_win(v.board)

    while state == 0:
        try:
            choice = input("Pos 1-7: ")
            v.board[check_empty_space(int(choice) - 1,v.board)][int(choice) - 1] = "1"
            state = check_win(v.board)
            print_map()
            
            if state == -1:
                print("PLAYER WIN")
                quit()
            
            if state == 1:
                print("PLAYER LOOSE")
                quit()
            
            ia_choice = monte_carlo(v.board,1,int(level))
            v.board[check_empty_space(ia_choice,v.board)][ia_choice] = "2"
            print_map()
            state = check_win(v.board)
            if state == 1:
                print("IA WIN")
                quit()
            
            if state == -1:
                print("IA LOOSE")
                quit()
            
            
        except KeyboardInterrupt:
            print("Bye")
            quit()
        except Exception as e:
            print("Error: " + str(e))


def ia_vs_ia():
    connect4 = var()

    print_map()

    state = check_win(v.board)

    while state == 0:
        try:
            ia_choice = monte_carlo(v.board,2,1000)
            print("Freedy played ", ia_choice + 1)
            v.board[check_empty_space(ia_choice,v.board)][ia_choice] = "2"
            state = check_win(v.board)
            print_map()
            
            #ime.sleep(2)
            if state == 1:
                print("FREDY WIN")
                quit()
            
            if state == -1:
                print("FREDY LOOSE")
                quit()
            
            ia_choice = monte_carlo(v.board,1,10000)
            print("Bob played", ia_choice + 1)
            v.board[check_empty_space(ia_choice,v.board)][ia_choice] = "1"
            state = check_win(v.board)
            print_map()

            if state == -1:
                print("BOB WIN")
                quit()
            
            if state == 1:
                print("BOB LOOSE")
                quit()
        
        
        except KeyboardInterrupt:
            print("Bye")
            quit()
        except Exception as e:
            print("Error: " + str(e))


choice = input("Choose 1-2-3-4 \n1) IA VS IA\n2) PLAYER VS IA\n3) PLAYER VS PLAYER\n4) QUIT\n")

if choice == "1":
    ia_vs_ia()
if choice == "2":
    plaer_vs_ia()
if choice == "3":
    player_vs_player()

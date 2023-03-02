table = list(range(1,10))

def line_table(table):
    print ("=" * 13)
    for i in range(3):
        print ("|", table[0+i*3], "|", table[1+i*3], "|", table[2+i*3], "|")
        print ("=" * 13)

def data_entry(player_move):
    valid = False
    while not valid:
        player = input("Следущий ход " + player_move+"? ")
        try:
            player = int(player)
        except:
            print ("Введите число от 1 до 9?")
            continue
        if player >= 1 and player <= 9:
            if (str(table[player-1]) not in "XO"):
                table[player-1] = player_move
                valid = True
            else:
                print ("Эта ячейка занята")
        else:
            print ("Введите число от 1 до 9")

def victory(table):
    winning_combinations = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for all in winning_combinations:
        if table[all[0]] == table[all[1]] == table[all[2]]:
            return table[all[0]]
    return False

def main(table):
    counter = 0
    win = False
    while not win:
        line_table(table)
        if counter % 2 == 0:
            data_entry("X")
        else:
            data_entry("O")
        counter += 1
        if counter > 4:
            tmp = victory(table)
            if tmp:
                print (tmp, "Выиграл!")
                win = True
                break
        if counter == 9:
            print ("Ничья!")
            break
    line_table(table)

main(table)
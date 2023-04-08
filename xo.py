maps = list(range(1,10))

def draw_maps():
    for i in range(3):
        print (maps[0+i*3], maps[1+i*3], maps[2+i*3])


def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if str(maps[player_answer-1]) not in "XO":
                maps[player_answer-1] = player_token
                valid = True
            else:
                print("Клетка уже занята")
        else:
            print("Введите число от 1 до 9.")


def check_win(maps):
    win_coord = ((0, 1, 2),(3, 4 ,5),(6, 7, 8),(0, 3, 6),(1, 4, 7),(2, 5, 8),(0, 4, 8),(2, 4, 6))
    for each in win_coord:
        if maps[each[0]] == maps[each[1]] == maps[each[2]]:
            return maps[each[0]]
    return False

def main(maps):
    counter = 0
    win = False
    while not win:
        draw_maps()
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(maps)
            if tmp:
                print (tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print ("Ничья!")
            break
    draw_maps()

main(maps)
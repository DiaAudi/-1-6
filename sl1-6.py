import requests

def Game():
    url = 'https://python666.cn/cls/number/guess/'
    n = int(requests.get(url).text)
    print(n)
    times = 0
    j = 1
    while j:
        num = int(input('guess a number'))
        times += 1
        if num < n:
            print('Too small, guess another one')
        elif num > n:
            print('Too big, guess another one')
        else:
            j = 0
    return times

def A(player):
    y = 'y'
    while y == 'y':
        name = input('enter your name')
        if player.get(name):
            round = int(player[name][0])
            times_min = int(player[name][1])
            times_t = float(player[name][2])
            avg = times_t / round
        else:
            round = 0
            times_min = 0
            times_t = 0
            avg = 0
        print('%s, total %d round, minimum %d round, average %.2f times, game start!'%(name,round, times_min, avg))

        times = Game()
        round += 1
        times_t += times
        if times_min == 0 or times_min > times:
            times_min = times
        time_avg = times_t / round
        print('%s,you are right, you guessed %d times, total %d round, min %d times, average %.2f times' %(name, times, round, times_min, time_avg))
        player[name] = [str(round), str(times_min), str(times_t)]
        y = input('输入y继续， 其他退出')
    print('退出游戏，欢迎下次再来')
    return player

def main():
    with open('game_many_user.txt' ) as f:
        info = f.readlines()
    player = {}
    for j in info:
        infol = j.strip().split()
        player[infol[0]] = infol[1:]
    player = A(player)
    info_new = []
    for k, v in player.items():
        info_new.append(k + ' '+' '.join(v)+'\n')

    with open('game_many_user.txt','w+') as f:
        f.writelines(info_new)
try:
    main()
except:
    print('error')
    main()



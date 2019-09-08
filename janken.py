import random
import utils

print('今からジャンケンを始めます')
player_name = input('名前を入力してください：')
player_hand = int(input('ジャンケン(0: グー, 1: チョキ, 2: パー)：'))

if utils.validate(player_hand):
    computer_hand = random.randint(0,2)

    if player_name == '':
        utils.janken(player_hand)
    else: 
        utils.janken(player_hand, player_name)

    utils.janken(computer_hand, 'コンピューター')
    
    result = utils.judge(player_hand, computer_hand)

    print('結果は'+result)
else:
    print('正しい値を入力してください')



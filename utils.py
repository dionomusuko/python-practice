def validate(hand):
    if hand < 0 or hand >2:
        return False
    return True

def janken(hand, name = 'ゲスト'):
    hands = ['グー', 'チョキ', 'パー']
    print(name + 'は' + hands[hand] + 'を出しました')

def judge(player, computer):
    if player == computer:
        return 'あいこです'
    elif player == 0 and computer == 1:
        return 'あなたの勝ちです'
    elif player == 1 and computer == 2:
        return 'あなたの勝ちです'
    elif player == 2 and computer == 0:
        return 'あなたの勝ちです'
    else:
        return 'あなたの負けです'
        
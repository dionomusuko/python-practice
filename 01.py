apple_price = 150
money = 3000

input_count = input('りんごの購入した個数を入力してください：')
count = int(input_count)
total_price = apple_price * count



if money > total_price:
    print('購入した代金は'+str(total_price)+'円です')
    print('残ったお金は'+str(money - total_price)+'円です')
elif money == total_price:
    print('購入するとお金が無くなります')
else:
    print('購入できません')
        
        
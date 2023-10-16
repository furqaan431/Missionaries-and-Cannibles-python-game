boat_side = 'Right'
missionaries_on_right = 3
cannibals_on_right = 3
missionaries_on_left = 0
cannibals_on_left = 0

print ('M=',missionaries_on_left, 'C=',cannibals_on_left, '|\U0001f30a *5 \U0001f6A2 |', 'M=',missionaries_on_right, 'C=',cannibals_on_right)
#taking input
while True :
    missionaries = int(input(" Enter No.of Missionaries or Type 10 to Quit :"))
    if(missionaries == 10):
        break

    cannibals = int(input("Enter No.of Cannibals :"))
    if(missionaries + cannibals)!=1 and (missionaries + cannibals)!=2 :
        print("Invalid mode: Total no.of people on the boat should be one or two")
        continue

    if boat_side == 'Right':
        if missionaries_on_right < missionaries or cannibals_on_right < cannibals :
           print('Invalid Move')
        missionaries_on_right = missionaries_on_right - missionaries
        cannibals_on_right = cannibals_on_right - cannibals
        missionaries_on_left = missionaries_on_left + missionaries
        cannibals_on_left = cannibals_on_left + cannibals
        print('M=',missionaries_on_left, 'C=',cannibals_on_left, '| \U0001f6A2  \U0001f30a *5 |', 'M=',missionaries_on_right, 'C=',cannibals_on_right)
        boat_side = 'Left'

    else:
        if missionaries_on_left < missionaries or cannibals_on_left < cannibals :
            print('Invalid Move')

        missionaries_on_left = missionaries_on_left - missionaries
        cannibals_on_left = cannibals_on_left - cannibals

        missionaries_on_right = missionaries_on_right +  missionaries
        cannibals_on_right = cannibals_on_right + cannibals

        print('M =',missionaries_on_left, 'C =',cannibals_on_left, '|\U0001f30a *5 \U0001f6A2|', 'M =',missionaries_on_right, 'C =',cannibals_on_right)
        boat_side = 'Right' 

    if(missionaries_on_right < cannibals_on_right and missionaries_on_right >0) or (missionaries_on_left < cannibals_on_left and missionaries_on_left > 0):
            print('You Loose')
            break
        # condition to win
    if(missionaries_on_left == 3 and cannibals_on_left == 3):
            print('You Win')
            break

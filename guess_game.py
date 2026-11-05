import random 
def guessing_game():
 print("Welcome to Ramu's word guessing game!!!!")
 computer=random.randint(1,100) 
 count=0
 while count<5:
    try:
     num=int(input("Enter the your  number (1 to 100):"))
    except ValueError:
        print("Enter integer value")
        continue
    if num<1 or num>100:
       print("Invalid number......\nNumber should be within 1-100")
    count+=1   
    if num==computer:
        print("Kudos to youuuu!!!!! You wonnn!!\n Number of attempts{}".format(count))
        break
    elif num>computer:
        print('The {} is too highh!!\n You have only {} attempts'.format(num,5-count))
    elif num<computer:
        print('The {} is too loww!!\n You have only {} attempts'.format(num,5-count))
 else:
    print('Good luck!! the game ended\n The correct number is {}'.format(computer))   
while True:
   guessing_game()
   choice=input('Do you want to play again :) (yes/no)').lower()
   if choice!='yes':
      print('Thanks for your efforts kiddoo')
      break
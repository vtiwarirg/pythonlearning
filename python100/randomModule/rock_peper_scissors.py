import random  
rock ='''        \                              /\| | | |
         \                            / /|_|_|_|
          \                           \        |
            (  ( ) ) ( )  )            \_______/
           ( ( ( ( )  )  ) )           /______/
          ( ( )) ) (   ) ( ( )        /       /
          ( (__.-.___.-.__) )        /       /
           /---._.---._.---\        /       /
           \||   '/  '   ||/       /       /
            |||  (_     |||       /       /
             || ///\\\  ||\______/       /
        ___/ ||||\__/|||||/             /
       /   \   ||||||||  /             /
      /     \   ||||||  /        _____/
      
      /       \  ||||  /        /
    '''

paper = '''
           __                       __
         __\_\___               ___/_/__
        /_______ \___       ___/\_______\
           \_\  \/__/\_____/\__\/  /_/
                    \/_____\/                      __
                     \o | o/_____ ________________/\_\
                      \ | /_______\_______________\/
                       \_/        /  b'ger        |
                                 /\           _   |
                                / /\_________/ |__|
                               / /             / /
                              /_/             /_/
                              \ \             \ \
                               \ \             \_\
                                \_\            /_/
                                /_/            |_|
                                  
    '''
scissors = '''
    _       ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\.
'''
            
                                         

user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
computer_choice = random.randint(0, 2)
print(f"Computer choice: {computer_choice}")
if computer_choice == 0:
    computer_choice = "rock"
elif computer_choice == 1:
    computer_choice = "paper"
elif computer_choice == 2:
    computer_choice = "scissors"
else:
    computer_choice = "Invalid choice"   
    
    
if user_choice == 0  and computer_choice == 0:
    print("It's a tie!")
elif user_choice == 0 and computer_choice == 1:
    print("You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 1 and computer_choice == 0:
    print("You win!")
elif user_choice == 1 and computer_choice == 1:         

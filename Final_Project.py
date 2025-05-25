# Excape Room Game

class EscapeRoom:
    def __init__(self):
        # Puzzle answers and game state
        self.room1_solved = False
        self.room2_solved = False
        self.room3_solved = False
        self.room4_solved = False
        self.room5_solved = False
        self.game_over = False
        self.inventory = []
        self.soul_stack = []

    def start_game(self):
        print("The outside world is dark and stormy. You find yourself in front of a creepy mansion.")
        print("You step inside, and the door slams shut behind you. A mix voice echoes in the hall...")
        while True:
            choice = input('"Please help me~ I am trapped here forever~"').strip().lower()
            if choice in ['yes', 'y', 'ok', 'sure']:
                print("\nA light comes into view. It leads you deeper into the mansion...")
                break
        self.play_game()

    def play_game(self):
        while not self.game_over:
            if not self.room1_solved:
                self.room1_puzzle()
            elif not self.room2_solved:
                self.room2_puzzle()
            elif not self.room3_solved:
                self.room3_puzzle()
            elif not self.room4_solved:
                self.room4_puzzle()
            elif not self.room5_solved:
                self.room5_puzzle()
            else:
                print("\nYou hear the mixed voice: 'Thank you for freeing us. We are finally at peace.'\n")
                self.game_over = True

    def room1_puzzle(self):
        # Room 1: Guessing game with Four-Digit Code
        print("\nRoom 1: The Locked Library")
        print("A dusty, forgotten library filled with old books. The air is thick with dust and the smell of old paper.")
        print("You can see an old, dusty book on a pedestal. It has a strange lock on it.")
        print("The lock need 4-digit number.")        
        
        four_code = 1525
        
        print("\nYou notice an old plaque on the wall with the inscription: 'The mansion was built in a five century ago...'")
        while True:
            guess = input("Enter the 4-digit code to unlock the book: ")
            if len(guess) != 4 or not guess.isdigit():
                print("Please enter a valid 4-digit code.")
                continue 
            
            if guess != str(four_code):
                print("Incorrect code. Try again...")
                continue

            else:
                print("\nThe book opens with a faint creak! Inside, you find a rusty key.")
                self.inventory.append("History Key")
                print("You have added a Rusty Key to your inventory.")
                self.soul_stack.append("Soul of History")
                print("The Soul of Knowledge has been freed and added to your soul stack.")
                print("\nThe door to the next room opens, and you step through.")

                self.room1_solved = True
                break

    def room2_puzzle(self):
        # Room 2: A logic puzzle
        print("\nRoom 2: The Portrait Hall")
        print("A long hallway filled with portraits of previous mansion owners. The paintings' eyes follow you...")

        print("Each painting represents an important phase in the mansion's history, with a plaque under each portrait.")
        print("The plaques bear numbers that represent significant years in the mansion's ownership.")

        print("\nThe portraits feature the following numbers: 1, 4, 9, 16... These numbers are trapped time...")
        print('A voice: "How many years should I wait to be free?"')

        answer = 25

        while True:
            try:
                answer = int(input("Enter the next number in the sequence: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if answer < 25:
                print("The number is higher!")
            elif answer > 25:
                print("The number is lower...")
            else:
                print("\nThe portraits shift, revealing a hidden key.")
                self.inventory.append("Memory Key")
                self.soul_stack.append("Soul of Memory")
                print("The Soul of Memory has been freed and added to your soul stack.")
                print("\nThe wall shifts, revealing a passage to the next room.")

                self.room2_solved = True
                break

    def room3_puzzle(self):
        # Room 3: A word-based riddle
        print("\nRoom 3: The Ghostly Study")
        print("The room is filled with old furniture, and a cold breeze flows through the cracked windows. The air is heavy...")
        print('A disembodied voice rings out: "I speak without a mouth and hear without ears. I have nobody, but I come alive with the wind. What am I?"')
        
        correct_word = "echo"

        guess = ""
        while guess != correct_word:
            guess = input("Enter the word: ").lower()
            if guess != correct_word:
                print("Incorrect, try again...")
            elif guess == correct_word:
                print("\nThe room shudders, and a ghostly figure appears and give a key. It points to a bookshelf.")
                self.inventory.append("Ghostly Key")
                print("\nThe bookshelf moves to reveal a hidden door!")
                self.soul_stack.append("Soul of Regret")
                print("The Soul of Regret has been freed and added to your soul stack.")
                print("The door opens, and you step through to the next room.")
                
                self.room3_solved = True
                break  

    def room4_puzzle(self):
        # Room 4: A math-based puzzle
        print("\nRoom 4: The Cryptic Chamber")
        print("A cold, stone chamber. The chamber is filled with mysterious carvings and symbols, and a pedestal sits in the center")
        print('"The pedestal bears a function: (3^4) - √144 + (7 * 6) = ?"')
        
        answer = int(111)

        while True:
            try:
                answer = int(input("Enter your answer: "))
            except ValueError:
                print("Please enter a valid number.")
                continue    

            if answer < 111:
                print("The answer is higher!")
            elif answer > 111:
                print("The answer is lower...")
            else:
                print("\nThe floor vibrates and a hidden drawer opens with a shiny golden key inside.")
                self.inventory.append("Golden Key")
                print("The Soul of Wisdom has been freed and added to your soul stack.")
                self.soul_stack.append("Soul of Wisdom")
                print("The back wall was reassembled into a staircase leading to the final room.")

                self.room4_solved = True
                break

    def room5_puzzle(self):
        # Room 5: Final puzzle involves a combination of previous clues
        print("\nRoom 5: The Escape")
        print("A large, ornate chamber with a huge door adorned with strange runes.")
        print("The voice from the beginning came back: 'You have freed us, but to escape, you must remember the names of the souls you've freed.'")
        print("'You must enter the names in the order you freed them.'")

        # souls collected so far: History, Memory, Regret, Wisdom
        index = 0
        while True:
            guess = input(f"Name soul {index+1}: ").strip().lower()
            if guess == self.soul_stack[index].lower():
                index += 1
                if index == len(self.soul_stack):
                    break
                else:
                    print("…correct. Now, the next soul.")
            else:
                print("That is not the correct soul. Let's start over.\n")
                index = 0

        self.soul_stack.append("Soul of Freedom")
        print("\nThe Soul of Freedom has been freed ")
        print("Soul Stack: ", self.soul_stack)

        print("\nYou have the following keys in your inventory: ")  
        print("Inventory: ", self.inventory)
        print("Insert combination of the keys...")

        print("\nThe door shimmers and the runes glow brightly.")
        print("The door is opening...")
        print("Each soul you freed is now at peace.")
        print("You feel a rush of fresh air and the storm outside has cleared.")
            
        self.room5_solved = True
   

# Start the game
game = EscapeRoom()
game.start_game()
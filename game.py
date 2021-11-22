import time
from functions import clear_terminal, game_over
from player import Player
from rooms import Room
from questions import (
    html_questions, css_questions,
    javascript_questions, python_questions
)


class Game:
    """
    Game instance brings player through each room,
    giving the player choices to make.
    """

    def __init__(self, user):
        self.user = Player(user)
        self.rooms = ['HTML', 'CSS', 'JavaScript', 'Python']
        self.html_room = Room('HTML', html_questions)
        self.css_room = Room('CSS', css_questions)
        self.javascript_room = Room('JavaScript', javascript_questions)
        self.python_room = Room('Python', python_questions)

    def start(self):
        clear_terminal()
        self.user.show_stats()
        print('Type "c" to continue or "q" to quit.')

        # Validating user input.
        answer = ''
        while answer not in ['c', 'q']:
            answer = input('> ').lower()
            if answer == 'c':
                self.morning()
            elif answer == 'q':
                game_over()
            else:
                print('\nInvalid choice. Please type "c" or "q".')

    # Checks to see if the player has lost all of their confidence and ends game if true.
    def is_player_dead(self):
        if self.user.confidence <= 0:
            game_over()

    def morning(self):
        clear_terminal()
        time.sleep(1)
        print("It's really early in the morning and your alarm goes off.")
        print("Will you?:\n")
        print('1 Go back to sleep.')
        print('2 Get up and get dressed.')

        # Validating user input. Catching any unexpected input.
        morning_choice = ''
        while morning_choice not in [1, 2]:
            try:
                morning_choice = int(input('> '))
                if morning_choice == 1:
                    clear_terminal()
                    print('\nYou really gave up on your journey that easy?\n')
                    self.user.lower_confidence(self.user.confidence)
                    self.is_player_dead()
                    break
                elif morning_choice == 2:
                    self.kitchen()
                    break
                else:
                    print("\nInvalid choice. Please type either 1 or 2.")
                    continue
            except ValueError:
                print("\nYou cannot input any text. You must type either 1 or 2.")
                continue

    def kitchen(self):
        print("\nYou put your clothes on and make you're way into the kitchen.")
        print("Friends is on the TV.")
        print("Will you?:\n")
        print("1 Eat breakfast and drink some coffee.")
        print("2 Watch 5 seasons of Friends. ")

        # Validating user input. Catching any unexpected input.
        kitchen_choice = ''
        while kitchen_choice == '':
            try:
                kitchen_choice = int(input('> '))
                if kitchen_choice not in [1, 2]:
                    print("\nPlease type 1 or 2.")
                    kitchen_choice = ''
                    continue
                else:
                    if kitchen_choice == 1:
                        self.drink_coffee()
                        break
                    elif kitchen_choice == 2:
                        clear_terminal()
                        print("You end up watching Friends all day and forget about your coding.")
                        self.user.lower_confidence(self.user.confidence)
                        self.is_player_dead()
                        break
            except ValueError:
                print("\nYou cannot enter any text. You must type either 1 or 2.")
                continue

    def drink_coffee(self):
        clear_terminal()
        print('You eat your breakfast and drink your coffee.')
        time.sleep(1)
        print("You're now feeling AWAKE and ready to start learning how to code.\n")
        time.sleep(1)
        self.choose_room(self.rooms)

    def check_answer(self, answers, correct_answer):
        while True:
            try:
                user_answer = int(input('> '))
                """
                Checks the user answer to see if it's the same index
                as the index of correct_answer in the list of answers.
                """
                if user_answer == answers.index(correct_answer) + 1:
                    print('Correct!\n')
                    time.sleep(0.5)
                    self.user.increase_score()
                    break
                elif user_answer > len(answers):
                    print(f"""
You must type a number from 1 - {len(answers)}.""")
                    continue
                else:
                    print('Incorrect.')
                    time.sleep(0.5)
                    self.user.lower_confidence()
                    print(f"""
Try again. Type 1, 2 or 3.""")
                    self.user.lower_score()
                    self.is_player_dead()
                    continue
            except ValueError:
                print(f"""
Invalid choice. You must type a number from 1 - {len(answers)}.""")
                continue

    def choose_room(self, rooms):
        """
        Prints each room and its index value,
        asks user to select the room to play.
        """
        while len(rooms) > 0:
            print("Which language would you like to learn?:")
            for index, value in enumerate(rooms):
                print(index + 1, value)
            try:
                choice = int(input('> '))
                room = self.rooms[choice - 1]
                if room == 'HTML':
                    self.play_quiz(self.html_room)
                    continue
                elif room == 'CSS':
                    self.play_quiz(self.css_room)
                    continue
                elif room == 'JavaScript':
                    self.play_quiz(self.javascript_room)
                    continue
                elif room == 'Python':
                    self.play_quiz(self.python_room)
                    continue
            except ValueError:
                print(f"""
Invalid choice. You must type a number from 1 - {len(rooms)}.
""")
                continue
            except IndexError:
                print(f"""
You must type a number from 1 - {len(rooms)}.
""")
                continue

        print('Type "c" to continue or "q" to quit.')

        answer = ''
        while answer not in ['c', 'q']:
            answer = input('> ')
            if answer == 'c':
                clear_terminal()
                print('Congratulations!')
                print('You have accquired all the skills needed to become a Developer!')
                print('You should be proud of yourself!')
                self.job_hunt()
                break
            elif answer == 'q':
                clear_terminal()
                game_over()
            else:
                print('\nInvalid choice. Please type "c" or "q".')
                continue

    def play_quiz(self, room):
        room.room_task()
        while len(room.room_questions) > 0:
            generated_question = room.generate_question()
            room.display_question(generated_question['question'])
            room.display_answers(generated_question['answers'])
            self.check_answer(generated_question['answers'], generated_question['correct_answer'])
        room.room_over()
        self.rooms.pop(self.rooms.index(room.room))
        self.user.set_skills(room.room)
        self.user.show_stats()
        time.sleep(1)

    def job_hunt(self):
        print('\nWould you like to begin your job hunt?')
        print('Type "y" or "n".')

        job_hunt_choice = ''
        while job_hunt_choice not in ['y', 'n']:
            job_hunt_choice = input('> ')
            if job_hunt_choice == 'y':
                self.job_choice()
            elif job_hunt_choice == 'n':
                clear_terminal()
                print('You give into imposter syndrome and never pursue a career as a developer.')
                game_over()
            else:
                print('\nInvalid choice. Please type "y" or "n".')

    def job_choice(self):
        clear_terminal()
        job_choices = ['Google', 'Facebook', 'Apple']

        print(f"""After many interviews, job applications, and further developing your coding knowledge.
You have made it to the final stage for the following 3 companies:
- {job_choices[0]}
- {job_choices[1]}
- {job_choices[2]}""")
        print('\nIf your score is high enough, you will be allowed to join the company of your choice.\n')
        print('Which company would you like to join?:')
        print(f'1 {job_choices[0]}')
        print(f'2 {job_choices[1]}')
        print(f'3 {job_choices[2]}')

        company_choice = ''
        while company_choice == '':
            try:
                company_choice = int(input('> '))
                if company_choice == 1 and self.user.score >= 15:
                    self.end("Front End Developer", "Google")
                    break
                elif company_choice == 1 and self.user.score < 15:
                    print('\nYour score is not high enough to join Google. Choose a different company.')
                    company_choice = ''
                    continue
                elif company_choice == 2 and self.user.score >= 10:
                    self.end("Back End Developer", "Facebook")
                    break
                elif company_choice == 2 and self.user.score < 10:
                    print('\nYour score is not high enough to join Facebook. Choose a different company.')
                    company_choice = ''
                    continue
                elif company_choice == 3:
                    self.end("iOS Developer", "Apple")
                    break
                else:
                    print('\nInvalid choice. Please type "1", "2" or "3" to continue.')
                    company_choice = ''
                    continue

            except ValueError:
                print('\nYou cannot enter any text. Please type "1", "2" or "3" to continue')
                continue

    def end(self, role, company):
        clear_terminal()
        self.user.job = f"{role} @ {company}"
        self.user.show_stats()
        time.sleep(1)

        if company == "Google":
            print(f"""You are officially a Noogler!
You have joined the {company} team as a {role} and work with an amazing team.""")
        elif company == "Facebook":
            print(f"""You joined Facebook!
You have joined the {company} team as a {role}
and get to work alongside with your childhood hero, Mark Zuckerburg!""")
        else:
            print(f"""You joined Apple!
You have joined the {company} team as an {role} and get to work on the next iOS updates.""")

        time.sleep(1)
        print("""
 _____                        _____               
|  __ \                      |  _  |      
| |  \/ __ _ _ __ ___   ___  | | | |_   _____ _ __
| | __ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__|
| |_\ \ (_| | | | | | |  __/ \ \_/ /\ V /  __/ |   
 \____/\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|
""")

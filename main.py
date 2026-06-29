from coding_question import coding_question
from explain_code import explain_code
from debug_code import debug_code
from theory_question import theory_question
from utils import print_menu

while True:

    print_menu()

    choice = input("\nChoose an option: ")

    if choice == "1":
        coding_question()

    elif choice == "2":
        explain_code()

    elif choice == "3":
        debug_code()

    elif choice == "4":
        theory_question()

    elif choice == "5":
        print("\nAllah Hafiz 👋")
        break

    else:
        print("\nInvalid Choice.")
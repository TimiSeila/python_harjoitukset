import os

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def enter_break():
    input("\nPress enter to continue...")

def invalid_selection(redirect):
    clear_console()
    print("Invalid selection")
    enter_break()
    return redirect()

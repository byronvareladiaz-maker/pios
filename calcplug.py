import subprocess
import sys

# Print 200 blank lines to clear the screen
print("\n" * 200)
print("Welcome to the Calculus plugin!")
print("Type your command below.\n")

# Define a variable for the target script if you use 'exit' to run one
script = r"C:\Users\30varela-diazb\PycharmProjects\WelcomeScreen\script.py"

while True:
    command = input("calcplug\\>>> ")

    if command == "exitcmd":
        sys.exit(0)
    elif command == "exit":
        subprocess.run(["python3", str(script)])
    elif command == "int":
        print(
            "This command is under development, please update, or stick around for the next update"
        )
        continue
    elif command == "der":
        print(
            "This command is under development, please update, or stick around for the next update"
        )
        continue
    else:
        print(f"{command} is not a valid command")

import subprocess

# Example 1: Run a simple shell command
result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE, text=True)
print(result.stdout)

# Example 2: Run a command with arguments
file_path = 'example.txt'
result = subprocess.run(['cat', file_path], stdout=subprocess.PIPE, text=True)
print(result.stdout)

# Example 3: Run a command with user input
user_input = input("Enter a command: ")
result = subprocess.run(user_input, shell=True, stdout=subprocess.PIPE, text=True)
print(result.stdout)
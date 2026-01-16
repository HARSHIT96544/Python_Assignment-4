'''Task-1'''
# Read a file and handle errors

try:
    with open('file_name.txt', 'r') as file:
        for line in file:
            print(line.rstrip())
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
print()

'''Task-2'''
# Write and append data to a file

# Taking user input and writing it to output.txt
user_input1 = input("Enter text to write to the file: ")
with open('output.txt', 'w') as file:
    file.write(user_input1 + '\n')
print("Data successfully written to output.txt.")

# Taking additional input and appending it to the same file
user_input2 = input("Enter additional text to append: ")
with open('output.txt', 'a') as file:
    file.write(user_input2 + '\n')
print("Data successfully appended.")

# Reading and displaying the final content of the file
print("Final content of output.txt:")
with open('output.txt', 'r') as file:
    print(file.read().strip())























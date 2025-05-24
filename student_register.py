# Prompt user to enter number of students
number_of_students = int(input("Enter number of students: "))

# Initialise count
i = 0

# Enter Id for each number of students
for i in range(0, number_of_students):
    idNumber = str(input("Enter ID: "))
# Write the above to the 'reg form' file
    with open("/Users/jessramathibe/downloads/reg_form.txt", "a") as f:
        f.write(idNumber + "..." + "\n")
    i = i + 1
  
# Read the file to ensure the code works
with open("/Users/jessramathibe/downloads/reg_form.txt", "r") as file:
    for line in file:
        print(line)

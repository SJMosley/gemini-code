# from functions.get_files_info import get_files_info
# from functions.get_file_content import get_file_content
from functions.write_file import write_file

#########################
#Get Files Info Tests
#########################
# print("---- test 1 -----------")
# output = get_files_info("calculator", ".")
# print(f"output: \n{output}")

# print("---- test 2 -----------")
# output = get_files_info("calculator", "pkg")
# print(f"output: \n{output}")

# print("---- test 3 -----------")
# output = get_files_info("calculator", "/bin")
# print(f"output: \n{output}")

# print("---- test 4 -----------")
# output = get_files_info("calculator", "../")
# print(f"output: \n{output}")

# print("---- test 5 -----------")
# output = get_files_info("calculator", "../../")
# print(f"output: \n{output}")

# print("---- test 6 -----------")
# output = get_files_info("calculator", "😵‍💫")
# print(f"output: \n{output}")

# print("---- test 7 -----------")
# output = get_files_info("calculator")
# print(f"output: \n{output}")

#########################
#Get File Content Test
#########################
# print("---- test 8 -----------")
# content = get_file_content("calculator", "lorem.txt")
# print(f"content:\n{content}")

# print("---- test 9 -----------")
# content = get_file_content("calculator", "main.py")
# print(f"content:\n{content}")

# print("---- test 10 -----------")
# content = get_file_content("calculator", "pkg/calculator.py")
# print(f"content:\n{content}")

# print("---- test 11 -----------")
# content = get_file_content("calculator", "/bin/cat")
# print(f"content:\n{content}")

#########################
# Write File Tests
#########################
print("---- test 12 -----------")
output = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
print(f"output: \n{output}")

print("---- test 13 -----------")
output = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
print(f"output: \n{output}")

print("---- test 14 -----------")
output = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
print(f"output: \n{output}")

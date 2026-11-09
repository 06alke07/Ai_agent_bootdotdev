from functions.get_file_content import get_file_content

result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")

r1 = get_file_content("calculator", "main.py")
print(r1)

r2 = get_file_content("calculator", "pkg/calculator.py")
print(r2)

r3 = get_file_content("calculator", "/bin/cat")
print(r3)

r4 = get_file_content("calculator", "pkg/does_not_exist.py") 
print(r4)
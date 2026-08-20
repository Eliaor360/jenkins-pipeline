import os
import sys

word = sys.argv[1]
file_path = os.environ["FILE_TO_TEST"]

with open(file_path, "r") as file:
    content = file.read()

if word in content:
    print(f"Found: {word}")
else:
    print(f"Not found: {word}")
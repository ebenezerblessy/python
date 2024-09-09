import os
files = os.listdir()

for file in files:
    full_path = os.path.join(os.getcwd(), file)
    print(full_path)

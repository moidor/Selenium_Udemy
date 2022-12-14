# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# file = open("file.txt")
# count = 0
# for line in file.readlines():
#     count += 1
#     print(f"{count}: {line}")
#
# file.close()

with open("file.txt", "r") as file:
    content = file.readlines()
    reversed(content)
    with open("w_file.txt", "w") as w_file:
        for line in reversed(content):
            w_file.write(line)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

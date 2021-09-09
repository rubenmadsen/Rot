# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    encrypt = True
ROT = -1
#alfa = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
alfa = "abcdefghijklmnopqrstuvwxyz "
mode = ""
while mode != "Encode" and mode != "Decode":
    mode = input("Encode or Decode?\n")
while ROT < 0:
    ROT = int(input("Choose ROT#: \n"))
print(mode + "ing with ROT:" + str(ROT))
message = input("Write your message\n").lower()
def encode(c):
    index = alfa.find(c)
    new_index = index + ROT
    if new_index > len(alfa)-1:
        new_index = (new_index - len(alfa) ) + ROT
    else:
       new_index = index + ROT
    return alfa[new_index]

def decode(c):
    index = alfa.find(c)
    new_index = index + (ROT*-1)
    if new_index < 0:
        new_index = len(alfa)-(index + (ROT*-1))
    else:
       index += (ROT*-1)
    return alfa[index]

newMessage = ""
for x in range(0,len(message)):
    if mode == "Encode":
        newMessage += encode(message[x])
    elif mode == "Decode":
        newMessage += decode(message[x])

#print(message)
print(newMessage)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


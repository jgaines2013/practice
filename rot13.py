def rot13(message):
    # did a problem using ascii seems to be a good approach here
    newMessage = ""
    for i in message:
        j = ascii(i)
        if ord(i) in range(97, 123):
            if ord(i) + 13 > 122:
                # print(" in lower change is", ord(i) - 26 +13)
                newChar = ord(i) - 26 + 13
                newMessage += chr(newChar)
            else:
                newMessage += chr(ord(i) + 13)
        elif ord(i) in range(65, 91):
            if ord(i) + 13 > 90:
                # print("in capitals ", ord(i) - 26 +13)
                newChar = ord(i) - 26 + 13
                newMessage += chr(newChar)
            else:
                newMessage += chr(ord(i) + 13)
        else:
            # print("auto")
            newMessage += i
    print(newMessage)

    return newMessage
    pass

# lot of extra time spent on here
# 1st issue was attempting to -ordmaxrange instead of alphabet length i.e. ord(i) - 122 +13
# 2nd did not have an elif statement tried diff syntax but never looked up correct one
# then got confused why it it was printing extra characters
# could have used a %26  to keep numbers in proper range
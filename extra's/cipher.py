
alfabet = ['a','b','c','d','e','f','g','h','i','j','k',
           'l','m','n','o','p','q','r','s','t','u','v',
           'w','x','y','z']

sp = ['@','#','$','%','^','&','*','(',')','_','-','=','+']

def ciphers(texts, process , shift):
    result = ""
    cd = 0
    if process == 'decrypt':
        shift *= -1
    for char in texts:
            if process == 'decrypt':
                if char in sp:
                    result += ' '
                else:
                    index = alfabet.index(char)
                    result += alfabet[index + shift]
            elif process == 'encrypt':
                if char == ' ':
                    result += sp[cd]
                    cd += 1
                else:
                    ind = alfabet.index(char)
                    if ind + shift < len(alfabet):
                        result += alfabet[ind + shift]
                    else:
                        result += alfabet[shift - (len(alfabet) - ind)]
    return print(result)

cipher = True
while cipher:
    process = input("write encrypt for encryption and decrypt for decryption ")
    shift = int(input("enter the shift value for encryption "))
    texts = input("enter the sentence for encryption ")
    ciphers(texts, process, shift)
    checker = input("press 'no' for  exit this code and yes for continue : ")
    if checker == 'no':
        print("exit this code")
        break



###########################################first attempt##########################################################################
# def encrypt():
#     text = input("enter the sentence for encryption ")
#     shift = int(input("enter the shift value for encryption"))
#     co = 0
#     result = ""
#     for char in text:
#         print(char)
#         if char == ' ':
#             result += sp[co]
#             co += 1
#         else:
#             index = alfabet.index(char)
#             if index + shift < len(alfabet):
#                 result += alfabet[index + shift]
#             else:
#                 result += alfabet[shift - (len(alfabet) - index)]
#     print(result)

# def decrypt():
#     text = input("enter the sentence for decryption ")
#     shift = int(input("enter the shift value for decryption"))
#     result = ""
#     for char in text:
#         print(char)
#         if char in sp:
#             result += ' '
#         else:
#             index = alfabet.index(char)
#             if index - shift < 0:
#                 dc = index - shift
#                 result += alfabet[dc]
#             else:
#                 result += alfabet[index - shift]
#     print(result)


#ryj@kjo#jyj







# -*- coding: utf-8 -*-




def encryption(plain_text, n):
    cipher_text = "".join([chr(ord(x)+n) for x in list(plain_text)])
    return cipher_text

def decryptViolence(cipher_text):
    for i in range(1, 27):
        plain_text = "".join([chr(ord(x)-i) for x in list(cipher_text)])
        print(i, '：', plain_text)

if __name__ == '__main__':
    plain_text = input("请输入明文：")
    n = int(input("请输入加密数："))
    cipher_text = encryption(plain_text, n)
    print("密文：", cipher_text)

    decryptViolence(cipher_text)


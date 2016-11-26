#!/usr/bin/env python3
import os, socket
import hashlib, binascii
from Crypto.Cipher import AES
import base64



salt='fdgdsfsdfksd48u48rh4ethdgdsfasfasddsvfbmfignspwiopetcosdfxz'
key=1
# авторизация пользователя.

def crypto(what,crypt):
        BLOCK_SIZE = 32
        PADDING = '{'
        pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING

        EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
        DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)

        secret = os.urandom(BLOCK_SIZE)

        cipher = AES.new(secret)

        if what == 1:
            # шифруем строку
            encoded = EncodeAES(cipher, crypt)
            true_key = encoded
        else:
            # расшифровываем строку
            decoded = DecodeAES(cipher, crypt)
            true_key = decoded
        return true_key

def get_key(s_key):


            f_key = open('/usr/local/my_vk/vk.conf', 'w')
            put_key = crypto(1, s_key)

            f_key.write(put_key)
            f_key.close()



def start():
    if os.path.exists("/usr/local/my_vk/vk.conf"):
            print('pshel nax')
    else:
        os.mkdir('/usr/local/my_vk/')
        f = open('/usr/local/my_vk/vk.conf','w')
        f.close()
        print('Готово, чувак!')



    key = input("Введите ваш ключ \n"
                    "Очень просто получить ключ, для этого нужно пройти по ссылке: \n"
                    "https://oauth.vk.com/authorize?client_id=5725898&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends,photos,audio,video,docs,notes,pages,status,wall,groups,messages,notifications,offline&response_type=token \n")

    if key != 1:
      get_key(key)




start()

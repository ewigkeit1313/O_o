#!/usr/bin/env python3
import os, socket
import hashlib, binascii
from Crypto.Cipher import AES
import base64
import vk
import subprocess

salt='fdgdsfsdfksd48u48rh4ethdgdsfasfasddsvfbmfignspwiopetcosdfxz'
key=1

# авторизация пользователя.
'''
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
            decoded = DecodeAES(cipher, crypt.encode())
            true_key = decoded
        return true_key
'''

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class life():



    def use_file(self, path, why, what='1'):
        f = open(path)

        if why == 'read':
            return f.read()
        if why == 'write':
            if what != 1:
                return f.write(what)


    def vk_auth(self):

        my_key = life.use_file(self, '/usr/local/my_vk/vk.conf', 'read')

        session = vk.Session(my_key)
        life.api = vk.API(session)
        return life.api

    def vk_wall(self, mess):
        message = input('wall \n')
        # life.vk_wall(self,message)
        life.vk_auth(self).wall.post(message=mess)


    def get_key(self, s_key):

            f_key = open('/usr/local/my_vk/vk.conf', 'w')
                                    #put_key = crypto(1, s_key)
                                    #print(put_key)
                                    #put_key = crypto(0, s_key)
                                    #print(put_key.decode("utf-8"))
            f_key.write(s_key)
            f_key.close()
            print('Ключ в конфиге!')


    def start(self):
        if os.path.exists("/usr/local/my_vk/vk.conf"):
            life.vk_auth(self)


        else:

            os.mkdir('/usr/local/my_vk/')
            f = open('/usr/local/my_vk/vk.conf','w')
            f.close()
            print('Готово, чувак!')

            key = input("Введите ваш ключ \n"
                    "Очень просто получить ключ, для этого нужно пройти по ссылке: \n"
                    "https://oauth.vk.com/authorize?client_id=5725898&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends,photos,audio,video,docs,notes,pages,status,wall,groups,messages,notifications,offline&response_type=token \n")

            if key != 1:
                life.get_key(key)



subprocess.Popen("sleep 10", stdin=True, stdout=True, shell=True)

print('!!!')

#life.start('t')




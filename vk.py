#!/usr/bin/env python3
import os


# авторизация пользователя.

def start():
    if os.path.exists("/usr/local/my_vk/vk.conf"):
            print('pshel nax')
    else:
           os.mkdir('/usr/local/my_vk/')
           f = open('/usr/local/my_vk/vk.conf','w')
           print('Готово, чувак!')





'''
    def get_key(self):
        key = input("Введите ваш ключ \n"
                    "Очень просто получить ключ, для этого нужно пройти по ссылке: \n"
                    "https://oauth.vk.com/authorize?client_id=5725898&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends,photos,audio,video,docs,notes,pages,status,wall,groups,messages,notifications,offline&response_type=token")




    def incode(self, ) :
    #    print("var--->", va)

'''
start()


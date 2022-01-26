import random
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher
import requests


# 此脚本设置每周执行一次
def get_key(key_file):
    with open(key_file) as f:
        data = f.read()
        key = RSA.importKey(data)
    return key


def encrypt_data(msg):
    public_key = get_key('rsa_public_key.pem')
    cipher = PKCS1_cipher.new(public_key)
    encrypt_text = base64.b64encode(cipher.encrypt(bytes(msg.encode("utf8"))))
    return encrypt_text.decode('utf-8')


if __name__ == '__main__':
    server_url = 'https://sctapi.ftqq.com/SCT94144TuDEe5IYr9NNt9vRWbw07TIoV.send'
    randPwd = str(random.randint(100000, 1000000))
    print(randPwd)
    # server酱发送到wechat
    data = {
        'title': '智能快递柜密码已更新!!',
        'desp': '新密码是：' + randPwd
    }
    requests.post(server_url, params=data)
    with open('/root/express_system/password2.txt', 'w+') as f:
        f.write(randPwd)
    encrypt_data(randPwd)
    with open('/root/express_system/password.txt', 'w') as f:
        f.write(encrypt_data(randPwd))

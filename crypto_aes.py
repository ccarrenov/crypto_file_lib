#!/usr/bin/env python
#IMPORT BASE64 LIB FOR ENCODE/DECODE BASE64
import base64
#IMPORT HASHLIB LIB FOR HASHING
import hashlib
#IMPORT CRYPTO LIB FOR CLASS RANDOM CRYPTO
from Crypto import Random
#IMPORT CRYPTO LIB FOR CLASS ENCRYPT/DECRYPT CRYPTO
from Crypto.Cipher import AES
#IMPORT UTILITIES FILE FOR CLASS  FILES
from utilities_file import Files
#IMPORT PATH LIB
from pathlib import Path
#IMPORT OS LIB FOR OPERATION SYSTEM
import os

class AESCipher(object):

    def __init__(self, key): 
        self.bs = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()
        self.filesutilities = Files()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_GCM, iv)
        return base64.b64encode(iv + cipher.encrypt(raw.encode()))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_GCM, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:]))

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    def encrypt_content_file_utf8(self, fullpathfile, fullpathdestinationfile):
        self.encrypt_content_file(fullpathfile, fullpathdestinationfile, 'utf-8')

    def encrypt_content_file(self, fullpathfile, fullpathdestinationfile, encoding):
        lines = self.filesutilities.file_to_lines(fullpathfile, encoding)
        newlines = []
        for line in lines:
            lineencrypt = str(self.encrypt(line), encoding)
            newlines.append(lineencrypt)
        self.filesutilities.lines_to_file_utf8(fullpathdestinationfile, newlines)

    def decrypt_content_file_utf8(self, fullpathfile, fullpathdestinationfile):
        self.decrypt_content_file(fullpathfile, fullpathdestinationfile, 'utf-8')

    def decrypt_content_file(self, fullpathfile, fullpathdestinationfile, encoding):
        lines = self.filesutilities.file_to_lines(fullpathfile, encoding)
        newlines = []
        for line in lines:
            decryptlinebyte = self.decrypt(bytes(line, encoding))
            decryptline = str(decryptlinebyte, encoding)
            newlines.append(decryptline.rstrip())
        self.filesutilities.lines_to_file_utf8(fullpathdestinationfile, newlines)        

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]   
     
def test_one(): 
    print('test_one')
    key = 'De934oi3mdsacVdkso247551fdad23f6c2vsdkeFXzx'
    print('key : {0}'.format(key))
    ciph = AESCipher(key)
    text = 'http://www.googel.cl'
    print('text : {0}'.format(text))
    enc = ciph.encrypt(text).decode('utf-8')
    print('encrypt : {0}'.format(enc))
    cipher = AESCipher(key)
    decbytes = cipher.decrypt(enc.encode('utf-8'))
    print('decryptbytes : {0}'.format(decbytes))
    dec = str(decbytes, 'utf-8')
    print('decrypt : {0}'.format(dec))

def test_two():
    print('test_two')
    key = 'De934oi3mdsacVdkso247551fdad23f6c2vsdkeFXzx'
    ciph = AESCipher(key)
    filesutilities = Files()
    rootfolder = Path(os.path.abspath("."))
    originfile = rootfolder.joinpath('example/app.properties')
    encrypfolder = rootfolder.joinpath(rootfolder, 'encrypt')
    encrypfile = rootfolder.joinpath(rootfolder,'encrypt/app.properties')
    print(" rootfolder ->{0}".format(rootfolder))
    print(" originfile ->{0}".format(originfile))
    print(" encrypfolder ->{0}".format(encrypfolder))
    print(" encrypfile ->{0}".format(encrypfile))
    filesutilities.delete_and_create_folder(encrypfolder)
    ciph.encrypt_content_file_utf8(originfile, encrypfile)


def test_three():
    print('test_three')
    key = 'De934oi3mdsacVdkso247551fdad23f6c2vsdkeFXzx'
    ciph = AESCipher(key)
    filesutilities = Files()
    rootfolder = Path(os.path.abspath("."))
    encrypfile = rootfolder.joinpath(rootfolder,'encrypt/app.properties')    
    decryptfolder = rootfolder.joinpath(rootfolder, 'decrypt')
    decryptfile = rootfolder.joinpath(rootfolder,'decrypt/app.properties')
    print(" originfile ->{0}".format(encrypfile))
    print(" decryptfolder ->{0}".format(decryptfolder))
    print(" decryptfile ->{0}".format(decryptfile))
    filesutilities.delete_and_create_folder(decryptfolder)        
    ciph.decrypt_content_file_utf8(encrypfile, decryptfile)

test_one()
test_two()
test_three()
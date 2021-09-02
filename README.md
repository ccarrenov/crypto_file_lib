# CRYPTO CONTENT FILE


### CREATE VIRTUAL ENV IN ROOT FOLDER
virtualenv env

### LOAD ACTIVATE VIRTUAL ENV

source env/bin/activate

### LOAD DEPENDENCY LIB

python -m pip install -r requirements.txt

### EXECUTE EXAMPLE LIB
python crypto_aes.py

### RESULT

```
test_one
key : De934oi3mdsacVdkso247551fdad23f6c2vsdkeFXzx
text : http://www.googel.cl
encrypt : ZhlYP8sbh7TaKgBnF1PhSwq7XJ3F9pvz/QWdHi9Fe5UJUOjjQK492LYR8ru0J9bl
decryptbytes : b'http://www.googel.cl'
decrypt : http://www.googel.cl
test_two
 rootfolder ->/home/ccarrenov/Documents/PROPIAS/crypto_file_lib
 originfile ->/home/ccarrenov/Documents/PROPIAS/crypto_file_lib/example/app.properties
 encrypfolder ->/home/ccarrenov/Documents/PROPIAS/crypto_file_lib/encrypt
 encrypfile ->/home/ccarrenov/Documents/PROPIAS/crypto_file_lib/encrypt/app.properties
test_three
 originfile ->/home/ccarrenov/Documents/PROPIAS/crypto_file_lib/encrypt/app.properties
 decryptfolder ->/home/ccarrenov/Documents/PROPIAS/crypto_file_lib/decrypt
 decryptfile ->/home/ccarrenov/Documents/PROPIAS/crypto_file_lib/decrypt/app.properties
 ```

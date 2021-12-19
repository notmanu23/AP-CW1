## This is a simple tool made using python, the pysqlitecipher libraries and sqllite.

### How the encryption is done -

Firstly Your password is converted to SHA256 , SHA512 , MD5.
Then a random key is generated using cryptography fernet algo which is then encrypted using onetimepad using SHA256 as a key.
Then this encrypted key is stored in data base. when you login next time then this encrypted key is decrypted back and used to create a instance of cryptography fernet tech.
SHA512 is stored directly into database to verify the password for the next input.
When you insert data into table , it is first encrypted by cryptography fernet tech and then shuffled with seed value = MD5 and vice versa for decryption.

### How to run -

#### if you have already unzipped the file run, 

    pip install -r requirement.txt
 
#### that's pretty much it. then run,

    python main.py 

#### or...

    python3 main.py



Made by : 
    Group 6.





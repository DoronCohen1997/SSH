import paramiko

def printDirsNamesAlphabetical():

    key = paramiko.RSAKey.from_private_key_file("C:/Users/Dafna Cohen/PycharmProjects/doron/rsa_private_key.pem")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print("Connecting")
    client.connect(hostname="ec2-52-59-204-217.eu-central-1.compute.amazonaws.com", username="ubuntu", pkey=key)
    print("Connected")
    stdin, stdout, stderr = client.exec_command("find . -type f -print0 | sort -z | xargs -r0 sha256sum > dirsNames.txt \n cat dirsNames.txt")
    move = str(stdout.read())
    print(move)
    f = open ("dirsNames.txt", "+w")
    f.write(move)
    f.close()

    # with open(move, "r") as logger_file:
    #     print(logger_file.read())



    # cat secretFile.txt | grep "is""\home\ ubuntu \n
    client.close()



printDirsNamesAlphabetical()
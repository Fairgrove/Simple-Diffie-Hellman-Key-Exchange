class person:
    sharedKey = 0
    def __init__(self, privateKey, generator, primeModulus):
        self.privateKey = privateKey
        self.publicKey = generator**privateKey % primeModulus # generator^privateKey mod primeModulus
    
class communication:
    def __init__(self, generator, primeModulus):
        self.generator = generator
        self. primeModulus = primeModulus

def genSharedKey (primeModulus, publicSender, privateKey):
    return publicSender**privateKey % primeModulus

def startMsg():
    print("Hey! \nThis is a simple demonstration of the Diffie-Hellman Key Exchange method")
    print("This method of securing communication uses a 'easy to cipher, hard to decipher' principle, by using maths!\nThe math behind it is the following:")
    print("First a public generator and prime modulus is decided for communication\nthen, each party chooses a private key which is used to generates a public key, using the generator and prime modulus... like so:")
    print("\n   publicKey = generator ^ (privateKey) mod primeModulus\n")
    print("Each part uses the others public key and their own private key, to generate a shared secret key that they will use to validate that the other party is the one they claim\nThis is how that calculation looks:")
    print("\n   sharedKey = partnerKey ^ (privateKey) mod primeModulus\n")
    print("this is the genious part of this method... both parties get the same number from that calculation AND a thrid party cannot generate this number, unless they have one of the private keys or they brute force it for a few years")
    print("This shared key can also potentially be used to decrypt the messages they are sending to each other!\nN.B Don't be afraid of using big numbers :D")
    print ("\n - by Frederik Fagerlund")
    input("PRESS ANY KEY TO START!\n")

startMsg()
input1 = int(input("choose a generator: "))
input2 = int(input("choose a prime modulus: "))
input3 = int(input("choose a private key for p1: "))
input4 = int(input("choose a private key for p2: "))

com = communication(input1, input2)
p1 = person(input3, com.generator, com.primeModulus)
p2 = person(input4, com.generator, com.primeModulus)

print("Generating shared key")
p1.sharedKey = genSharedKey(com.primeModulus, p2.publicKey, p1.privateKey)
p2.sharedKey = genSharedKey(com.primeModulus, p1.publicKey, p2.privateKey)

print("p1 public key: ", p1.publicKey, "   p1 private key: ", p1.privateKey)
print("p2 public key: ", p2.publicKey, "   p2 private key: ", p2.privateKey)
print()
print("p1 generated shared key: ", p1.sharedKey)
print("p2 generated shared key: ", p2.sharedKey)



#print(p1.privateKey, "   ", p1.publicKey)
#print(sharedA, "     ", sharedB)
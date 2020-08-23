# Simple-Diffie-Hellman-Key-Exchange
Hey! \
This is a simple demonstration of the Diffie-Hellman Key Exchange method. This method of securing communication uses a 'easy to cipher, hard to decipher' principle, by using maths! \
The math behind it is the following:

First a public generator and prime modulus is decided for communication.
Then, each party each chooses an unique private key (usually a random number) which is used to generate a public key, using the generator and prime modulus... \
Like so:

```publicKey = generator ^ (privateKey) mod primeModulus```

Each party uses the others public key and their own private key, to generate a shared secret key that they will use to validate that the other party is the one they claim \
This is how that calculation looks:

```sharedKey = partnerKey ^ (privateKey) mod primeModulus```

This is the genious part of this method... both parties get the same number from that calculation AND a thrid party cannot generate this number, unless they have one of the private keys or they brute force it for a few years.

This shared key can also potentially be used to encrypt / decrypt the messages they are sending to each other! 

N.B. Don't be afraid of using big numbers

- by Frederik Fagerlund   

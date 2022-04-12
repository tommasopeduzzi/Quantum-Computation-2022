## Extra Lecture - Quantum Cryptography

There's two parties A & B that want to share a message and a third party that shouldnt be able to understand a intercepted message. 
One method is to XOR with a random key known to both parties. Doing a XOR on that result with the key returns it back to the original message. As this is virtually impossible to crack the encryped message without the key, the big practical difficulty is to share the key in a secure way. This is where the quantum advantage comes in.
To encode the key we have a list of bases with the length of the key. Then the first party encodes the key by putting a qubit into the state according to the bit at that position in the key in the corresponding base. The second party can then also make a completely random list of bases and measures the qubits in the corresponding base. 
Then the bases are shared and this generates "common randomness".
If a third party were to intercept the message would be corruped, as the superpositions would be destroyed, as the common bases are known.

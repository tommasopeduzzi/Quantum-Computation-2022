# Week 10
## Why do we need QEC?
Because qubits (for any implementation) and gates, which are two-level quantum systems and Hamiltonians applied to those systems, don't work perfectly (e.g. each gate is slightly wrong, noise, incorrect measurements, effects that are not accounted for in the simple theory of two level systems etc.), we have to correct for those shortcomings. 
If we rely on one physical qubit to represent one qubit in our circuit we get garbage, because when we write algorithms, we think of the qubits like being ideal. Instead we get imperfect *physical* qubits, when we would like to have perfect *logical* qubits. 

## Pauli errors
To do exactly this correction we use the fact that any matrix $U$ can be decomposed into the Pauli bases: $U = \alpha I + \beta X + \gamma Y + \delta Z$. Therefore any error (which is basically a unitary applied at a random point in the circuit) can be decomposed to some Pauli being applied to the qubits. This can be done even easier, because $Y\sim XZ$ and therefore we just have to account for $X$ and $Z$ errors.
When a $X$-error happens we call it a bitflip-error, because$X\Ket{0} = \Ket{1}$ and $X \Ket{1} = \Ket{0}$. Similarly we call Z-errors phase flips errors, because $Z \Ket{+} = \Ket{-}$ and $Z \Ket{-} = \Ket{+}$. The goal is to know where these bit- or phase-flips happen, correct for them. 

## Combining physical qubits to make logical qubits
In quantum error correction (QEC) many physical qubits are used to represent one logical qubit. As this is still a long-term goal and difficult to achieve, we try to mitigate the errors at the moment. We can expect there to be a transition from these mitigation methods to full quantum error correction.
For example if we have a $d= 5$ surface code for one logical qubit, we need 17 physical qubits. 

## Classical error correction
Assuming one has to send a single bit of information over a noisy lines, there are two important probabilities when talking about the probability that the message arrives at the destination. $p$ is the probability that a $1$ is interpreted as a $0$ and that a $0$ is interpreted as a $1$. $P_\alpha$ is the maximum acceptable fault probability. 
If we want to make sure that the message arrives well, we could *encode* the message by repeating the bit of information and choose the option with the majority. The probability of error $P$ decays exponentially with the number of repetions $d$, meaning that we can make $P$ as small as needed just by doing enough repetitions $d$.
Thus we have taken our small message and encoded it into a larger, but more fault-tolerant, message and then decoded it at the destination by taking the majority. This is called the Repetition code.
Error correction can be thought of as having 4 stages:
- Input: Some information to protect
- Encoding: Transform the input information to make it easier to protect.
- Errors: Random changes of the encoded information with probability $P$.
- Decoding: Deduce the information from the corrupted encoding.
In computation, this is not only done once like in communication but over the course of the computation as new errors are introduced. We can do this by constantly encoding, correcting and re-decoding the information. 

## Quantum error correction
In the quantum world, we can't just encode and decode superpositions willy-nilly, as this would destroy the superpositions by doing measurement when decoding.
Instead of measuring the whole system, we measure only as much as we need to detect where errors occured. We do this by checking if the two bits are the same for every pair of physical qubits representing one logical qubit. If they are different, we know that a error happened there and we can correct for it by looking at the majority. This allows us to check where errors occured without actually knowing anything about the information and therefore not destroy the superposition.
In practicality this can be done by adding some an extra qubit for each pair of qubits in the repetition and doing CNOTS with the two qubits in the pair, like this:
![[Repetition code circuit.png]]
The result of the measurement of this auxillary qubit tells us if the qubits are the same (measurement result of $0$) or different (measurement result of $1$) and allow us to act on the errors we detect using this method.
Doing this multiple times over the course of the circuits handles bitflips and corrects them. 
This process of decoding by getting some information on where an error occured is called a syndrome measurement. Sydrome measurements are present in all QEC-codes.

36:08
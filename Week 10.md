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

## Decoding stage in detail
If we don't take into account that errors can occur during the syndrome measurements and we focus on identifying where the errors happen instead of correcting them, we can do a simple model: Instead of looking at every discrepancy at every stage, we look at the differences between the syndrome measurements. This allows us to see where the errors happen, because every error creates a pair of differences from the previous stage:
![[Simple Decoding.png]]
In more complicated settings, we can use majority voting to determine what we have to correct. We split the bitstring along the domain of the errors and correct the one with less occurences (because the probability of an error occuring $P < 0.5$ for Repetition codes). 

When we account for errors being able to occur during syndrome measurements, we can see that errors can also occur vertically, as we flag the differences:
![[Advanced Decoding.png]]
As this information is more conviluted, we have to have more sophisticated methods to interpret it, as majority voting isn't enough. There are many ways to do this, but one of the simplest is by using graph theory:
Using the hints we get from measurements, we can create a graph between the hints, by drawing edges between them and weighing between by the amount of errors between them. We can also change these weights to account for the actual probability of the errors occuring.
![[Graph.png]]
Then we can find the minimal weight matching using a classical algorithm (*Blossom* Algorithm). This gives us the pairs of hints with the minimal amount of errors between them, allowing us to correct them.

## Logical Operations
Performing simpe operations, like $X$s, is really easy: We can just apply an X on every repetition physical qubit of that logical qubit. This is easy to do and corrects the imperfections while it's doing it.
When doing an operation like $Rx (2\theta) = \cos \theta \Ket{0} + \sin\theta \Ket{1}$ on a logical qubit requires us to encode the logical state into physical repetitions $\cos\theta\Ket{000}+\sin\theta\Ket{111}$. To do this wee need to unencode the state, which leaves it unprotected while performing the operation. Therefore fault-tolerant universal quantum computing is not possible using only repetition codes.
Even though we can't create a repetition code that corrects both a bit and phase flips, we can easily create a circuit that only protects against bit or phase flips. This will become relevant later.
If we want an ideal QEC-code we have to overcome a couple of hurdles. Firstly, Z basis states are a lot easier, as they are just product states, while the others are entangled states. Also differenciating between Z-basis states is way easier than betwen X-basis states. Another fundamental problem is that doing a bitflip over $n$ qubits requires $n$ operations, while doing a phase flip requires only a single operation, thus errors are harder to track.

## Implement QEC codes in qiskit
In qiskit, we can use the *Ignis* (deprecated by now) package that takes care of the bulk of the work to implement different QEC codes, such as repetition codes. 
We also get the ability of specifying what physical qubits our circuit should run on. This allows us to avoid complicated errors that occur when the transpiler tries to make the circuit work on a real device.

## Using repetition codes for benchmarking
Because repetition codes use the base properties needed for universal QEC, suhc as encoding bit values, performing stabilizer measurements and decoding the encoded qubits, we can use them for benchmarking. Because repetition codes are very easy to implement and have low requirements (only 5 qubits needed, not a lot of connectivity), this can be done quite simply. 
By being able to finely control what actually goes on inside the QC, we can get important insights into how they actually work.

## Shor's code 
In shors code, we use physical qubits to encode a logical qubit that is then used as an encoding for an even more fault-tolerant logical qubit and so on. 
![[Shors code.png]]
By then using both the phase and bit flip error codes at different stages, we can protect against both kinds of errors.
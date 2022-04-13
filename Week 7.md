# Week 7
**Quantifying Computational Work**
To quantify how much work a computer is doing, we use a notiaton called the Big-O-Notation. This doesn't take in account the unit we measure work in, as the scaling is independant of the unit of measurement. For example the classic algorithm of adding numbers column by column is $O(n)$, where $n$ is the number of digits, so it scales linearly.
More formally a function $f(n) \in O(g(n))$ if $|f(n)| \leq C |g(n)|$, where $n > n_0$. We often write $f(n) = O(g(n))$, even though it isn' formally correct.
Often if we have an algorithm that scales less dramatically than a counterpart, there are tradebacks, that have to be taken into account. This is also the case for quantum computers, as sometimes they are more resource-intensive, even though, they implement "better" algorithms.

**Applying a bunch of Hadamards**
As $H \Ket{0} = \frac{1}{\sqrt2}(\Ket{0} +\Ket{1})$, applying n Hadmards to a set of n qubits in the zero states looks like this: $H^{\otimes n}\Ket{0}^{\otimes n} = \frac{\sum\limits_x \Ket{x}}{2^\frac{n}{2}}$. This is a normalized superposition over all possible states, of which there are $2^n$. 
When applying a Hadamard to a general bit $s_j$ we can say that it's sum over all possible states of that bit $x_j$ (in this case 
 the possible states are $\{0,1\}$) with a possible phase of $-1$ when applying it to a $1 = s_j$ and when it the output is a one $x_j = 1$, because $H \Ket{1} = \frac{1}{\sqrt2}(\Ket{0}-\Ket{1})$: $H \Ket{s_j} = \frac{1}{\sqrt2}\sum\limits_{x_j} (-1)^{s_j\cdot x_j} \Ket{x_j}$ .
 So when applying $n$ Hadamards to a bitstring of length $n$ we get back a superposition of all possible states with some phases... : $H^{\otimes n}\Ket{0}^{\otimes n} = \frac{1}{2^\frac{n}{2}} \sum\limits_x (-1)^{s\cdot x} \Ket{x}$, where $s\cdot x = \sum\limits_j s_jx_j$. 
**Deutsch-Josza-Algorithm**
We have a function $f(x)$ that takes in a n-bit string and where $f(x) = 0$ or $f(x)=1$ for all x. The function is either constant (where $f(x) = b$ for all $x$) or balanced (where half of the inputs are $0$ and the other half are $1$) and the task is to find out which one of these cases it is. 
Classically in the worst case it is $O(2^{n-1})$ as we have to check at least half of the possible inputs to determine with absolute certainty if the function is constant or ballanced.
The algorithm in the quantum case starts out by applying n Hadamards and then the phase oracle for that function to n qubits in the $\Ket{0}$ state: $U_f H^{\otimes n}\Ket{0}^{\otimes n} =\frac{1}{2^\frac{n}{2}} \sum\limits_x (-1)^{f(x)} \Ket{x}$, where the phase is $(-1)^{f(x)}$, because it is determined by the function.  
If $f(x)$ is constant, the phase becomes a global phase, because all the phases in the same are the same, so it can be ignored. So in the case that $f(x)$ is constant we can say that: $U_f H^{\otimes n}\Ket{0}^{\otimes n} \equiv H^{\otimes n}\Ket{0}^{\otimes n}$. At the end of the algorithm we again apply n Hadamards, which, because of the relation above, gives us back the state we started out with: $H^{\otimes n} H^{\otimes n}\Ket{0}^{\otimes n} = \Ket{0}^{\otimes n}$. Therfore the probability of measuring all $0$ is 1: $P_{0...00} = 1$
In the case that the function is balanced, half of the outputs of the function are 0 and the other half are 1. So after applying the phase oracle ($U_f H^{\otimes n}\Ket{0}^{\otimes n} =\frac{1}{2^\frac{n}{2}} \sum\limits_x (-1)^{f(x)} \Ket{x}$, where the phase is $(-1)^{f(x)}$) we end up with a state where half of the phases are $-1$ and the other half are $1$, because half of the outputs of $f(x)$ are $1$ and the other half are $0$. After then applying the last Hadamards we end up with a state orthogonal to the one we started out with, which was $\Ket{0}^{\otimes n}$, so the probability of measuring all $0$  is 0: $P_{0...00} = 0$.
These two end-results allow us to distinct from the two different types of function with just one call to that function, therefore netting us an exponential speed-up.

**Bernstein-Vazirani-Algorithm**
We have a function $f(x) = s\cdot x \mod 2 = s\cdot x = \left(\sum\limits_j s_jx_j\right) \mod2$, where $s\cdot x = \sum\limits_j s_jx_j$  has already been defined above and $s,x$ are both bitstrings of length $n$ and $s$ is constant. We are tasked to deduce the bitstring $s$ based on the inputs and outputs of this function.
Classically we would have to do $n$ calls to the function, by passing in a bitstring with the bit of the current position set to $1$ and all the rest $n-1$ bits set to $0$. This allows us to find the bitstrig $s$ bit by bit, so the runtime of this classical algorithm is $O(n)$.
For the quantum algorithm, we do the same as above, by applying $n$ Hadmards and then the phase oracle of the function: $U_f H^{\otimes n}\Ket{0}^{\otimes n} =\frac{1}{2^\frac{n}{2}} \sum\limits_x (-1)^{f(x)} \Ket{x}$. Because of how the function is defined, we can say that $U_f H^{\otimes n}\Ket{0}^{\otimes n} =\frac{1}{2^\frac{n}{2}} \sum\limits_x (-1)^{f(x)} \Ket{x} \equiv  H^{\otimes n}\Ket{s}$. When we then apply the anther n Hadamards, we get to the state $\Ket{s} = H^{\otimes n}U_f H^{\otimes n}\Ket{0}^{\otimes n} = H^{\otimes n}H^{\otimes n}\Ket{s}$.

**Bell basis**
We define these orthogonal states:
$\Ket{\phi^+} = \frac{1}{\sqrt2}(\Ket{00} + \Ket{11})$
$\Ket{\phi^-} = \frac{1}{\sqrt2}(\Ket{00} - \Ket{11})$
$\Ket{\psi^+} = \frac{1}{\sqrt2}(\Ket{01} + \Ket{10})$
$\Ket{\psi^-} = \frac{1}{\sqrt2}(\Ket{01} - \Ket{10})$
Because they are orthogonal, any state of two qubits can be expressed as a superposition of these states. 
These states can be obtained from eachother, by applying local unitaries to another state. Local unitaries are unitaries that only act on one qubit:
For example: $\Ket{\phi⁻} = Z \otimes I \Ket{\phi ^+} = I \otimes Z \Ket{\phi ^+}$ 
We can measure these states by entangling them and performing a Z-measurement.

**Quantum Communication - Superdense Coding**
Let's assume we have two bits of data we want transmit. We could just send two qubits that are prepared in a superposition encoding the information and have the other party measure it. This would work, but we can take advantage of entanglement, and apply this circuit to our two bits:
![[Pasted image 20220413181048.png]]
This creates entanglement between the two bits:
 ![[Pasted image 20220413181214.png]]
 Then we can apply the inverse of this circuit, we just get back the original states:
 ![[Pasted image 20220413181454.png]]
The interesting thing here is, that because they are entangled, the first party (often called Alice) can prepare a Bell state and send one qubit to the second party (often called Bob), before even knowing what she wants to send. When she knows the message, she can apply a local unitary that only affects her qubit, to change it the entangled state into the state encoding the message, without having to touch the qubit she has already sent off to Bob. Effectively she only has to send one qubit at the point she sends the message, with one entangled qubit already sent to Bob.

**Teleportation**
Teleportation is a protocol to transfer an unkown quantum state $\Ket{\sigma}$ in form of a qubit from one party (Alice) to another party (Bob), so that the second party has that state, while the first one doesn't. 
To start of, there is a state $\Ket{\sigma} \otimes \Ket{\phi⁺}$, where the qubit representing state $\Ket{\sigma}$ and the first qubit of the entangled pair and are in the hands of Alice and the second qubit of the entangled pair is in Bob's hands.
Alice can now apply a CNOT to her two qubits and a Hadamard to her qubit $\Ket{\sigma}$ and measure her two qubits, and in the case that she gets $\Ket{\phi⁺}$, Bob's qubit is now in state $\Ket{\sigma}$. In the other cases, Bob knows what gate to apply to that his qubit, to transform from that state to the original state (in our case $\Ket{\phi⁺}$). 
Mathematically this can be explained as the following:
THey start out with the following state, where $\Ket{\sigma} = \alpha \Ket{0} + \beta \Ket{1}$:$$\Ket{\sigma}\otimes \Ket{\phi⁺} = \frac{1}{\sqrt2}(\alpha \Ket{0} \otimes (\Ket{00} + \Ket{11}) + \beta(\Ket{00} + \Ket{11})) = \frac{1}{\sqrt2}(\alpha \Ket{000} + \alpha \Ket{011}  + \beta \Ket{100} + \beta \Ket{111})$$
After applying the CNOT and then the Hadamard we get: $$(H \otimes I \otimes I)(C_X \otimes I)(\Ket{\sigma} \otimes \Ket{\phi⁺}) = \frac{1}{2}(\alpha(\Ket{000}+ \Ket{011}+\Ket{100}+\Ket{111}) + \beta(\Ket{010}+\Ket{001}-\Ket{110}-\Ket{101}))$$By separating out some terms we get:
$$(H \otimes I \otimes I)(C_X \otimes I)(\Ket{\sigma} \otimes \Ket{\phi⁺}) = \frac{1}{2}(\Ket{00}(\alpha \Ket{0} + \beta \Ket{1} + \Ket{01}(\alpha \Ket{1} + \beta \Ket{0})+ \Ket{10}(\alpha \Ket{0} - \beta \Ket{1}) + \Ket{11}((\alpha \Ket{1} - \beta \Ket{0})))$$
We can now see, that depending on what the first two qubits get measured out as, we get a state that can then be made into our original $\Ket{\sigma}$ state using only one pauli, which get decided by that measurement.
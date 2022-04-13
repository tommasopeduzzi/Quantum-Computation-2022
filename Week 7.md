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

**Bell states**
We define these states:
$\Ket{\phi^+} = \frac{1}{\sqrt2}(\Ket{00} + \Ket{11})$
$\Ket{\phi^-} = \frac{1}{\sqrt2}(\Ket{00} - \Ket{11})$
$\Ket{\psi^+} = \frac{1}{\sqrt2}(\Ket{01} + \Ket{10})$
$\Ket{\psi^-} = \frac{1}{\sqrt2}(\Ket{01} - \Ket{10})$
These states can be obtained from eachother, by applying local unitaries to another state. Local unitaries are unitaries that only act on one qubit:
For example: $\Ket{\phi⁻} = Z \otimes I \Ket{\phi ^+} = I \otimes Z \Ket{\phi ^+}$ 

**Quantum Communication**
Let's assume we have two bits of data we want transmit. We could just send two qubits that are prepared in a superposition encoding the information and have the other party measure it. This would work, but we can take advantage of entanglement, and apply this circuit to our two bits:
![[Pasted image 20220413181048.png]]
This creates entanglement between the two bits:
 ![[Pasted image 20220413181214.png]]
 Then we can apply the inverse of this circuit, we just get back the original states:
 ![[Pasted image 20220413181454.png]]
The interesting thing here is, that because they are entangled, the first party (often called Alice) can prepare a Bell state and send one qubit to the second party (often called Bob), before even knowing what she wants to send. When she knows the message, she can apply a local unitary that only affects her qubit, to change it the entangled state into the state encoding the message, without having to touch the qubit she has already sent off to Bob. Effectively she only has to send one qubit at the point she sends the message, with one entangled qubit already sent to Bob.

**Teleportation**

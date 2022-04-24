# Week 9
## Grover's Algorithm
Grover's algorithm is an algorithm for search.  
Classically, searching through an ordered list has the complexity $O(\log_2N)$ (binary search) and searching through an unordered list has an average runtime of $\frac N2$ and such is $O(N)$, where $N$ is the number of items. There is a exponential difference between the two.

The same thing can be said about finding a bitstring of $N$ bits that satisifies some boolean condition. If we know the condition, we can deduce such a string from the structure of the condition and we have a efficiency of $O(N)$. If we don't know, we have to try (in the worst case) every bitstring and thus have the efficiency of $O(2^N)$.

For the quantum algorithm, we have bitstrings of length $N$ and we have a state encoded with N qubits, for example $$\Ket{w} = \Ket{01010101010101}$$ (that we call the winning state), that is the state that we ultimately want to end up with. This could be an entry in phone book or a some general bitstring (or anything else).
We also have a starting state $\Ket{s}$, which must not be orthogonal to the winning state. Generally as we don't know the winning state (yet), we can say that the starting state $\Ket{s}$, because we know that the winning state is in there somewhere and therefore the superposition is not orthogonal, is a superpositions over all bitstrings of length N: $$\Ket{s} = \frac{1}{\sqrt{N}}\sum\limits_b \Ket{b} = \Ket{+}^{\otimes n}$$
Another state that is useful is $\Ket{s'}$, that is the state over all superpositions of N qubits, excluding the winning state: $$\Ket{s'} = \frac{1}{\sqrt{N-1}}\sum\limits_{b \neq w} \Ket{b}$$. We cannot prepare the state, as we don't know it, but we can deduce from the construction that it is orthogonal to the winning state: $$\Braket{w|s'} = 0$$
We can now define two phase oracles:
The first is $U_f$: It applies a phase of $-1$ to the winning states and acts trivially on all other states: $$U_f = -\Ket{w}\Bra{w} + \sum\limits_{b \neq w} \Ket b \Bra{b}$$The second one is $U_s$. it applies a state of $-1$ to all states that are not s ($I - \Ket s \Bra{s}$) and acts trivially on s: $$U_s = \Ket{s}\Bra{s} - (I - \Ket s \Bra{s})$$
Because of the orthogonality of $\Ket{s'}$ and $\Ket{w}$, we can use these as basis states to describe $\Ket{s}$ with some amplitudes: $$\Ket{s} = \cos(\theta_0) \Ket{s'} + \sin(\theta_0)\Ket{w}$$Because of the normalization of $\Ket{s'}$ and $\Ket{w}$, we can deduce $\theta_0$, because $\cos(\theta_0) =\frac{\sqrt{N-1}}{\sqrt{N}}$ and $\sin(\theta_0) =\frac{1}{\sqrt{N}}$. Assuming $N$ is large, we can assume that $\theta_0 \approx \frac{1}{\sqrt N}$ .

We can now draw this graph that represents the $\Ket{s}$ state:
![[Grover 1.png]]

By applying $U_f$, which negates the $\Ket{w}$ component of the superposition, we get:
![[Grover 2.png]]

By then applying $U_s$, that negates everything that is not the $\Ket{s}$ state (effectively flipping it around $\Ket{s}$), we get:
![[Grover 3.png]]

The new angle we get (after one repetition that's $\theta_1$), we get $\theta_1 = 3\theta_1$. More generally we can say, that after t repetitions $(U_sU_f)^t$ we get an angle of $\theta_t = (2t + 1)\theta_0$. To achieve our end goal, which is to have the state $\Ket{w}$ we have to do $t$ repetitions, which is in the order $O(\sqrt N)$. 
Thus we have a polynomial improvement.
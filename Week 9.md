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

## Problems about running these kinds of algorithms on quantum computers
There are three main factors that decide if/when we can run complex algorithms:
The first one is number of qubits. In many of the algorithms we assume to have a certain number of qubits, which we need to run that algorithm. For example for Shor's algorithm for factoring a $64$ bit number, we need $64$ qubits. the problem with building a ton of qubits, is that they become very noisy. More about this later.
The second one is connectivity. In a practical quantum computer, there's only a limited set of qubits that can be used to perform non-local gates (like the CNOT, Toffoli etc.) on. To compensate in practice the often lacking connectivity, you have to use a lot more gates, which leads to even more noise.
The third (and arguably the biggest one) is noise. Noise is describing any factors that cause things in circuits we don't want. These can be external factors or interactions between different gates/measurements etc. 
We need to find ways to minimize this noise, but that won't be enough as the systems become more complex. We also need to develop methods to combat the errors produced by the noise and minimize their effect on the end result. These methods are the focus of quantum error correction.

## Simple ways to model noise
### Density Matrix
Normally we use statevectors to describe quantum states in quantum computers. But there are situations where we can't use normalized statevectors, like we're used to. For example, if we get given a state, $$\Ket{\psi} = q_0 \Ket{\psi_0} +  q_1 \Ket{\psi_1}$$ the probability of getting a $0$ $P_0$ is: $$\begin{aligned}
P_0 &= q_0P_0^\Ket{\psi_0} q_1P_0^\Ket{\psi_1}\\
&=q_0 \langle0|\psi_0\times\psi_0|0\rangle +q_1 \langle0|\psi_1\times\psi_1|0\rangle\\&=\Bra 0 (q_0 |\psi_0\times\psi_0| +q_1 |\psi_1\times\psi_1|)\Ket{0} \end{aligned}$$ This object between the $0$ states is called the density matrix: $$\rho = q_0 |\psi_0\times\psi_0| +q_1 |\psi_1\times\psi_1|$$
An example is: $$\begin{aligned}\rho &= \frac{1}{2} I\\ &= \frac{1}{2}|0\times0| + \frac{1}{2}|1\times1|\\ &= \frac{1}{2}|+\times+| + \frac{1}{2}|-\times-|\end{aligned}$$
A property of these density matrix is that it's Hermitian, because the outer products of states with themselves are also hermitian and the probabilities are real and non-negative. Also, because each density matrix can be written like $\rho = \sum\limits_j q_j |\psi_j \times \psi_j|$ in its spectral form with its eigenstates $\psi_j$ and the eigenstates are orthogonal ($\langle \psi_j | \psi_k\rangle = 0$), the trace of a density matrix is $1 = tr(\rho) \sum\limits_j q_j$. Anything that satisfies these conditions is a valid density matrix and therefore a valid representation of a quantum state.

## Density matrices in Noise
When applying a unitary $U$ to a state represented by a density matrix $\rho = | \psi\times\psi|$, we write $$U\rho U^\dagger = U\Ket{\psi}\Bra{\psi}U^\dagger$$
If we have a unitary that applies an $X$ with teh probability $e_x$, a $Y$ with a probability of $e_y$ and a $Z$ with a probability of $e_z$, we write U applied to a density matrix $\rho$ as $$\rho \rightarrow e_x X \rho X + e_yY\rho Y + e_zZ\rho Z + (I - e_x - e_y - e_z)\rho$$
This kind of probabilistic unitary is what is called a superoperator. We can model the environment and the noise that comes from that as a big superoperator, which helps us understand how mitigate and correct for it.


## Errors in circuits
We can think of errors as occuring with some probability at each step (or gate) in a circuit. We can think of these errors as some $X$, $Y$ or $Z$ error, to simplify things. As the circuits get bigger, the amount of errors introduced grows dramatically. 


## Measurement Error Mitigation
There's also the chance that erros occur while measuring, which would give us incorrect results when measuring the result of a qubit. These errors can be quite easily mitigated.

In this strategy we define a pauli error (like described above) and apply that with a certain probability when measuring. In the textbook we apply an $X$ 1% of the time when measuring.
In the simulation it is equally likely for a $0$ to change to a $1$ and a $1$ into a $0$, but in reality it is far less likely for a $0$ to become a $1$.

We could go through the results and manually find out what makes sense, but that is tedious (and I am lazy). This can be done more sistematically:
We can write a result, such as the result for $10000$ shots of a circuit that should give us $00$, like this $00$: $98.08\%$, $01$: $0.95\%$, $10$: $0.96\%$ and $11$: $0.001\%$, or we can write them in a normalized column vecor: $\begin{pmatrix}0.9808 \\ 0.0095 \\ 0.0096 \\ 0.0001\end{pmatrix}$.
We can then do this for all possible results and write a matrix for each possible result and combining the column vectors into a big matrix: $$M = 
\begin{pmatrix}
    0.9808&0.0107&0.0095&0.0001 \\
    0.0095&0.9788&0.0001&0.0107 \\
    0.0096&0.0002&0.9814&0.0087 \\
    0.0001&0.0103&0.0090&0.9805
\end{pmatrix}$$
Because $M C_{ideal} = C_{noisy}$, where $C_{noisy}$ and $C_{ideal}$ are the ideal and noisy results respectively. This can then be formed to $C_{ideal} = M^{-1}C_{noisy}$. So under the condition that we can take the inverse, we can transform noisy results into ideal ones by analysing the results of the noisy circuits.

Doing this for a larger amount of qubits is really infeasable, you might as well simulate the quantum computer. There are some generalizations, that can be done to make this more efficient.
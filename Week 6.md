# Week 6
**General Computers**
In general a computer takes in an inpout $x$ that can be expressed as a binary string in case of digital computers and computes a function $f(x)$. It's like a black box inbetween the input and the output. Anything that can perform this mapping is considered general.
An easy way to perform these kinds of data is to use a look-up table, where each input maps to an output. For large inputs like images, this is not ideal.

To talk about universality with quantum computers, let's first define some things: A computer has a $n$-bit input and transforms it using a function into a $n$-bit output. Each unique input produces a unique output.

For quantum computers, we use a tensor product of $2n_i$ qubits, where $n_i$ is the number of qubits in the input bitstring. The first $n_i$ qubits are in the same state as the input bitstring, while the rest are 0, so that we can write our output there and we get a unique output:
$\Ket x \otimes \Ket0^{\otimes n_0} \rightarrow \Ket x \otimes \Ket {f(x)}$ 

For a quantum computer we have to create a Unitary, so that $U_f: \Ket x \otimes \Ket0^{\otimes n_0} \rightarrow \Ket x \otimes \Ket{f(x)}$ for any arbitrary $f(x)$, so that we can say, that that quantum computer is universal. The binary aspect of the problem doesn't actually help in this case. More generally, we can say that a quantum computer is universal if we can implement any arbitrary unitary for $n$ qubits.

---
**Proving universality of a gate set**
Last week we took a look at the gate set consisting of the following gates: $R_x(\theta), H, S, s^\dagger = s^3, CX$, where the $R_x(\theta)$ is a Clifford and can be expressed as $R_x(\theta) = e^{i \frac{\theta}{2}X}$, while the others are Non-Cliffords. Using the two-cubit Clifford (in this case $CX$) we can turn this rotation into a multi-qubit rotation. We can get to the point that it can be expressed as $e^{i\frac{\theta}{2}P}$, where $P$ is a general n-qubit Pauli: $P = P_{n-1} \otimes ... \otimes P_0$ and $P_j \in \{ X, Y, Z, I\}$. 
This isn't an arbitrary unitary with though. 
We can express any unitary $U$ with two Paulis as $U =e^{i (\frac{\theta}{2} P + \frac{\theta'}{2}P')}$. Because that matrices don't always commute, we can't write $U \neq e^{i \frac{\theta}{2} P}e^{i \frac{\theta'}{2} P'}$. By saying that $U = {U^{\frac{1}{N}}}^N= (e^{i \frac{\theta}{2N} P}e^{i \frac{\theta'}{2N} P'})^N + \delta$, where $\delta$ is the error rate require. By choosing an appropriate $N$ (or number of repetitions) we can approximate this Unitary very well. This is known as the Trotter-Suzsuki-Method.
This still isn't an arbitrary unitary though, it is still limited by the two-qubit Paulis. For an arbitrary unitary for $n$$ qubits $U$ we say that $U = e^{iH}$, where $H$ is a Hermitian, so it's a linear combination of $n$-qubit Paulis with real coefficients: $H = \sum\limits_j J_j P_j$. This can then be decomposed: $U = e^{iH} = e^{i\sum\limits_j J_j P_j} = \prod\limits_j e^{i \frac{\theta_j}{2}P_j}$, where $\frac{\theta_j}{2}=J_j$. We can then find a unitary gate for each of these terms by setting the right angle and by using the Trotter-Suzuki-Method. This proves that any unitary can be expressed using the gates set described above. 

The Trotter-Suzuki-Method is not the best way to express any unitary. It's just one relatively simple way that proves universality.

---
**Alternative universal gate sets**
Any Non-Clifford with the Cliffords is a universal gate set. An example is the set of the Cliffords with the $T$-Gate ($T = R_Z\left(\frac{\pi}{4}\right)$). This is useful for any error-resistant quantum computers, as Cliffords are relatively easy to make error-resistant and only having to perfect a single Non-Clifford makes things easy.
Another (surprising) example is the Toffoli with the Hadamard.

---
**Motivating example of quantum advantage**
Simulating quantum systems (such as spin$\frac{1}{2}$ particles, like electrons) on classical computers is very difficult, because of the exponential memory requirements of storing all possible states. On a classical computer, we need $2^n$ units of memory just to store the state of the system, while on a classical computer we only need $n$ qubits, which is an exponential advantage.
As the math in the study of quantum systems, such as spin$\frac{1}{2}$ particles is often very similar to the math used in quantum computing, they are the ideal system to study them. Inversely, these systems are often used to implement quantum computers, like using photon polarization for qubits. 

---
**Oracles**
There are two types of oracles: boolean oracles and phase oracles:
A Boolean oracle is just like the Unitary we described above for solving universal classical problems on a quantum computer: $U_f^b \Ket x \otimes \Ket{0}^{\otimes n} \rightarrow \Ket x \otimes \Ket{f(x)}$. These unitaries are useful for interference effects, as we can describe the input as a sum of superpositions and take advantage of interference effects: $U_f^b \sum\limits_x c_x \Ket x \otimes \Ket{0}^{\otimes n} \rightarrow \sum\limits_x c_x \Ket x \otimes \Ket{f(x)}$.
A Phase oracle acts on an input and gives it a phase: $U_f^p \Ket{x} = (-1)^{f(x)} \Ket{x}$, where $f(x)$ is most often a binary function $f(x) \in \left\{0,1\right\}$. In the case of a single qubit, this has no effect, but when applying it to a multi-qubit system, it becomes a relative phase and becomes relevant.
Boolean oracles can be used to implement phase oracles, by passing the input with a $\Ket{-}$-state instead of a $\Ket{0}$-state, as the boolean oracle decides whether to apply an $X$-operation to the input based on if the function $f(x)$ has the result $1$ or $0$ and applying an $X$ to a minus state changes its phase to $-1$, so the whole oracle decides whether to apply a phase of $-1$ to the input based on the function of the input: $U_f^b \Ket{x}\otimes \Ket{-} = (-1)^{f(x)}\Ket{x}\otimes \Ket{-}$. As the $\Ket{-}$-state remains unchanged and unentangled, it can be effectively ignored. 

Implementing boolean oracles, can be a challenge, as there is often garbage at the end of the result and it can't be ignored like in classical computing, because of the destructive effect of getting rid of this garbage on the interference effects: $U: \Ket{x} \otimes \Ket{0...} \otimes \Ket{0...} \rightarrow \Ket{x} \otimes \Ket{f(x)} \otimes \Ket{g(x)}$.  By taking the hermitian conjugate of that unitary, we can revert this process: $U^\dagger:\Ket{x} \otimes \Ket{f(x)} \otimes \Ket{g(x)} \rightarrow \Ket{x} \otimes \Ket{0...} \otimes \Ket{0...}$. This also gets rid of the output. Because of not being to just copy an arbitrary result, before undoing it (no cloning adftheorem: there exists no unitary, such that $U: \Ket{\psi} \otimes \Ket{0} \rightarrow \Ket{\psi} \otimes\Ket{\psi}$ $\forall \Ket{\psi}$), we are limited to binary functions. Here the controlled-not can be used to effectively copy the state into a new register. This leads us to the following process, that effectively applying a boolean oracle:
1) Apply Unitary to perform computation: $U_f: \Ket{x} \otimes \Ket{0...} \otimes \Ket{0...} \otimes \Ket{0...}\rightarrow \Ket{x} \otimes \Ket{f(x)} \otimes \Ket{g(x)}\otimes \Ket{0...}$
2) Apply a bunch of controlled-nots to copy the result into the last register: $C_x^{\otimes n}: \Ket{x} \otimes \Ket{f(x)} \otimes \Ket{g(x)}\otimes \Ket{0...}\rightarrow \Ket{x} \otimes \Ket{f(x)} \otimes \Ket{g(x)}\otimes \Ket{f(x)}$ 
3) Apply the hermitian conjugate of the unitary, undoing the computation and removing the garbage: $U^\dagger_f: \Ket{x} \otimes \Ket{f(x)} \otimes \Ket{g(x)}\otimes \Ket{f(x)} \rightarrow \Ket{x} \otimes \Ket{0...} \otimes \Ket{0...} \otimes \Ket{f(x)}$.
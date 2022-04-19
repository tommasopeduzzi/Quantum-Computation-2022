# Week 8
## Quantum Fourier Transform
I won't be writing down every equation, as this is a waste of time. To get more info go to https://qiskit.org/textbook/ch-algorithms/quantum-fourier-transform.html.

The goal of the Fourier Transform is to give some information about the frquencies inside that function, by putting it through the integral $$\widehat f(\omega) = \int\limits_{-\infty}^\infty f(x) e^{i2\pi x \omega} dx$$
 A discrete version can be defined, where the continous function is replaced by a discrete vector $\Ket{f} = \sum\limits_{j=0}^{N-1} f_j \Ket{j}$. The transform acts on the basis states ($\Ket{j} \rightarrow \Ket{\widehat j} = \frac{1}{\sqrt N} \sum\limits_{k = 0}^{N-1}\omega^{jk} \Ket{k}$, where $\omega = e^{\frac{i2\pi}{N}}$): $$\Ket{f} = \sum\limits_{j=0}^{N-1} f_j \Ket{j} \rightarrow \Ket{\widehat f} = \frac{1}{\sqrt N} \sum\limits_{j=0}^{N-1}\sum\limits_{k=0}^{N-1}\omega^{jk} \Ket{k}$$
 In this case a Z-basis state is in the 'big-endian' ordering, because it's easier for fractions, where $j= \sum\limits_{l=1}^n j_l 2^{n-l}$: 
 $$\Ket{j} = \Ket{j_1 j_1 ... j_n}$$
using this property we can express these transformations on basis states like this:$$\Ket{j}\rightarrow\Ket{\widehat j}= \frac{1}{\sqrt N} \bigotimes\limits_{l=1}^n\left[\sum\limits_{k=0}^l e^{i2\pi jK2^{-l}}\Ket{k}\right] = \bigotimes\limits_{l=1}^n \frac{\Ket{0}+e^{i2\pi j2^{-l}} \Ket{1}}{\sqrt2}$$
To understand how we can construct an algorithm that get's us to this state, we have to convert $j$ (the input of the fourier transform) to binary. We know that we can express $j = j_1 j_2 ... j_{n-1} j_n$, where $j_i$ is the $i$th most significant bit of $j$, because of the big endian ordering of the bits. So we can say $\frac{j}{2^l}= \text {int} + 0.j_{n-l-1}...j_n$. Because $e^{i2\pi\times \text{integer}} = e^{i2\pi\times 0}$, the only thing that we care about are the bits after the decimal point. So for every incrementation of $l$ we get one more bit after the decimal point: $$\Ket{\widehat j} = \frac{\Ket{0}+e^{i2\pi 0.j_n} \Ket{1}}{\sqrt2} \otimes \frac{\Ket{0}+e^{i2\pi 0.j_{n-1}j_n} \Ket{1}}{\sqrt2} \otimes... \otimes\frac{\Ket{0}+e^{i2\pi 0.j_{n-l-1}...j_{n-1}j_n} \Ket{1}}{\sqrt2}$$
So we just need to create a circuit that can put the qubits into these states.
For the leftmost qubut, the phase is either going to be $+1$ or $-1$, if $j_n = 0$ ($e^{i2\pi 0.0} = 1$) or $j_n = 1$ ($e^{i2\pi 0.5} = 1$ ($0.5$ is decimal for binary $0.1$)). We can achieve this by just applying a Hadamard to the first qubit. For the rest of the of the qubits we can use some controlled rotations ($R_k = \begin{pmatrix}1&&0 \\ 0&&e^{i\frac{2\pi}{2^k}}\end{pmatrix}$), to get a circuit that performs the FT as follows:
![[Pasted image 20220418235733.png]]
Note that this also reverses the order of the qubits.We can use these rotations because $e^{i2\pi 0.j_{n-1}j_n} = e^{i2\pi 0.j_{n-1}} e^{i2\pi 0.0j_n}$. 
This solution required $O(n²)$ gates, whilst a classical computer needs at least $O(n2^n)$ operations. Practically you can't really apply a DFT on a quantum computer and get a huge speedup, as preparing the state is in itself computationally expensive.


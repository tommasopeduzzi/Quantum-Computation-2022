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
This solution required $\frac {n(n-1)}2$ gates, so it scales as $O(n²)$, whilst a classical computer needs at least $O(n2^n)$ operations. Practically you can't really apply a DFT on a quantum computer and get a huge speedup, as preparing the state is in itself computationally expensive.
If you have a state naturally prepared, it is useful to perform a QFT, as there isn't any need anymore, so it can serve as a sub algorithm in another algorithm.

---
## Phase estimation
Phase estimation is such an algorithm, where a QFT can be applied:
In phase estimation the goal is to find the eigenvalue for a given unitary with a given eigenstate: $$U \Ket{u} = e^{i2\pi \phi} \Ket{u}$$
where $\phi = 0.\phi_1\phi_2 ... \phi_t$ and t is the number of required bits. We assume that we have the ability to prepare such a state, as well as construct the unitary $U$ apply a controlled $U$ (we only apply $U$ if the control is $\Ket{1}$ ).

With these assumptions we can apply this circuit:
![[Pasted image 20220419153649.png]]
Because the second register is an eigenstate, the controlled $U$s don't do anything to the register, and it remains in state $\Ket{u}$. 
On the first register though, we get phase kickbacks the eigenvalue of $U$ according to the the amount of times $U$s we controlled on that qubit. 
We can write the down the state of the first register as follows:$$\bigotimes\limits_{l = t}^1 \frac{\Ket{0} + e^{i2\pi \phi 2^{l-1}}\Ket{1}}{\sqrt2}$$
We can consider that $2^0\phi = \text{int} + 0.\phi_1 ... \phi_t$,$2^1\phi = \text{int} + 0.\phi_2 ... \phi_t$, $2^2\phi = \text{int} + 0.\phi_2 ... \phi_t$ etc. and we can ignore the integer part. 
This final state is just the FT of the state representing the eigenvalue. Doing a reverse QFT gives us the binary representation of the eigenstate $\Ket{\lambda} \otimes \Ket{u}$ .

## Order finding
An application in abstract mathematics of this principle is to find the smallest possible integer $r$, with a given $x$ and $N$ ($x < N$), such that $$x^r = 1 \mod N$$
This is useful because $x^{r+1} = x \mod N$ and we have found the periodicity of the process.
Classically it is believed, that there is no algorithm that is polynomial to the number of bits used $L$ to express  $N$.
On a quantum computer, we consider the unitary $$\sum\limits_{j=0}^{2^L-1} \Ket{ xj \mod N }\Bra j$$
When $j \ge N$, we say that $xj \mod N = j$, because we don't really care about these. The eigenstates of this unitary are $$\Ket{u_s} = \frac{1}{\sqrt r} \sum\limits_{k=0}^{r-1} exp\left[\frac{i2\pi s}{r}\right] \Ket{x^k \mod N}$$
This is because when we apply the unitary to these states, we multiply everything by $x$ so $x^k$ becomes $x^{k+1}$ and we end up with with the same states at the end. The eigenvalues are: $$\exp\left[\frac{i2\pi s}{r}\right]$$
By performing phase estimation we can find these phases $\frac{s}{r}$ and thus find $r$.

To perform phase estimation, we need to prepare the eigenstate first.
Luckily the superposition of the first r eigenstates is $$\frac{1}{\sqrt r}\sum\limits_{s = 0}^{r-1} \Ket{u_s} = \Ket{000\text{...}1}$$
which is really easy to prepare.
Doing a phase estimation on these states results in the state $$\sum\limits_{s= 0}^{r-1}\Ket{\frac{s}{r}} \otimes \Ket{u_s}$$
We can then randomly choose one phase $\phi(s) = \frac{s}{r}$ accuracte to n bits and can estimate the fraction in polynomial time. The number of qubits needed to represent this can be determined from $x$ and $N$. 

## Shor's Algorithm
Shor's algorithm performs factoring: it finds a non-trivial factor of N (not 1 or $N$), so that we can divide $N$ by this factor and repeat the process and find all non-trivial factors of N. 
The first theorem we utilise is that if we have a $y$, such that $y² = 1 \mod N$ and $1 < y < N-1$, then $\gcd(y-1, N)$ and/or $\gcd(y+1, N)$ is a non-trivial factor of N. Therefore to factor $N$, we need to find an appropriate $y$.
The second theorem is that $y = x^{r/2}$, for a randomly chosen $x$, such that $2 \le x \le N-1$ and $\gcd(x, N) = 1$. We can then, using order finding described above, find an r such that $x^r = 1 \mod N$. If r is even and $x^{\frac{r}{2}} \neq -1 \mod N$ (probability of which is basically $O(1)$), we have found $y² = (x^{\frac{r}{2}})² = 1\mod N$.
Shors algorithm then consists of of the following steps:
1) Determine wheter N is prime or not. If it is prime output it, otherwise continue
2) Determine wheter N is even, because it's easy. If even output 2
3) Check whether n only has one distinct prime factor and if it's just a power of that.
4) Randomly choose a $x$, such that $2 \le x \le N-1$ and $\gcd(x,N) = 1$. if $\gcd(x,N) > 1$, output x.
5) Determine $y$ using steps described above.
6) Output $\gcd(x-1, N)$ and $\gcd(x+1, N)$. 

This succeeds with with $O(1)$ probability.

 
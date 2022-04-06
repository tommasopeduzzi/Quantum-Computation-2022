# Week 6
**General Computers**
In general a computer takes in an inpout $x$ that can be expressed as a binary string in case of digital computers and computes a function $f(x)$. It's like a black box inbetween the input and the output. Anything that can perform this mapping is considered general.
An easy way to perform these kinds of data is to use a look-up table, where each input maps to an output. For large inputs like images, this is not ideal.

To talk about universality with quantum computers, let's first define some things: A computer has a $n$-bit input and transforms it using a function into a $n$-bit output. Each unique input produces a unique output.

For quantum computers, we use a tensor product of $2n_i$ qubits, where $n_i$ is the number of qubits in the input bitstring. The first $n_i$ qubits are in the same state as the input bitstring, while the rest are 0, so that we can write our output there and we get a unique output:
$\Ket x \otimes \Ket0^{\otimes n_0} \rightarrow \Ket x \otimes \Ket {f(x)}$ 
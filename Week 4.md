# Week 4
**Tensor Product**
Example for 2 2x2 matrices:
$A = \begin{pmatrix}a_{00}&&a_{01}\\ a_{10}&&a_{11}\end{pmatrix}$
$B = \begin{pmatrix}b_{00}&&b_{01}\\ b_{10}&&b_{11}\end{pmatrix}$
$A\otimes B =\begin{pmatrix}a_{00} b_{00} && a_{00}b_{01}&& a_{01} b_{00} && a_{01} b_{01} \\ a_{00} b_{10} && a_{00}b_{11}&& a_{01} b_{10} && a_{01} b_{11} \\ a_{10} b_{00} && a_{10}b_{01}&& a_{11} b_{00} && a_{11} b_{01} \\ a_{10} b_{10} && a_{10}b_{11}&& a_{11} b_{10} && a_{11} b_{11}\end{pmatrix}$   

Example for vectors representing quantum states:
$\Ket a = a_{0}\Ket0 + a_{1}\Ket1=\begin{pmatrix}a_0\\a_1\end{pmatrix}$ 
$\Ket b = \begin{pmatrix}b_0\\b_1\end{pmatrix}$
$\Ket a \otimes \Ket b = \begin{pmatrix}a_{0}\Ket b \\ a_{1}\Ket b\end{pmatrix} = \begin{pmatrix}a_{0}b_{0}\\a_{0}b_{1}\\a_{1}b_{0}\\a_{1}b_{1}\end{pmatrix}$ 

**Representing multiple qubit states**
Example with 2 qubits:
Like we do with one qubit systems, we can represent a system of 2 qubits as a linear superposition of the possible outcomes for measuring.
As an example, a system made up of one qubit has a state $\psi$ defined as $\Ket\psi = a_{0}\Ket0 + a_{1}\Ket1$ where $\Ket 0$ and $\Ket1$ are the states where we get a 0, or a 1 respectively, 100% of the time, and the probability $P_0$ of getting a 0 is $P_{0}=|a_0|^2$ and $P_{1}=|a_1|^2$ for a 1. These amplitudes are complex and satisfy the normalization condition of $|a_{0}|^{2}+|a_{1}|^{2}=1$.

In a system of two qubits we can consider the states $\Ket{00}, \Ket{01}, \Ket{10}, \Ket{11}$, where $\Ket{00}$ is a state where we measure 00 100% of the time, for $\Ket{10}$ we measure 10 100% of the time etc.
A general system with two qubits can again be represented as a linear superposition of all the possible outcomes: $\Ket \psi = c_{00}\Ket{00} +c_{01}\Ket{01}+c_{10} \Ket{10}+ c_{11}\Ket{11}$ and where again the probability of measuring a 00 $P_{00}= |c_{00}|^{2}$ etc. Again these amplitudes are complex and follow the normalization condition $\sum\limits_{j,k\in\left\{0,1\right\}}|c_{jk}|^{2}= 1$

The states $\Ket{00}, \Ket{01}, \Ket{10}, \Ket{11}$ are defined using the tensor product. For example, $\Ket{01} = \Ket0 \otimes \Ket1 = \begin{pmatrix}1\\0\end{pmatrix}\otimes\begin{pmatrix}0\\1\end{pmatrix}=\begin{pmatrix}0\\1\\0\\0\end{pmatrix}$, where the first element in the column vector describes the amplitude of the state $\Ket {00}$, the second the state $\Ket {01}$ and so on.

This is also how we describe states of systems with multiple qubits. For example, if we want to describe the system above with the qubits in states $\Ket a$ and $\Ket b$ we could say that the entire system is in state $\Ket {ab} = \Ket a \otimes \Ket b = \begin{pmatrix}a_{0}b_{0}\\a_{0}b_{1}\\a_{1}b_{0}\\a_{1}b_{1}\end{pmatrix}$, like described above in the section on the tensor product. For example, the amplitude of the state $\Ket {00}$ is equal to $a_{0}b_{0}$. 

**Single qubit gates on a multiple qubits system**
To be able to apply single qubit gates to these multiple qubit states, you need to find matrices to these states, as you cant multiply a $2\times2$ matrix to a column vector with 4 rows, you need a $4\times4$ matrix. For example, we have a 2 qubit state, and we want to apply an X-gate to the second qubit. The matrix describing is the tensor product of the identity matrix times the matrix representing the X Gate, so it does an X operation on the second one and nothing on the first one:
$$X =\begin{pmatrix}0&&1\\1&&0\end{pmatrix}$$
$$I = \begin{pmatrix}1&&0\\0&&1\end{pmatrix}$$
Matrix that applies an X-gate on the second qubit and does nothing on the first:
$$I\otimes X = \begin{pmatrix}1&&0\\0&&1\end{pmatrix}\otimes\begin{pmatrix}0&&1\\1&&0\end{pmatrix} = \begin{pmatrix}0&&1&&0&&0\\1 && 0 && 0 && 0\\0&&0&&0&&1\\0&&0&&1&&0\end{pmatrix}$$
Another example: We have a system with three qubits and want to apply a Hadamard to the middle one. The matrix describing that one is $I\otimes H\otimes I$.

**Multiple qubit gates**
There are gates, such as the Controlled NOT gate, that cannot be represented as the tensor product of single qubit gates. 
When applying these gates, we can find that we get states, that we cannot express as tensor products of single qubit states. When a state cannot be described as such, we say that the state is entangled. This is a key factor in why quantum computing can be far more powerful than classical computers.

Here is a list of multiple qubit gates 
| **Gate**              | **Matrix**                                                                                    | **Comment**                                                                                                                                               |
| --------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Controlled Not (CNOT/$C_x$) | $\begin{pmatrix}1 && 0 && 0 && 0 \\ 0 && 1 && 0 && 0 \\ 0 &&0&&0&&1\\0&&0&&1&&0\end{pmatrix}$ |  |
|                       |                                                                                               |                                                                                                                                                           |

**More on the CNOT**
We have already come across an interpretation of the CNOT: It does an X operation on the target if the control is 1. This is also expressed in the matrix of CNOT: The $2\times2$ matrix on the top right ($\begin{pmatrix}1&&0\\0&&1\end{pmatrix} = I$) acts on the $\Ket {00}$ and $\Ket {01}$. The $2\times2$ matrix the lower right ($\begin{pmatrix}0&&1\\1&&0\end{pmatrix} = X$) acts on the states $\Ket {10}$ and $\Ket {11}$.
This is only one of many interpretations of the CNOT. Another way of seeing it, is as doing a Z on the target if the control is in the state $\Ket-$. 
Following this logic, the following can be written:
$$C_{x}= \begin{pmatrix}1 && 0 && 0 && 0 \\ 0 && 1 && 0 && 0 \\ 0 &&0&&0&&1\\0&&0&&1&&0\end{pmatrix} = I\otimes |0\times0| + X \otimes|1\times1| = I\otimes|+\times+| + Z\otimes|-\times-|$$

**Circuit Identities**
These are some combinations of gates that are useful and often used in QC.
Just like quantum states have two equivalent representations, namely Ket and Bra, quantum gates have a similar equivalent representation. So for a gate $U$ there exists a gate $U^\dagger$. The property of that gate is that has the same effect U has on a state in its Ket form, but on a state in the Bra form.
There are gates where $U = U^\dagger$. These are called Hermitian gates. Most of the gates we have looked at so far have this property, like the X, Y, Z, Hadamard, CNOT.
As an example we have the Hadamard: $H\Ket 0 =\Ket +$ and $\Bra 0 H = \Bra +$ etc.
This can be used to transform different Pauli gates into eachother. For example $$HXH = |+\times-| + |-\times+| = Z$$because $X = |0\times1| + |1\times0|$ and the right Hadamard acts on all the Ket forms, while the left one acts in the Bra forms.
Another example with the $C_{x}=|0\times0|\otimes I + |1\times1|\otimes X$: $$(I\otimes H)C_{x}(I\otimes H) = |0\times0|\otimes I + |1\times1|\otimes Z = C_{Z}$$
Yet another example is can be seen with rotations. Here is an example with the $R_{Z}$. $$XR_{Z}(\theta)X = R_{Z}(-\theta)$$ More Circuit Identitities can be found in the *[section of the qiskit textbook](https://qiskit.org/textbook/ch-gates/more-circuit-identities.html).

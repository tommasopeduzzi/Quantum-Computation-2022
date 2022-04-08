# Week 5

**Hermitian Conjugate**
$m = \begin{pmatrix}a && b\\ c && d\end{pmatrix}$
$m^T = \begin{pmatrix}a && c \\ b && d\end{pmatrix}$
$m^* = \begin{pmatrix}a^{*} && b^*\\c^* && d^*\end{pmatrix}$
$m^\dagger = (m^*)^T = (m^T)^* = \begin{pmatrix}a^* && c^*\\b^* && d^*\end{pmatrix}$ 
---
**Paulis**
Examples: X Y Z (I)
$X^2 = Y^2 = Z^2 = I$
$XY = -YX$        $XZ = -ZX$         $ZY = -YZ$
$ZX = iY$ and $XZ = -iY$, etc.

---
**Writing matrices as sums of outer products/Paulis**
$m =  \begin{pmatrix}a&&b\\c&&d\end{pmatrix} = a \begin{pmatrix}1&&0\\0&&0\end{pmatrix} + b\begin{pmatrix}0&&1\\0&&0\end{pmatrix} + c\begin{pmatrix}0&&0\\1&&0\end{pmatrix} + d\begin{pmatrix}0&&0\\0&&1\end{pmatrix}$ 
Because $\begin{pmatrix}1&&0\\0&&0\end{pmatrix} = \begin{pmatrix}1\\0\end{pmatrix}\begin{pmatrix}1&&0\end{pmatrix}=|0\times0|$ etc we can write any matrix as a sum of outer products: $m = a|0\times0| + b|0\times1| + c|1\times0| + d|1\times1|$ 

Because $|0\times0| = \begin{pmatrix}1&&0\\0&&1\end{pmatrix} = \begin{pmatrix}1&&0\\0&&1\end{pmatrix} +\begin{pmatrix}1&&0\\0&&-1\end{pmatrix} = I +Z$, $|1\times1| = I-Z$, $|1\times0| = X|0\times0| = X(I+Z) = X -iY$ and $|0\times1| =X + iY$, we can express any matrix as a sum of the Paulis: $m = \alpha I + \beta X + \gamma Y + \delta Z$ 

---
**Unitary matrices**
We call a matrix $U$ unitary, if $U^\dagger U =UU^\dagger = I$ 

Suppose there is a state$\Ket\psi$ and $\langle\psi|\psi\rangle = 1$, so $\Ket\psi$ is normalized. If $U$ is a unitary and $U\Ket\psi = \Ket\phi$, $\langle\psi |\psi\rangle = \Bra\phi U^\dagger U\Ket\phi = \langle\phi |\phi\rangle = 1$. This shows that applying a unitary to a normalized state gives back a normalized state.

More generally we can say that if we have the states $\Ket{\psi_0}$, $\Ket{\psi_1}$ and $\Ket{\phi_0} = U \Ket{\psi_0}$, $\Ket{\phi_1} = U\Ket{\psi_1}$, $\langle \psi_0|\psi_1\rangle =\langle \phi_0|\phi_1\rangle$.

If $U \Ket{\psi_0}= \Ket{\phi_0}$ and $U \Ket{\psi_1} = \Ket{\psi_1}$, $U = |\psi_0\times\phi_0| + |\psi_1\times\phi_1|$ 

Similarly, we can express unitaries as the sum of the product of the outer product of their eigentstates and the eigenvalue for that eigenstate. An eigenstate is a state, where only the global phase is changed. Example:
$U \Ket{h_j} = e^{ih_j}\Ket{h_j}$, where $\Ket{h_j}$ is a basis state. For $U^\dagger$, we can say that $U^\dagger\Ket {h_j} = e^{-ih_j}\Ket{h_j}$. This proves that $UU^\dagger = I$ 
We can now write this unitary as $U = \sum\limits_j e^{ih_j}|h_j\times h_j|$. This is called the spectral form.

---
**Hermitian matrices**
These matrices are defined as any matrix that is equal to its hermitian form: $H = H^\dagger$. An example for such a matrix is the $\Ket0$ state. 
When applying a Hermitian to a state, we don't always get back a normalized state. When applying it to one of its eigenstates, we get that state multiplied by some real number: $H\Ket{h_j} = h_j \Ket{h_j}$. The coefficient is real, because $h_j = h_j^*$ and that is only correct for real numbers.
So we write Hermitian matrices as their spectral form: $H = \sum\limits_{j} h_j |h_j \times h_j|$ 
For every Hermitian we can find a corresponding Unitary: $U = e^{iH}$ 

---
**Clifford Gates**
Clifford gates have the property of turning Paulis into Paulis by conjugation. Conjugation means applying the gate on one side and the hermitian conjugate of that gate on the other side. An example of one of these Clifford gates is the Hadamard: $HXH^\dagger = Z$ 
Most of the gates that we have looked at are Clifford's. Interestingly the Paulis are also Clifford gates.

---

**Multi qubit Paulis**
Paulis also exist in multi qubit forms. For example, if we have a Clifford gate $U$ this still holds: $UX\otimes IU^\dagger = X\otimes X$. In this case $U = C_X$.

---
**Non-clifford Gates**
Non-clifford gates can always be represented as a matrix exponential of a Hermitian.
Examples for this are the Rotation gates:
$R_X(\theta) = e^{iX \frac{\theta}{2}}$
$R_Y(\theta) = e^{iY \frac{\theta}{2}}$
$R_Z(\theta) = e^{iZ \frac{\theta}{2}} = H e^{i X\frac{\theta}{2}}H = e^{i (HXH^\dagger)\frac{\theta}{2}}$ 

Let's suppose we have a system with 4 qubits and we want to rotate the last one by an angle theta around the x-Axis. For one qubit the operation looks like this: $e^{i \frac{\theta}{2} X }$. The gate for 4 qubits would look this: $R_X(\theta) \otimes I\otimes I\otimes I = e^{i \frac{\theta}{2} X \otimes I\otimes I\otimes I}$, because the Hermitian and Unitary have the same eigenbasis.     

So for expressing a $R_x(\theta)$ and Ciiffords, we can express it as $e^{u \frac{\theta}{2}P_{n-1} \otimes P_{n-2} \otimes ... \otimes P_1 \otimes P_0}$ where $P_j \in \left\{\text{X, Y, Z, I} \right\}$ 

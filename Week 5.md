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

More gennerally we can say that if we have the states $\Ket{\psi_0}$, $\Ket{\psi_1}$ and $\Ket{\phi_0} = U \Ket{\psi_0}$, $\Ket{\phi_1} = U\Ket{\psi_1}$, $\langle \psi_0|\psi_1\rangle =\langle \phi_0|\phi_1\rangle$.

If $U \Ket{\psi_0}= \Ket{\phi_0}$ and $U \Ket{\psi_1} = \Ket{\psi_1}$, $U = |\psi_0\times\phi_0| + |\psi_1\times\phi_1|$ 

Similarly, we can express unitaries as the sum of the product of the outer product of their eigentstates and the eigenvalue for that eigenstate. Example:
$U \Ket{h_j} = e^{ih_j}\Ket{h_j}$, where $\Ket{h_j}$ is a basis state. $U = \sum\limits_j e^{ih_j}|h_j\times h_j|$  

---
**Hermitian matrices**

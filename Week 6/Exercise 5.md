# Exercise 5
### 1. Clifford Gates and Paulis
a) To express any Pauli for 1 qubit up to a phase, we only need the $X$ and $Z$. This is because $XX = I$ and $XZ = iY$ Therefore the generators for 1 qubit are $X$ and $Z$. 

For two qubits, we can use the generators $X \otimes I$, $I \otimes X$, $Z \otimes I$ and $I \otimes Z$:
$Y \otimes I = (iX\otimes I)(Z \otimes I) = iXZ \otimes II$
$I \otimes Y = (I \otimes iX)(I\otimes I) = iXZ \otimes II$ etc.

Because of $(a \otimes b)(c \otimes d) = ac \otimes bd$, we can say that for any $N$ qubits, the set of generators to express any $N$-qubit Pauli is: $\bigcup\limits_N X_n \cup \bigcup\limits_N Z_n$, where $X_n = I^{\otimes n-1} \otimes X \otimes I^{\otimes N -n}$ and $Z_n = I^{\otimes n-1} \otimes Z \otimes I^{\otimes N -n}$. A product of elements of these generators can be used to express any arbitrary $N$-qubit Pauli, up to a phase.

1b)
We need to be show, that if the relation holds for the generators described above, it also holds for a product of generators.
The relation $UPU^\dagger \sim P'$ holds for the generators, because the generators are guaranteed to be made up of Paulis and thus are n-qubit Paulis themselves.
Because $P_1P_2 = P_3$ a product of generators is also guaranteed to be a Pauli and therefore the relation also holds for any arbitrary n-qubit Pauli, as it can be expressed as such a product
## 2. Single-Qubit Clifford Gates
a) $XXX = X \sim X$
$XZX = iX \sim X$, therefore $X$ is Clifford

$ZXZ = -iX$
$ZZZ = Z \sim Z$, therefore $Z$ is Clifford

$YXY = -X \sim X$
$YZY = -Z \sim Z$, therefore $Y$ is Clifford

b) $HXH = Z \sim Z$
$HYH = -Y \sim Y$
$HZH = X \sim X$
$HIH = I \sim I$, therefore $H$ is Clifford

$SXS^\dagger = -Y\sim Y$
$SYS^\dagger = X \sim X$ 
$SZS^\dagger = Z \sim Z$
$SIS^\dagger = I \sim I$, therefore $S$ is Clifford

$S^\dagger X S = Y\sim Y$
$S^\dagger Y S = -X\sim X$
$S^\dagger Z S = Z\sim Z$
$S^\dagger I S = I\sim I$, therefore $S^\dagger$

c) $T= \begin{pmatrix}1&&0\\0&&e^{i \frac{\pi}{4}}\end{pmatrix}$ 
$TYT^\dagger = \begin{pmatrix}0&&-ie^{-i \frac{\pi}{4}}\\ie^{i \frac{\pi}{4}}&&0\end{pmatrix} \not\sim P$ $\forall P \in \{X,Y,Z,I\}$, therefore $T$ is not Clifford.

### 3. Two-Qubit Clifford Gates
Because we found the generators, we only need to show that the relation holds for the generators, which in this case are: $X \otimes I$, $I \otimes X$, $Z \otimes I$ and $I \otimes Z$.

a) $C_x (X \otimes I) C_x = i(Y \otimes X) \sim Y \otimes X$
 $C_x (I \otimes X) C_x = I \otimes X \sim I \otimes X$
 $C_x (Z \otimes I) C_x = Z \otimes I) \sim Z \otimes I$
 $C_x (I \otimes Z) C_x = Z \otimes Z \sim Z \otimes Z$, therefore $C_x$ is Clifford

b) $C_H (X \otimes I) C_H = \begin{pmatrix}0&&0&&1&&0 \\ 0&&1&&0&&0 \\ 1&&0&&0&&0 \\ 0&&0&&0&&-1\end{pmatrix} \not\sim P$ $\forall P \in P_2$ 
### 4. Three-Qubit Clifford Gates
a) Fredkin Gate: $$CSwap = \begin{pmatrix} 1&& 0&& 0&& 0 &&0&&0&& 0&& 0\\0&& 1 &&0&& 0&& 0&& 0&& 0&& 0  \\0 &&0&& 1&& 0&& 0&& 0&& 0&& 0  \\0&& 0&& 0&& 1&& 0&& 0&& 0&& 0  \\0&& 0&& 0&& 0&& 1&& 0&& 0&& 0  \\0&& 0&& 0&& 0&& 0&& 0&& 1&& 0  \\
0&& 0&& 0&& 0&& 0&& 1&& 0&& 0  \\0&& 0&& 0&& 0&& 0&& 0&& 0&& 1\end{pmatrix}$$

b) $CCNOT(I \otimes I \otimes Z)CCNOT^\dagger =\begin{pmatrix}1&0&0&0&0&0&0&0\\ 0&-1&0&0&0&0&0&0\\ 0&0&1&0&0&0&0&0\\ 0&0&0&-1&0&0&0&0\\ 0&0&0&0&1&0&0&0\\ 0&0&0&0&0&-1&0&0\\ 0&0&0&0&0&0&-1&0\\ 0&0&0&0&0&0&0&1\end{pmatrix} \not \sim P$ $\forall P \in P_3$
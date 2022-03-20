# Week 3 - Representng Single Qubit States and Gates

- Qubits can be represented as a probability of either getting a 1 or a 0 when doing a Z-Measurement. The probability is the square of the amplitude. 
- A qubit normally starts with a probability of getting a 0  $P_0$ of 1 and a probability of getting a 1 ($P_1$) of 0. This state is written as $\Ket{0} = \begin{pmatrix} 1\\ 0 \end{pmatrix}$. The opposite of this (probability of getting a 1 is 100%) is $\Ket1 =\begin{pmatrix}0\\1\end{pmatrix}$ 
- More generally, a quantum state can be written as: $\Ket\psi = \begin{pmatrix}a_0\\a_1\end{pmatrix} = a_0\Ket0 + a_1\Ket1$, where the $a_0$ and $a_1$ are the amplitudes for each state.

**Dot product in Quantum Computing**

- For representing quantum states we can write the Ket form $\Ket\psi = \begin{pmatrix}a_0\\a_1\end{pmatrix}$, like described above, or the Bra form $\Bra\psi = \begin{pmatrix}\overline {a_0}&&\overline {a_1}\end{pmatrix}$ of the same state, where the amplitudes are the complex conjugates of the amplitudes in the Ket form (inverted sign in front of imaginary part, in case you didn't remember, you dumb fuck). 
- Inner Product using these definitions, by example: $\Braket{\psi|\psi} = \Bra\psi \times \Ket\psi = \begin{pmatrix}\overline{a_0}&&\overline{a_1}\end{pmatrix}\cdot\begin{pmatrix}a_0\\a_1\end{pmatrix} = \overline{a_0}a_0 + \overline{a_1}a_1=|a_0|^2 + |a_1|^2 = 1$ Another example : $\Braket{0|\psi} =\begin{pmatrix}1&&0\end{pmatrix}\cdot\begin{pmatrix}a_0\\a_1\end{pmatrix} = a_0$. Doing the inner product on two orthogonal states always gives 0 and on two identical states always 1, like above.
- Outer Product: 
  $\Ket0 \times \Bra0 = \begin{pmatrix} 1\\0\end{pmatrix} \begin{pmatrix} 1&&0\end{pmatrix}=\begin{pmatrix} 1&&0\\0&&0\end{pmatrix} = |0\times0|$  
- When applying Hadamard we get that it is equally likely to be a 0 or 1, which means that it can be written as $\Ket0 + \Ket1$. Because this isn't normalized, we have to multiply it by some constant, which in this case is $\frac1{\sqrt2}$. We can then define the following 'plus'- state, which is the state we get when we just apply a Hadamard gate: $\Ket+ = \frac1{\sqrt2}(\Ket0 + \Ket1)$, so $|a_0|^2 = |a_1|^2 = \frac1{2} = P_0 = P_1$. 
- This also holds in general: $|a_0|^2 = P_0$ and $|a_1|^2 = P_1$. This is called the Born rule.
- When first applying a x-gate and then a hadamard, we always get a 1 one when doing an x-measurement, which is the opposite of the 0 we would get without the x-gate. The state we get is $\Ket- = \frac1{\sqrt2}(\Ket0 - \Ket1)$. Because we square the amplitudes when getting the probability for a z- measurement, the - disappears.
- Global Phase: 
	For Z Measurement: $\Ket0 := a_0 =1 => P_0 = 1$ and $-\Ket0 := a_0 = -1 => P_0 = 1$. So they are indistinguishable when measuring
	Actually, the $\Ket0$ and the $-\Ket0$ state are indistinguishable with any kind of measurement. More generally, $e^{i\theta}\Ket0$, where the complex phase $e^{i\theta}$ has magnitude 1 and therefore the state remains normalized is indistinguishable from $\Ket0$, because the phase dissappears. So when writing quantum states we can ignore the phase.
	- $\Ket\psi = a_0\Ket0 + a_1\Ket1$, where $a_0 = Re(a_0) + Im(a_0)i = e^{i\alpha_0}|a_0|$, so $\Ket\psi = e^{i\alpha_0}|a_0|\Ket0 + e^{i\alpha_1}|a_1|\Ket1$ This can be written as, because we can consider $e^{i\alpha_0}$ as a global phase and remove it from the equation. $\Ket\psi = e^{i\alpha_0}(|a_0|\Ket0 + e^{i(\alpha_1-\alpha_0)}\Ket1) = |a_0|\Ket0 + e^{i\phi}\Ket1$, where $\phi = a_1-a_0$. Because $cos^2(\theta) + sin^2(\theta)=|a_0|^2 + |a_1|^2 = 1$ we can write $\Ket\psi = cos\frac\theta2\Ket0 +e^{i\phi}sin\frac\theta2\Ket1$ 
- 	 These paramaters $\theta$ and $\phi$ can be visualized as angles describing points on a sphere, the bloch sphere.
![[Pasted image 20220315083927.png]]

- Gates are just things that transform one state to another. For example $R_x(\pi)$ is a  rotation around the x-axis of $\pi$ degrees, so a X-Gate. Similarly, a $R_z(\pi)$ is a rotation around the Z axis by $\pi$, so a Z-gate.  Similarly there are the following gates:
| Rotation | Name |
| --- | -----------: |
| $R_z(\frac\pi2)$ | S |
| $R_z(\frac\pi4)$ | T |

- These transformations can also be written as matrixes. For example, the Identity gate (which does absolutetly nothing) is defined as $I=\begin{pmatrix}1&&0\\0&&1\end{pmatrix}$. When applying these gates, we perform matrix multiplication: $I\Ket\psi =\begin{pmatrix}1&&0\\0&&1\end{pmatrix}  \begin{pmatrix}a_0\\a_1\end{pmatrix}= \begin{pmatrix}a_0\\a_1\end{pmatrix}$. Here are some gates and their matrix representations:
| **Gate** | **Matrix** | **Example**| **Comment**|
| ---- | ------- | ------ |----|
|X|$\begin{pmatrix}0&&1\\1&&0\end{pmatrix}$ | $X\Ket\psi =\begin{pmatrix}a_1\\a_0\end{pmatrix}$ |
|Z|$\begin{pmatrix}1&&0\\0&&-1\end{pmatrix}$ | $Z\Ket\psi = a_0\Ket0 - a_1\Ket1 = \begin{pmatrix}a_0\\-a_1\end{pmatrix}$|
| H |$\frac1{\sqrt2}\begin{pmatrix}1&&1\\1&&-1\end{pmatrix}$|  $H\Ket0 = \Ket+$ | Rotation around axis between z- and x-axis |
| $R_z(\theta)$ | $\begin{pmatrix}1&&0\\0&&e^{i\theta}\end{pmatrix}$, but also $\begin{pmatrix}e^{i\frac\theta2}&&0\\0&&e^{i\frac\theta2}\end{pmatrix}$ | | | 




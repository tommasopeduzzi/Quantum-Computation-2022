# Extra Lecture - Stabilizer States
- Class of states describable in a simple way: $S = \pm P$ for any Pauli $P$
	- The part with different signs can be divided in two equally subspaces.
-  Transformation: $\mathbb P = I + S$, if we have a $S'$ then $\mathbb P = I + S'$. For this to be interesting, $S$ and $S'$ must commute and be independant from one another.
- $S \Ket{\psi} = S' \Ket{\psi} = S'' \Ket{\psi} = \Ket{\psi}$, so they all have eigenvalues of $\pm 1$ and the same eigenstates.


Given the stabilizers $Z \otimes I \otimes I$, $I \otimes Z \otimes I$ and $I \otimes I \otimes Z$, the state that is stabilized by these is $\Ket{000}$.

Given a set of stabilizers, we can conjugate their Paulis with some Clifford, transforming it to another Pauli. The phase of that tranformation is not applied to the Pauli, but to the state.


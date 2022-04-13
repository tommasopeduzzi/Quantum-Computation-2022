# Exercise 4
### Part 1
a) State a is orthogonal if $\Braket{\overline0|\overline1} = 0$. So we need to find a matrix $\Ket{\overline1} = \begin{pmatrix}a_0 \\ a_1 \end{pmatrix}$, where $\begin{pmatrix}\cos\theta && \sin\theta\end{pmatrix}\begin{pmatrix}a_0 \\a_1\end{pmatrix} = a_0\cos\theta + a_1\sin\theta = 0$.  One solution is when $\Ket{\overline1} = \begin{pmatrix}\sin\theta \\ -\cos\theta\end{pmatrix}$. 
b) $\Ket{\overline+} = \left(\frac{\Ket{\overline0} + \Ket{\overline1}}{\sqrt2}\right)= \frac{1}{\sqrt2}\begin{pmatrix}\cos\theta + \sin\theta\\sin\theta-\cos\theta\end{pmatrix}$ 
$\Ket{\overline-} = \left(\frac{\Ket{\overline0} - \Ket{\overline1}}{\sqrt2}\right)= \frac{1}{\sqrt2}\begin{pmatrix}\cos\theta - \sin\theta\\sin\theta+\cos\theta\end{pmatrix}$ 
**Correction:**  Should've shown that they are indeed bases ($\Braket{\bar x | \bar -} = 0$) and that are mutually unbiased to $\Ket {\bar0}$ and $\Ket {\bar1}$.

### Part 2
a) $XX = \begin{pmatrix}0 && 1\\1&&0\end{pmatrix}\begin{pmatrix}0 && 1\\1&&0\end{pmatrix} =\begin{pmatrix}0 \times0 + 1\times 1 && 0\times 1 + 1 \times 0\\0 \times1+1\times0 && 1\times1 + 0\times0\end{pmatrix} = \begin{pmatrix}1&&0\\0&&1\end{pmatrix} =I$
$YY = \begin{pmatrix}0&&-i\\ i && 0\end{pmatrix}\begin{pmatrix}0&&-i\\ i && 0\end{pmatrix}= \begin{pmatrix}0\times0 + (-i)i &&0\times-i +(-i)\times0\\i\times0+0\times i&&i\times(-i)+0\times0\end{pmatrix}=\begin{pmatrix}1&&0\\0&&1\end{pmatrix}=I$
$ZZ = \begin{pmatrix}1 && 0 \\0&&-1\end{pmatrix}\begin{pmatrix}1 && 0 \\0&&-1\end{pmatrix} = \begin{pmatrix}1\times1+0\times0 &&1\times0+0\times(-1)\\1\times0 + 0\times(-1) && 0\times0 + (-1)\times(-1)\end{pmatrix}=\begin{pmatrix}1&&0\\0&&1\end{pmatrix}=I$
b)
$XY = \begin{pmatrix}0&&1\\1&&0\end{pmatrix}\begin{pmatrix}0&&-i\\i&&0\end{pmatrix} = \begin{pmatrix}i &&0 \\0&&-i\end{pmatrix} =-\begin{pmatrix}-i&&0\\0&&i\end{pmatrix} = -\begin{pmatrix}0&&-i\\i&&0\end{pmatrix}\begin{pmatrix}0&&1\\1&&0\end{pmatrix} = -YX$
$YZ = \begin{pmatrix}0&&-i\\i&&0\end{pmatrix}\begin{pmatrix}1&&0\\0&&-1\end{pmatrix}=\begin{pmatrix}0&&i\\i&&0\end{pmatrix}=-\begin{pmatrix}0&&-i\\-i&&0\end{pmatrix}=-\begin{pmatrix}1&&0\\0&&-1\end{pmatrix}\begin{pmatrix}0&&-i\\i&&0\end{pmatrix}=-ZY$
$XZ = \begin{pmatrix}0&&1\\1&&0\end{pmatrix}\begin{pmatrix}1&&0\\0&&-1\end{pmatrix}=\begin{pmatrix}0&&-1\\1&&0\end{pmatrix}=-\begin{pmatrix}0&&1\\-1&&0\end{pmatrix}=-\begin{pmatrix}1&&0\\0&&-1\end{pmatrix}\begin{pmatrix}0&&1\\1&&0\end{pmatrix}=-ZX$
c) $XY = \begin{pmatrix}0&&1\\1&&0\end{pmatrix}\begin{pmatrix}0&&-i\\i&&0\end{pmatrix}=\begin{pmatrix}i &&0 \\0&&-i\end{pmatrix}= i Z \sim Z$     
$YZ = \begin{pmatrix}0&&-i\\i&&0\end{pmatrix}\begin{pmatrix}1&&0\\0&&-1\end{pmatrix}=\begin{pmatrix}0&&i\\i&&0\end{pmatrix}=-iX \sim X$ 
$XZ = \begin{pmatrix}0&&1\\1&&0\end{pmatrix}\begin{pmatrix}1&&0\\0&&-1\end{pmatrix}=\begin{pmatrix}0&&-1\\1&&0\end{pmatrix}=iY \sim Y$
d)
$X$:
$det(X-\lambda I)= \lambda^2 -1 = 0$ => $\lambda_{1,2}= \pm1$
For $\lambda = 1$: $\begin{pmatrix}0&&1\\1&&0\end{pmatrix}\begin{pmatrix}a_0\\a_1\end{pmatrix}=\begin{pmatrix}a_1\\a_0\end{pmatrix}=\begin{pmatrix}a_0\\a_1\end{pmatrix}$, so $a_0 = a_1$. Because of normalization condition the eigenstate is $\frac{1}{\sqrt2}\begin{pmatrix}1\\1\end{pmatrix}$
For $\lambda = 1$: $\begin{pmatrix}0&&1\\1&&0\end{pmatrix}\begin{pmatrix}a_0\\a_1\end{pmatrix}=\begin{pmatrix}a_1\\a_0\end{pmatrix}=\begin{pmatrix}a_0\\a_1\end{pmatrix}$, so $a_0 = a_1$. Because of normalization condition the eigenstate is $\frac{1}{\sqrt2}\begin{pmatrix}1\\1\end{pmatrix}$
For $\lambda = -1$: $\begin{pmatrix}0&&1\\1&&0\end{pmatrix}\begin{pmatrix}a_0\\a_1\end{pmatrix}=\begin{pmatrix}a_1\\a_0\end{pmatrix}=-\begin{pmatrix}a_0\\a_1\end{pmatrix}$, so $a_0 = a_1$. Because of normalization condition the eigenstate is either $\frac{1}{\sqrt2}\begin{pmatrix}1\\-1\end{pmatrix}$ or $\frac{1}{\sqrt2}\begin{pmatrix}-1\\1\end{pmatrix}$
$Y$:
$det(Y-\lambda I) = \lambda^2 -1 = 0$ => $\lambda_{1,2} = \pm1$
For $\lambda = 1$: $\begin{pmatrix}0&&-i\\i&&0\end{pmatrix}\begin{pmatrix}a_0\\a_1\end{pmatrix}=\begin{pmatrix}-ia_1\\ia_0\end{pmatrix}=\begin{pmatrix}a_0\\a_1\end{pmatrix}$
Because of normalization condition: $\frac{1}{\sqrt2}\begin{pmatrix}1\\i\end{pmatrix}$
For $\lambda =-1$: $\begin{pmatrix}0&&-i\\i&&0\end{pmatrix}\begin{pmatrix}a_0\\a_1\end{pmatrix}=\begin{pmatrix}-ia_1\\ia_0\end{pmatrix}=-\begin{pmatrix}a_0\\a_1\end{pmatrix}$
Because of normalization condition: $\frac{1}{\sqrt2}\begin{pmatrix}1\\-i\end{pmatrix}$ 

$Z$:
$det(Z-\lambda I) = (1-\lambda)(-1-\lambda) = 0$ => $\lambda_{1,2} = \pm1$ 
For $\lambda = 1$: $\begin{pmatrix}1 && 0\\0&&-1\end{pmatrix}\begin{pmatrix}a_0\\a_1\end{pmatrix}=\begin{pmatrix}a_0\\-a_1\end{pmatrix}=\begin{pmatrix}a_0\\a_1\end{pmatrix}$  => Eigenstate: $\begin{pmatrix}1\\0\end{pmatrix}$

For $\lambda = -1$: $\begin{pmatrix}1 && 0\\0&&-1\end{pmatrix}\begin{pmatrix}a_0\\a_1\end{pmatrix}=\begin{pmatrix}a_0\\-a_1\end{pmatrix}=-\begin{pmatrix}a_0\\a_1\end{pmatrix}$ => Eigenstate: $\begin{pmatrix}0\\1\end{pmatrix}$ 

### Part 3
a) To find the eigenvalues and eigenstates, the following must hold: $det(H-\lambda I) = 0$, where $\lambda$ is the eigenvalue.
$det\left(\begin{pmatrix}\frac{1}{\sqrt2} && \frac{1}{\sqrt2} \\\frac{1}{\sqrt2} && -\frac{1}{\sqrt2}\end{pmatrix}-\begin{pmatrix}\lambda && 0\\0 && \lambda\end{pmatrix}\right)  = (\frac{1}{\sqrt2}-\lambda)(-\frac{1}{\sqrt2}-\lambda)-(\frac{1}{\sqrt2})(\frac{1}{\sqrt2})=0$
$\lambda^2-1 =(\lambda + 1)(\lambda-1)= 0$ => $\lambda_{1,2} = \pm 1$ 

For $\lambda = 1$
$\frac{1}{\sqrt2}\begin{pmatrix}1&&1\\1&&-1\end{pmatrix}\begin{pmatrix}a_0\\a_1\end{pmatrix}=\frac{1}{\sqrt2}\begin{pmatrix} a_0 + a_1\\a_0 - a_1\end{pmatrix} =\begin{pmatrix}a_0\\a_1\end{pmatrix}$ 
System of equations:
1: $\frac{1}{\sqrt2}a_0 + \frac{1}{\sqrt2}a_1 -a_0 = 0$
2: $\frac{1}{\sqrt2}a_0 - \frac{1}{\sqrt2}a_1 -a_1 = 0$
$\frac{1}{\sqrt2}a_0 + \frac{1}{\sqrt2}a_1 -a_0 = \frac{1}{\sqrt2}a_0 - \frac{1}{\sqrt2}a_1 -a_1$  =>$\frac{1}{\sqrt2}a_1 -a_0 =  - \frac{1}{\sqrt2}a_1 -a_1$ => $a_0 = \sqrt2a_1+a_1$ 
Insert into 2: $\frac{1}{\sqrt2}(\sqrt2a_1+a_1) - \frac{1}{\sqrt2}a_1 -a_1 = 0$ => $0 = 0$ => $a_1 = 1$
Insert $a_1 = 1$ into 2: $\frac{1}{\sqrt2}a_0 = \frac{1}{\sqrt2}+1$ => $a_0 = 1+\sqrt2$ 
So eigenstate for $\lambda = 1$ is $\begin{pmatrix}1+\sqrt2\\1\end{pmatrix}$

For $\lambda = -1$:
$\frac{1}{\sqrt2}\begin{pmatrix}1&&1\\1&&-1\end{pmatrix}\begin{pmatrix}a_0\\a_1\end{pmatrix}=\frac{1}{\sqrt2}\begin{pmatrix} a_0 + a_1\\a_0 - a_1\end{pmatrix} =-\begin{pmatrix}a_0\\a_1\end{pmatrix}$ 
System of equations:
1: $\frac{1}{\sqrt2}a_0 + \frac{1}{\sqrt2}a_1 +a_0 = 0$
2: $\frac{1}{\sqrt2}a_0 - \frac{1}{\sqrt2}a_1 +a_1 = 0$
System of equations:
$\frac{1}{\sqrt2}a_0 - \frac{1}{\sqrt2}a_1 +a_1 = \frac{1}{\sqrt2}a_0 + \frac{1}{\sqrt2}a_1 +a_0$ =>$- \frac{1}{\sqrt2}a_1 +a_1 = \frac{1}{\sqrt2}a_1 +a_0$ => $a_0 = a_1-\sqrt2a_1$
Insert in to 2:
$\frac{1}{\sqrt2}( a_1-\sqrt2a_1) - \frac{1}{\sqrt2}a_1 +a_1 = 0$ =>$0=0$ => $a_1 = 1$
$a_0 = 1 -\sqrt2$
Eigenstate for $\lambda = -1$: $\begin{pmatrix}1-\sqrt2\\1\end{pmatrix}$

b) $HH = \frac{1}{\sqrt2}\begin{pmatrix}1 && 1 \\1 && -1\end{pmatrix}\frac{1}{\sqrt2}\begin{pmatrix}1 && 1 \\1 && -1\end{pmatrix} = \frac{1}{2}\begin{pmatrix}1 && 1 \\1 && -1\end{pmatrix}\begin{pmatrix}1 && 1 \\1 && -1\end{pmatrix} = \frac{1}{2}\begin{pmatrix}1\times1+1\times1&&1\times1+1\times(-1)\\1\times1 + (-1)\times1&&1\times1+(-1)\times(-1)\end{pmatrix} = \frac{1}{2}\begin{pmatrix}2 && 0 \\0&&2\end{pmatrix} = \begin{pmatrix}1&&0\\0&&1\end{pmatrix} = I$ c)
For $P_1 = X$: $HXH = \frac{1}{\sqrt2}\begin{pmatrix}1 && 1 \\1 && -1\end{pmatrix}\begin{pmatrix}0&&1\\1&&0\end{pmatrix}\frac{1}{\sqrt2}\begin{pmatrix}1 && 1 \\1 && -1\end{pmatrix} = \frac{1}{\sqrt2}\begin{pmatrix}1 && 1\\-1&&1\end{pmatrix}H = \begin{pmatrix}1&&0\\0&&-1\end{pmatrix}=Z\sim Z$
Für $P_1 = Y$
$HYH = \frac{1}{\sqrt2}\begin{pmatrix}1&&1\\1&&-1\end{pmatrix}\begin{pmatrix}0&&-i\\i&&0\end{pmatrix}\frac{1}{\sqrt2}\begin{pmatrix}1&&1\\1&&-1\end{pmatrix} = \frac{1}{\sqrt2}\begin{pmatrix}1&&-i\\-i&&-i\end{pmatrix}\frac{1}{\sqrt2}\begin{pmatrix}1&&1\\1&&-1\end{pmatrix} = \begin{pmatrix}0&&i\\-i&&0\end{pmatrix} = -Y \sim Y$ Für $P_1 = Z$

$HZH = \frac{1}{\sqrt2}\begin{pmatrix}1&&1\\1&&-1\end{pmatrix}\begin{pmatrix}1&&0\\0&&-1\end{pmatrix}\frac{1}{\sqrt2}\begin{pmatrix}1&&1\\1&&-1\end{pmatrix}=\frac{1}{\sqrt2}\begin{pmatrix}1&&-1\\1&&1\end{pmatrix}\frac{1}{\sqrt2}\begin{pmatrix}1&&1\\1&&-1\end{pmatrix} = X \sim X$
### Part 4
For $Z_1$, we can say that $Z_1 = \begin{pmatrix}a&&b\\c&&d\end{pmatrix} \otimes Z =\begin{pmatrix} a&&0&&b&&0\\0&&-a&&0&&-b\\c&&0&&d&&0\\0&&-c&&0&&-d\end{pmatrix}$.
Where the commutation with all elements from the other set ($X_0$, $Y_0$, $Z_0$) is true.
$\begin{pmatrix} a&&0&&b&&0\\0&&-a&&0&&-b\\c&&0&&d&&0\\0&&-c&&0&&-d\end{pmatrix}\begin{pmatrix}0&&0&&0&&1\\0&&0&&1&&0\\0&&1&&0&&0\\1&&0&&0&&0\end{pmatrix} = \begin{pmatrix}0&&0&&0&&1\\0&&0&&1&&0\\0&&1&&0&&0\\1&&0&&0&&0\end{pmatrix} \begin{pmatrix} a&&0&&b&&0\\0&&-a&&0&&-b\\c&&0&&d&&0\\0&&-c&&0&&-d\end{pmatrix}$
	
$\begin{pmatrix} a&&0&&b&&0\\0&&-a&&0&&-b\\c&&0&&d&&0\\0&&-c&&0&&-d\end{pmatrix}\begin{pmatrix}0&&0&&0&&i\\0&&0&&i&&0\\0&&-i&&0&&0\\-i&&0&&0&&0\end{pmatrix}=\begin{pmatrix}0&&0&&0&&i\\0&&0&&i&&0\\0&&-i&&0&&0\\-i&&0&&0&&0\end{pmatrix}\begin{pmatrix} a&&0&&b&&0\\0&&-a&&0&&-b\\c&&0&&d&&0\\0&&-c&&0&&-d\end{pmatrix}$ only true if $a==-d$ and $b == c$ 

$\begin{pmatrix} a&&0&&b&&0\\0&&-a&&0&&-b\\c&&0&&d&&0\\0&&-c&&0&&-d\end{pmatrix}\begin{pmatrix}1&&0&&0&&0\\0&&-1&&0&&0\\0&&0&&-1&&0\\0&&0&&0&&1\end{pmatrix}=\begin{pmatrix}1&&0&&0&&0\\0&&-1&&0&&0\\0&&0&&-1&&0\\0&&0&&0&&1\end{pmatrix}\begin{pmatrix} a&&0&&b&&0\\0&&-a&&0&&-b\\c&&0&&d&&0\\0&&-c&&0&&-d\end{pmatrix}$
also only true if $b=c=0$, so only possible  solution is $Z_1 = Z\otimes Z$

For $X_1$ we can say that:
$X_1 = \begin{pmatrix}a && b\\c&&d\end{pmatrix}\otimes X = \begin{pmatrix}0&&a&&0&&b\\a&&0&&b&&0\\0&&c&&0&&d\\c&&0&&d&&0\end{pmatrix}$ 
Commutation:
$\begin{pmatrix}0&&a&&0&&b\\a&&0&&b&&0\\0&&c&&0&&d\\c&&0&&d&&0\end{pmatrix}(X\otimes X) = (X\otimes X)\begin{pmatrix}0&&a&&0&&b\\a&&0&&b&&0\\0&&c&&0&&d\\c&&0&&d&&0\end{pmatrix}$  only true if $a=d$ and $b = c$
$\begin{pmatrix}0&&a&&0&&b\\a&&0&&b&&0\\0&&c&&0&&d\\c&&0&&d&&0\end{pmatrix}(Z\otimes Z) = (Z\otimes Z)\begin{pmatrix}0&&a&&0&&b\\a&&0&&b&&0\\0&&c&&0&&d\\c&&0&&d&&0\end{pmatrix}$
$\begin{pmatrix}0&&a&&0&&b\\a&&0&&b&&0\\0&&c&&0&&d\\c&&0&&d&&0\end{pmatrix}(Y\otimes Z) = (Y\otimes Z)\begin{pmatrix}0&&a&&0&&b\\a&&0&&b&&0\\0&&c&&0&&d\\c&&0&&d&&0\end{pmatrix}$
only true if $b = -c$ and $a=d$. Therefore, $b = c = -c = 0$ and therefore $X_1 = I\otimes X$

For $Y_1$ we can say that $Y_1 = \begin{pmatrix}a&&b\\c&&d\end{pmatrix}\otimes Y =\begin{pmatrix}0&&-ai&&0&&-bi \\ ai&&0 && bi &&0 \\ 0&&-ci&&0&&-di \\ ci&&0&&di&&0\end{pmatrix}$ 
Because of Commutation:

$\begin{pmatrix}0&&-ai&&0&&-bi \\ ai&&0 && bi &&0 \\ 0&&-ci&&0&&-di \\ ci&&0&&di&&0\end{pmatrix}(I\otimes Z)=(I\otimes Z)\begin{pmatrix}0&&-ai&&0&&-bi \\ ai&&0 && bi &&0 \\ 0&&-ci&&0&&-di \\ ci&&0&&di&&0\end{pmatrix}$ Only true if $a = d = 0$

$\begin{pmatrix}0&&-ai&&0&&-bi \\ ai&&0 && bi &&0 \\ 0&&-ci&&0&&-di \\ ci&&0&&di&&0\end{pmatrix}(Y\otimes Z) = (Y\otimes Z)\begin{pmatrix}0&&-ai&&0&&-bi \\ ai&&0 && bi &&0 \\ 0&&-ci&&0&&-di \\ ci&&0&&di&&0\end{pmatrix}$ 
Only true if $c = -b$ and $a = -d$, but that is already guaranteed.
$\begin{pmatrix}0&&-ai&&0&&-bi \\ ai&&0 && bi &&0 \\ 0&&-ci&&0&&-di \\ ci&&0&&di&&0\end{pmatrix}(X\otimes X)=(X\otimes X)\begin{pmatrix}0&&-ai&&0&&-bi \\ ai&&0 && bi &&0 \\ 0&&-ci&&0&&-di \\ ci&&0&&di&&0\end{pmatrix}$
Therefore $Y_1 = Y \otimes Y$

Because $P_1P_2 \sim P_3$. $Y_1X_1 = \begin{pmatrix}0&&0&&-1&&0 \\ 0&&0&&0&&1 \\ 1&&0&&0&&0 \\ 0&&-1&&0&&0\end{pmatrix} = -i(Y\otimes Z)\sim Y \otimes Z = Z_1$




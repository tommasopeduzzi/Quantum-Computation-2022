# Exercise 3
### 1. Mutually unbiased bases
I couldn't find a way to prove this generally, so I just calculated all the probabilities of getting a 0 or a 1 for each of the other bases for each basis state. If they are all $\frac{1}{2}$ then they are unbiased, because there's a 50/50 chance of getting either a 0 or 1. Technically, I didn't have to calculate $P_1^\alpha$ for each base, because if $P_0^\alpha$ is known it can be calculated because of the normalization condition of the amplitudes.

**Z-Bases**:
For $\Ket0$:
$P_{0}^{x} = |\braket{-|0}|^{2}= \left|\begin{pmatrix}\frac{1}{\sqrt2} && -\frac{1}{\sqrt2} \end{pmatrix} \begin{pmatrix}1\\0\end{pmatrix}\right|^{2} = \frac{1}{2}$  
$P_{1}^{x} = |\braket{+|0}|^{2}= \left|\begin{pmatrix}\frac{1}{\sqrt2} && \frac{1}{\sqrt2} \end{pmatrix} \begin{pmatrix}1\\0\end{pmatrix}\right|^{2} = \frac{1}{2}$ 
$P_{0}^{y} = |\braket{L|0}|^{2}= \left|\begin{pmatrix}\frac{1}{\sqrt2} && \frac{i}{\sqrt2} \end{pmatrix} \begin{pmatrix}1\\0\end{pmatrix}\right|^{2} = \frac{1}{2}$  
$P_{1}^{y} = |\braket{R|0}|^{2}= \left|\begin{pmatrix}\frac{1}{\sqrt2} &&- \frac{i}{\sqrt2} \end{pmatrix} \begin{pmatrix}1\\0\end{pmatrix}\right|^{2} = \frac{1}{2}$   
For $\Ket 1$:
$P_{0}^{x} = |\braket{-|1}|^{2}= \left|\begin{pmatrix}\frac{1}{\sqrt2} && -\frac{1}{\sqrt2} \end{pmatrix} \begin{pmatrix}0\\1\end{pmatrix}\right|^{2} = \frac{1}{2}$  
$P_{1}^{x} = |\braket{+|1}|^{2}= \left|\begin{pmatrix}\frac{1}{\sqrt2} && \frac{1}{\sqrt2} \end{pmatrix} \begin{pmatrix}0\\1\end{pmatrix}\right|^{2} = \frac{1}{2}$ 
$P_{0}^{y} = |\braket{L|1}|^{2}= \left|\begin{pmatrix}\frac{1}{\sqrt2} && \frac{i}{\sqrt2} \end{pmatrix} \begin{pmatrix}0\\1\end{pmatrix}\right|^{2} = \frac{1}{2}$  
$P_{1}^{y} = |\braket{R|1}|^{2}= \left|\begin{pmatrix}\frac{1}{\sqrt2} && -\frac{i}{\sqrt2} \end{pmatrix} \begin{pmatrix}0\\1\end{pmatrix}\right|^{2} = \frac{1}{2}$   

**X-Bases**
For $\Ket -$:
$P_{0}^{Z}= |\braket{0|-}|^{2}=\left|\begin{pmatrix}1&&0\end{pmatrix}\begin{pmatrix} \frac{1}{\sqrt2}\\-\frac{1}{\sqrt2}\end{pmatrix}\right|^{2}= \frac{1}{2}$
$P_{1}^{Z}= |\braket{1|-}|^{2}=\frac{1}{2}$ 
$P_{0}^{Y}= |\braket{L|-}|^{2}= \left|\begin{pmatrix}\frac{1}{\sqrt2} && \frac{i}{\sqrt2} \end{pmatrix}\begin{pmatrix} \frac{1}{\sqrt2}\\-\frac{1}{\sqrt2}\end{pmatrix}\right|^{2} =\frac{1}{2}$ 
$P_{1}^{Y}= |\braket{R|-}|^{2} =\frac{1}{2}$ 

For $\Ket +$:
$P_{0}^{Z}= |\braket{0| +}|^{2}=\left|\begin{pmatrix}1&&0\end{pmatrix}\begin{pmatrix} \frac{1}{\sqrt2}\\\frac{1}{\sqrt2}\end{pmatrix}\right|^{2}= \frac{1}{2}$
$P_{1}^{Z}= |\braket{1| +}|^{2}=\frac{1}{2}$ 
$P_{0}^{Y}= |\braket{L| +}|^{2}= \left|\begin{pmatrix}\frac{1}{\sqrt2} && \frac{i}{\sqrt2} \end{pmatrix}\begin{pmatrix} \frac{1}{\sqrt2}\\\frac{1}{\sqrt2}\end{pmatrix}\right|^{2} =\frac{1}{2}$ 
$P_{1}^{Y}= |\braket{R| +}|^{2} =\frac{1}{2}$ 

**Y-Bases**
For $\Ket L$:
$P_{0}^{Z}= |\braket{0|L}|^{2}= \left|\begin{pmatrix}1 && 0\end{pmatrix}\begin{pmatrix} \frac{1}{\sqrt2}\\ \frac{-i}{\sqrt2}\end{pmatrix}\right|^2 = \frac{1}{2}$ 
$P_{1}^{Z}= |\braket{1|L}|^{2}= \frac{1}{2}$ 
$P_{0}^{x}= |\braket{-|L}|^{2}= \left|\begin{pmatrix} \frac{1}{\sqrt2} && - \frac{1}{\sqrt2}\end{pmatrix}\begin{pmatrix} \frac{1}{\sqrt2}\\ \frac{-i}{\sqrt2}\end{pmatrix}\right|^2 = \frac{1}{2}$  
$P_{1}^{X}= |\braket{+|L}|^{2}= \frac{1}{2}$ 

For $\Ket R$:
$P_{0}^{Z}= |\braket{0|R}|^{2}= \left|\begin{pmatrix}1 && 0\end{pmatrix}\begin{pmatrix} \frac{1}{\sqrt2}\\ \frac{i}{\sqrt2}\end{pmatrix}\right|^2 = \frac{1}{2}$ 
$P_{1}^{Z}= |\braket{1|R}|^{2}= \frac{1}{2}$ 
$P_{0}^{x}= |\braket{-|R}|^{2}= \left|\begin{pmatrix} \frac{1}{\sqrt2} && - \frac{1}{\sqrt2}\end{pmatrix}\begin{pmatrix} \frac{1}{\sqrt2}\\ \frac{i}{\sqrt2}\end{pmatrix}\right|^2 = \frac{1}{2}$  
$P_{1}^{X}= |\braket{+|R}|^{2}= \frac{1}{2}$ 



### 2. Shifting certainty
$\braket{\sigma^{x}}^{2}+ \braket{\sigma^{y}}^{2}+\braket{\sigma^{z}}^{2} = 1$, where $\sigma^{\alpha}= p_{0}^{\alpha}-p_{1}^{\alpha}$. So: 
$(p^{x}_{0} -p^{x}_{1})^{2}+(p^{y}_{0} -p^{y}_{1})^{2}+(p^{z}_{0} -p^{z}_{1})^{2} = 1$
$(|\braket{-|\psi}|^2 -|\braket{+|\psi}|^2)^{2}+(|\braket{L|\psi}|^2 -|\braket{R|\psi}|^2)^{2}+(|\braket{0|\psi}|^2 -|\braket{1|\psi}|^2)^{2} = 1$
$\left(\left|\begin{pmatrix} \frac{1}{\sqrt2}&&- \frac{1}{\sqrt2}\end{pmatrix}\begin{pmatrix}a_0\\a_1\end{pmatrix}\right|^2-\left|\begin{pmatrix}\frac{1}{\sqrt2}&&\frac{1}{\sqrt2}\end{pmatrix}\begin{pmatrix}a_0\\a_1\end{pmatrix}\right|^2\right)^2+\left(\left|\begin{pmatrix} \frac{1}{\sqrt2}&&\frac{i}{\sqrt2}\end{pmatrix}\begin{pmatrix}a_0\\a_1\end{pmatrix}\right|^2-\left|\begin{pmatrix}\frac{1}{\sqrt2}&&-\frac{i}{\sqrt2}\end{pmatrix}\begin{pmatrix}a_0\\a_1\end{pmatrix}\right|^2\right)^{2}+\left(\left|\begin{pmatrix} 1&&0\end{pmatrix}\begin{pmatrix}a_0\\a_1\end{pmatrix}\right|^2-\left|\begin{pmatrix}0&&1\end{pmatrix}\begin{pmatrix}a_0\\a_1\end{pmatrix}\right|^{2}\right)^{2}=1$ $(|\frac{{a_{0}-a_{1}}}{\sqrt{2}}|^{2}-|\frac{{a_{0}+a_{1}}}{\sqrt{2}}|^{2})^{2}+(|\frac{a_0+ia_1}{\sqrt2}|^2-|\frac{a_0-ia_1}{\sqrt2}|^2)^2+(|a_{0}|^2-|a_{1}|^2)^2 = 1$    
$(\frac{|{a_{0}-a_{1}}|^2-|{a_{0}+a_{1}}|^2}{|\sqrt2|^2})^{2}+(\frac{|a_0+ia_1|^2-|a_0-ia_1|^2}{|\sqrt2|^2})^2+(|a_{0}|^2-|a_{1}|^2)^2 = 1$    
$\frac{1}{4}(|{a_{0}-a_{1}}|^{2}-|{a_{0}+a_{1}}|^{2})^{2}+ \frac{1}{4}(|a_0+ia_1|^2-|a_0-ia_1|^2)^{2}+(|a_{0}|^2-|a_{1}|^2)^{2}=1$ 

a) $a_0 = \cos\theta$ and $a_1 =\sin\theta$
$(\frac{|{\cos\theta-\sin\theta}|^2-|{\cos\theta+\sin\theta}|^2}{2})^{2}+(\frac{|\cos\theta+i\sin\theta|^2-|\cos\theta-i\sin\theta|^2}{2})^2+(\cos^2\theta-\sin^2\theta)^2 = 1$    
$\frac{(\cos^2\theta-2\cos\theta\sin\theta+\sin^2\theta - \cos^2\theta-2\cos\theta\sin\theta - \sin^2\theta)^2}{4}+\frac{1-1}{4}+(\cos^2\theta-\sin^2\theta)^2 = 1$ 
$\frac{(-4\cos\theta\sin\theta)^2}{4}+(\frac{0}{2})^2+(\cos^2\theta-\sin^2\theta)^2 = 1$ 
$\frac{16\cos^{2}\theta\sin^{2}\theta}{4}+(\cos^2\theta-\sin^2\theta)^2 = 1$ 
$4\cos^2\theta\sin^2\theta+\cos^4\theta-2\cos^2\theta\sin^2\theta+\sin^4\theta = 1$ 
$\cos^{4}\theta+ 2\cos^{2}\theta\sin^{2}\theta+\sin^{4}\theta = 1$ 
$(\cos^2\theta + \sin^{2}\theta)^{2}=1^{2} = 1$  Correct

b) $a_{0}=\frac{1}{\sqrt2}$ and $a_{1}= \frac{1}{\sqrt2}(\cos\phi + i\sin\phi)$ 
$\frac{1}{4}\left(|\frac{1}{\sqrt2} - \frac{1}{\sqrt2}(\cos\phi + i\sin\phi)|^{2} -|\frac{1}{\sqrt2} + \frac{1}{\sqrt2}(\cos\phi + i\sin\phi)|^{2}\right)^{2}+ \frac{1}{4}\left(|\frac{1}{\sqrt2} + \frac{i}{\sqrt2}(\cos\phi + i\sin\phi)|^{2} -|\frac{1}{\sqrt2} - \frac{i}{\sqrt2}(\cos\phi + i\sin\phi)|^{2}\right)^{2} + (|\frac{1}{\sqrt2}|^{2}-|\frac{1}{\sqrt2}(\cos\phi + i\sin\phi)|^{2})^{2} = 1$ $\frac{1}{4}((\frac{1}{\sqrt2}-\frac{1}{\sqrt2}\cos(\phi))^{2}+(\frac{1}{\sqrt2}\sin(\phi))^{2}-((\frac{1}{\sqrt2}+\frac{1}{\sqrt2}\cos(\phi))^{2}+(\frac{1}{\sqrt2}\sin(\phi))^{2}))^{2} + \frac{1}{4}\left(|\frac{1}{\sqrt2} + \frac{i}{\sqrt2}(\cos\phi + i\sin\phi)|^{2} -|\frac{1}{\sqrt2} - \frac{i}{\sqrt2}(\cos\phi + i\sin\phi)|^{2}\right)^{2} + (|\frac{1}{\sqrt2}|^{2}-|\frac{1}{\sqrt2}(\cos\phi + i\sin\phi)|^{2})^{2} = 1$
$\frac{1}{4}(\frac{1}{2}-\cos(\phi)+ \frac{1}{2}\cos^2(\phi)+\frac{1}{2}\sin^2(\phi)-((\frac{1}{\sqrt2}+\frac{1}{\sqrt2}\cos(\phi))^{2}+(\frac{1}{\sqrt2}\sin(\phi))^{2}))^{2} + \frac{1}{4}\left(|\frac{1}{\sqrt2} + \frac{i}{\sqrt2}(\cos\phi + i\sin\phi)|^{2} -|\frac{1}{\sqrt2} - \frac{i}{\sqrt2}(\cos\phi + i\sin\phi)|^{2}\right)^{2} + (|\frac{1}{\sqrt2}|^{2}-|\frac{1}{\sqrt2}(\cos\phi + i\sin\phi)|^{2})^{2} = 1$ $\frac{1}{4}(\frac{1}{2}-\cos(\phi)+ \frac{1}{2}\cos^2(\phi)+\frac{1}{2}\sin^2(\phi)-(\frac{1}{2}+\cos(\phi)+ \frac{1}{2}\cos^2(\phi)+\frac{1}{2}\sin^2(\phi)))^{2} + \frac{1}{4}\left(|\frac{1}{\sqrt2} + \frac{i}{\sqrt2}(\cos\phi + i\sin\phi)|^{2} -|\frac{1}{\sqrt2} - \frac{i}{\sqrt2}(\cos\phi + i\sin\phi)|^{2}\right)^{2} + (|\frac{1}{\sqrt2}|^{2}-|\frac{1}{\sqrt2}(\cos\phi + i\sin\phi)|^{2})^{2} = 1$ $\frac{1}{4}(\frac{1}{2}-\cos(\phi)+ \frac{1}{2}\cos^2(\phi)+\frac{1}{2}\sin^2(\phi)-\frac{1}{2}-\cos(\phi)- \frac{1}{2}\cos^2(\phi)-\frac{1}{2}\sin^2(\phi)))^{2} + \frac{1}{4}\left(|\frac{1}{\sqrt2} + \frac{i}{\sqrt2}(\cos\phi + i\sin\phi)|^{2} -|\frac{1}{\sqrt2} - \frac{i}{\sqrt2}(\cos\phi + i\sin\phi)|^{2}\right)^{2} + (|\frac{1}{\sqrt2}|^{2}-|\frac{1}{\sqrt2}(\cos\phi + i\sin\phi)|^{2})^{2} = 1$ $\frac{1}{4}(-2\cos(\phi))^{2} + \frac{1}{4}\left(|\frac{1}{\sqrt2} + \frac{i}{\sqrt2}(\cos\phi + i\sin\phi)|^{2} -|\frac{1}{\sqrt2} - \frac{i}{\sqrt2}(\cos\phi + i\sin\phi)|^{2}\right)^{2} + (|\frac{1}{\sqrt2}|^{2}-|\frac{1}{\sqrt2}(\cos\phi + i\sin\phi)|^{2})^{2} = 1$
$\cos^2(\phi) + \frac{1}{4}\left(|\frac{1}{\sqrt2} + \frac{1}{\sqrt2}(i\cos\phi -\sin\phi)|^{2} -|\frac{1}{\sqrt2} - \frac{1}{\sqrt2}(i\cos\phi -\sin\phi)|^{2}\right)^{2} + (|\frac{1}{\sqrt2}|^{2}-|\frac{1}{\sqrt2}(\cos\phi + i\sin\phi)|^{2})^{2} = 1$  $\cos^{2}(\phi) + \frac{1}{4}\left(((\frac1{\sqrt2}+\frac1{\sqrt2}\sin\phi)^2+(\frac1{\sqrt2}\cos\phi)^2)-((\frac1{\sqrt2}-\frac1{\sqrt2}\sin\phi)^2+(\frac1{\sqrt2}\cos\phi)^2)\right)^{2} + (|\frac{1}{\sqrt2}|^{2}-|\frac{1}{\sqrt2}(\cos\phi + i\sin\phi)|^{2})^{2} = 1$
$\cos^{2}(\phi) + \frac{1}{4}\left(\frac12 +\sin\phi+\frac12\sin^{2}\phi+\frac1{2}\cos^{2}\phi-(\frac12 -\sin\phi+\frac12\sin^{2}\phi+\frac1{2}\cos^{2}\phi)\right)^{2} + (|\frac{1}{\sqrt2}|^{2}-|\frac{1}{\sqrt2}(\cos\phi + i\sin\phi)|^{2})^{2} = 1$
$\cos^{2}(\phi) + \frac{1}{4}\left(\frac12 +\sin\phi+\frac12\sin^{2}\phi+\frac1{2}\cos^{2}\phi-\frac12 +\sin\phi-\frac12\sin^{2}\phi-\frac1{2}\cos^{2}\phi\right)^{2} + (|\frac{1}{\sqrt2}|^{2}-|\frac{1}{\sqrt2}(\cos\phi + i\sin\phi)|^{2})^{2} = 1$
$\cos^{2}(\phi) + \frac{1}{4}\left(2\sin\phi\right)^{2} + (\frac{1}{2}-\frac12)^{2} = 1$
$\cos^2\phi +\sin^2\phi =1$ Correct

### 3. A useful matrix
$p_0^z-p_1^z = \Bra \psi M \Ket \psi$  
$\left|\begin{pmatrix}1&&0\end{pmatrix}\begin{pmatrix}a_0\\a_1\end{pmatrix}\right|^2-\left|\begin{pmatrix}0&&1\end{pmatrix}\begin{pmatrix}a_0\\a_1\end{pmatrix}\right|^{2}=|a_0|^2-|a_1|^2=a_0^*a_0 - a_1^*a_1=\begin{pmatrix}a_{0}^*&&a_{1}^*\end{pmatrix}M\begin{pmatrix}a_{0}\\a_{1}\end{pmatrix}$ 

For this to be true, the following must hold: $M\Ket\psi=M\begin{pmatrix}a_{0}\\a_{1}\end{pmatrix} = \begin{pmatrix}a_0\\-a_1\end{pmatrix}$ 
An example where this is true is when $M = \begin{pmatrix}1&&0\\0&&-1\end{pmatrix} = \sigma_3$  
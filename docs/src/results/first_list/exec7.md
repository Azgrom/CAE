# Exercício 7

**Aluno:** Rafael Lúcio Negrão Cordeiro<br/>
**Matrícula:** 201310323<br/>
**Disciplina:** CET961 - Engenharia Assistida por Computador

---
1. Uma estrutura é composta de dois elementos unidimensionais de barra (conforme Fig. 7). Quando uma força de $10 N$ é aplicada ao nó 2, calcule o vetor dos deslocamentos<br/> $Q^T = u_1, u_2, u_3$ usando o método de elementos finitos.

    ![](img/exec7_structure.png)

    <span class="caption">Figura 7: Ilustraçao da questao 7</span>
```python
k1 = 200 # N / m
k2 = 300 # N / m

f2 = 10 # N

u1 = u3 = 0
```
#### Compondo o sistema na notaçao matricial $[K^{(g)}]\{U^{(g)}\} = \{F^{(g)}\}$, temos:

$$
\overbrace{
    \begin{bmatrix}
        k_1 & -k_1 & 0\\
        -k_1 & k_1 + k_2 & -k_2\\
        0 & -k_2 & k_2
    \end{bmatrix}
}^{[K^{(g)}]}
\overbrace{
    \begin{Bmatrix}
        u_1\\
        u_2\\
        u_3
    \end{Bmatrix}
}^{\{U^{(g)}\}}=\overbrace{
    \begin{Bmatrix}
        f_1\\
        f_2\\
        f_3
    \end{Bmatrix}
}^{\{F^{(g)}\}}
$$
Onde, considerando que queremos apenas os deslocamentos dos corpos e as forças nas paredes, temos:
$$
\begin{bmatrix}
    200 & -200 & 0\\
    -200 & 500 & -300\\
    0 & -300 & 300
\end{bmatrix}
\begin{Bmatrix}
    0\\
    u_2\\
    0
\end{Bmatrix}=\begin{Bmatrix}
    1\\
    10\\
    1
\end{Bmatrix}
$$
#### Ao executar as multiplicações das matrizes, temos:
$$
\begin{equation}
    \begin{cases}
        -200u_2 = R_1\\
         500u_2 = 10\\
        -300u_2 = R_3
    \end{cases}
\end{equation}
$$

Se isolarmos todas as variáveis para o lado esquerdo da equaçao, teremos: $ \begin{equation}
    \begin{cases}
        -200u_2 - R_1 + 0R_3= 0\\
         500u_2 + 0R_1 + 0R_3= 10\\
        -300u_2 + 0R_1 - R_3 = 0
    \end{cases}
\end{equation} $

Da algebra linear, verifica-se que pode-se resolver um sistema de 2 equaçoes com 2 variáveis com uma matriz de seus coeficientes:

$$
\begin{bmatrix}
    -200 & -1 & 0\\
     500 &  0 & 0\\
    -300 &  0 & -1
\end{bmatrix}
\begin{bmatrix}
    R_1\\
    u_2\\
    R_3
\end{bmatrix}
=
\begin{bmatrix}
    0\\
    10\\
    0
\end{bmatrix}
$$

Existe uma biblioteca no python dedicada a resolver equações organizadas na forma matricial acima. No pacote numpy, módulo de algebra linear. O código a seguir criará os vetores da matriz acima e executará o módulo de algebra linear do numpy, já entregando os resultados.

```python
import numpy as np

# coeffs de coeficientes
coeffs = [[  -k1,    -1, 0],
          [k1 + k2,   0, 0],
          [  -k2,     0,-1]]

# image de conjunto imagem de uma funç~ao
image = [0, 10, 0]

# Transformando os vetores nativos python em vetores numpy
coeffs = np.array(coeffs)
image = np.array(image)
```

```python
# Visualizando o conteúdo dos vetores

coeffs, image
```

```python
(array([[-200,   -1,    0],
        [ 500,    0,    0],
        [-300,    0,   -1]]), array([ 0, 10,  0]))
```

```python
# Resolvendo ele com o módulo de álgebra linear

variaveis = np.linalg.solve(coeffs, image)

print('Os resultados são: R1 = %.2em, u2 = %.2eN, R3 = %.2eN' % tuple(variaveis))
```
<span class="caption">Os resultados são: $R_1 = 2.00 x 10^{-2} N$, $u_2 = -4.00 N$ e $R_3 = -6.00 N$</span>

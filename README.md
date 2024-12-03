# Conservação de Energia Mecânica e o Problema do Looping

## Descrição Básica do Projeto
Este projeto é uma simulação criada para ilustrar o conceito de conservação de energia mecânica e seu papel no problema do looping. A ideia central é demonstrar como a energia potencial gravitacional é convertida em energia cinética enquanto um objeto percorre um looping circular, sem considerar os efeitos de atrito.

**Um objeto atravessando um looping circular:**
Imagine um corpo que inicia seu movimento a partir de uma altura $h$ acima do topo de um looping de raio $R$. Este objeto possui energia potencial gravitacional no início e, à medida que se move, converte essa energia em energia cinética para completar o percurso no looping. Este projeto permite explorar como a altura inicial do corpo impacta sua habilidade de completar o looping.

O código foi implementado em Python, permitindo que os usuários configurem parâmetros como altura inicial, raio do looping e aceleração da gravidade para observar diferentes cenários.

<p align="center">
  <img src="imagens/looping.png" alt="Simulação de looping">
  <br>
</p>

## Conceitos de Física e Modelo Matemático

### Conservação de Energia Mecânica

No contexto da conservação de energia mecânica, a energia total do sistema permanece constante na ausência de forças dissipativas, como o atrito. A energia total pode ser expressa como a soma da energia potencial gravitacional ($E_p$) e da energia cinética ($E_c$):

$$
E_{total} = E_p + E_c
$$

A energia potencial gravitacional é dada por:

$$
E_p = m \cdot g \cdot h
$$

e a energia cinética por:

$$
E_c = \frac{1}{2} m \cdot v^2
$$

Ao longo do movimento, a energia é convertida entre $E_p$ e $E_c$. A condição para completar o looping é que o objeto tenha energia suficiente para superar o ponto mais alto do percurso, onde a velocidade mínima é:

$$
v_{min} = \sqrt{g \cdot R}
$$

### Trajetória no Looping

A partir da conservação de energia, a posição e a velocidade do objeto são calculadas em função do tempo. O movimento inclui uma descida vertical até a entrada no looping e, em seguida, um movimento circular descrito por:

$$
\theta = \arccos\left(\frac{y}{R}\right)
$$

onde $\theta$ é o ângulo no looping, $y$ é a altura atual, e $R$ é o raio do looping.

<p align="center">
  <img src="imagens/conservacao_energia.png" alt="Conceitos de conservação de energia">
  <br>
  <em>Figura 1: Conversão de energia durante o looping.</em>
</p>

## Implementação

- **Linguagens e Pacotes:**
  Este projeto foi desenvolvido em Python, utilizando os pacotes:
  - **NumPy:** para cálculos matemáticos.
  - **Matplotlib:** para criação de gráficos e animações.

## Como Usar

### Instalação e Dependências
1. Certifique-se de ter o Python 3.6+ instalado.
2. Instale os pacotes necessários com o comando:

```bash
pip install -r requirements.txt
```

### Execução da Simulação
1. Baixe o código e os arquivos auxiliares.
2. Execute o script principal com:

```bash
python main.py
```

3. Configure os seguintes parâmetros no código, conforme desejado:
   - Altura inicial do objeto ($h$).
   - Raio do looping ($R$).
   - Aceleração da gravidade ($g$).
   - Duração da simulação.

### Saída do Programa
O programa gera uma animação que mostra o movimento do objeto, destacando a conservação de energia mecânica durante o percurso do looping.

## Informações sobre o Projeto
Este projeto foi desenvolvido por:

Julia Marcolan Teixeira: juliamarcolan@usp.br

Como exemplo de entrega para a disciplina 7600105 - Física Básica I (2024) da USP-São Carlos, ministrada pelos professores Krissia de Zawadzki e Esmerindo de Sousa Bernardes.

## Referências
(1) Bernardes, E. de S. (2024). Dinâmica-v2 (Notas de aula). 7600105 - Física Básica I. Universidade de São Paulo, São Carlos.


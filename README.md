# ChessAI: Inteligência Artificial Aprendendo Xadrez

## 📌 Sobre o Projeto
Este projeto tem como objetivo desenvolver e treinar duas inteligências artificiais para jogar xadrez, utilizando aprendizado de máquina. Em primeiro momento a intenção é fazer com que dois modelos que usam algortimos distintos joguem xadrez. Posteriormente, depois que os dois modelos estiverem implementados será possívei fazer testes mais complexos, como por exemplo: colocar ambos os modelos para jogar um contra o outro e avaliar o desempenho; usar as partidas em que eles se enfrentam para retreinar os modelos e etc. 

## 🧠 Tecnologias Utilizadas
- Python 🐍
- `chess` ♟️ (biblioteca para manipulação do jogo de xadrez)
- `Scikit-Learn` (para uma árvore ou floresta de decisão)
- `PyTorch` (para uma rede neural)
- `Flask` (Como API para visualizar as partidas)
- `Jupyter Notebook` (para experimentação e análise)

## 🚀 Como Executar o Projeto

### 1️⃣ Clonar o Repositório
```bash
git clone [https://github.com/GusttavoOliveira/chessAI.git](https://github.com/GusttavoOliveira/chessAI.git)
cd chessAI
```

### 2️⃣ Criar e Ativar um Ambiente Virtual
```bash
python -m venv venv  # Criar o ambiente virtual
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```

### 3️⃣ Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Executar a Simulação
```bash
python main.py
```

## 📊 Estrutura do Projeto
```
chessAI/
│-- data/            # Armazena dados de treinamento e logs
│-- models/          # Modelos treinados da IA
│-- scripts/         # Scripts auxiliares para análise e treinamento
│-- main.py          # Arquivo principal para rodar o treinamento
│-- README.md        # Documentação do projeto
│-- requirements.txt # Dependências do projeto
```

## 📈 Como Funciona o Treinamento
1. As duas IAs começam jogando partidas aleatórias.
2. Cada IA ajusta sua estratégia usando aprendizado por reforço.
3. A cada nova partida, as IAs se tornam mais eficientes e competitivas.
4. O progresso pode ser acompanhado através de estatísticas e gráficos gerados pelo script.

## 📌 Roadmap
- [X] Implementar motor básico de jogo
- [ ] Criar a lógica do modelo de árvore de decisão
- [ ] Criar a lógica do modelo de rede neural
- [ ] Treinar e salvar modelos
- [X] Criar visualização gráfica das partidas
- [ ] Desenvolver um dashboard para acompanhar o progresso

## 🤝 Contribuição
Contribuições são bem-vindas! Para contribuir:
1. Faça um **fork** do projeto 🍴
2. Crie um **branch** para sua funcionalidade (`git checkout -b minha-feature`)
3. Faça um **commit** das suas alterações (`git commit -m 'Adicionando nova feature'`)
4. Faça um **push** para o branch (`git push origin minha-feature`)
5. Abra um **Pull Request** 📢

---
✍️ Desenvolvido por [Luiz Gusttavo](https://github.com/GusttavoOliveira) 🚀


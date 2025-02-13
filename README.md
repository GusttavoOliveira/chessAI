# ChessAI: Inteligência Artificial Aprendendo Xadrez

## 📌 Sobre o Projeto
Este projeto tem como objetivo desenvolver e treinar duas inteligências artificiais para jogar xadrez, utilizando aprendizado de máquina e técnicas de reforço. As IAs irão evoluir suas estratégias jogando repetidamente uma contra a outra, aprendendo com suas partidas e ajustando suas decisões para melhorar seu desempenho ao longo do tempo.

## 🧠 Tecnologias Utilizadas
- Python 🐍
- `chess` ♟️ (biblioteca para manipulação do jogo de xadrez)
- `TensorFlow` ou `PyTorch` (para aprendizado de máquina)
- `OpenAI Gym` (para ambiente de reforço)
- `Flask` ou `FastAPI` (se desejar criar uma API para visualização das partidas)
- `Matplotlib` (para visualização do progresso do treinamento)
- `Jupyter Notebook` (para experimentação e análise)

## 🚀 Como Executar o Projeto

### 1️⃣ Clonar o Repositório
```bash
git clone https://github.com/GusttavoOliveira/chessAI.git
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
- [ ] Implementar motor básico de jogo
- [ ] Criar a lógica de aprendizado por reforço
- [ ] Treinar e salvar modelos
- [ ] Criar visualização gráfica das partidas
- [ ] Desenvolver um dashboard para acompanhar o progresso

## 🤝 Contribuição
Contribuições são bem-vindas! Para contribuir:
1. Faça um **fork** do projeto 🍴
2. Crie um **branch** para sua funcionalidade (`git checkout -b minha-feature`)
3. Faça um **commit** das suas alterações (`git commit -m 'Adicionando nova feature'`)
4. Faça um **push** para o branch (`git push origin minha-feature`)
5. Abra um **Pull Request** 📢

## 📜 Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---
✍️ Desenvolvido por [Gusttavo Oliveira](https://github.com/GusttavoOliveira) 🚀


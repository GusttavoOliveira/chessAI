from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from utils import load_games_from_pgn
from utils import extract_features_from_position
import pickle

class DecisionTreeChessModel():
    def __init__(self, max_games=1000):
        self.max_games = max_games
        self.x, self.y = load_games_from_pgn('../api/data/lichess_db_standard_rated_2014-08.pgn', max_games)
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.x, self.y, test_size=0.2, random_state=42)

    def train(self):
        self.model = RandomForestClassifier()
        self.model.fit(self.x_train, self.y_train)

    def predict(self, x):
        return self.model.predict(x)

    def accuracy(self):
        return self.model.score(self.x_test, self.y_test)

    def save(self, path):
        with open(path, 'wb') as f:
            pickle.dump(self.model, f)

    def get_best_moves(self, board):
        features = extract_features_from_position(board)
        legal_moves = [move.uci() for move in board.legal_moves]
        

        # Obter probabilidades para todos os movimentos legais
        move_probabilities = {}
        probabilities = self.model.predict_proba([features])[0]
        classes = self.model.classes_

        for i, move in enumerate(legal_moves):
            if move in legal_moves:
                move_probabilities[move] = probabilities[i]

        # Escolher o melhor movimento com base nas probabilidades
        best_move = max(move_probabilities, key=move_probabilities.get)

        return chess.Move.from_uci(best_move)
        



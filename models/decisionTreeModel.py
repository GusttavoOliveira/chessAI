from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from utils import load_games_from_pgn
from utils import extract_features_from_position
import pickle

class DecisionTreeChessModel():
    def __init__(self, max_games=1000):
        self.max_games = max_games
        self.x, self.y = load_games_from_pgn(max_games)
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.x, self.y, test_size=0.2, random_state=42)

    def train(self):
        self.model = DecisionTreeClassifier()
        self.model.fit(self.x_train, self.y_train)

    def predict(self, x):
        return self.model.predict(x)

    def evaluate(self):
        return self.model.score(self.x_test, self.y_test)

    def save(self, path):
        with open(path, 'wb') as f:
            pickle.dump(self.model, f)


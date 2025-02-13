import chess
import chess.svg


class ChessGame:
    def __init__(self):
        self.board = chess.Board()
        self.svg_path = "static/board.svg"
        self.save_svg()

    def save_svg(self):
        with open(self.svg_path, "w") as f:
            f.write(chess.svg.board(board=self.board))

    def make_move(self, move):
        """Aplica um movimento ao tabuleiro e o atualiza."""
        try:
            self.board.push_san(move)
            self.save_svg()
            return {"status": "success", "message": "Move applied successfully."}
        except chess.InvalidMoveError:
            return {"status": "error", "message": "Invalid move!"}
        except chess.IllegalMoveError:
            return {"status": "error", "message": "Illegal move!"}
        except chess.AmbiguousMoveError:
            return {"status": "error", "message": "Ambiguous move!"}
        
    def get_board(self):
        with open(self.svg_path, "r") as f:
            return f.read()

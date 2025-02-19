import chess
import chess.svg
import random

class ChessGame():
    def __init__(self):
        self.board = chess.Board()
        self.svg_path = "../api/static/board.svg"
        self.save_svg()
        random.seed(42)

    def save_svg(self):
        with open(self.svg_path, "w") as f:
            f.write(chess.svg.board(board=self.board))

    def make_move(self, move):
        """Aplica um movimento ao tabuleiro e o atualiza."""
        try:
            self.board.push_san(move)
            self.save_svg()
            if self.board.is_checkmate():
                return {"status": "success", "message": "Checkmate!"}
            elif self.board.is_stalemate():
                return {"status": "success", "message": "Stalemate!"}
            elif self.board.is_insufficient_material():
                return {"status": "success", "message": "Insufficient material!"}
            elif self.board.is_seventyfive_moves():
                return {"status": "success", "message": "Fifty move rule!"}
            elif self.board.is_fivefold_repetition():
                return {"status": "success", "message": "Fivefold repetition!"}
            elif self.board.is_threefold_repetition():
                return {"status": "success", "message": "Threefold repetition!"}
            else:
                return {"status": "success", "message": "Move applied successfully."}
            
        except chess.InvalidMoveError:
            return {"status": "error", "message": "Invalid move!"}
        except chess.IllegalMoveError:
            return {"status": "error", "message": "Illegal move!"}
        except chess.AmbiguousMoveError:
            return {"status": "error", "message": "Ambiguous move!"}
    
    def make_response_move(self):
        legal_moves = list(self.board.legal_moves)
        move = str(random.choice(legal_moves))
        self.make_move(move)
        
        return {"status": "Response success", "message": "Response move applied successfully."}
        
    def get_board(self):
        with open(self.svg_path, "r") as f:
            return f.read()

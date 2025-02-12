import chess
import chess.svg


def display_new_move():
    board = chess.Board()

    while not board.is_game_over():
        # Salva o tabuleiro como arquivo SVG
        with open("board.svg", "w") as f:
            f.write(chess.svg.board(board=board))
        
        move = input("Enter your move: ")

        try:
            board.push_san(move)
        except chess.InvalidMoveError:
            print("Invalid move!")
            continue
        except chess.IllegalMoveError:
            print("Illegal move!")
            continue
        except chess.AmbiguousMoveError:
            print("Ambiguous move!")
            continue

        if board.is_checkmate():
            print("Checkmate!")
            break

        if board.is_check():
            print("Check!")

    # Salva o tabuleiro como arquivo SVG
    with open("board.svg", "w") as f:
        f.write(chess.svg.board(board=board))
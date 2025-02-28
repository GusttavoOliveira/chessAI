from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import chess.pgn
import io

def extract_features_from_position(board):
    features = []

    # A posição das peças será codificada como números
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        piece_value = 0
        if piece is not None:
            # Valores positivos para as peças brancas, negativos para as peças pretas
            piece_value = piece.piece_type*(1 if piece.color == chess.WHITE else -1)
        features.append(piece_value)

    # Adicionar informações sobre o movimento
    features.append(len(list(board.legal_moves))) # Número de movimentos legais
    features.append(1 if board.is_check() else 0) # Se há um xeque
    features.append(1 if board.is_checkmate() else 0) # Se há um xeque-mate
    features.append(1 if board.turn == chess.WHITE else 0) # Se é a vez do branco ou do preto
    
    return np.array(features)

def load_games_from_pgn(pgn_file, max_games=1000):
    x = []  # features
    y = []  # jogadas escolhidas (alvos)

    with open(pgn_file, 'r') as f:
        for i in range(max_games):
            game = chess.pgn.read_game(f)
            if game is None:
                break
            
            if game.headers['Result'] == '*' or len(list(game.mainline_moves())) < 10:
                continue

            board = game.board()
            for move in game.mainline_moves():
                # Extrair características da posição atual
                features = extract_features_from_position(board)

                move_uci = move.uci()

                # Adicionar as características à lista de features
                x.append(features)

                # Adicionar a jogada escolhida como alvo
                y.append(move_uci)
                
                # Aplicar a jogada na posição atual
                board.push(move)
                
                # Se chegarmos ao final do jogo, parar o loop
                if board.is_game_over():
                    break
    
    return np.array(x), np.array(y)
                


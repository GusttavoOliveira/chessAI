from flask import Flask, render_template, jsonify, request, send_file
from flask_socketio import SocketIO
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.chess_logic import ChessGame


app = Flask(__name__, static_folder="static", template_folder="templates")
socketio = SocketIO(app, cors_allowed_origins="*")
game = ChessGame()

@app.route("/")
def index():
    """Renderiza a página inicial com o tabuleiro de xadrez."""
    return render_template("index.html")

@app.route("/board")
def get_board():
    """Retorna o SVG do tabuleiro de xadrez."""
    return send_file(game.svg_path, mimetype="image/svg+xml")

@app.route("/move", methods=["POST"])
def make_move():
    """Recebe um movimento e aplica-o ao tabuleiro."""
    data = request.get_json()
    move = data.get("move")

    if not move:
        response = jsonify({"status": "error", "message": "No move provided."})
        return response

    response = game.make_move(move)

    if response["status"] == "success":
        
        # Validar casos especiais
        if response["message"] == "Checkmate!":
            socketio.emit("update_board", {"message": "Checkmate!"})
            return jsonify(response)
        elif response["message"] == "Stalemate!":
            socketio.emit("update_board", {"message": "Stalemate!"})
            return jsonify(response)
        elif response["message"] == "Insufficient material!":
            socketio.emit("update_board", {"message": "Insufficient material!"})
            return jsonify(response)
        elif response["message"] == "Fifty move rule!":
            socketio.emit("update_board", {"message": "Fifty move rule!"})
            return jsonify(response)
        elif response["message"] == "Fivefold repetition!":
            socketio.emit("update_board", {"message": "Fivefold repetition!"})
            return jsonify(response)
        elif response["message"] == "Threefold repetition!":
            socketio.emit("update_board", {"message": "Threefold repetition!"})
            return jsonify(response)

        # Caso comum de movimentação valida
        socketio.emit("update_board", {"message": "Board updated!"})
        game.make_response_move()

    return jsonify(response)

if __name__ == "__main__":
    socketio.run(app, debug=True)
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
        return jsonify({"status": "error", "message": "No move provided."})

    response = game.make_move(move)

    if response["status"] == "success":
        socketio.emit("update_board", {"message": "Board updated!"})

    return jsonify(response)

if __name__ == "__main__":
    socketio.run(app, debug=True)
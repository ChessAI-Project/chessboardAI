import chess
import chess.engine
from received import *
board = chess.Board()

engine = chess.engine.SimpleEngine.popen_uci(r"/home/akash/stockfish/stockfish-ubuntu-x86-64-modern")

def reset_board():
    global board
    board = chess.Board()

def chessmove(move, depth):
    board.push_san(move)
    print(board)
    # Get the best move from the engine
    result = engine.play(board, chess.engine.Limit(depth=depth))  # Set a time limit for the engine's move
    best_move = result.move
    
    # Apply the engine's move to the board
    board.push(best_move)
    print("Engine's Move:", best_move)
    print(board)
    received(str(best_move))
    return str(best_move)

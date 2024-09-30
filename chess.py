# Import the required libraries
import chess
import chess.svg
from IPython.display import SVG

# Initialize the chessboard
board = chess.Board()

# Display the board as an SVG image
SVG(chess.svg.board(board=board))

# Function to print the current board
def print_board(board):
    print(board)

# Print the current state of the board
print_board(board)
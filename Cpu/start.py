import time
from crop import *
from boxout import *
from pieces import *
from compute import *
from newai import *
import pickle
def start(file):
    start = time.time()
    crop(file)
    image_path = 'cropped.png'
    rows = 8  # Adjust this value based on your chessboard
    cols = 8  # Adjust this value based on your chessboard
    output_folder = 'out/'  # Change this to your desired output folder
    find_chessboard_intersections(image_path, rows, cols, output_folder)
    found = pieces(output_folder)

    # Load the initial array from a pickle file if it exists
    try:
        with open('initial_array.pkl', 'rb') as initial_file:
            initial_array = pickle.load(initial_file)
    except FileNotFoundError:
        # If the file is not found, use the default initial array
        initial_array = [
            [2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2, 2],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1]
        ]
    color = read_variable()
    print("the AI is playing" + str(color))
    # Create an instance of ChessArrayComparator
    # comparator = ChessArrayComparator(initial_array)

    # Check the initial array once
    # if playerIsWhite:
    #     turn = 1
    # else:
    #     turn = 2
    print("Intial Array:")
    for row in initial_array:
        print(row)
    move = findMove(initial_array, found, color) #change to 2 if AI is playing black




    # If the initial array is checked and some pieces are moved, update the initial array
    if move:
        initial_array = found
        # Save the updated initial array using pickle
        with open('initial_array.pkl', 'wb') as initial_file:
            pickle.dump(initial_array, initial_file)

    chessai = chessmove(move)
    end = time.time()
    output = "It took " + str(end - start) + " to finish. " + "The output saved in " + output_folder + " moves that occurred " + move
    print(output)
    return chessai

def read_variable():
    filename = "AIcolor.pkl"
    try:
        if os.path.exists(filename):
            with open(filename, "rb") as file:
                return pickle.load(file)
        else:
            return None
    except (IOError, EOFError, pickle.PickleError) as e:
        print("Error reading variable:", e)
        return None
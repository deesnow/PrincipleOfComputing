import poc_ttt_provided as provided

game = provided.TTTBoard(3)

print game
print game.get_empty_squares()
print game.check_win()


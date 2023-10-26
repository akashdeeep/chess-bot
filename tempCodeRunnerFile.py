:
        copy_white_locations[piece_ind] = move
        if move in copy_black_locations:
            copy_black_pieces.pop(copy_black_locations.index(move))
            copy_black_locations.remove(move)
        if copy_white_pieces[piece_ind] == "P" and move[1] == 7:
            copy_white_pieces[piece_ind] = "Q"
    else:
        copy_black_locations[piece_ind] = move
        if move in copy_white_locations:
            copy_white_pieces.pop(copy_white_locations.index(move))
            copy_white_locations.remove(move)
        if copy_black_pieces[piece_ind] == "P" and move[1] == 0:
            copy_black_pieces[piece_ind] = "Q"
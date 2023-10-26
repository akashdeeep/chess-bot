def pawn_moves(locations, other_locations, pieces, other_pieces, color, coord):
    moves_list = []
    if color == "white":
        if (
            (coord[0], coord[1] + 1) not in locations
            and (
                coord[0],
                coord[1] + 1,
            )
            not in other_locations
            and coord[1] >= 0
        ):
            moves_list.append((coord[0], coord[1] + 1))
        if (
            (coord[0], coord[1] + 1) not in locations
            and (
                coord[0],
                coord[1] + 1,
            )
            not in other_locations
            and (coord[0], coord[1] + 2) not in locations
            and (
                coord[0],
                coord[1] + 2,
            )
            not in other_locations
            and coord[1] == 1
        ):
            moves_list.append((coord[0], coord[1] + 2))
        if (coord[0] + 1, coord[1] + 1) in other_locations:
            moves_list.append((coord[0] + 1, coord[1] + 1))
        if (coord[0] - 1, coord[1] + 1) in other_locations:
            moves_list.append((coord[0] - 1, coord[1] + 1))

    else:
        if (
            (coord[0], coord[1] - 1) not in locations
            and (
                coord[0],
                coord[1] - 1,
            )
            not in other_locations
            and coord[1] >= 1
            and coord[1] < 7
        ):
            moves_list.append((coord[0], coord[1] - 1))
        if (
            (coord[0], coord[1] - 1) not in locations
            and (
                coord[0],
                coord[1] - 1,
            )
            not in other_locations
            and (coord[0], coord[1] - 2) not in locations
            and (
                coord[0],
                coord[1] - 2,
            )
            not in other_locations
            and coord[1] == 6
        ):
            moves_list.append((coord[0], coord[1] - 2))
        if (coord[0] + 1, coord[1] - 1) in other_locations:
            moves_list.append((coord[0] + 1, coord[1] - 1))
        if (coord[0] - 1, coord[1] - 1) in other_locations:
            moves_list.append((coord[0] - 1, coord[1] - 1))
    return moves_list


def rook_moves(locations, other_locations, pieces, other_pieces, color, coord):
    moves_list = []

    for i in range(4):
        if i == 0:
            x = 1
            y = 0
        elif i == 1:
            x = -1
            y = 0
        elif i == 2:
            x = 0
            y = 1
        else:
            x = 0
            y = -1
        for j in range(8):
            new_coord = (coord[0] + x * (j + 1), coord[1] + y * (j + 1))
            if new_coord in locations:
                break
            elif new_coord in other_locations:
                moves_list.append(new_coord)
                break
            elif (
                new_coord[0] < 0
                or new_coord[0] > 7
                or new_coord[1] < 0
                or new_coord[1] > 7
            ):
                break
            else:
                moves_list.append(new_coord)
    return moves_list


def knight_moves(locations, other_locations, pieces, other_pieces, color, coord):
    moves_list = []
    for i in range(8):
        if i == 0:
            x = 1
            y = 2
        elif i == 1:
            x = 1
            y = -2
        elif i == 2:
            x = -1
            y = 2
        elif i == 3:
            x = -1
            y = -2
        elif i == 4:
            x = 2
            y = 1
        elif i == 5:
            x = 2
            y = -1
        elif i == 6:
            x = -2
            y = 1
        else:
            x = -2
            y = -1
        new_coord = (coord[0] + x, coord[1] + y)
        if new_coord in locations:
            continue
        elif new_coord in other_locations:
            moves_list.append(new_coord)
            continue
        elif (
            new_coord[0] < 0 or new_coord[0] > 7 or new_coord[1] < 0 or new_coord[1] > 7
        ):
            continue
        else:
            moves_list.append(new_coord)
    return moves_list


def bishop_moves(locations, other_locations, pieces, other_pieces, color, coord):
    moves_list = []
    for i in range(4):
        if i == 0:
            x = 1
            y = 1
        elif i == 1:
            x = 1
            y = -1
        elif i == 2:
            x = -1
            y = 1
        else:
            x = -1
            y = -1
        for j in range(8):
            new_coord = (coord[0] + x * (j + 1), coord[1] + y * (j + 1))
            if new_coord in locations:
                break
            elif new_coord in other_locations:
                moves_list.append(new_coord)
                break
            elif (
                new_coord[0] < 0
                or new_coord[0] > 7
                or new_coord[1] < 0
                or new_coord[1] > 7
            ):
                break
            else:
                moves_list.append(new_coord)
    return moves_list


def queen_moves(locations, other_locations, pieces, other_pieces, color, coord):
    moves_list = rook_moves(
        locations, other_locations, pieces, other_pieces, color, coord
    ) + bishop_moves(locations, other_locations, pieces, other_pieces, color, coord)
    return moves_list


def king_moves(locations, other_locations, pieces, other_pieces, color, coord):
    moves_list = []
    for i in range(8):
        if i == 0:
            x = 1
            y = 1
        elif i == 1:
            x = 1
            y = -1
        elif i == 2:
            x = -1
            y = 1
        elif i == 3:
            x = -1
            y = -1
        elif i == 4:
            x = 1
            y = 0
        elif i == 5:
            x = -1
            y = 0
        elif i == 6:
            x = 0
            y = 1
        else:
            x = 0
            y = -1
        new_coord = (coord[0] + x, coord[1] + y)
        if new_coord in locations:
            continue
        elif new_coord in other_locations:
            moves_list.append(new_coord)
            continue
        elif (
            new_coord[0] < 0 or new_coord[0] > 7 or new_coord[1] < 0 or new_coord[1] > 7
        ):
            continue
        else:
            moves_list.append(new_coord)
    return moves_list

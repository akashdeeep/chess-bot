import pygame
import copy
import moves

pygame.init()
width = 1000
height = 900
margin = 50
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game")
font = pygame.font.SysFont("Arial", 30)
big_font = pygame.font.SysFont("Arial", 50)
clock = pygame.time.Clock()
fps = 60
counter = 0


white_pieces = [
    "R",
    "N",
    "B",
    "Q",
    "K",
    "B",
    "N",
    "R",
    "P",
    "P",
    "P",
    "P",
    "P",
    "P",
    "P",
    "P",
]
white_locations = [
    (0, 0),
    (1, 0),
    (2, 0),
    (3, 0),
    (4, 0),
    (5, 0),
    (6, 0),
    (7, 0),
    (0, 1),
    (1, 1),
    (2, 1),
    (3, 1),
    (4, 1),
    (5, 1),
    (6, 1),
    (7, 1),
]

black_pieces = [
    "P",
    "P",
    "P",
    "P",
    "P",
    "P",
    "P",
    "P",
    "R",
    "N",
    "B",
    "Q",
    "K",
    "B",
    "N",
    "R",
]
black_locations = [
    (0, 6),
    (1, 6),
    (2, 6),
    (3, 6),
    (4, 6),
    (5, 6),
    (6, 6),
    (7, 6),
    (0, 7),
    (1, 7),
    (2, 7),
    (3, 7),
    (4, 7),
    (5, 7),
    (6, 7),
    (7, 7),
]

captured_pieces_white = []
captured_pieces_black = []

turn_step = 0
selection = 100
valid_moves = []
piece_size = (80, 80)
piece_size_small = (45, 45)
black_queen = pygame.transform.scale(
    pygame.image.load("assets/images/black queen.png"), piece_size
)
black_queen_small = pygame.transform.scale(
    pygame.image.load("assets/images/black queen.png"), piece_size_small
)
white_queen = pygame.transform.scale(
    pygame.image.load("assets/images/white queen.png"), piece_size
)
white_queen_small = pygame.transform.scale(
    pygame.image.load("assets/images/white queen.png"), piece_size_small
)
black_king = pygame.transform.scale(
    pygame.image.load("assets/images/black king.png"), piece_size
)
black_king_small = pygame.transform.scale(
    pygame.image.load("assets/images/black king.png"), piece_size_small
)
white_king = pygame.transform.scale(
    pygame.image.load("assets/images/white king.png"), piece_size
)
white_king_small = pygame.transform.scale(
    pygame.image.load("assets/images/white king.png"), piece_size_small
)
black_bishop = pygame.transform.scale(
    pygame.image.load("assets/images/black bishop.png"),
    ((piece_size[0] * 9) // 10, (piece_size[1] * 9) // 10),
)
black_bishop_small = pygame.transform.scale(
    pygame.image.load("assets/images/black bishop.png"),
    ((piece_size_small[0] * 9) // 10, (piece_size_small[1] * 9) // 10),
)
white_bishop = pygame.transform.scale(
    pygame.image.load("assets/images/white bishop.png"),
    ((piece_size[0] * 9) // 10, (piece_size[1] * 9) // 10),
)
white_bishop_small = pygame.transform.scale(
    pygame.image.load("assets/images/white bishop.png"),
    ((piece_size_small[0] * 9) // 10, (piece_size_small[1] * 9) // 10),
)
black_knight = pygame.transform.scale(
    pygame.image.load("assets/images/black knight.png"),
    ((piece_size[0] * 8) // 10, (piece_size[1] * 8) // 10),
)
black_knight_small = pygame.transform.scale(
    pygame.image.load("assets/images/black knight.png"),
    ((piece_size_small[0] * 8) // 10, (piece_size_small[1] * 8) // 10),
)
white_knight = pygame.transform.scale(
    pygame.image.load("assets/images/white knight.png"),
    ((piece_size[0] * 8) // 10, (piece_size[1] * 8) // 10),
)
white_knight_small = pygame.transform.scale(
    pygame.image.load("assets/images/white knight.png"),
    ((piece_size_small[0] * 8) // 10, (piece_size_small[1] * 8) // 10),
)
black_rook = pygame.transform.scale(
    pygame.image.load("assets/images/black rook.png"),
    ((piece_size[0] * 8) // 10, (piece_size[1] * 8) // 10),
)
black_rook_small = pygame.transform.scale(
    pygame.image.load("assets/images/black rook.png"),
    ((piece_size_small[0] * 8) // 10, (piece_size_small[1] * 8) // 10),
)
white_rook = pygame.transform.scale(
    pygame.image.load("assets/images/white rook.png"),
    ((piece_size[0] * 8) // 10, (piece_size[1] * 8) // 10),
)
white_rook_small = pygame.transform.scale(
    pygame.image.load("assets/images/white rook.png"),
    ((piece_size_small[0] * 8) // 10, (piece_size_small[1] * 8) // 10),
)
black_pawn = pygame.transform.scale(
    pygame.image.load("assets/images/black pawn.png"),
    ((piece_size[0] * 7) // 10, (piece_size[1] * 7) // 10),
)
black_pawn_small = pygame.transform.scale(
    pygame.image.load("assets/images/black pawn.png"),
    ((piece_size_small[0] * 7) // 10, (piece_size_small[1] * 7) // 10),
)
white_pawn = pygame.transform.scale(
    pygame.image.load("assets/images/white pawn.png"),
    ((piece_size[0] * 7) // 10, (piece_size[1] * 7) // 10),
)
white_pawn_small = pygame.transform.scale(
    pygame.image.load("assets/images/white pawn.png"),
    ((piece_size_small[0] * 7) // 10, (piece_size_small[1] * 7) // 10),
)
white_images = [
    white_pawn,
    white_rook,
    white_knight,
    white_bishop,
    white_queen,
    white_king,
]
small_white_images = [
    white_pawn_small,
    white_rook_small,
    white_knight_small,
    white_bishop_small,
    white_queen_small,
    white_king_small,
]
black_images = [
    black_pawn,
    black_rook,
    black_knight,
    black_bishop,
    black_queen,
    black_king,
]
small_black_images = [
    black_pawn_small,
    black_rook_small,
    black_knight_small,
    black_bishop_small,
    black_queen_small,
    black_king_small,
]
piece_list = ["P", "R", "N", "B", "Q", "K"]


def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(
                screen, "light gray", [600 - column * 200, row * 100, 100, 100]
            )
        else:
            pygame.draw.rect(
                screen, "light gray", [700 - column * 200, row * 100, 100, 100]
            )
    pygame.draw.rect(screen, "gray", [0, 800, width, 100])
    pygame.draw.rect(screen, "gold", [0, 800, width, 100], 5)
    pygame.draw.rect(screen, "gold", [800, 0, 200, height], 5)
    pygame.draw.rect(screen, "gold", [600, 800, width, 100], 5)
    # pygame.draw.rect(screen, "gold", [400, 600, width, 100], 5)
    status_text = [
        "White: Select a Place to Move!",
        "White: Select a Destination!",
        "Black: Select a Place to Move!",
        "Black: Select a Destination!",
    ]
    screen.blit(font.render(status_text[turn_step], True, "black"), (10, 810))
    for i in range(9):
        pygame.draw.line(screen, "black", (0, 100 * i), (800, 100 * i), 2)
        pygame.draw.line(screen, "black", (100 * i, 0), (100 * i, 800), 2)


pieces_offset = [(22, 25), (18, 20), (18, 20), (14, 16), (11, 11), (11, 11)]


def print_board():
    board = [[" " for i in range(8)] for j in range(8)]
    for i in range(len(white_pieces)):
        board[white_locations[i][1]][white_locations[i][0]] = white_pieces[i]
    for i in range(len(black_pieces)):
        board[black_locations[i][1]][black_locations[i][0]] = black_pieces[i]
    for i in range(8):
        print(board[i])


def draw_pieces():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == "P":
            screen.blit(
                white_pawn,
                (
                    white_locations[i][0] * 100 + pieces_offset[index][0],
                    white_locations[i][1] * 100 + pieces_offset[index][1],
                ),
            )
        else:
            screen.blit(
                white_images[index],
                (
                    white_locations[i][0] * 100 + pieces_offset[index][0],
                    white_locations[i][1] * 100 + pieces_offset[index][1],
                ),
            )
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(
                    screen,
                    "red",
                    [
                        white_locations[i][0] * 100 + 1,
                        white_locations[i][1] * 100 + 1,
                        100,
                        100,
                    ],
                    2,
                )

    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == "P":
            screen.blit(
                black_pawn,
                (
                    black_locations[i][0] * 100 + pieces_offset[index][0],
                    black_locations[i][1] * 100 + pieces_offset[index][1],
                ),
            )
        else:
            screen.blit(
                black_images[index],
                (
                    black_locations[i][0] * 100 + pieces_offset[index][0],
                    black_locations[i][1] * 100 + pieces_offset[index][1],
                ),
            )
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(
                    screen,
                    "blue",
                    [
                        black_locations[i][0] * 100 + 1,
                        black_locations[i][1] * 100 + 1,
                        100,
                        100,
                    ],
                    2,
                )


def detect_check(
    turn_step,
    white_pieces=white_pieces,
    black_pieces=black_pieces,
    white_locations=white_locations,
    black_locations=black_locations,
):
    print("detect_check")
    print_board()
    if turn_step < 2:
        king_location = white_locations[white_pieces.index("K")]
        other_locations = black_locations
        other_pieces = black_pieces
        locations = white_locations
        pieces = white_pieces
        color = "white"
    else:
        king_location = black_locations[black_pieces.index("K")]
        other_locations = white_locations
        other_pieces = white_pieces
        locations = black_locations
        pieces = black_pieces
        color = "black"
    for i in range(len(other_pieces)):
        piece = other_pieces[i]
        location = other_locations[i]
        if piece == "P":
            moves_list = moves.pawn_moves(
                other_locations,
                locations,
                other_pieces,
                pieces,
                color,
                location,
            )
        elif piece == "R":
            moves_list = moves.rook_moves(
                other_locations,
                locations,
                other_pieces,
                pieces,
                color,
                location,
            )
        elif piece == "N":
            moves_list = moves.knight_moves(
                other_locations,
                locations,
                other_pieces,
                pieces,
                color,
                location,
            )
        elif piece == "B":
            moves_list = moves.bishop_moves(
                other_locations,
                locations,
                other_pieces,
                pieces,
                color,
                location,
            )
        elif piece == "Q":
            moves_list = moves.queen_moves(
                other_locations,
                locations,
                other_pieces,
                pieces,
                color,
                location,
            )
        elif piece == "K":
            moves_list = moves.king_moves(
                other_locations,
                locations,
                other_pieces,
                pieces,
                color,
                location,
            )
        if king_location in moves_list:
            return True
    return False


def detect_pre_check(
    turn_step,
    move,
    piece_ind,
):
    copy_white_pieces = copy.deepcopy(white_pieces)
    copy_white_locations = copy.deepcopy(white_locations)
    copy_black_pieces = copy.deepcopy(black_pieces)
    copy_black_locations = copy.deepcopy(black_locations)

    if turn_step < 2:
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

    if detect_check(
        (turn_step) % 4,
        copy_white_pieces,
        copy_black_pieces,
        copy_white_locations,
        copy_black_locations,
    ):
        return True
    return False


def filter_moves(moves_list, piece_ind):
    out_list = []
    for i in moves_list:
        if not detect_pre_check(
            turn_step,
            i,
            piece_ind,
        ):
            out_list.append(i)
    return out_list


def check_options(color):
    if color == "white":
        pieces = white_pieces
        locations = white_locations
        other_pieces = black_pieces
        other_locations = black_locations
    else:
        pieces = black_pieces
        locations = black_locations
        other_pieces = white_pieces
        other_locations = white_locations

    # print("check_options")
    # print_board()
    moves_list = []
    all_moves_list = []
    for i in range(len(pieces)):
        location = locations[i]
        piece = pieces[i]
        if piece == "P":
            moves_list = moves.pawn_moves(
                locations, other_locations, pieces, other_pieces, color, location
            )
        elif piece == "R":
            moves_list = moves.rook_moves(
                locations, other_locations, pieces, other_pieces, color, location
            )
        elif piece == "N":
            moves_list = moves.knight_moves(
                locations, other_locations, pieces, other_pieces, color, location
            )
        elif piece == "B":
            moves_list = moves.bishop_moves(
                locations, other_locations, pieces, other_pieces, color, location
            )
        elif piece == "Q":
            moves_list = moves.queen_moves(
                locations, other_locations, pieces, other_pieces, color, location
            )
        elif piece == "K":
            moves_list = moves.king_moves(
                locations, other_locations, pieces, other_pieces, color, location
            )
        moves_list = filter_moves(moves_list, i)
        all_moves_list.append(moves_list)
    return all_moves_list


def check_valid_moves():
    if turn_step < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options


def draw_valid(moves):
    if turn_step < 2:
        color = "red"
    else:
        color = "blue"
    for i in range(len(moves)):
        pygame.draw.circle(
            screen, color, (moves[i][0] * 100 + 50, moves[i][1] * 100 + 50), 5
        )


def draw_captured_pieces():
    for i in range(len(captured_pieces_white)):
        captured_piece = captured_pieces_white[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_black_images[index], (825, 20 + 50 * i))
    for i in range(len(captured_pieces_black)):
        captured_piece = captured_pieces_black[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_white_images[index], (925, 20 + 50 * i))


def draw_check():
    checked = detect_check(turn_step)

    if turn_step < 2:
        king_location = white_locations[white_pieces.index("K")]
        if checked:
            if counter < 15:
                pygame.draw.circle(
                    screen,
                    "dark red",
                    (king_location[0] * 100 + 50, king_location[1] * 100 + 50),
                    20,
                )
    else:
        king_location = black_locations[black_pieces.index("K")]
        if checked:
            if counter < 15:
                pygame.draw.circle(
                    screen,
                    "dark blue",
                    (king_location[0] * 100 + 50, king_location[1] * 100 + 50),
                    20,
                )


black_options = check_options("black")
white_options = check_options("white")

game_over = False
moves_counter = 0
while not game_over:
    clock.tick(fps)
    if counter < 30:
        counter += 1
    else:
        counter = 0

    screen.fill("dark gray")
    draw_board()
    draw_pieces()
    draw_captured_pieces()
    draw_check()
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coords = (x_coord, y_coord)
            if turn_step < 2:
                if click_coords in white_locations:
                    selection = white_locations.index(click_coords)
                if turn_step == 0:
                    turn_step = 1
                if click_coords in valid_moves and selection != 100:
                    white_locations[selection] = click_coords
                    if click_coords in black_locations:
                        black_piece = black_locations.index(click_coords)
                        captured_pieces_white.append(black_pieces[black_piece])
                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece)
                        white_piece = white_pieces[white_locations.index(click_coords)]
                        if white_piece == "P" and click_coords[1] == 7:
                            white_pieces[white_locations.index(click_coords)] = "Q"

                    black_options = check_options("black")
                    white_options = check_options("white")
                    turn_step = 2
                    selection = 100
                    valid_moves = []
                    moves_counter += 1
            if turn_step >= 2:
                if click_coords in black_locations:
                    selection = black_locations.index(click_coords)
                if turn_step == 2:
                    turn_step = 3
                if click_coords in valid_moves and selection != 100:
                    black_locations[selection] = click_coords
                    if click_coords in white_locations:
                        white_piece = white_locations.index(click_coords)
                        captured_pieces_black.append(white_pieces[white_piece])
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece)
                        black_piece = black_pieces[black_locations.index(click_coords)]
                        if black_piece == "P" and click_coords[1] == 0:
                            black_pieces[black_locations.index(click_coords)] = "Q"
                    black_options = check_options("black")
                    white_options = check_options("white")
                    turn_step = 0
                    selection = 100
                    valid_moves = []
                    moves_counter += 1

    pygame.display.update()


pygame.quit()

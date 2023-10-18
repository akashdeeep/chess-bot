import pygame

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


def check_options():
    pass


black_options = check_options("black")
white_options = check_options("white")

game_over = False
while not game_over:
    clock.tick(fps)
    screen.fill("dark gray")
    draw_board()
    draw_pieces()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
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
                        black_options = check_options("black")
                        white_options = check_options("white")
                        turn = 1
                        selection = 100
                        valid_moves = []
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
                        black_options = check_options("black")
                        white_options = check_options("white")
                        turn = 0
                        selection = 100
                        valid_moves = []

    pygame.display.update()


pygame.quit()

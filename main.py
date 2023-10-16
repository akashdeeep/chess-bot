import pygame

pygame.init()
width = 1000
height = 900
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
selection = 1000
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
    pygame.image.load("assets/images/black bishop.png"), piece_size
)
black_bishop_small = pygame.transform.scale(
    pygame.image.load("assets/images/black bishop.png"), piece_size_small
)
white_bishop = pygame.transform.scale(
    pygame.image.load("assets/images/white bishop.png"), piece_size
)
white_bishop_small = pygame.transform.scale(
    pygame.image.load("assets/images/white bishop.png"), piece_size_small
)
black_knight = pygame.transform.scale(
    pygame.image.load("assets/images/black knight.png"), piece_size
)
black_knight_small = pygame.transform.scale(
    pygame.image.load("assets/images/black knight.png"), piece_size_small
)
white_knight = pygame.transform.scale(
    pygame.image.load("assets/images/white knight.png"), piece_size
)
white_knight_small = pygame.transform.scale(
    pygame.image.load("assets/images/white knight.png"), piece_size_small
)
black_rook = pygame.transform.scale(
    pygame.image.load("assets/images/black rook.png"), piece_size
)
black_rook_small = pygame.transform.scale(
    pygame.image.load("assets/images/black rook.png"), piece_size_small
)
white_rook = pygame.transform.scale(
    pygame.image.load("assets/images/white rook.png"), piece_size
)
white_rook_small = pygame.transform.scale(
    pygame.image.load("assets/images/white rook.png"), piece_size_small
)
black_pawn = pygame.transform.scale(
    pygame.image.load("assets/images/black pawn.png"), piece_size
)
black_pawn_small = pygame.transform.scale(
    pygame.image.load("assets/images/black pawn.png"), piece_size_small
)
white_pawn = pygame.transform.scale(
    pygame.image.load("assets/images/white pawn.png"), piece_size
)
white_pawn_small = pygame.transform.scale(
    pygame.image.load("assets/images/white pawn.png"), piece_size_small
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
piece_list = ["p", "r", "n", "b", "q", "k"]


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


game_over = False
while not game_over:
    clock.tick(fps)
    screen.fill("dark gray")
    draw_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    pygame.display.update()


pygame.quit()

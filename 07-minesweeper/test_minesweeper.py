import game


def test_get_neighbors():
    neighbors = game.get_neighbors(0, 0)

    assert len(neighbors) == 3
    assert (0, 1) in neighbors
    assert (1, 0) in neighbors
    assert (1, 1) in neighbors


def test_count_mines():
    board = [
        ["*", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]

    assert game.count_mines(board, 1, 1) == 1
    assert game.count_mines(board, 4, 4) == 0


def test_has_won():
    game_board = [
        ["*", "1"],
        ["1", "1"],
    ]

    visible_board = [
        ["□", "1"],
        ["1", "1"],
    ]

    assert game.has_won(game_board, visible_board) is True


def test_has_not_won():
    game_board = [
        ["*", "1"],
        ["1", "1"],
    ]

    visible_board = [
        ["□", "□"],
        ["1", "1"],
    ]

    assert game.has_won(game_board, visible_board) is False
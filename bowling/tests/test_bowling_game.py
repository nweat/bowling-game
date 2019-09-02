from bowling.bowling_game import BowlingGame


def test_is_frame_valid():
    assert BowlingGame._is_frame_valid([5, 4]) == True


def test1_is_frame_invalid():
    assert BowlingGame._is_frame_valid([5, 4.6]) == False


def test2_is_frame_invalid():
    assert BowlingGame._is_frame_valid([5, ""]) == False


def test_is_number_of_frames_valid():
    assert BowlingGame._is_number_of_frames_valid([[5, 2], [8, 1], [6, 4], [10], [0, 5], [2, 6], [8, 1], [5, 3], [6, 1], [10, 2, 6]]) == True


def test_is_number_of_frames_invalid():
    assert BowlingGame._is_number_of_frames_valid([[5, 2], [8, 1], [6, 4], [10], [0, 5], [2, 6], [8, 1], [5, 3], [6, 1]]) == False


def test_is_strike():
    assert BowlingGame._is_strike([10]) == True


def test_is_not_strike():
    assert BowlingGame._is_strike([5, 1]) == False


def test_game1_results():
    g1 = BowlingGame([[5, 2], [8, 1], [6, 4], [10], [0, 5], [2, 6], [8, 1], [5, 3], [6, 1], [10, 2, 6]])
    assert g1.play() == [7, 16, 26, 41, 46, 54, 63, 71, 78, 96]


def test_game2_results():
    g2 = BowlingGame([[10], [10], [10], [3, 3], [5, 0], [6, 3], [5, 4], [3, 2], [9, 0], [3, 2, 0]])
    assert g2.play() == [30, 56, 72, 78, 83, 92, 101, 106, 115, 120]


def test_game3_results():
    g3 = BowlingGame([[10], [10], [10], [10], [10], [10], [10], [10], [10], [10, 10, 10]])
    assert g3.play() == [30, 60, 90, 120, 150, 180, 210, 240, 270, 300]


def test_game4_results():
    g4 = BowlingGame([[10], [10], [10], [10], [10], [10], [10], [10], [10], [10, 3, 1]])
    assert g4.play() == [30, 60, 90, 120, 150, 180, 210, 240, 263, 277]

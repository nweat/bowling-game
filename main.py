from bowling.bowling_game import BowlingGame

if __name__ == '__main__':
    g1 = BowlingGame([[5, 2], [8, 1], [6, 4], [10], [0, 5], [2, 6], [8, 1], [5, 3], [6, 1], [10, 2, 6]])
    g2 = BowlingGame([[10], [10], [10], [3, 3], [5, 0], [6, 3], [5, 4], [3, 2], [9, 0], [3, 2, 0]])
    g3 = BowlingGame([[10], [10], [10], [10], [10], [10], [10], [10], [10], [10, 10, 10]])
    g4 = BowlingGame([[10], [10], [10], [10], [10], [10], [10], [10], [10], [10, 3, 1]])
    print(g1.play())
    print(g2.play())
    print(g3.play())
    print(g4.play())

import re


class BowlingGame(object):
    STRIKE = 10

    def __init__(self, frames):
        self.frames = frames

    @staticmethod
    def _is_number_of_frames_valid(arr):
        try:
            return len(arr) == 10
        except ValueError:
            return False

    @staticmethod
    def _is_frame_valid(arr):
        valid = False
        try:
            for a in arr:
                if int(str(a)) and a >= 1 and a <= 10:
                    valid = True
        except ValueError:
            return valid
        return valid

    @staticmethod
    def _is_strike(frame):
        return len(frame) >= 1 and frame[0] == BowlingGame.STRIKE

    @staticmethod
    def _get_sum(frame):
        return sum(frame)

    def play(self):
        finalScores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if BowlingGame._is_number_of_frames_valid(self.frames):
            for index, frame in enumerate(self.frames):
                if BowlingGame._is_frame_valid(frame):
                    if index <= 8:
                        if not BowlingGame._is_strike(frame):
                            finalScores[index] = BowlingGame._get_sum(frame) + finalScores[index - 1]
                        else:
                            if BowlingGame._is_strike(frame) and not BowlingGame._is_strike(self.frames[index + 1]):
                                finalScores[index] = BowlingGame.STRIKE + finalScores[index - 1] + BowlingGame._get_sum(self.frames[index + 1])
                            elif BowlingGame._is_strike(frame) and BowlingGame._is_strike(self.frames[index + 1]):
                                if index + 2 <= 9:
                                    if(BowlingGame._is_strike(self.frames[index + 2])):
                                        finalScores[index] = (BowlingGame.STRIKE * 2) + self.frames[index + 1][0] + finalScores[index - 1]
                                    else:
                                        finalScores[index] = (BowlingGame.STRIKE * 2) + BowlingGame._get_sum(self.frames[index + 2]) + finalScores[index - 1]
                                else:
                                    if(BowlingGame._is_strike(self.frames[index + 1])):
                                        finalScores[index] = (BowlingGame.STRIKE * 2) + self.frames[index + 1][1] + finalScores[index - 1]

                    else:
                        finalScores[index] = BowlingGame._get_sum(frame) + finalScores[index - 1]

                else:
                    print("Invalid values found in frame. Must be integers between 1 and 10.")

        else:
            print("Please enter an array of arrays containing 10 frames. This is a ten pin bowling game!")

        return finalScores

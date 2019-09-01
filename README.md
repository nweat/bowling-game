# CarPal Backend Coding Challenge

This test is to write a program for a ten-pin bowling game.

A bowler has ten frames to knock down pins. In each of one to nine frames, the bowler makes one or two throws while the tenth frame has up to three throws.

You program should be able to receive an array of arrays of pins knocked down by each throw as an input. Each number should always be an integer between 0 and 10. Each sub-array represents one frame of a game. The basic rules of this bowling game are:

No additional score for a spare.
If a bowler knocks down all ten pins on the first throw, it’s a strike. A strike is worth 10, plus the score in the next frame if the next frame is not a strike. If the next frame is also a strike, which means the bowler has made two strikes, then the score from the third frame is also added to the first frame.
Ex. 10 (first frame)+10 (second frame)+10 (third frame) results in the first frame with a score of 30.
Ex. 10 (first frame)+6 (second frame) results in the first frame with a score of 16.
If a strike is not made in a frame, the score of the frame is just the sum of pins knocked down.
The last frame has up to three throws. If a bowler had a strike on the first throw, the bowler is allowed to have one additional throw. So the bowler has three throws in total. If the bowler made two strikes he will still be able to do the last throw
Your program should display a list of integers representing the total scores at the end of each frame.

Example

Input: [[5,2],[8,1],[6,4],[10],[0,5],[2,6],[8,1],[5,3],[6,1],[10,2,6]]

Output: [7, 16, 26, 41, 46, 54, 63, 71, 78, 96]


# Requirements
pip install -r requirements.txt


# Test
pytest -v bowling\tests


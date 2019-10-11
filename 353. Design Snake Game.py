'''
Title     : 353. Design Snake Game ($$$)
Problem   : https://leetcode.com/problems/design-snake-game/description/
'''
''' Reference: https://gfzj.online/leetcode/detail.html?id=353 '''
from collections import deque
class SnakeGame(object):

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        # Space: O(n)
        initial_pos = (0, 0)
        self.snake = deque([initial_pos])
        self.snakePos = set([initial_pos])
        self.foods = deque(food)
        self.width, self.height = width, height
        self.directions = { 'U': (-1, 0), 'L': (0, -1), 'R': (0, 1), 'D': (1, 0) }

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        # Time: O(1), Space: O(1)
        head = self.snake[0]
        next_pos = (head[0] + self.directions[direction][0], head[1] + self.directions[direction][1])
        
        tail = self.snake.pop()   # remove the tail before checking because the new head can be in the previous tail position
        self.snakePos.remove(tail)

        if next_pos in self.snakePos or not (0 <= next_pos[1] < self.width and 0 <= next_pos[0] < self.height):
            return -1        
        self.snake.appendleft(next_pos)
        self.snakePos.add(next_pos)

        curr_food = (-1, -1)
        if len(self.foods):
            curr_food = tuple(self.foods[0])
        if curr_food == next_pos:
            self.foods.popleft()
            self.snake.append(tail)   # add back tail because eating the food is equivalent to combining the food with the body
            self.snakePos.add(tail)
        
        return len(self.snake) - 1

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
'''
example:
width = 3; height = 3; food = [[1,2],[0,1]]
snake = SnakeGame(width, height, food)
snake.move('R')
snake.move('D')
snake.move('R')
snake.move('U')
snake.move('L')
snake.move('U')
'''
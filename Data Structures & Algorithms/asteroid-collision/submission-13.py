class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            if stack and (stack[-1] > 0 and asteroids[i] < 0):
                if abs(asteroids[i]) > stack[-1]:
                    while stack and (stack[-1] > 0 and asteroids[i] < 0) and abs(asteroids[i]) > stack[-1]:
                        stack.pop()
                    if stack and stack[-1] == abs(asteroids[i]):
                        stack.pop()
                    elif not stack or (stack[-1] < 0 and asteroids[i] < 0):
                        stack.append(asteroids[i])
                elif abs(asteroids[i]) == stack[-1]:
                    stack.pop()
                    print(stack)
            else:
                stack.append(asteroids[i])

        return stack
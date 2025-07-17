# We are given an array asteroids of integers representing asteroids in a row. The indices of the asteriod in the array represent their relative position in space.
# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left).
# Each asteroid moves at the same speed.
# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. 
#If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

def asteroidCollision(asteroids): 
    collisionStack = [] 
    for i in range(len(asteroids) - 1, -1, -1):
        finalPush = asteroids[i]
        while (collisionStack and collisionStack[0] < 0 and finalPush > 0):
            topElem = collisionStack.pop(0)
            if (topElem + finalPush == 0):
                finalPush = 0 
            else: 
                finalPush = finalPush if (-1 * topElem < finalPush) else topElem

        collisionStack.insert(0,finalPush) if finalPush != 0 else collisionStack
    return collisionStack


from math import pi, sin, cos

class Point(tuple):
    def __new__(cls, *args):
        return tuple.__new__(cls, args)
    def __add__(self, other):
        return Point(*([sum(x) for x in zip(self, other)]))
    @property
    def x(self):
        return self[0]
    @property
    def y(self):
        return self[1]

class Cart:
    carts, collision = {}, None
    steps = {'^': Point(0, -1), '>': Point(1, 0), 'v': Point(0, 1), '<': Point(-1, 0)}
    cross_turns = [-pi/2, 0, pi/2]
    
    def __init__(self, x, y, orientation):
        self.pos, self.step, self.count = Point(x, y), self.steps[orientation], -1

    def step_cart_collision(self):
        def turn():
            if grid[self.pos.y][self.pos.x] == '\\':
                self.step = Point(self.step.y, self.step.x)
            elif grid[self.pos.y][self.pos.x] == '/':
                self.step = Point(-self.step.y, -self.step.x)
            elif grid[self.pos.y][self.pos.x] == '+':
                self.count = (self.count + 1) % 3
                theta = Cart.cross_turns[self.count]
                self.step = Point(self.step.x * int(cos(theta)) - self.step.y * int(sin(theta)), self.step.x * int(sin(theta)) + self.step.y * int(cos(theta)))

        del Cart.carts[self.pos]
        self.pos += self.step

        turn()
        Cart.collision = Cart.carts.get(self.pos, None)
        Cart.carts[self.pos] = self
        return Cart.collision

    def __repr__(self):
        return  str(self.pos) + next((a for a in Cart.steps if Cart.steps[a] == self.step))

if __name__ == "__main__":
    grid = list(map(list, open('input-13.txt').read().split('\n')))

    for i, row in enumerate(grid):  # find and create carts
        for j, tile in enumerate(row):
            if tile in ('>', '<', 'v', '^'):
                Cart.carts[Point(j, i)] = Cart(j, i, tile)  # add new cart to it's position


    while not Cart.collision:  # while no collision
        for (x,y), cart in sorted(Cart.carts.items()): # calculate 1 round of movement
            if cart.step_cart_collision():  # stop if cllision found
                break

    print(Cart.collision)


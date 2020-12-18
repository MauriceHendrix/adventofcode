from timing import timing
import itertools
input_data = list(map(list, open('input-17.txt').read().split('\n')))

@timing
def simulate(dimensions=3, simulation_runs = 6):
    cubes = set()

    for y, row in enumerate(input_data):
        for x, cube in enumerate(row):
            if cube == '#':
                point = (x,y) + tuple(0 for _ in range(dimensions -2))
                cubes.add(point)

    def calc_adjecent(cubes):
        new_active_cubes = set()
        adjecent = {}
        # count all adjacent fields
        for point in cubes:
            adjecent[point] = adjecent.get(point, 0) # make sure current active cubes are counted even if they have 0 adjecent cubes
            ranges = ([point[i]-1, point[i], point[i]+1] for i in range(dimensions))
            combos = list(itertools.product(*ranges))
            for adj_point in combos:
                if adj_point != point:
                    adjecent[adj_point] = adjecent.get(adj_point, 0) +1  # count adjacent

        for point, count in adjecent.items():
            if point in cubes and adjecent[point] in (2,3): #If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
                new_active_cubes.add(point)
            elif adjecent[point] == 3:#If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.
                new_active_cubes.add(point)
        return new_active_cubes

    for _ in range(simulation_runs):
        cubes = calc_adjecent(cubes)
    return len(cubes)

if __name__ == "__main__":
    print(simulate())
    print(simulate(dimensions=4))


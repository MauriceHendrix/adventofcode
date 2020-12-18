f = open("input-17.txt") ;
lines = readlines(f)


function simulate(dimensions, simulation_runs=6)

    cubes = Set()
    for (i, row) in enumerate(lines)
        j=0
        for cube in row
            if cube == '#'
                point = zeros(Int64,dimensions)
                point[1],point[2]  = i, j
                push!(cubes, point)
            end
            j+=1
        end
    end

    function calc_adjecent(cubes)
        new_active_cubes = Set()
        adjecent = Dict{Array{Int64,1},Int64}()
        # count all adjacent fields

        for point in cubes
            #push!(adjecent, point => get(adjecent, point, 0))
            adjecent[point] = get(adjecent, point, 0) # make sure current active cubes are counted even if they have 0 adjecent cubes
            ranges = [[point[i]-1, point[i], point[i]+1] for i in 1:dimensions]
            combos = (Iterators.product(ranges...))# generate neighbor combos
            #println(typeof(combos))
            for c in combos
                adj_point = [i for i in c]
                if adj_point != point
                    #println(get(adjecent, adj_point, 0))
                    adjecent[adj_point] = get(adjecent, adj_point, 0) + 1  # count adjacent
                end
            end
        end
        for (point, count) in adjecent
            if count == 3 || (point in cubes && count == 2)
                push!(new_active_cubes, point)
            end
        end
        return new_active_cubes
    end

    for i = 1:simulation_runs
        cubes = calc_adjecent(cubes)
    end
    return length(cubes)
end

print(simulate(6))
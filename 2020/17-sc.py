from timing import timing
import numpy as np
import scipy.ndimage as image


def create_larger_array(original_array):
    """
    Return a zeros array that expands the existing array by 1 in each direction in
    each dimension
    """
    shape = original_array.shape
    return np.zeros([dim_size+2 for dim_size in shape])


def apply_timestep(ref_arr, larger_arr, dim, kernel):
    # Sums array counts up all neighbouring occupied chairs
    larger_ref_arr = np.zeros_like(larger_arr)
    larger_ref_arr[(dim * [slice(1, -1)])] = ref_arr
    sums_array = image.convolve(larger_ref_arr,
                                weights=np.array(kernel),
                                mode='constant',
                                cval=0)

    # Iterate over all elements in the reference array
    it = np.nditer(larger_ref_arr, flags=['multi_index'])
    for x in it:
        m_i = it.multi_index
        if (larger_ref_arr[m_i] == 1 and sums_array[m_i] in [2, 3]) or \
                (larger_ref_arr[m_i] == 0 and sums_array[m_i] == 3):
            larger_arr[m_i] = 1

    return larger_arr


@timing
def main(list_of_lines):
    dim = 3
    # Process lines into a dim-D array.
    # Create zeros array, with len=1 dimensions padding up from 2 dims to n dims
    arr = np.zeros([1] * (dim-2) + [len(list_of_lines[1]), len(list_of_lines)])
    for line_no, line in enumerate(list_of_lines):
        for col_no, char in enumerate(line):
            if char == '#':
                arr[tuple([0] * (dim-2) + [line_no, col_no])] = 1

    # Create dim-D convolution kernel
    kernel = np.ones([3] * dim, dtype=np.int64)
    kernel[tuple([1] * dim)] = 0
    print(kernel)
    assert False

    for cycle_counter in range(6):
        # Create new larger array
        new_arr = create_larger_array(arr)

        # Populate new larger array based on rules from old array
        # Loop over all elements in larger array, and apply rules based on old array
        # (remembering to offset all indices by +1 to account for the larger size)
        arr = apply_timestep(arr, new_arr, dim, kernel)

        # Remove up to one layer of values at each end of each dimension
        for d in range(dim):
            for col in [-1, 0]:
                if np.sum(arr[dim_loc(dim, d, col)]) == 0:
                    arr = arr[dim_loc_not(dim, d, col)]

    return np.sum(arr)


def dim_loc(dim, this_dim, value):
    blank = [slice(None)]*dim
    blank[this_dim] = value
    return tuple(blank)


def dim_loc_not(dim, this_dim, value):
    blank = [slice(None)]*dim
    if value == 0:
        blank[this_dim] = slice(1, None)
    else:
        blank[this_dim] = slice(0, -1)
    return tuple(blank)


if __name__ == "__main__":
    with open('input-17.txt') as input_file:
        lines_in = [item.strip() for item in input_file.readlines()]

    print(main(lines_in))

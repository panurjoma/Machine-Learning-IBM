
class MapNode:
    def __init__(self, row_number, initial_index, value):
        self.row_number = row_number
        self.column_indexes = [initial_index]
        self.value = value
        self.neigbours = []

    def increase_value(self, value_to_add):
        self.value += value_to_add

    def increase_indexes(self, index_to_add):
        self.column_indexes.append(index_to_add)

    def add_neighbor(self, neigbour):
        self.neigbours.append(neigbour)

def check_first_row_block_points(block_points, matrix):
    number_block_first = 0
    for block_point in block_points:
        if block_point[0] == 0:
            number_block_first += 1

    if number_block_first == len(matrix[0]) - 1:
        return False

    return True

def findnumberindex(matrix, number_to_find, block_points):
    for i,lst in enumerate(matrix):
        for j,number in enumerate(lst):
            if number == number_to_find and (i, j) not in block_points and check_first_row_block_points(block_points, matrix):
                return (i, j)

    return False

def matrixLand(A):
    # Write your code here
    max_sol = 0
    all_nums = []
    for row in A:
        max_sol += sum(row)
        all_nums.extend(row)
    all_nums.sort()
    improve = True
    block_points = []
    while improve:
        # Check first row
        block_point_to_add = False
        while not block_point_to_add:
            block_point_to_add = findnumberindex(A, all_nums[0], block_points)
            if block_point_to_add:
                block_points.append(block_point_to_add)
            all_nums.pop(0)

        # Create first row paths
        available = False
        row_ini = 0
        col_ini = 0
        list_initial_nodes = []
        while not available:
            if (row_ini, col_ini) not in block_points:
                default_node = MapNode(row_ini, col_ini, A[0][col_ini])
                available = True
            else:
                col_ini += 1

        node_index = 0
        list_initial_nodes.append(default_node)
        flag = 0
        for j, value in enumerate(A[0]):
            if (0,j) not in block_points and not flag:
                list_initial_nodes[node_index].increase_value(A[0][j + col_ini])
                list_initial_nodes[node_index].increase_indexes(j + col_ini)
                flag = 0
            elif (0,j) in block_points:
                node_index += 1
                flag = 1
                list_initial_nodes.append(MapNode(0, j, A[0][j + 1]))

        prev_list_nodes = list_initial_nodes
        for i, row in enumerate(A):
            if i == 0:
                continue
            list_nodes_local_row = []
            index_local_row = 0
            flag = 0
            for j, num in enumerate(row):
                if (i, j) not in block_points and not flag:
                    try:
                        list_nodes_local_row[index_local_row].increase_value(A[0][j])
                        list_nodes_local_row[index_local_row].increase_indexes(j)
                    except:
                        list_nodes_local_row.append(MapNode(i, j, A[i][j]))
                    flag = 0
                elif (0, j) in block_points:
                    node_index += 1
                    flag = 1
                    list_initial_nodes.append(MapNode(0, j, A[0][j + 1]))

            # Stablish conections between currrent row and previous row
            for prev_node in prev_list_nodes:
                for current_node in list_nodes_local_row:
                    list1_as_set = set(prev_node.column_indexes)
                    intersection = list1_as_set.intersection(current_node.column_indexes)
                    intersection_as_list = list(intersection)
                    if len(intersection_as_list) >= 1:
                        prev_node.add_neighbor(current_node)

            # Set new prev list of nodes
            prev_list_nodes = list_nodes_local_row

        # go through all possible paths
        # TODO create a recursive function to go throuht all the graph





        paths_list = []


    return max_sol

A = [[1, 2, 3, -1, -2], [-5, -8, -1, 2, -150], [1, 2, 3, -250, 100], [1, 1, 1, 1, 20]]
matrixLand(A)

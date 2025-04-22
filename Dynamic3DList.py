import numpy as np

class Dynamic3DList:
    def __init__(self):
        self.data = []

    def __setitem__(self, indices, value):
        i, j, k = indices

        # Expand outer list
        while len(self.data) <= i:
            self.data.append([])

        # Expand middle list
        while len(self.data[i]) <= j:
            self.data[i].append([])

        # Expand inner list
        while len(self.data[i][j]) <= k:
            self.data[i][j].append(0)

        self.data[i][j][k] = value

    def __getitem__(self, indices):
        i, j, k = indices

        try:
            return self.data[i][j][k]
        except IndexError:
            return 0  # Return 0 for anything out of bounds

    def get_data(self):
        # Pad all dimensions to make a full rectangular 3D list
        max_i = len(self.data)
        max_j = max((len(plane) for plane in self.data), default=0)
        max_k = max((len(row) for plane in self.data for row in plane), default=0)

        result = []
        for i in range(max_i):
            plane = []
            for j in range(max_j):
                if j < len(self.data[i]):
                    row = self.data[i][j] + [0] * (max_k - len(self.data[i][j]))
                else:
                    row = [0] * max_k
                plane.append(row)
            result.append(plane)

        return result
    
    def pad_iterations_per_file(self):
        """
        For each k and file, pad missing iterations by copying the last non-zero value 
        repeatedly until the max iteration count (within that k) is reached.
        """
        num_k = len(self.data)
        if num_k == 0:
            return

        # Determine the number of files (max length of any row across all k)
        num_files = 0
        for k in range(num_k):
            for iteration in self.data[k]:
                num_files = max(num_files, len(iteration))

        for k in range(num_k):
            # Step 1: determine max number of iterations in this k
            max_iter = len(self.data[k]) if self.data[k] else 0
            for file in range(num_files):
                iter_count = 0
                for j in range(len(self.data[k])):
                    if file < len(self.data[k][j]) and self.data[k][j][file] != 0:
                        iter_count = j + 1
                max_iter = max(max_iter, iter_count)

            # Step 2: pad each file in k to max_iter
            for file in range(num_files):
                last_value = 0
                for j in range(max_iter):
                    # Expand iterations if needed
                    while len(self.data[k]) <= j:
                        self.data[k].append([0] * num_files)

                    # Expand file index in row if needed
                    while len(self.data[k][j]) <= file:
                        self.data[k][j].append(0)

                    current_value = self.data[k][j][file]
                    if current_value != 0:
                        last_value = current_value
                    else:
                        self.data[k][j][file] = last_value

    def average_over_files(self):
        """
        Computes the average over the file dimension (3rd index) for each (k, iteration).
        Returns a 2D list: result[k][iteration].
        """
        result = []
        for k_index, k_layer in enumerate(self.data):
            k_result = []
            for j_index, iteration_list in enumerate(k_layer):
                if iteration_list:
                    avg = sum(iteration_list) / len(iteration_list)
                else:
                    avg = 0
                k_result.append(avg)
            result.append(k_result)
        return result

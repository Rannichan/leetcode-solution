# this solution works but is slow
import copy
class Solution:
    def containVirus(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        wall_num = 0
        regions = []
        grid, regions, wall_num = self.main(grid, regions, wall_num)
        return wall_num

    def main(self, input_grid, regions, wall_num):
        # init the "regions"
        if not regions:
            regions = self.regions_init(input_grid)

        # find the region we need to block, and count the num of walls we need
        max_num = 0
        max_wnum = 0
        region_chosen = set()
        next_grid = input_grid
        for region in regions:
            _, points_in_danger = self.expand_region(input_grid, region)
            num = len(points_in_danger) - len(region)
            tmp_grid, wnum = self.get_wall_num(input_grid, region)
            if num > max_num:
                max_num = num
                max_wnum = wnum
                region_chosen = region
                next_grid = tmp_grid

        # if no more wall could be built, stop and return
        # otherwise, update the "regions" and the grid, record the total num of walls
        if max_num == 0:
            return next_grid, regions, wall_num
        else:
            input_grid = next_grid
            wall_num += max_wnum
            regions.remove(region_chosen)
            new_regions = []
            for region in regions:
                input_grid, region = self.expand_region(input_grid, region)
                new_regions.append(region)
            regions = self.merge_regions(input_grid, new_regions)

            input_grid, regions, wall_num = self.main(input_grid, regions, wall_num)
            return input_grid, regions, wall_num

    def regions_init(self, input_grid):
        """
        Get all regions at initial status
        :param input_grid: List of lists, initial status
        :return: List of sets, each of which denotes a region and contains the coord of its points
        """
        regions = []
        for i in range(len(input_grid)):
            for j in range(len(input_grid[0])):
                p_val = input_grid[i][j]  # 0 means uninfected; 1 means infected; -1 means blocked
                p_xy = (i, j)
                if p_val == 0 or p_val == -1:
                    # if current point is uninfected or blocked, we will skip it
                    continue
                else:
                    # if current point is infected
                    if i == 0 and j == 0:
                        # for the point at the left-up corner
                        # we add it into a new empty region
                        regions.append({p_xy})
                        continue
                    if i == 0 and j > 0:
                        # for the point in the top row (except the first point)
                        if input_grid[i][j - 1] == 1:
                            # if the point at left of the current points has already belongs to an existed region
                            # add the current point into the region found
                            for region in regions:
                                if (i, j - 1) in region:
                                    region.add((i, j))
                        else:
                            # if the left point is uninfected
                            # we add current point into a new empty region
                            regions.append({p_xy})
                    if j == 0 and i > 0:
                        # for the point in the most left column (except the first point)
                        if input_grid[i - 1][j] == 1:
                            # if the point at the top of the current points has already belongs to an existed region
                            # add the current point into the region found
                            for region in regions:
                                if (i - 1, j) in region:
                                    region.add((i, j))
                        else:
                            # if the upper point is uninfected
                            # we add current point into a new empty region
                            regions.append({p_xy})
                    # i, j > 0
                    if input_grid[i - 1][j] == 0 and input_grid[i][j - 1] == 0:
                        # if left point/upper point are both uninfected
                        # we add current point into an new empty region
                        regions.append({p_xy})
                    else:
                        if input_grid[i - 1][j] == 1:
                            # if the upper point is infected
                            # add current point into the region the upper point belongs to
                            for region in regions:
                                if (i - 1, j) in region:
                                    region.add((i, j))
                        if input_grid[i][j - 1] == 1:
                            # if the left point is infected
                            # add current point into the region the left point belongs to
                            for region in regions:
                                if (i, j - 1) in region:
                                    region.add((i, j))
        regions = self.merge_regions(input_grid, regions)
        return regions

    @staticmethod
    def get_wall_num(input_grid, region):
        tmp_grid = copy.deepcopy(input_grid)
        counter = 0
        for point in region:
            i = point[0]
            j = point[1]
            tmp_grid[i][j] = -1
            if i - 1 >= 0 and input_grid[i - 1][j] == 0:
                counter += 1
            if j - 1 >= 0 and input_grid[i][j - 1] == 0:
                counter += 1
            if i + 1 < len(input_grid) and input_grid[i + 1][j] == 0:
                counter += 1
            if j + 1 < len(input_grid[0]) and input_grid[i][j + 1] == 0:
                counter += 1
        return tmp_grid, counter

    @staticmethod
    def expand_region(input_grid, region):
        next_grid = copy.deepcopy(input_grid)
        new_points = set()
        for point in region:
            i = point[0]
            j = point[1]
            if i - 1 >= 0 and next_grid[i - 1][j] != -1:
                new_points.add((i - 1, j))
                next_grid[i - 1][j] = 1
            if j - 1 >= 0 and next_grid[i][j - 1] != -1:
                new_points.add((i, j - 1))
                next_grid[i][j - 1] = 1
            if i + 1 < len(next_grid) and next_grid[i + 1][j] != -1:
                new_points.add((i + 1, j))
                next_grid[i + 1][j] = 1
            if j + 1 < len(next_grid[0]) and next_grid[i][j + 1] != -1:
                new_points.add((i, j + 1))
                next_grid[i][j + 1] = 1
        return next_grid, region | new_points

    def merge_regions(self, input_grid, regions):
        """
        merge adjacent regions
        :param regions:
        :return:
        """
        if len(regions) == 0 or len(regions) == 1:
            return regions

        current_region = regions[0]
        _, current_region_expand = self.expand_region(input_grid, current_region)

        flag = 0
        for region in regions[1:]:
            if len(current_region_expand & region) != 0:
                flag = 1
                break

        if flag == 1:
            regions.remove(current_region)
            regions.remove(region)
            region = current_region | region
            regions.append(region)
            regions = self.merge_regions(input_grid, regions)
        else:
            regions = [current_region] + self.merge_regions(input_grid, regions[1:])
        return regions


if __name__ == '__main__':
    grid = [[1, 1, 1, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 0, 0, 0, 0, 0]]
    grid2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
             [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    grid3 = [[0, 1, 0, 1, 1, 1, 1, 1, 1, 0],
             [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 1, 1, 0, 0, 0, 1, 0],
             [0, 0, 0, 1, 1, 0, 0, 1, 1, 0],
             [0, 1, 0, 0, 1, 0, 1, 1, 0, 1],
             [0, 0, 0, 1, 0, 1, 0, 1, 1, 1],
             [0, 1, 0, 0, 1, 0, 0, 1, 1, 0],
             [0, 1, 0, 1, 0, 0, 0, 1, 1, 0],
             [0, 1, 1, 0, 0, 1, 1, 0, 0, 1],
             [1, 0, 1, 1, 0, 1, 0, 1, 0, 1]]
    grid4 = [[0,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
             [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0],
             [1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
             [0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
             [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
             [0,0,0,0,0,0,0,0,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
             [0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
             [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
             [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0],
             [0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
             [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,1,0,0],
             [0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],
             [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
             [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
             [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
             [0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0],
             [1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
             [0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
             [0,0,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
             [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0]]

    s = Solution()
    print(s.containVirus(grid4))

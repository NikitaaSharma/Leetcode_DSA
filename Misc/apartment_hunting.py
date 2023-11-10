blocks = [
    {
        "gym":False,
        "school":True,
        "store":False
    },
    {
        "gym":True,
        "school":False,
        "store":False
    },
    {
        "gym":True,
        "school":True,
        "store":False
    },
    {
        "gym":True,
        "school":True,
        "store":False
    },
    {
        "gym":False,
        "school":True,
        "store":True
    },
]

reqs = ["gym", "school", "store"]


def get_best_apartment(blocks, reqs):
    max_block_distances = [float("-inf") for _ in blocks]
    total_blocks = len(blocks)

    for block in range(total_blocks):
        for req in reqs:
            closest_req_dist = float("inf")
            for j in range(total_blocks):
                if blocks[j][req]:
                    closest_req_dist = min(closest_req_dist, get_dist(block, j))

            max_block_distances[block] = max(max_block_distances[block], closest_req_dist)
        
    min_val = min(max_block_distances)
    return max_block_distances.index(min_val)


def get_dist(a,b):
    return abs(a-b)


res = get_best_apartment(blocks, reqs)
print(res)
import heapq
import time
from typing import List, Tuple, Set

from PuzzleNode import PuzzleNode
from node_utils import backtrack_actions, state_to_tuple


def uniform_cost_search(init_state: Tuple[Tuple[int]], goal_state: Tuple[Tuple[int]]):
    t0 = time.time()
    print("Running Uniform-cost Search...")
    visited = set[Tuple]()

    heap = [PuzzleNode(None, None, init_state)]
    heapq.heapify(heap)

    while heap:
        node = heapq.heappop(heap)
        if node.current_state == goal_state:
            pass

        for action in node.actions():
            new_state = node.step(action)
            if new_state not in visited:
                pass

    t_dfs = (time.time() - t0) / 1
    print(f'Finished in {t_dfs}s')

    return backtrack_actions(node, visited, False)


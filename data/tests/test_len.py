import networkx as nx
import time
from pipeline.steps.draw_longest_path import list_to_nx_path, draw_networkx
from pipeline.steps.get_max_lenght import find_longest_path_with_multiprocessing, to_acyclic_graph, \
    find_longest_path_nodes_mp, get_max_lenght
from pipeline.steps.make_graph import make_example_graph


def test_find_longest_path():
    example = make_example_graph()
    example = to_acyclic_graph(example)
    my_longest_path = find_longest_path_with_multiprocessing(example)
    max_path = nx.dag_longest_path(example)
    if len(my_longest_path) == len(max_path):
        return True
    return False


def check_path(graph: nx.DiGraph, path):
    path_nx = []
    for idx, x in enumerate(path):
        l = len(path) - 1
        if idx != l:
            if (path[idx + 1]) in list(graph.successors(x)):
                path_nx.append('1')
    if len(path_nx) == len(path) - 1:
        return True
    return False


def pipeline_example():
    example = make_example_graph()
    start_time = time.time()
    l = find_longest_path_with_multiprocessing(example)
    print("--- %s seconds ---" % (time.time() - start_time))
    print(l)
    print("-----------------------------------------")

    start_time = time.time()
    l2 = find_longest_path_nodes_mp(example)
    print("--- %s seconds ---" % (time.time() - start_time))
    print(l2)

    print("-----------------------------------------")

    start_time = time.time()
    l3 = get_max_lenght(example)
    print("--- %s seconds ---" % (time.time() - start_time))
    print(l3)
    lens = [l, l2, l3]
    final = max(lens, key=len)
    print("FINAL PATH = ", final)
    if (check_path(example, final)):
        path = list_to_nx_path(example, final)
        draw_networkx(path)


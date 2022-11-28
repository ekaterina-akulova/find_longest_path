import networkx as nx
from matplotlib import pyplot as plt

def to_nx_path(path):
    path_nx = []
    for some_path in path:
        inner_path_nx = []
        for idx, x in enumerate(some_path):
            l = len(some_path) - 1
            if idx != l:
                inner_path_nx.append((x, (some_path[idx + 1])))
        path_nx.append(inner_path_nx)
    return (path_nx[0])


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


def list_to_nx_path(g, path):
    if check_path(g, path):
        path_nx = []
        for idx, x in enumerate(path):
            l = len(path) - 1
            if idx != l:
                path_nx.append((x, (path[idx + 1])))
        return (path_nx)


def draw_networkx(paths_nx):
    g = nx.DiGraph()
    g.add_edges_from(paths_nx)
    nx.draw_networkx(g)
    plt.show()

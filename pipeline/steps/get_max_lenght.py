import networkx as nx
from pipeline.steps.make_graph import as_spanning_trees
import ast
import multiprocessing as mp
from multiprocessing.pool import ThreadPool
import math

def to_acyclic_graph(G: nx.DiGraph):
    if nx.is_directed_acyclic_graph(G) == False:
        tree = as_spanning_trees(G)
        return tree
    return G


def subgraphs(g: nx.DiGraph):
    sub_graphs = [g.subgraph(c) for c in nx.weakly_connected_components(g)]
    return sub_graphs


def get_max_lenght(tree):
    dict_path = {}
    tree = to_acyclic_graph(tree)
    subrgarhs = subgraphs(tree)
    for graph in subrgarhs:
        dict_path[str(nx.dag_longest_path(graph))] = len(nx.dag_longest_path(graph))
    return_list = ast.literal_eval(max(dict_path, key=dict_path.get))
    return return_list


def find_longest_path_from(graph, start, path=None):
    if path is None:
        path = []
    path = path + [start]
    max_path = path
    nodes = list(graph.successors(start))
    for node in nodes:
        if node not in path:
            candidate_path = find_longest_path_from(graph, node, path)
            if len(candidate_path) > len(max_path):
                max_path = candidate_path
    return max_path


def find_nongest_path_on_nodes(graph, nds):
    max_path = []
    for node in nds:
        if (node != None):
            if len(list(graph.predecessors(node))) == 0:
                candidate_path = find_longest_path_from(graph, node)
                if len(candidate_path) > len(max_path):
                    max_path = candidate_path
    return max_path


def find_longest_path_nodes_mp(graph):
    max_path = []
    res = []
    n_workers = mp.cpu_count()
    subgraph = subgraphs(graph)
    max_sub = max_len_sub(subgraph)
    nodes = list(max_sub.nodes())
    if len(max_sub) > n_workers:
        nds = list(func_chunks_num(nodes, n_workers))
    else:
        n_workers = len(max_sub)
        nds = list(func_chunks_num(nodes, n_workers))
    with ThreadPool(processes=n_workers) as pool:
        for nodes in nds:
            res.append(pool.apply_async(find_nongest_path_on_nodes, (max_sub, nodes,)).get())
    for candidate_path in res:
        if len(candidate_path) > len(max_path):
            max_path = candidate_path
    return max_path


def func_chunks_num(lst, c_num):
    n = math.ceil(len(lst) / c_num)
    for x in range(0, len(lst), n):
        e_c = lst[x : n + x]
        yield e_c



def max_len_sub(subs):
    max_sub = []
    for sub in subs:
        if len(sub) > len(max_sub):
            max_sub = sub
    return max_sub


def find_longest_path_sub(graph):
    max_path = []
    for node in graph.nodes():
        candidate_path = find_longest_path_from(graph, node)
        if len(candidate_path) > len(max_path):
            max_path = candidate_path
    return max_path

def find_nongest_path_on_subgraphs(subgraphs: list):
    max_path = []
    for sub in subgraphs:
        path = find_longest_path_sub(sub)
        if len(path) > len(max_path):
            max_path = path
    return max_path


def find_longest_path_with_multiprocessing(graph):
    n_workers = mp.cpu_count()
    max_path = []
    res = []
    subgraph = list(subgraphs(graph))
    subgraph_count = len(subgraph)
    if subgraph_count > n_workers:
        subs = list(func_chunks_num(subgraph, n_workers))
    else:
        n_workers = subgraph_count
        subs = [[sub] for sub in subgraph]
    with ThreadPool(processes=n_workers) as pool:
        for sub in subs:
            res.append(pool.apply_async(find_nongest_path_on_subgraphs, (sub, )).get())
    for candidate_path in res:
        if len(candidate_path) > len(max_path):
            max_path = candidate_path
    return max_path



def find_longest_path(graph):
    max_path = []
    subgraph = subgraphs(graph)
    for sub in subgraph:
        candidate_path = find_longest_path_sub(sub)
        if len(candidate_path) > len(max_path):
            max_path = candidate_path
    return max_path
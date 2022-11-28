import networkx as nx
from pipeline.steps.make_graph import as_spanning_trees
import ast
from multiprocessing import Pool
import queue

str_nodes = ""


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
    # print("nx.is_directed_acyclic_graph(tree) = ", nx.is_directed_acyclic_graph(tree))
    tree = to_acyclic_graph(tree)
    subrgarhs = subgraphs(tree)
    # print("len subgraphs in get_max_lenght(tree) = ", len(subrgarhs))
    for graph in subrgarhs:
        # print(nx.find_cycle(graph))
        dict_path[str(nx.dag_longest_path(graph))] = len(nx.dag_longest_path(graph))
    # print(max(list_len))
    # print(list_len)
    # print(max(dict_path, key=dict_path.get))
    # print(dict_path)
    return_list = ast.literal_eval(max(dict_path, key=dict_path.get))
    return return_list


def get_max_len(graph: nx.DiGraph):
    subgraph = subgraphs(graph)
    # print(subgraph)
    # print(type(subgraph))
    # print("len subgraphs in get_max_lenght(tree) = ", len(subgraph))
    # with Pool(20) as pool:
    lenghts = [get_max_lenght_from_subgraph(graph, ) for graph in subgraph]
    # lenghts = [get_max_lenght_from_subgraph(graph, ) for graph in subgraph]
    # print(str_nodes)
    # print(str_split(str_nodes, max(lenghts)))
    print("choosing max from get_max_len BETWEEN: ", lenghts)
    return max(lenghts)


def get_max_lenght_from_subgraph(graph: nx.DiGraph):
#     print(type(graph))
    lenghts = []
    for vertex in graph.nodes():
        lenghts.append(get_max_lenght_recursiv(graph, vertex, ))
    # print("LENS = ",   lenghts)
    return max(lenghts)


def get_paths(max_len):
    return str_split(str_nodes, max_len)


def str_split(st, num):
    nds = [x.split(',') for x in st.split('\n')]
    tpl = {tuple(n) for n in nds if len(n) >= num}
    new_lst = [list(i) for i in tpl]
    return new_lst


def str_append(nodes=None):
    global str_nodes
    for node in nodes:
        if node != nodes[0]:
            str_nodes += ', ' + node
        else:
            str_nodes += node
    # print(str_nodes)
    str_nodes += '\n'


def get_max_lenght_recursiv(G: nx.DiGraph, vertex, previous_vertexes=None,):
    if previous_vertexes == None:
        previous_vertexes = []
    while (previous_vertexes != [] and len(list(G.predecessors(vertex))) > 0
            and previous_vertexes[-1] not in G.predecessors(vertex)):
        previous_vertexes.remove(previous_vertexes[-1])
    if vertex not in previous_vertexes:
        previous_vertexes += [vertex]
        # list_append(previous_vertexes)
    else:
        return len(previous_vertexes)
    if len(list(G.successors(vertex))) > 0:
        lenghts = []
        child_vertexes = list(G.successors(vertex))
        # print("G.successors(vertex) ", list(child_vertexes))
        for child_vertex in child_vertexes:
            # print("child_vertex = ", child_vertex)
            lenght = get_max_lenght_recursiv(G, child_vertex, previous_vertexes, )
            lenghts += [lenght]
            str_append(previous_vertexes)
        return max(lenghts)
    else:
        # print("!!!!!else!!!!!")
        return len(previous_vertexes)


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


def find_longest_path_sub(graph):
    max_path = []
    for node in graph.nodes():
        candidate_path = find_longest_path_from(graph, node)
        if len(candidate_path) > len(max_path):
            max_path = candidate_path
    return max_path


def find_longest_path(graph):
    max_path = []
    q = queue.Queue()
    subgraph = subgraphs(graph)
    for sub in subgraph:
        q.put(find_longest_path_sub(sub))
    while not q.empty():
        if len(q.get()) > len(max_path):
            max_path = q.get()
    return max_path
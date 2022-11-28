import pandas as pd
import networkx as nx

def as_spanning_trees(G):
    G2 = nx.DiGraph()
    # We find the connected constituents of the graph as subgraphs
    graphs = (G.subgraph(c) for c in nx.weakly_connected_components(G))

    # For each of these graphs we extract the spanning tree, removing the cycles
    for g in graphs:
        T = nx.algorithms.minimum_spanning_tree(g.to_undirected())
        E = set(T.edges())  # optimization
        # l = [e for e in G.edges() if e in E or reversed(e) in E]

        G2.add_edges_from(E)
        G2.add_nodes_from(T.nodes())

    return G2


def make_example_graph():
    example = nx.DiGraph()
    example.add_edges_from([("root", "a"), ("a", "b"), ("a", "e"), ("b", "c"), ("b", "d"),
                            ("d", "a"), ("g", "f"), ("f", "p"), ("p", "o"), ("o", "u"), ("u", "i"), ("i", "g")])
    # print("Directed? ", nx.is_directed(example))
    return example


def make_graph(df):
    graph = nx.DiGraph()
    # df_to_graph = df.values.tolist()
    graph.add_weighted_edges_from(df)
    # print(nx.is_directed_acyclic_graph(graph))
    # print(nx.is_directed(graph))
    # print(nx.find_cycle(graph))
    return graph

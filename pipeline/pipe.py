from pipeline.steps.get_max_lenght import get_max_lenght
from pipeline.steps.get_max_lenght import get_max_len
from pipeline.steps.get_max_lenght import get_paths
from pipeline.steps.make_graph import make_graph
from pipeline.steps.make_graph import make_example_graph
from pipeline.steps.preprocessing import preprocessing_spark
from pipeline.steps.load_data import load_data
from pipeline.steps.draw_longest_path import draw_networkx
from pipeline.steps.draw_longest_path import to_nx_path
from pipeline.steps.draw_longest_path import list_to_nx_path
from pipeline.steps.get_max_lenght import find_longest_path

def pipeline():
    data = load_data('/Users/ekaterinaakulova/PycharmProjects/pythonProject/data/data4task.csv')
    data = preprocessing_spark(data, 1000)
    graph = make_graph(data)
    max_len = get_max_len(graph)
    path = get_paths(max_len)
    to_draw = to_nx_path(path)
    print("to_draw = ", to_draw)
    draw_networkx(to_draw)
    print("PATH get_max_len_recursive = ", get_paths(max_len))
    print("LEN get_max_len_recursive = ", max_len)

    print("\n-----------------------------------------\n")
    max_lenght = get_max_lenght(graph)
    print("PATH get_max_lenght = ", max_lenght)
    print("LEN get_max_lenght = ", len(max_lenght))

    print("\n-----------------------------------------\n")
    print("FINAL")
    path_final = find_longest_path(graph)
    print("PATH find_longest_path = ", path_final)
    print("LEN find_longest_path = ", len(path_final))
    to_draw = list_to_nx_path(graph, path_final)
    print("to_draw = ", to_draw)
    draw_networkx(to_draw)


def pipeline_example():
    example = make_example_graph()
    max_len = get_max_len(example)
    path = get_paths(max_len)
    print("PATH get_max_len_recursive = ", get_paths(max_len))
    print("LEN get_max_len_recursive = ", max_len)
    to_draw = to_nx_path(path)
    # print("to_draw = ", to_draw)
    draw_networkx(to_draw)
    print("-----------------------------------------")

    max_lenght = get_max_lenght(example)
    print("PATH get_max_lenght = ", max_lenght)
    print("LEN get_max_lenght = ", len(max_lenght))




def another_example():
     data = load_data('/Users/ekaterinaakulova/PycharmProjects/pythonProject/data/data4task.csv')
     data = preprocessing_spark(data, 1000)
     graph = make_graph(data)
    # max_len = get_max_len(graph)
    # example = make_example_graph()
     l = find_longest_path(graph)
     print(l)


if __name__ == '__main__':
    # another_example()
     # pipeline_example()
    # print("----------------------------------")
    pipeline()

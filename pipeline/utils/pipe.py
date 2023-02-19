from pipeline.steps.get_max_lenght import get_max_lenght
from pipeline.steps.make_graph import make_graph
from pipeline.steps.make_graph import make_example_graph
from pipeline.steps.preprocessing import preprocessing_spark
from pipeline.steps.load_data import load_data
from pipeline.steps.draw_longest_path import draw_networkx
from pipeline.steps.draw_longest_path import list_to_nx_path
from pipeline.steps.get_max_lenght import find_longest_path_nodes_mp
from pipeline.steps.get_max_lenght import find_longest_path_with_multiprocessing
from data.tests.test_len import check_path, pipeline_example, test_find_longest_path
import time


def pipeline():
     data = load_data('data/data4task.csv')
     data = preprocessing_spark(data, 8500)
     graph = make_graph(data)
     start_time = time.time()
     l = find_longest_path_with_multiprocessing(graph)
     print("--- %s seconds ---" % (time.time() - start_time))
     print(l)
     start_time = time.time()
     l2 = find_longest_path_nodes_mp(graph)
     print("--- %s seconds ---" % (time.time() - start_time))
     print(l2)
     start_time = time.time()
     l3 = get_max_lenght(graph)
     print("--- %s seconds ---" % (time.time() - start_time))
     print(l3)
     lens = [l, l2, l3]
     final = max(lens, key=len)
     print("FINAL PATH = ", final)
     if check_path(graph, final):
         path = list_to_nx_path(graph, final)
         draw_networkx(path)


if __name__ == '__main__':
       # pipeline()
       # pipeline_example()
       print(test_find_longest_path())


from multiprocessing import Pool
from loguru import logger


def f(x):
    logger.info(x)


def parallel_for():
    with Pool(20) as pool:
        pool.map(f, range(100))


if __name__ == '__main__':
    parallel_for()



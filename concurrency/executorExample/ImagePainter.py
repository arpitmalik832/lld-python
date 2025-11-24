from concurrent.futures import as_completed
from concurrent.futures.thread import ThreadPoolExecutor
from math import floor


def image_quadrant_painter(no_of_rows, no_of_columns, color):
    return [[color for _ in range(no_of_columns)] for _ in range(no_of_rows)]


class ImagePainter:
    def __init__(self, image):
        self.__image = image

    def paint_image(self, color):
        rows = len(self.__image)
        cols = len(self.__image)
        half_rows = floor((rows + 1) / 2)
        half_cols = floor((cols + 1) / 2)

        executor = ThreadPoolExecutor(max_workers=4)
        futures = [
            executor.submit(image_quadrant_painter, half_cols, half_rows, i * color)
            for i in range(1, 5)
        ]
        results = [future.result() for future in as_completed(futures)]

        for i in range(len(results[0])):
            for j in range(len(results[0][0])):
                self.__image[i][j] = results[0][i][j]

        for i in range(len(results[1])):
            for j in range(len(results[1][0])):
                self.__image[i][half_cols + j] = results[1][i][j]

        for i in range(len(results[2])):
            for j in range(len(results[2][0])):
                self.__image[half_rows + i][j] = results[2][i][j]

        for i in range(len(results[3])):
            for j in range(len(results[3][0])):
                self.__image[half_rows + i][half_cols + j] = results[3][i][j]

        executor.shutdown()

    def get_image(self):
        return self.__image


def main():
    image = [[0 for _ in range(4)] for _ in range(4)]

    painter = ImagePainter(image)
    painter.paint_image(1)

    painted_image = painter.get_image()
    for i in range(len(painted_image)):
        line = ""
        for j in range(len(painted_image[i])):
            line += str(painted_image[i][j]) + " "
        print(line)


main()

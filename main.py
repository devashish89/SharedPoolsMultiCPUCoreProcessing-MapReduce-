import time
from multiprocessing import Pool
import os
import cv2

print("No. of CPU cores:", os.cpu_count())


def f(num):
    return num*num


if __name__ == '__main__':

    t1 = time.time()
    p = Pool(processes=8) #run it on 8 cores
    result = p.map(func=f, iterable=range(10000))
    p.close()
    p.join()
    # print(result)
    t2 = time.time()
    print("Time taken:", t2-t1)

    img = cv2.imread("MapReduce.jpg")
    # print(img)
    cv2.imshow("Map Reduce", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


import numpy

import scipy 

#활성화함수 정의
def step(x):
    if x >=0:
        return 1
    else:
        return 0
# CodingTest_Practice

네이버 ai 부트캠프의 코딩테스트를 위한 준비작업

2022.06.24

### sys.stdin.readline()

여러 줄 입력 받을 경우 input() 대신 사용(시간초과 개선)

import sys 필요

### combinations 함수

```` python
from itertools import combinations

for _ in combinations(list, 3):
    sum = sum(_)
````

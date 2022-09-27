import random
from demos import *
import time

list_size = int(input("What size list do you want to create? "))
max_value = int(input("What is the max value of range? "))
run_amount = int(input("How many times do you want to run? "))


def create_list():
    int_list = []
    for _ in range(list_size):
        int_list.append(random.randint(0, max_value))
    return int_list

def analyze_func(func_name, arr):
    tic = time.time()
    func_name(arr)
    toc = time.time()
    seconds = toc - tic
    print(f"{func_name.__name__.capitalize()}\t-> Elapsed time: {seconds:.5f}")

for run in range(run_amount):
    print(f"Run: {run + 1}")
    l = create_list()

    analyze_func(quicksort, l)
    analyze_func(mergesort, l)
    #analyze_func(selectsort, l)
    analyze_func(sorted, l)
    print("-" * 40)



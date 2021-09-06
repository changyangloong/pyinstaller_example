# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 16:58:45 2021

@author: user
"""
import argparse
import numpy as np

def sort_number(nums):
    print(f'before:{nums}')
    print(f'after:{np.sort(nums)}')

if __name__ == '__main__':   
    parser = argparse.ArgumentParser(description='Pyinstaller example')
    parser.add_argument('--number_to_sort', nargs='+', default=[4,6,2,7], 
                        help='Number to sort')
    args = parser.parse_args()
    sort_number(nums = [float(x) for x in args.number_to_sort])
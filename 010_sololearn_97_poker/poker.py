#!/usr/bin/env python3

import os
import sys

def count_list(lst):
    d = {}
    for x in lst:
        d[x] = d.get(x, 0) + 1
    return d

def to_num(v):
    if v == 'J': return 11
    if v == 'Q': return 12
    if v == 'K': return 13
    if v == 'A': return 14
    return int(v)

def main():
    hand = sys.stdin.readline().strip().split(" ")
    values = list(map(to_num, map(lambda x:x[0:-1], hand)))
    suits = list(map(lambda x:x[-1], hand))
    
    # print(hand)
    # print(values)
    # print(suits)
    
    suits_dict          = count_list(suits)
    values_dict         = count_list(values)
    sorted_values       = sorted(values)
    sorted_values_count = sorted(values_dict.values(), reverse=True)
    
    # print(suits_dict)
    # print(values_dict)
    # print(sorted_values)
    # print(sorted_values_count)
    
    #--- is Straight ?
    is_straight = False
    if len(sorted_values) == 5 and sum(sorted_values) == sorted_values[0] * 5 + 10:
        is_straight = True

    #--- is Flush ?
    is_flush = False
    if len(suits_dict) == 1:
        is_flush = True

    #--- Royal Flush
    if sum(values) == 60:
        print("Royal Flush")
        return
    
    #--- Straight Flush
    if is_flush and is_straight:
        print("Straight Flush")
        return
    
    #--- Four of a Kind
    if sorted_values_count[0] == 4:
        print("Four of a Kind")
        return
    
    #--- Full House
    if sorted_values_count[0:2] == [3,2]:
        print("Full House")
        return
    
    #--- Flush
    if is_flush:
        print("Flush")
        return

    #--- Straight
    if is_straight:
        print("Straight")
        return
    
    #--- Three of a Kind
    if sorted_values_count[0] == 3:
        print("Three of a Kind")
        return
    
    #--- Two Pairs
    if sorted_values_count[0:2] == [2,2]:
        print("Two Pairs")
        return
    
    #--- One Pair
    if sorted_values_count[0] == 2:
        print("One Pair")
        return

    #--- High Card
    print("High Card")

    sys.exit(0)

if __name__ == '__main__':
    main()


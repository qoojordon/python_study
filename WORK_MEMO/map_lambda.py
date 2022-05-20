#!/usr/bin/env python3

def rm(sa):
    return sa.strip()

TEST_LIST=[
"line1\n",
"line2\n",
"line3\n"
]

if __name__ == "__main__":
    
    print('== begin ==')
    print(f"step1-1: {      rm(line) for line in TEST_LIST }")
    print(f"step1-2: {list (rm(line) for line in TEST_LIST)}")
    print(f"{TEST_LIST}")

    print(f"step2-1: {      map(rm,TEST_LIST) }")
    print(f"step2-2: {list( map(rm,TEST_LIST) )}")
    print(f"{TEST_LIST}")

    print(f"step-3: {list( map(lambda x: x.strip(), TEST_LIST) )}")
    print(f"{TEST_LIST}")

    with open("a.txt", 'r') as f:
        for line in list(map( lambda x: x.strip(), f.readlines() )):
            print(f"{line}")
    print('== end ==')

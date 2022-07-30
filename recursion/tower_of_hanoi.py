def tower_of_hanoi(n,A,B,C):
    if n==1:
        print(f"Disc {n} moves from {A} to {C}.")
    else:
        tower_of_hanoi(n-1,A,C,B)
        print(f"Disc {n} moves from {A} to {C}.")
        tower_of_hanoi(n-1,B,A,C)

if __name__ == '__main__':
    tower_of_hanoi(4,"A","B","C")
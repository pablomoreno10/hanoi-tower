# Tower of Hanoi solution using recursion, even though recursion melts my brain
def hanoi_tower(N, first, middle, destination):
    if N == 1:
        # Move the smallest disk directly
        print(f"Move disk 1 from {first} to {destination}")
        return

    #Move N-1 disks from source to helper using destination as temp
    hanoi_tower(N-1, first, destination, middle)

    #Move the largest disk (N) from source to destination
    print(f"Move disk {N} from {first} to {destination}")

    #Move N-1 disks from helper to destination using source as temp
    hanoi_tower(N-1, middle, first, destination)
  
def main():
    hanoi_tower(3, "A", "B", "C")

if __name__ == "__main__":
    main()

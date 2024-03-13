# Example file for Programming Foundations: Algorithms by Joe Marini
# use recursion to implement a countdown counter


def countdown(x):
    if x == 0:
        print("Done!")
    else:
        print(x, "...")
        countdown(x - 1)
        print("Hey") # hey its called after all the "..."


countdown(5)

# python3
#arturs janis karss 211rec029
def parallel_processing(n: int, m:int, data: list) -> list:
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    threads =[(i,0) for i in range (n)]
    t = data[i]
    thread = min(threads, key=lambda x: x[1])
    output.append((thread[0], thread[1]))
    threads[threads.index(thread)] = (thread[0], thread[1] + t)
    return output

def main() -> None:
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    n,m = map (int, input().split())
    data = list(map(int, input().split()))
    
    # n = 0
    # m = 0

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    # data = []

    # TODO: create the function
    result = parallel_processing(n,m,data)
    for t in result:
        print(t[0], t[1])
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()

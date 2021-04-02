# This program obtains the class-precedence list for given three example class hierarchies 
# starting from the given nodes by structing those examples as a graph data structure
# and applying iterative topologial sort on them starting from a given node
tempvar=99
def dummyfunct():
    print("dummy")

# This funtion applies iterative topological sort on a graph starting from the given node
def iterative_topological_sort(graph, start):
    seen = set()    # will be the list of visited nodes
    # stack will hold the 
    stack = []      # path variable is gone, stack and order are new
    # order will hold the class-precedence list
    order = []      # order will be in reverse order at first
    q = [start]     # q is the given start node
    print("start node is : ", q, "\n")
    while q:    # will loop while q exists
        v = q.pop() # v is the current node
        print("visited node is : ", v)
        if v not in seen: 
            # if the current node is not in the seen list
            # it will be added to the seen list to be maked as visited
            seen.add(v)     # no need to append to path any more
            q.extend(graph[v])  # adding the parent node(s) to q list
            print("next node(s) : ",q)
            # while stack and visited node are not the parent node(s)
            # add stack's last element to order list
            while stack and v not in graph[stack[-1]]: # new stuff here
                order.append(stack.pop())
            stack.append(v) # add the current node to the stack list 
            print("So far the class-precedence list is : ", stack, "\n")
    print("The result is : ")
    return stack + order[::-1]   # returns the new return value


# First example in the homework is structed as a graph and added "Everything" node at top
ex1 = {
    'iostream_withassign': ['iostream'],
    'iostream':['istream(input)', 'ostream(output)'],
    'istream_withassign(cin)': ['istream(input)'],
    'ostream_withassign(cout, cerr, clog)': ['ostream(output)'],
    'istream(input)': ['ios'],
    'ostream(output)': ['ios'],
    'ios': ['ios_base'],
    'ios_base': ['Everything'],
    'Everything': []
}
# The class-precedence list starting from the node istream_withassign(cin)
print("\n\n\nThe class-precedence list for example 1 : \n")
print (iterative_topological_sort(ex1, 'istream_withassign(cin)'))
# The class-precedence list starting from the node iostream_withassign
print("\n\n\nThe class-precedence list for example 1 : \n")
print (iterative_topological_sort(ex1, 'iostream_withassign'))
# The class-precedence list starting from the node ostream_withassign(cout, cerr, clog)
print("\n\n\nThe class-precedence list for example 1 : \n")
print (iterative_topological_sort(ex1, 'ostream_withassign(cout, cerr, clog)'))


# Second example in the homework is structed as a graph and added "Everything" node at top
ex2 = {
    'RotamerToSequenceGraphLBwrapper': ['BaseSequenceSpaceGraphLBwrapper'],
    'SequenceSpaceGraphLBwrapper':['BaseSequenceSpaceGraphLBwrapper'],
    'BaseSequenceSpaceGraphLBwrapper': ['GraphLBwrapper'],
    'GraphLBwrapper': ['GraphWrapper'],
    'Astar': ['GraphWrapper'],
    'GraphWrapper': ['Graph'],
    'Graph': ['Everything'],
    'Everything': []
}
# The class-precedence list starting from the node Astar
print("\n\n\nThe class-precedence list for example 2 : \n")
print (iterative_topological_sort(ex2, 'Astar'))
# The class-precedence list starting from the node RotamerToSequenceGraphLBwrapper
print("\n\n\nThe class-precedence list for example 2 : \n")
print (iterative_topological_sort(ex2, 'RotamerToSequenceGraphLBwrapper'))
# The class-precedence list starting from the node SequenceSpaceGraphLBwrapper
print("\n\n\nThe class-precedence list for example 2 : \n")
print (iterative_topological_sort(ex2, 'SequenceSpaceGraphLBwrapper'))


# Third example in the homework is structed as a graph and added "Everything" node at top
ex3 = {
    'puddle::MetaTemplatedClass': ['puddle::MetaTemplatedType', 'puddle::MetaClass'],
    'puddle::MetaTemplatedType':['puddle::MetaType'],
    'puddle::MetaClass': ['puddle::MetaType', 'puddle::MetaScope'],
    'puddle::MetaType': ['puddle::MetaNamedScopedObject'],
    'puddle::MetaScope': ['puddle::MetaNamedScopedObject'],
    'puddle::MetaNamedScopedObject': ['puddle::MetaNamedObject', 'puddle::MetaScopedObject'],
    'puddle::MetaNamedObject': ['puddle::MetaObject'],
    'puddle::MetaScopedObject': ['puddle::MetaObject'],
    'puddle::MetaObject': ['Everything'],
    'Everything': []
}
# The class-precedence list starting from the node puddle::MetaTemplatedClass
print("\n\n\nThe class-precedence list for example 3 : \n")
print (iterative_topological_sort(ex3, 'puddle::MetaTemplatedClass'), "\n\n\n")






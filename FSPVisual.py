from Tkinter import *
root = Tk()

w = Canvas(root, width=800, height=600)
w.pack()

widgetlist = []

Gvertices = []
Gsearched = {}
Gparent = {}

class Graph:
    def __init__(self,n):
        self.name = n
        self.graph = {}

    def add_vertex(self, vertex):
        self.graph[vertex] = []
        Gvertices.append(vertex)
        Gsearched[vertex] = False
        Gparent[vertex ] = None

    def add_edges(self, vertex, edges):
        self.graph[vertex].append(edges)

G = Graph('G')

coords = []
vertices_save = {}
alphab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def createcoor(event):
    coords.append((event.x, event.y))

    if len(coords) == 1:
        btn = Button(root, text=alphab[0], bg='white', command = lambda j=alphab[0]: clickbutton(j))
        btn.place(x=coords[0][0], y=coords[0][1])
        widgetlist.append(btn)
        vertices_save[alphab[0]] = (coords[0][0], coords[0][1])
        G.add_vertex(alphab[0])
        del alphab[0]

    if len(coords) == 1:
        del coords[0]

w.bind("<Button-1>", createcoor)

connecter = []

def clickbutton(a):
    connecter.append(a)
    if len(connecter) == 2:
        w.create_line(vertices_save[connecter[0]][0],vertices_save[connecter[0]][1], vertices_save[connecter[1]][0], vertices_save[connecter[1]][1])
        G.add_edges(connecter[0], (connecter[0], connecter[1]))
        G.add_edges(connecter[1], (connecter[1], connecter[0]))
        del connecter[0]
        del connecter[0]

def neighbors(g,v):
    nbs = []
    for i in range(len(g[v])):
        nbs.append(g[v][i][1])
    return nbs

# def printgraph1():
#     print 'Graph = ' + str(G.graph)
#     print 'Gsearched = ' + str(Gsearched)
#     print 'Gparent = ' + str(Gparent)
#     print 'Gvertices = ' + str(Gvertices)
#
# printgraph = Button(root, text="print graph", command = printgraph1)
# printgraph.pack(side = LEFT)

entry1 = Entry(root)
entry1.pack(side = RIGHT)
label2 = Label(root, text='Goal')
label2.pack(side = RIGHT)
entry2 = Entry(root)
entry2.pack(side = RIGHT)
label1 = Label(root, text='Start')
label1.pack(side = RIGHT)

def fsp(graph, start, goal):
    queue = [start]
    while len(queue) > 0:
        if queue[0] == goal:
            break
        else:
            Gsearched[queue[0]] = True
            for i in neighbors(graph, queue[0]):
                if ((Gsearched[i] == False) and (i not in queue)):
                    queue.append(i)
                    Gparent[i] = queue[0]
            queue.pop(0)
    node = goal
    path = [node]
    while True:
        for i in neighbors(graph, node):
            if i == Gparent[node]:
                path.append(i)
        node = Gparent[node]
        if node == start:
            print "Shortest path from " + start + " to " + goal + " is ",
            for i in path[::-1]:
                if i != goal:
                    print i + " - ",
                if i == goal:
                    print i + " with length: " + str(len(path)) + "."
            for p in widgetlist:
                if p.cget('bg') == 'green':
                    p.config(bg='white')
            for k in path:
                for m in widgetlist:
                    if k == m.cget('text'):
                        m.config(bg='green')
            for key in Gsearched:
                Gsearched[key] = False
            for key in Gparent:
                Gparent[key] = None
            break

def FSPexec():
    fsp(G.graph, entry2.get(), entry1.get())

FsPBtn = Button(root, text="Find Shortest Path from Start to Goal", command=FSPexec)
FsPBtn.pack(side = LEFT)

# def printWidgetlist():
#     list1 = []
#     for i in widgetlist:
#         list1.append(i.cget('text'))
#     print list1
#
# printwidgs = Button(root, text="Print list of widgets", command=printWidgetlist)
# printwidgs.pack(side = LEFT)

root.mainloop()
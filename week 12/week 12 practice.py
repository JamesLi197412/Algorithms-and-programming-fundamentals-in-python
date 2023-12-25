def task1():
    #   Task 1: Max-Clique Problem

    def createMatrix(filename):
        edgesFile = open(filename)
        adjMat = vertices * [0]
        for vertex in range(vertices):
            adjMat[vertex] = vertices * [0]

            #   This segment generates teh adjacency matrix
            for lin in edgesFile:
                edgeEndpoints = line.split()

                #   Uses the splits as indecies in the adj matrix
                adjMat[int(edgeEndpoints[0])][int(edgeEndpoints[1])] = 1

                #   Adjacency matrix of an undirected graph is symmetrical
                adjMat[int(edgeEndpoints[1])][int(edgeEndpoints[0])] = 1

            edgesFile.close()
            return adjMat

    def cliqueChecker(adjMat, cliqueSize, fileName):
        cliqueFile = open(fileName)
        validClique = True
        for line in cliqueFile:
            potClique = line.strip().split(',')
            validClique = True

            for vert in range(len(potClique)):
                for adj in range(vert + 1, len(potClique)):
                    if adjMat[int(potClique[vert])][int(potClique[adj])] == 0:
                        validClique = validClique and False

                    if validClique == True and len(potClique) == cliqueSize:
                        print(potClique, ' Yes')

                    else:
                        print(potClique, 'No')

            cliqueFile.close()

    vertices = int(input('Please input the number of vertices: '))
    fileName = input('Please enter the name of file: ')
    cliqueSize = int(input('Enter the clique size: '))
    clFile = input(' Enter the filename for clique: ')
    edgesFile = open(fileName)
    adjMat = createMatrix(fileName)
    cliqueChecker(adjMat, cliqueSize, clFile)


def task2():
    #   Task 2: certificate to Max-Independent Set Problem
    def createMatrix(filename):
        edgesFile = open(filename)
        adjMat = vertices * [0]
        for vertex in range(vertices):
            adjMat[vertex] = vertices * [0]

            #   This segment generates teh adjacency matrix
            for lin in edgesFile:
                edgeEndpoints = line.split()

                #   Uses the splits as indecies in the adj matrix
                adjMat[int(edgeEndpoints[0])][int(edgeEndpoints[1])] = 1

                #   Adjacency matrix of an undirected graph is symmetrical
                adjMat[int(edgeEndpoints[1])][int(edgeEndpoints[0])] = 1

            edgesFile.close()
            return adjMat

    def indsetChecker(adjMat, independentsetSize, fileName):
        indFile = open(fileName)
        flag = True

        for line in indFile:
            potInd = line.strip().split(',')
            for vert in range(len(potInd)):
                for adj in range(vert + 1, len(potInd)):
                    if adjMat[int(potInd[vert])][int(potInd[adj])] == 1:
                        validIndSet = validIndSet and False
                        break
                if validIndSet == True and len(potInd) == independentsetSize:
                    print(potInd, 'Yes')
                else:
                    print(potInd, 'No')

        indFile.close

    vertices = int(input(' Please input the number of vertices: '))
    fileName = input('Please enter the name of file: ')
    independentsetSize = int(input('Enter the independent set size: '))
    isetFile = input(' Enter the filename for independent set: ')
    edgesFile = open(fileName)
    adjMat = createMatrix(fileName)
    indsetChecker(adjMat, independentsetSize, isetFile)

def task3():
    ##  Task 3: Find complement of a graph

    def complement(adjMat):
        tempMat = copy.deepcopy(adjMat)
        for row in range(len(tempMat)):
            for col in range(len(tempMat)):
                if tempMat[row][col] == 0:
                    tempMat[row][col] = 1
                    tempMat[col][row] = 1
                else:
                    tempMat[row][col] = 0
                    tempMat[col][row] = 0

        return tempMat

def taskworkshop():
    """
    How to use this file.

    read the testGraph.txt file as a list of lines and call this FileData

    M.isAdjacent(vertexNameOne,vertexNameTwo) will be True/False if the
    two vertices have an edge between them

    M.getVertexNames() will give you a list of the names of vertices in the
    graph

    print whatever you want to see to the console
    """

    class adjMatrix:
        def __init__(self, edgeList):
            self._matrix = []
            self.vertexMap = dict()
            self.populateMatrix(edgeList)

        """
        gets the mapping for the vertex name given
        """

        def _ID(self, vName):
            return self.vertexMap[vName]

        """
        goes through a list of strings or list of pairs of names (list)
        and converts into a list of lists for later use. Can also handle
        a mix of list of list and list of string (provided space/comma sep)
        (if given a list of lists, output is unchanged)
        outputs processed version
        """

        def processEdgeList(self, edgeList):
            processedEdgeList = []
            for each in edgeList:
                if type(each) == type(""):
                    each = each.strip()
                    if 1 <= each.count(" ") <= 2:  # either a vertex pair
                        #  or vertex pair with weight
                        each = each.split(" ")  # for space sep
                    elif 1 <= each.count(",") <= 2:
                        each = each.split(",")  # for comma sep
                    else:
                        raise ValueError(
                            "list of edges (if given as a list of strings) must be two vertex names separated by a space or a comma")
                    processedEdgeList.append(each)
                elif type(each) == type([]):
                    processedEdgeList.append(each)
                else:
                    raise ValueError("edge list must either be a list of lists (or vertex names) or a list of strings")
            return processedEdgeList

        """
        assigns an appropriate mapping to a set (python type) of vertices
        by order in the set
        modifies self.vertexMap
        """

        def mapVertexNames(self, uniqueVertices):
            vertNum = 0
            for vertex in uniqueVertices:
                self.vertexMap[vertex] = vertNum
                vertNum += 1

        """
        accepts an edgeList (as a list of pairs of vertices)
        outputs a set (python type) of unique vertices
        """

        def getUniqueVertices(self, edgeList):
            vertices = set()
            for each in edgeList:
                if each[0] not in vertices:
                    vertices.add(each[0])
                if each[1] not in vertices:
                    vertices.add(each[1])
            return vertices

        """
        constructs an n by n matrix of zeroes for overwriting
        changes self._matrix to match
        """

        def zeroMatrix(self, numVertices):
            for _ in range(numVertices):
                self._matrix.append([0] * numVertices)

        """
        takes a list of edges and adds these edges into the matrix
        self._matrix is updated to match

        precond: vertexmapping must be defined already and edgeList must
                be a list of lists (pairs of vertex names) 
                self._matrix must be defaulted to correct size already 
        """

        def edgeListToEdges(self, edgeList):
            weight = 1  # default weight
            for edge in edgeList:
                start = self._ID(edge[0])
                end = self._ID(edge[1])
                if len(edge) == 3:  # then this has a weight
                    weight = edge[2]  # for each edge
                    # overwrite with correct weight
                self._matrix[start][end] = weight

        """
        accepts a raw edge list (either a list of lists of vertex name pairs
        or a list of strings of two vertices seperated by space/comma)
        no outputs, modifies self._matrix
        """

        def populateMatrix(self, rawEdgeList):
            edgeList = self.processEdgeList(rawEdgeList)
            vertices = self.getUniqueVertices(edgeList)
            self.zeroMatrix(len(vertices))
            # now we have the set of unique vertices, let's make the mapping then matrix
            self.mapVertexNames(vertices)
            self.edgeListToEdges(edgeList)

        """
        gives the full list of vertex names in this graph
        """

        def getVertexNames(self):
            return self.vertexMap.keys()

        """
        determines whether any two vertices are adjacent
        @:param vertOne: a string holding the name of the first vertex
        @:param vertTwo: a string holding the name of the second vertex
        @:return True/False: if adjacent/not adjacent
        """

        def isAdjacent(self, vertOne, vertTwo):
            start = self._ID(vertOne)
            end = self._ID(vertTwo)
            return not self._matrix[start][end] == 0

    FileData = []  # you will need to replace this with the list from the file

    ### your code here

    M = adjMatrix(FileData)

    vertexNames = M.getVertexNames()  # this is a list of all vertices in the graph

    DogCatAdjacent = M.isAdjacent("dog", "cat")  # this is True if
    # the vertex "dog" is adjacent to the vertex "cat"
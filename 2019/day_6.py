class Node:
    def __init__(self, data):
        self.item = data
        self.nref = []
        self.pref = None

def constructNodes(connections):
  foundItems = dict()
  nodes = []

  for connection in connections:
    orbited, orbiter = connection.split(")")
    orbitedNode = None
    orbiterNode = None

    if orbited not in foundItems:
      foundItems[orbited] = 1
      orbitedNode = Node(orbited)
      nodes.append(orbitedNode)
    elif orbited in foundItems:
      for node in nodes:
        if node.item == orbited:
          orbitedNode = node

    if orbiter not in foundItems:
      foundItems[orbiter] = 1
      orbiterNode = Node(orbiter)
      nodes.append(orbiterNode)
    elif orbiter in foundItems:
      for node in nodes:
        if node.item == orbiter:
          orbiterNode = node
  
    orbitedNode.nref.append(orbiterNode)
    orbiterNode.pref = orbitedNode
  
  return len(foundItems), nodes

def distanceToCOM(node, d=0):
  if node.pref == None:
    return d
  return distanceToCOM(node.pref, d+1)

def distanceBetweenMainChainNodes(node1, node2):
  pass

def getYOUNode(nodes):
  for node in nodes:
    if node.item == "YOU":
      return node
  return None

def getSANNode(nodes):
  for node in nodes:
    if node.item == "SAN":
      return node
  return None

def getCOMNode(nodes):
  for node in nodes:
    if node.item == "COM":
      return node
  return None

def getPathToCOM(node):
  prevNode = node
  path = []
  while prevNode.pref != None:
    path.append(prevNode)
    prevNode = prevNode.pref
  path.append(prevNode)
  return path

def distanctToCommonNode(commonNode, sourceNode):
  d = 0
  prevNode = sourceNode
  while prevNode.pref != None:
    if prevNode.item == commonNode.item:
      return d
    d += 1
    prevNode = prevNode.pref
  return d

def getCommonNode(nodes1, nodes2):
  commonNodes = [k for k in nodes1 if k in nodes2]
  return commonNodes[0] if len(commonNodes) > 0 else None

def part1(connections):
  foundItemsCount, nodes = constructNodes(connections)
  
  indirectOrbits = 0
  for node in nodes:
    d = distanceToCOM(node)
    indirectOrbits += d - 1
  return indirectOrbits + foundItemsCount

def part2(connections):
  _, nodes = constructNodes(connections)
  youNode = getYOUNode(nodes)
  path1 = getPathToCOM(youNode)
  sanNode = getSANNode(nodes)
  path2 = getPathToCOM(sanNode)

  commonNode = getCommonNode(path1, path2)

  if commonNode == None: return None

  d1 = distanctToCommonNode(commonNode, youNode) - 1
  d2 = distanctToCommonNode(commonNode, sanNode) - 1

  return d1 + d2


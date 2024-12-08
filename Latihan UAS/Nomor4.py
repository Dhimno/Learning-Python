from ListOfList import *

def akar(P):
    return P[0]

def anak(P):
    return P[1]

def isTreeNEmpty(P):
    return P == []

# ===========================================================

def IsSame(x, PN):
    return x == PN[0]  # Check if the value matches the first element of the pair (node, subtree)

def FlattenTreePN(x, PN):
    # Base case: If PN is not a valid list structure, return None
    if not isinstance(PN, list) or len(PN) == 0:
        return None

    # Check if the current node matches
    if IsSame(x, PN):
        return PN[1]  # Return the subtree if the node matches
    
    # Recursive case: If the current node does not match, search the children
    if len(PN) > 1 and isinstance(PN[1], list):  # Ensure PN[1] exists and is a list
        # Check the first child and the remaining children separately
        result = FlattenTreePN(x, PN[1][0])
        if result is not None:  # If the result is found, return it
            return result
        return FlattenTreePN(x, [PN[0], PN[1][1:]])  # Check the remaining children
    
    return None  # Return None if no match is found

# Tree structure
T3 = ['A', 
        [
            ['B', 
                [
                    ['D', []], 
                    ['E', []], 
                    ['F', []]
                ]
            ], 
            ['C', 
                [
                    ['G', []], 
                    ['H', 
                        [
                            ['I', []]
                        ]
                    ]
                ]
            ]
        ]
    ]

# Testing the function
print(FlattenTreePN('C', T3))




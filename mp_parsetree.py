from binarytree import BinaryTree
from stack import Stack
import unittest
import operator
import random

def buildMPLogicParseTree(s):
    """ To build the logic Parse tree, getting each element for it. """
    fplist = s.split()
    pStack = Stack()
    leTree = BinaryTree('')
    pStack.push(leTree)
    currentTree = leTree


    for j in fplist:
        if j == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()

        elif j in ['AND', 'OR']:
            currentTree.setRootVal(j)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()

        elif j in[ 'T','F']:
            currentTree.setRootVal(j)
            parent = pStack.pop()
            currentTree = parent
        
        elif j[0] == 'M' or j[0] == 'P':
            currentTree.setRootVal(j[0])
            currentTree.insertLeft(j[2:])
            parent = pStack.pop()
            currentTree = parent

        elif j == ')':
            currentTree = pStack.pop()

        else:
            print("token '{}' is not a valid expression".format(j))
            return None

    return leTree
    

def evaluateMPLogicParseTree(t):
    """ Function to evaluate if the Logic parse tree function works properly using True,False,Maybe,and Probably """
    opers = {'AND':operator.and_, 'OR':operator.or_}
    
    leftC = t.getLeftChild()
    rightC = t.getRightChild()
    ran=random.random()

    if leftC and rightC:
    
       
        if leftC.getRootVal() == 'T':
            leftC = BinaryTree(True)
        elif leftC.getRootVal() =='F':
            leftC = BinaryTree(False)

        if rightC.getRootVal() == 'T':
            rightC = BinaryTree(True)
        elif rightC.getRootVal() == 'F':
            rightC = BinaryTree(False)
        
        

        if leftC.getRootVal() == 'M':
            h = leftC.getLeftChild()
            m = str(h.getRootVal())
            if 0<= float(m) and float(m)<= ran:
                leftC = BinaryTree(True)
            elif ran < float(m)and float(m)< 1:
                leftC  = BinaryTree(False)
        elif leftC.getRootVal() == 'P':
            h = leftC.getLeftChild()
            m = str(h.getRootVal())
            if 0<= float(m) and float(m) <= ran:
                leftC = BinaryTree(False)
            elif ran < float(m)and float(m) < 1:
                leftC = BinaryTree(True)
        if rightC.getRootVal() == 'M':
            h = rightC.getLeftChild()
            m = str(h.getRootVal())
            if 0<= float(m) and float(m)<= ran:
                rightC = BinaryTree(True)
            elif ran < float(m)and float(m)< 1:
                rightC  = BinaryTree(False)
        elif rightC.getRootVal() == 'P':
            h = rightC.getLeftChild()
            m = str(h.getRootVal())
            if 0<= float(m) and float(m) <= ran:
                rightC = BinaryTree(False)
            elif ran < float(m)and float(m) < 1:
                rightC = BinaryTree(True)

        fn = opers[t.getRootVal()]
        return fn(evaluateMPLogicParseTree(leftC),evaluateMPLogicParseTree(rightC))
    else:
        return t.getRootVal()



def printMPLogicExpression(t):
    """ Function to print the Logic tree expression."""
    sVal = ""

    if t:
        sVal = '(' + printMPLogicExpression(t.getLeftChild())
        sVal = sVal + str(t.getRootVal())
        sVal = sVal + printMPLogicExpression(t.getRightChild())+')'
    return sVal



class TestParseTree(unittest.TestCase):
    """ Extend unittest.TestCase and add methods to test HashTable """

    def testParseTreeBuildLogicOnly(self):
        """ Check that ParseTreePrints correctly a simple case."""
        pt = buildMPLogicParseTree('( T AND F )')
        expected='((T)AND(F))'
        self.assertEqual(printMPLogicExpression(pt),expected)

    def testParseTreeEvaluateLogicOnly(self):
        """ Check that ParseTreeWorks correctly a simple case."""
        pt = buildMPLogicParseTree('( T AND F )')
        expected=False
        self.assertEqual(evaluateMPLogicParseTree(pt),expected)

    def testParseTreeBuildProbMaybe(self):
        """ Check that ParseTreePrints correctly a moderate case."""
        pt = buildMPLogicParseTree('( P_0.9 OR M_0.4 )')
        expected='(((0.9)P)OR((0.4)M))'
        self.assertEqual(printMPLogicExpression(pt),expected)

    def testParseTreeBuildCombine(self):
        """ Check that ParseTreePrints correctly a moderate case."""
        pt = buildMPLogicParseTree('( ( T OR M_0.3 ) AND P_0.8 )')
        expected='(((T)OR((0.3)M))AND((0.8)P))'
        self.assertEqual(printMPLogicExpression(pt),expected)

def unittest_main():
    unittest.main()


def main():
    pt = buildMPLogicParseTree('( P_0.9 AND M_0.4 )')
    print("Evaluating parse tree...", evaluateMPLogicParseTree(pt))
    print(printMPLogicExpression(pt))

# only executed if run as a standalone program
if __name__ == '__main__':
    main()
    unittest_main()

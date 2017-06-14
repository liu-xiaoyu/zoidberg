#https://leetcode.com/problems/evaluate-reverse-polish-notation/#/description
import logging
log = logging.getLogger()
LOG_FILENAME = 'EvalRPN.log'
logging.basicConfig(filename=LOG_FILENAME, filemode='w', level=logging.DEBUG)

class Solution:
    operators = ['+', '-', '*', '/']
    def __init__(self):
        self.op_stack = []
        self.rpm_stack = []
        self.ret_stack = []

    class mytreenode:
        def __init__(self):
            self.data = None
            self.left = None
            self.right = None

    def createTree(self, tokens):
        for token in tokens:
            newNode = self.mytreenode()
            newNode.data = token
            if token not in self.operators:
                self.rpm_stack.append(newNode)
                log.debug("append token {0}".format(token))
            else:
                newNode.right = self.rpm_stack.pop()
                newNode.left = self.rpm_stack.pop()
                log.debug("find operator {0}, use {1} and {2} to form a tree".format(token, newNode.left.data, newNode.right.data))
                self.rpm_stack.append(newNode)

    def evalTree(self, rpm_stack):
        log.debug('evalTree...')
        for token in rpm_stack:
            if token.__class__.__name__ == 'mytreenode':
                self.evalNode(token)
            else:
                self.ret_stack.append(token)

    def evalNode(self, node):
        log.debug('evalNode...')
        if node is None:
            return
        if node.left is None:
            self.ret_stack.append(node.data)
        else:
            log.debug("node.left is {0}".format(node.left))
            self.ret_stack.append('(')
            self.evalNode(node.left)
            self.ret_stack.append(node.data)
            self.evalNode(node.right)
            self.ret_stack.append(')')

    def evalRPN(self, tokens):
        log.debug('evalRPN: {0}'.format(tokens))
        self.createTree(tokens)
        self.evalTree(self.rpm_stack)
        log.info('ret_stack: {0}'.format(self.ret_stack))




tests = []
token1 = ["2", "1", "+", "3", "*"]
token2 = ["4", "13", "5", "/", "+"]
tests.append(token1)
tests.append(token2)

for test in tests:
    mysolution = Solution()
    mysolution.evalRPN(test)
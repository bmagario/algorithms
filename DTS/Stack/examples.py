from Stack import Stack

def reverseStr(strVar):
	stack = Stack()
	for ch in strVar:
		stack.push(ch)
	result = ''
	while	not stack.isEmpty():
		result += stack.pop()
	return result

def parenthesisChecker(strVar):
	stack = Stack()
	balanced = True
	i = 0
	while i < len(strVar) and balanced:
		ch = strVar[i]
		if ch == '(':
			stack.push(ch)
		elif stack.isEmpty() and ch == ')':
			balanced = False
		elif ch == ')':
			stack.pop()
		
		i += 1

	return stack.isEmpty() and balanced

def parChecker(strVar):
	stack = Stack()
	balanced = True
	i = 0
	while i < len(strVar) and balanced:
		ch = strVar[i]
		if ch in "([{":
			stack.push(ch)
		else:
			if stack.isEmpty():
				balanced = False
			else:
				top = stack.pop()
				if not matches(top, ch):
					balanced = False
		
		i += 1

	return stack.isEmpty() and balanced


def matches(open, close):
	opens = "([{"
	closers = ")]}"
	return opens.index(open) == closers.index(close)

def divideBy2(num):
	stack = Stack()
	while num > 0:
		rest = num % 2
		num //= 2
		stack.push(rest)

	binStr = ''
	while not stack.isEmpty():
		binStr += str(stack.pop())

	return binStr

def baseConverter(num, base):
	digits = "0123456789ABCDEF"
	stack = Stack()

	while num > 0:
		rest = num % base
		num //= base
		stack.push(rest)

	binStr = ''
	while not stack.isEmpty():
		binStr += digits[stack.pop()]

	return binStr

def infixToPostfix(infixexpr):
	prec = {}
	prec["*"] = 3
	prec["/"] = 3
	prec["+"] = 2
	prec["-"] = 2
	prec["("] = 1
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	digits = "0123456789"
	opStack = Stack()
	postfixList = []
	tokenList = infixexpr.split()

	for token in tokenList:
		if token in alphabet or token in digits:
			postfixList.append(token)
		elif token == '(':
			opStack.push(token)
		elif token == ')':
			topToken = opStack.pop()
			while topToken != '(':
				postfixList.append(topToken)
				topToken = opStack.pop()
		else:
			while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
				postfixList.append(opStack.pop())
			opStack.push(token)

	while not opStack.isEmpty():
		postfixList.append(opStack.pop())

	return " ".join(postfixList)

def postfixEval(postfixExpr):
	operandStack = Stack()
	tokenList = postfixExpr.split()
	digits = "0123456789"

	for token in tokenList:
		if token in digits:
			operandStack.push(int(token))
		else:
			operand2 = operandStack.pop()
			operand1 = operandStack.pop()
			result = doMath(token,operand1,operand2)
			operandStack.push(result)
	return operandStack.pop()

def doMath(op, op1, op2):
	if op == "*":
		return op1 * op2
	elif op == "/":
		return op1 / op2
	elif op == "+":
		return op1 + op2
	else:
		return op1 - op2

print(postfixEval('7 8 + 3 2 + /'))
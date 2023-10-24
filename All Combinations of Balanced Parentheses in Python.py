Here on this page, we will learn how to generate All Combinations of Balanced Parentheses in Python programming language. We are given an integer N representing the number of pairs of parentheses, the task is to generate all combinations of well-formed(balanced) parentheses.

All Combinations of Balanced Parentheses

-------------------------------------------------------Algorithm ( Method 1 )-------------------------------------------------------A

Create a recursive function that accepts a string say s, count of opening brackets say, o and count of closing brackets say, c and the value of n.
If the value of the opening bracket and closing bracket is equal to n then print the string and return.
If the count of the opening bracket is greater than the closing bracket, then call the function recursively.
If the count of the opening bracket is less than n then call the function recursively.
All Combinations of Balanced Parentheses in Python

Python Code

def printParenthesis(str, n):
	if n > 0:
		_printParenthesis(str, 0, n, 0, 0)
	return


def _printParenthesis(str, pos, n, open, close):

	if close == n:
		for i in str:
			print(i, end="")
		print()
		return
	else:
		if open > close:
			str[pos] = '}'
			_printParenthesis(str, pos + 1, n, open, close + 1)
		if open < n:
			str[pos] = '{'
			_printParenthesis(str, pos + 1, n, open + 1, close)


n = 3
string = [""] * 2 * n
printParenthesis(string, n)
Output
{}{}{}
{}{{}}
{{}}{}
{{}{}}
{{{}}}

-------------------------------------------------------AAlgorithm ( Method 2 )-------------------------------------------------------A

In this method, we write the simple code for the above algorithm.

Run
def generateParenthesis(n, Open, close, s, ans):

    if Open == n and close == n:
        ans.append(s)
        return

    if Open < n:
        generateParenthesis(n, Open + 1, close, s + "{", ans)

    if close < Open:
        generateParenthesis(n, Open, close + 1, s + "}", ans)


n = 3
ans = []
generateParenthesis(n, 0, 0, "", ans)
for s in ans:
    print(s)
Output
{{{}}}
{{}{}}
{{}}{}
{}{{}}
{}{}{}

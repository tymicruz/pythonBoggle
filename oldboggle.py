import sys

def printBoard(board, rows, cols):
	print ("")

	print("board:")

	for i in range(len(board)):
		sys.stdout.write(board[i])
		sys.stdout.write(' ')

		if (i + 1) % cols == 0:
			print ("")

	print ("")

def wordExists(board, rows, cols, word):

	if not word or not board:
		print ("empty word: %s or board: %s" % (word, board))
		return 0;

	print ("looking for \"%s\"" % word)
	taken = []
	for letter in board:
		taken.append(0)

	first_letter = word[0]

	firsts = []

	for i in range(len(board)):
		if board[i] == first_letter:
			firsts.append(i)		

	if len(firsts) <= 0:
		print ("first letter of \"%s\" not found. word doesn't exist." % word)
		return 0

	for i in firsts:
		found = lookUp(board, i, rows, cols, word, 0, taken)
		if found:
			r = i / cols
			c = i % cols
			print ("found \"%s\" starting @ (%d, %d)" % (word, c + 1, r + 1))
			return 1

	print ("%s not found." % word)
	return 0

#board = array of chars simulating boggle board
#bindex = board index
#rows = # rows of boggle board
#cols = # cols of boggle board
#word = word we are searching for
#windex = word index
#taken = string which simulated bit array to check if letter was visited
def lookUp (board, bindex, rows, cols, word, windex, taken):

	if board[bindex] != word[windex]:
		return 0

	r = bindex / cols
	c = bindex % cols

	if windex + 1 == len(word):
		print ("done. found all of %s" % word)
		print ("found %s at (%d, %d)" % (word[windex], c + 1, r + 1))
		return 1

	#found letter keep moving

	#get indexes of virtual up, down, left, right of board array
	#if out of bounds, set to -1
	up = (r - 1) * cols + c if r - 1 >= 0 else -1
	down = (r + 1) * cols + c if r + 1 < rows else -1
	left = r * cols + c - 1 if c - 1 >= 0 else -1
	right = r * cols + c + 1 if c + 1 < cols else -1

	up = -1 if up >= 0 and taken[up] else up
	down = -1 if down >= 0 and taken[down] else down
	left = -1 if left >= 0 and taken[left] else left
	right = -1 if right >=0 and taken[right] else right

	#possible indexes to check
	ways = [up, left, down, right]

	for way in ways:
		#if way is negative, we can't go that way
		if way < 0:
			continue
		#set current bit corresponding to letter to indicate we used this letter
		taken[bindex] = 1
		#look rest of word in all a direction of way
		found = lookUp(board, way, rows, cols, word, windex + 1, taken)
		if found:

			print ("found %s at (%d, %d)" % (word[windex], c + 1, r + 1))
			return 1
		#that way didn't work do clear bit corresponding to letter
		taken[bindex] = 0


	return 0








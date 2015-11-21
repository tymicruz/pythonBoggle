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

	#get indexes of virtual up, down, left, right (north, sourth east, west)  of board array
	#if out of bounds, set to -1
	n = (r - 1) * cols + c if r - 1 >= 0 else -1 #north
	s = (r + 1) * cols + c if r + 1 < rows else -1 #south
	w = r * cols + c - 1 if c - 1 >= 0 else -1 #west
	e = r * cols + c + 1 if c + 1 < cols else -1 #east
	
	#diagonal directions
	ne = (r - 1) * cols + c + 1 if r - 1 >= 0 and c + 1 < cols else -1 #northeast
	nw = (r - 1) * cols + c - 1 if r - 1 >= 0 and c - 1 >= 0 else -1 #northwest
	se = (r + 1) * cols + c + 1 if r + 1 < rows and c + 1 < cols else -1 #southeast
	sw = (r + 1) * cols + c - 1 if r + 1 < rows and c - 1 >=0 else -1 #southwest

	#make sure direction hasn't already been visited
	n = -1 if n >= 0 and taken[n] else n
	s = -1 if s >= 0 and taken[s] else s
	w = -1 if w >= 0 and taken[w] else w
	e = -1 if e >= 0 and taken[e] else e
	
	ne = -1 if ne >= 0 and taken[ne] else ne
	nw = -1 if nw >= 0 and taken[nw] else nw
	se = -1 if se >= 0 and taken[se] else se
	sw = -1 if sw >= 0 and taken[sw] else sw

	#possible indexes to check
	ways = [n, s, w, e, ne, nw, se, sw]

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








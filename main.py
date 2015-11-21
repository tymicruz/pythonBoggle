import boggle
from boggle import sys

if __name__ == "__main__":
	print ("cruz boggle\n");
	rows = 0
	cols = 0
	board = []

	f = open("input")

	lines = f.readlines();

	loop_1 = 1
	input_line_number = 0

	#loop to read boggle board input file
	for li in lines:
		input_line_number = input_line_number + 1
		if li[0] == "#": 
			continue

		letters = li.split()

		if len(letters):
			rows = rows + 1
		else:
			#line full of spaces
			continue

		#each row must have same number of letters (cols)
		if (not loop_1) and cols != len(letters):
			#previous cols count doesn't equal this line's col count
			print("%d, %d, %d" % (loop_1, cols, len(letters)))
			print ("invalid board @ line %d" % input_line_number)
			boggle.sys.exit(-1)

		cols = 0

		for le in letters:
			cols = cols + 1
			board.append(le)

		loop_1 = 0
	#end of boggle board input file reading loop


	print ('#rows = %d', rows)
	print ('#cols = %d', cols)

	boggle.printBoard(board, rows, cols)

	sys.stdout.write("find word: ")
	uinput = boggle.sys.stdin.readline()
	uinput = uinput[0: len(uinput) - 1]

	#success = boggle.wordExists(board, rows, cols, "tylercruz")
	#success = boggle.wordExists(board, rows, cols, "zeeeeeeeeeeeeeek")
	success = boggle.wordExists(board, rows, cols, uinput)

	print ("")

	if success:
		print("NICE, SUCCESS!")
	else:
		print("BAD, FAIL!")
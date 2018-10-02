# This program accepts a chess piece and the square it sits on
# and returns all possible squares that piece could move to
# assuming that there are no other pieces on the chess board
#
# It accepts 2 parameters: 
#	-p PIECE
#		where PIECE is a 2 letter sequence
#			The first letter signifies the piece's color, w for white or b for black
#			The second letter signifies the piece itself using standard chess algebraic notation but using P for pawn
#	-s SQUARE
#		where SQUARE is the standard algebraic notation for the square indicated (a1 - h8)
#
# Usage:
# 	piecemv.py -p wN -s e3
#
import sys

def RetrieveArgs():
	# get and validate the command line args given
	# if multiple of an arg is given, the last one given will be used
	validpieces = ['wp','wr','wn','wb','wq','wk','bp','br','bn','bb','bq','bk']
	validsquares = ['a1','a2','a3','a4','a5','a6','a7','a8',
					'b1','b2','b3','b4','b5','b6','b7','b8',
					'c1','c2','c3','c4','c5','c6','c7','c8',
					'd1','d2','d3','d4','d5','d6','d7','d8',
					'e1','e2','e3','e4','e5','e6','e7','e8',
					'f1','f2','f3','f4','f5','f6','f7','f8',
					'g1','g2','g3','g4','g5','g6','g7','g8',
					'h1','h2','h3','h4','h5','h6','h7','h8']

	args = {}
	nexta = ''	# the next argument will be...
	for arg in sys.argv:
		if (nexta == 'p'):
			if (arg.lower() in validpieces):
				args['p'] = arg.lower()
				nexta = ''
			else:
				print "Invalid piece specified: " + arg
			nexta = ''
		elif (nexta == 's'):
			if (arg.lower() in validsquares):
				args['s'] = arg.lower()
			else:
				print "Invalid square specified: " + arg
			nexta = ''
		elif (arg == '-p'):
			# next arg is the piece
			nexta = 'p'
		elif (arg == "-s"):
			# next arg is the piece's square
			nexta = 's'
		elif (arg == "-h"):
			# user asked for help
			print '''Piecemv help

Piecemv accepts 2 parameters: 
-p PIECE
   where PIECE is a 2 letter sequence
      The first letter signifies the piece's color, w for white or b for black
      The second letter signifies the piece itself, 
      using standard algebraic notation but using P for pawn
-s SQUARE
   where SQUARE is the standard algebraic notation of the square indicated

Sample usage:
   piecemv.py -p wN -s e3'''
			exit()
		else:
			if (arg != "piecemv.py"):
				print "argument " + arg + " is invalid and will be ignored."

	return args

def RookMoves (rank, file, distance):
	# returns the squares a rook could get to, in (rank, file) format
	squares = []

	for c in range (1,distance):
		if ((rank + c) < 9):
			squares.append (((rank + c), file))
		# moving down
		if ((rank - c) > 0):
			squares.append (((rank - c), file))
		# moving left
		if ((file - c) > 0):
			squares.append ((rank, (file - c)))
		# moving right
		if ((file + c) < 9):
			squares.append ((rank, (file + c)))

	return squares
''' end RookMoves '''

def BishopMoves (rank, file, distance):
	# returns the squares a bishop could get to, in (rank, file) format
	squares = []

	# moving up and right
	for c in range (1,distance):
		if (((rank + c) < 9) and ((file + c) < 9)):
			squares.append (((rank + c), (file + c)))
		# moving down and right
		if (((rank - c) > 0) and ((file + c) < 9)):
			squares.append (((rank - c), (file + c)))
		# moving up and left
		if (((rank + c) < 9) and ((file - c) > 0)):
			squares.append (((rank + c), (file - c)))
		# moving down and left
		if (((rank - c) > 0) and ((file - c) > 0)):
			squares.append (((rank - c), (file - c)))

	return squares
''' end BishopMoves '''

def ListSquares (color, piece, rank, file):
	# returns the squares the given piece to could to from the given square
	squares = []

	if (piece == 'r'): # rook
		squares = RookMoves (rank, file, 8)
	elif (piece == 'n'): # knight
		# list all of the possible squares it might be able to go to
		possibleSquares = [(rank+2, file-1),(rank+2, file+1),(rank+1,file-2),(rank+1,file+2),(rank-1,file-2),(rank-1,file+2),(rank-2,file-1),(rank-2,file+1)]
		# only keep the squares that are on the board
		for r, f in possibleSquares:
			if (r > 0 and r < 9 and f > 0 and f < 9):
				squares.append ((r,f))
	elif (piece == 'b'): #bishop
		squares = BishopMoves (rank, file, 8)
	elif (piece == 'q'): # queen
		squares = BishopMoves (rank, file, 8)
		squares += RookMoves (rank, file, 8)
	elif (piece == 'k'): # king
		squares = BishopMoves (rank, file, 2)
		squares += RookMoves (rank, file, 2)
	elif (piece == 'p'): # pawn
		if (color == 'w'):
			if (rank == 2):
				squares.append(((rank + 1), file))
				squares.append (((rank + 2), file))
			elif (rank < 8):
				squares.append((rank + 1, file))
		else: # color = b
			if (rank == 7):
				squares.append(((rank - 1), file))
				squares.append(((rank - 2), file))
			elif (rank > 1):
				squares.append(((rank - 1), file))

	# convert rank,file to algebraic notation
	sq = ''
	for (r, f) in squares:
		sq += chr(f+96) + str(r) + ','

	return (sq[:-1])
''' end ListSquares '''

#####################
### begin program ###
#####################
# get the command line arguments
args = RetrieveArgs()

# parse command line arguments
if ('p' in args):
	color = args['p'][:1]
	piece = args['p'][1:]
else:
	print "No piece given. Aborting..."
	exit()
if ('s' in args):
	# convert the file of the square into a number from 1-8, like the rank
	file = ord(args['s'][:1]) - 96
	rank = int(args['s'][1:])
else:
	print "No square given. Aborting..."
	exit()

if (piece == 'p' and ((color == 'w' and rank == 1) or (color == 'b' and rank == 8))):
	print "Illegal square for a pawn. Aborting..."
	exit()

# print out the squares the given piece could move to
print ListSquares (color, piece, rank, file)

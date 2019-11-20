key_words = ["and", "array", "asm", "begin", "break", 
"case", "const", "constructor", "continue", "dectructor", 
"div", "do", "downto", "else", "end", "false", "file", "for", 
"function", "goto", "if",  "implementation", "in", "inline", 
"interface", "label", "mod", "nil", "not", "object", "of", "on", 
"operator", "or", "packed", "procedure", "program", "record", 
"repeat", "set", "shl", "shr", "string", "then", "to", "true", 
"type", "unit", "until", "uses", "var", "while", "with", "xor",
"abs", "exp", "ord", "reset", "true", "arctan", "false", "output", 
"rewrite", "trunc write", "boolean", "input", "pack", "round",
"writeln", "char", "integer", "page", "sin", "cos", "ln",
"pred", "sqr", "dispose", "maxint", "read", "sqrt", "eof",
"new", "readln", "succ", "eoln", "odd", "real", "text",
"+", "-", "=", "<", ">", "<=", ">=", "<>", "@", "^", "*", ":=", "'"] # Pascal's key words

brackets_d_c = "([)].,;"

bigcomment = False
identifires = []
end_str = "~~"
goident = False
curr_name = ''

def parse_file(input_file):
	minimal_u = 1e300
	minimal_n = ''
	counted_words = 1
	curr_line = input_file.readline()
	while curr_line != '':
		try:
			counted_words += parse_line(curr_line)
		except:
			check_and_print(curr_name[2:], counted_words)
			if counted_words < minimal_u:
				minimal_u = counted_words
				minimal_n = curr_name[2:]
			elif counted_words == minimal_u:
				minimal_n += curr_name[2:]
			counted_words = 0
		curr_line = input_file.readline()
	print(minimal_n, minimal_u)



def parse_line(curr_line):
	global goident, identifires, bigcomment, curr_name

	counted_words = 0
	quote = True
	#print(curr_line.strip().split())
	if curr_line[0] == "~":
		curr_name = curr_line
		return None

	elif '}{' in curr_line[0]:
		bigcomment = not bigcomment
	if bigcomment:
		return 0

	for word in curr_line.strip().split():			
		if curr_line[:2] == '//':
			return counted_words

		if word == "VAR":
			goident = True
		
		if goident and garbagedel(word) == "END":
			goident = False

		if brackets_founder(word):
			counted_words += 1
		
		if garbagedel(word.lower()) in key_words:
			counted_words += 1 
			#print(word, "key_words")
		
		elif garbagedel(word) in identifires:
			counted_words += 1
			#print(word, "identifires")
		
		elif is_const(word):
			counted_words += 1
			#print(word, "constant")
		
		elif '.' in word and word.lower().split('.')[1] != '':
			counted_words += 2
			#print(word, "more than two words sep with .")

		elif goident and "'" not in word and ':' not in word:
			identifires.append(garbagedel(word))
			counted_words += 1
			#print(word, "has been added to identifires")
			
		else:
			for letter in word:
				if letter == "'" and quote:
					counted_words += 1
					#print(word, "STRING FOUND")
					quote = not quote
				
				elif letter == "'" and not quote:
					quote = not quote
	return counted_words

def main():
	try:
		input_file = open("input.txt")
		print("Файл 'input.txt' был успешно найден.")
		parse_file(input_file)
	except:
		print("Файл 'input.txt' не был найден")
		return

def is_const(input_str):
	alphabet = "0123456789e-+."
	for i in input_str.lower().strip(',);'):
		if i not in alphabet:
			return False
	return True

def brackets_founder(input_str):
	for letter in brackets_d_c[:2]:
		if input_str.find(letter) != -1:
			return True
	return False

def garbagedel(input_str):
	return input_str.strip(brackets_d_c)


def check_and_print(input_string, total_words):
	print("Program by {} contains {} units".format(input_string, total_words))

main()


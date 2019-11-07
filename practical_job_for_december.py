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
"new", "readln", "succ", "eoln", "odd", "real", "text"
"+", "-", "=", "<", ">", "<=", ">=", "<>", "@", "^", "*", ":=" "(", "[", "{", "'"] # Pascal's key words

end_str = "~~"

def parse_file():
	pass

def parse_line(curr_line):
	counted_words = 0
	quote = True
	print(curr_line.strip().split())
	for word in curr_line.strip().split():
		if word.lower() in key_words:
			counted_words += 1 
		elif len(word.lower().split('.')) != 1:
			counted_words += 2
		elif is_const(word):
			counted_words += 1
		else:
			for letter in word:
				if letter in ["(", "[", "{"]:
					counted_words += 1
				elif letter == "'" and quote:
					counted_words += 1
					quote = not quote
				elif letter == "'" and not quote:
					quote = not quote
				elif letter.isnumeric():
					counted_words += 1
	print(counted_words)

def main():
	try:
		input_file = open("input.txt")
		print("Файл 'input.txt' был успешно найден.")
	except:
		print("Файл 'input.txt' не был найден")
		return

def is_const(input_str):
	alphabet = "0123456789e-+."
	if not len(input_str):
		return False
	if input_str[-1] in [",", ")"]:
		input_str = input_str[:-1]
	for i in input_str.lower():
		if i not in alphabet:
			return False
	return True

main()

parse_line("('THE ANSWER IS', TEMP.FIRST * TEMP.SECOND : 7 : 3, 1.0E-6)")
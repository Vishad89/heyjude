import sys

def remove_white_spaces_string(sentence):
    str = list(sentence)
    reading_pos = 0
    writing_pos = 0
    while reading_pos < len(str):
        if str[reading_pos] != " ":
            str[writing_pos] = str[reading_pos]
            writing_pos += 1
        reading_pos += 1
    str[writing_pos] = '\0'
    
    print_array(str)

def print_array(s):
  i = 0
  while i < len(s) and s[i] != '\0':
    sys.stdout.write(s[i])
    i += 1
  print()

remove_white_spaces_string("hello world    super")

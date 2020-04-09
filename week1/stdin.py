import sys

def text_to_ints(text: str) -> list:
    text = text.rstrip()
    text = text.split()
    ints = text
    ints[0], ints[1] = int(text[0]), int(text[1])
    return ints

raw_text = sys.stdin.readlines()
num_of_lines = int(raw_text[0].rstrip())

for line in range(num_of_lines):
   ints = text_to_ints(raw_text[line+1])
   print(f'{ints[0] + ints[1]} {ints[0] * ints[1]}')

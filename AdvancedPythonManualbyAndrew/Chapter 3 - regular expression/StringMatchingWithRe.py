import re
pattern = 'AAGCTT'
p = re.compile(pattern)
seq1 = 'AAGCTTNNAAGCTT'
seq2 = 'GGGGGG'
seq3 = 'NNAAGCTT'
print(p.match(seq1))
print(p.match(seq2))
print(p.match(seq3))
print(p.search(seq3))

m = p.search(seq3)
print(m.group())
print(m.start())
print(m.end())

pattern2 = 'CAR*T'
p2 = re.compile(pattern2)
seq4 = 'CART'
seq5 = 'CAT'
seq6 = 'CAAR'

m1 = p2.search(seq4)
m2 = p2.search(seq5)
m3 = p2.search(seq6)
print(m1)
print(m2)
print(m3)

pattern3 = '[aeiuo]+'
p3 = re.compile(pattern3)
word = 'euouae'
mat = p3.search(word)
print(mat)

pattern_greedy = 'Pneu.*s'
pattern_non_greedy = 'Pneu.*?s'
p_greedy = re.compile(pattern_greedy)
p_non_greedy = re.compile(pattern_non_greedy)
seq7 = 'Pneumonoultramicroscopicsilicovolcanoconiosis'
m_greedy = p_greedy.search(seq7)
m_non_greedy = p_non_greedy.search(seq7)
print(m_greedy)
print(m_non_greedy)

# Groups
pattern4 = '^([A-z]+)(\d+)([A-z]+)$'
p4 = re.compile(pattern4)
seq8 = 'The6Hundred'
m4 = p4.search(seq8)
print(m4)
print(m4.group(0))
print(m4.group(1))
print(m4.group(2))
print(m4.group(3))


p_ignore_case = re.compile(pattern, re.IGNORECASE)
seq9 = 'aagctt'
m = p.search(seq9)
m_ignore_case = p_ignore_case.search(seq9)
print(m)
print(m_ignore_case)

pattern5 = '[A-z]+$'
p5 = re.compile(pattern5)
m5 = p5.sub('Thousand', seq8)
print(m5)
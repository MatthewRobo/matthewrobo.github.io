import re

regex = []
subst = []

button = r'(?<!\w)((((j\.)|([0-9]|(?<=(\+|~))))+(x|\[x\])+)|(\]x\[))'
color = r'{{clr|x|\1}}'

regex.append(r'fl\.{(.+?)}')
subst.append(r'fl.<nowiki>{</nowiki>\1<nowiki>}</nowiki>')

regex.append(r'(\[(\d)\] )((Very )?\w+)')
subst.append(r'\1{{clr|\2|\3}}')

for c in 'ABCD':
	regex.append(button.replace('x', c))
for c in '4235':
	subst.append(color.replace('x', c))

string = ''
# string = r'j.A > j.B~8 > fl.{5A > 6A} > Overdrive Cancel > j.C(41236D) > j.63214B > (41236D HIts) > IAD > j.C~8 > fl.{5C > 3C~dl.9hjc} > j.C > 5C > 6A > j.63214B~8 > fl.{3C}'

# file = open('input.txt', 'r')
# string = file.read()
# file.close()

if string == '':
	regexs = ['/' + s + '/gm' for s in regex]
	substs = ['`' + s.replace('\\', '$') + '`' for s in subst]
	string =   'const regex = [\n'        \
	         + ' ,\n'.join(regexs) + '\n' \
	         + '];\n\n'                   \
	         + 'const subst = [\n'        \
	         + ' ,\n'.join(substs) + '\n' \
	         + '];\n'

else:
	for i in range(len(regex)):
		string = re.sub(regex[i], subst[i], string)

print(string)

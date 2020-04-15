import math as m
import collections

def Translate(arg, l):
            num = ""
            for i in range(0,l):
                arg = arg * 2.0
                num += str(m.trunc(arg))
                if arg >= 1.0:
                    arg -= 1.0
            return num
			
def gilbertMur():
	text = input()
	coded_text=''
	id_2 = {}
	decode = {}
	sum=0.0
	for i in text:
		if i not in id_2:
			id_2[i.lower()] = [1,0,0,'']
		else:
			id_2[i][0] += 1
	id_2 = collections.OrderedDict(sorted(id_2.items(),key = lambda i:i[0]))
	for i in id_2:
		id_2[i][0] /= len(text)
		id_2[i][1] = m.ceil(m.log2(1 / id_2[i][0])) + 1
		id_2[i][2] = id_2[i][0] / 2 + sum
		id_2[i][3] = Translate(id_2[i][2], id_2[i][1])
		sum+=id_2[i][0]
	for i in text.lower():
		coded_text += id_2[i][3]
	print(coded_text)
	for j, i in id_2.items():
		decode[i[3]] = j
	count = ''
	for i in coded_text:
		try:
			count += i
			print(decode[count], end = ' ')
			count = ''
		except:
			pass

	s = 0.0
	h = 0.0
	for i in text.lower():
		s += id_2[i][0] * id_2[i][1]
		h += id_2[i][0] * m.log2(1 / id_2[i][0])
	print()
	print(s)
	print(h + 2)
gilbertMur()

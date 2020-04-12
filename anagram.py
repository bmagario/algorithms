def anagram(s1, s2):
	result = True
	if(len(s1) != len(s2)):
		return False

	alist2 = list(s2)
	i = 0
	while i < len(s1) and result:
		j = 0
		found = False
		while j < len(alist2) and not found:
			if(s1[i] == alist2[j]):
					found = True
					alist2[j] = None
			j += 1
		i += 1
		result = found

	return found


def anagramSort(s1, s2):
	olist1 = list(s1)
	olist2 = list(s2)

	olist1.sort()
	olist2.sort()

	result = True
	i = 0
	while i < len(s1) and result:
		result = olist1[i] == olist2[i]
		i += 1

	return result

def anagramAlphabet(s1,s2):
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    stillOK = True
    while j < 26 and stillOK:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            stillOK = False

    return stillOK

print(anagram("heahrt", "ehahrt"))
print(anagramSort("hehrahrt", "ehahrthr"))
print(anagramAlphabet("hehrahrt", "ehahrthr"))
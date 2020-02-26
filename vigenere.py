#!/usr/bin/env python3
# Daniel Schlicht - Cryptography Project 2
# vigenere.py - Decrypt a block of text encoded using the Vigenere Cipher 
# by using the Friedman Test.

from collections import Counter
from prettytable import PrettyTable

# function to split cipher into m substrings
def createSubstrings(m, s):
	for x in range(0, m):
		string = s[x::m] # take every mth char of the string
		arr[x] = string
	return arr

# prints the substrings found in arr in a readable format
def printSubstrings(arr):
	for s in arr:
		print("y_%d: " %(arr.index(s)+1), end = '')
		idx = 0
		for c in s:
			print(c, end = '')
			idx += 1
			if idx % 80 == 0:
				print()
		print()
		
# function to calculate incidence of coincidence on string
def findIndexofCoincidence(arr):
	# I_c(x) = Sum (from 0-25) {f_i * (f_i-1)} / n(n-1)
	# get repeat letter counts (f_i)
	for s in arr:
		sumRepeats = 0
		freqCount = Counter(s)
		for key in freqCount.keys():
			if freqCount.get(key) > 1:
				# get the sum of f_i's
				sumRepeats += (freqCount.get(key) * (freqCount.get(key)-1))	
		# divide by n(n-1)		
		indexOfCoincidence = sumRepeats / ((len(s) - 1) * len(s))
		print(indexOfCoincidence)

# function to find and fill in values of M_g table	
def findM_g(arr, table):
	# frequency of letters in english
	p = [0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.020, 0.061, 0.070, 0.002,\
		0.008, 0.040, 0.024, 0.067, 0.075, 0.019, 0.001, 0.060, 0.063, 0.091,\
		0.028, 0.010, 0.023, 0.001, 0.020, 0.001]
	# dictionary for counting frequencies
	alphaDict = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0,\
	 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, \
	 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, \
	 'X': 0, 'Y': 0, 'Z': 0}
	allmg = []
	
	for s in arr:	# for each substring in the list	
		for c in s:	# for each character in the string
			alphaDict[c] += 1	# increment freq score for character
				
		# q = a list of all freq values / length of string
		q = list(alphaDict.values())
		q = [i / len(s) for i in q]
		
		#calculate mg = p dot vg
		mg = [0] * 26
		for g in range(0, 26): # for g = 0 to g = 25
			vg = q[g:] + q[:g] # vg = rotate frequencies by g places
			# mg = p dot vg
			mg[g] = float("{0:.4f}".format(sum([a * b for a, b in zip(p, vg)] * 100)))
		allmg.append(mg) # add mg for substring to list of all mgs
		alphaDict = dict.fromkeys(alphaDict, 0) # reset freqs for next substring
		
	# add rows to table	
	for x in range(0, 25):
		new_row = [x]
		new_row.extend(y[x] for y in allmg)
		table.add_row(new_row)

# function to decrypt the ciphertext
def decrypt(key, ciphertext):
	# alphabet encoding in Z26
	alphaDict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6,\
	 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14,\
	 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22,\
	 'X': 23, 'Y': 24, 'Z': 25}
	invDict = {v: k for k, v in alphaDict.items()} # swapped key-value in alphaDict
	
	# translate the text into its coding
	cipherCoding = []
	for c in ciphertext:
		cipherCoding.append(alphaDict.get(c))
	
	# translate key into coding
	keyCoding = []
	for c in key:
		keyCoding.append(alphaDict.get(c))
	
	# subtract the coding of the key from the text and mod 26 it
	idx = 0
	decipheredCoding = [0] * len(cipherCoding)
	for i in range(0, len(cipherCoding)):
		decipheredCoding[i] = (cipherCoding[i] - keyCoding[idx]) % 26
		idx += 1
		if idx > len(keyCoding) - 1:
			idx = 0	

	# translate back into letters
	text = ""
	for j in decipheredCoding:
		text += str(invDict.get(j))

	# print the deciphered text in a readable format
	idx = 0
	for c in text:
		print(c, end='')
		idx += 1
		if idx % 80 == 0:
			print()
	print()
			
# the ciphertext
ciphertext = '''
LAVHEBSJMDINFGXCLWTUUWARWBQWFTEHWUDDTCAAKKTXTSMYALMVHTAHJHKICFAFZKLEXA
TXIXYMFVLVGUDALRFJTTGKXNLOYOWLVVVQAFKVGEZLEHEXHEZGPVZEDOWARZEAFSGVASOS
DXJIEZESBEWTDWSFGVOPMUMJENPKWKMMCQKVXJMGZWVBEEWMQLARXGUNWLLWEDKKHCICAF
LKFPOHWJTTGEEKLHKLEUJVTKEAESJXJYLFDSPVRFAJUXDINFAKLFQEFAEXJYNMTDXKSRQU
GOVVTTWUHEXEZLGYVPEOLJHEMCOGEFLRIOSLBFRSRJGFKLEFWUAESLAYQIISVUVWKVZEZA
FKVWPAFKXKSAOGMKKSRPWJHIHUXQSNKLODARXUAADJSGKMSEMWWSCARWVXIELVMVZVJODW
PTDTLQESGPGOYEMGZGAFAGGJWEDNAVVWNAOWGTVYBLUXIXAUFUHDQUZAUTKMOZKTRUIFMM
DMNMTTLZXBIYZWUXJWADQLHUICDQHMKLEOGEFLRIOSLBFRSEGDXCCIZLZXYENPKGYKLEQF
VNJIRFZALRTPXAWLSSTTOZXEXHQVSMRMSUFEHKMOZGNXIILQULKFRIOFWMNSRWKGKRXRQK
LHEENQDWVKVOZAUWVZIOWAYKLEOGEFLRIOSLBFRSBJGOZHEDAKLVVVQVOBKLAISJKRRTEW
WDZRGFZGLVGOYEMGZGAFAGGJXHQHJHMMDQJUTEROFHJHMMDQLZXUETMTWVRYSQALARWDQK
AZEIDFZWMVGHZGDHXCSGUZMYETULUTEROFTWTTGEEKWWSCAZQLAZVDBSJMPAEPGFHKLAHW
SGPWIXNWKSYLXWLLRRDFZWWZWCGKKBFRSIALAZRTTWWQVGUFANXSVAZUZTIISFADEFRGAA
FZNLIXWLAVVETSKGFXYQLTXVRAPWUBJMOZOZXKLEDLGLVIKXWYBJPAFAGGNIMGKLPFVKIA
LATSNSJWLJMNPMKMICAOSVXDMCEHJBMECKYJHLTSMFVHKLEDKLHTVARLSGRTPDGSVYXHML
SWUVEEKWLRPLAXLAVQUXLAICICAEHXKMNSUGGTIRZKLARXHMNWUVINFZWYFGUEGXLFQUOZ
VXSETQTMMNICMFSECEGDWWMYETIWOBCPNQWVHEKOUFYAFREELSGUMNRGJFVHPGTDBTHENS
LXRFOGLZHNFEELLHGVOFWUMCMBQJLRRRDEWUNIMTKAFUFXHAMJERASMFVHLVTQUZGFPOSQ
'''.replace('\n', '')

arr = [] # list for the substrings
text = ""
# find indices of coincidence for m = 4 through m = 8
for m in range(4, 9):
	print("\nSubstrings when m = %d:" %(m))
	arr = ['']*m
	# create substrings
	createSubstrings(m, ciphertext)
	printSubstrings(arr)
	# find the index of coincidence of each substring
	print("\nIndicies of Coincidence when m = %d:" %(m))
	findIndexofCoincidence(arr)
	
print("\nThe Indices of Coincidence when m = 7 are the closest to that \
of natural English (0.065).\n")
	
# create the M_g table
arr = ['']*7
table = PrettyTable(['g', 'M_g 1', 'M_g 2', 'M_g 3', 'M_g 4', 'M_g 5', 'M_g 6', 'M_g 7'])
createSubstrings(7, ciphertext) # get the correct length substrings
findM_g(arr, table) # calculate M_g and fill out the table
print(table)
print("* Values are multiplied by 100 for readability")

print("\nFrom the M_g table, the values from each column closest to 0.065 are:")
print("18\t19\t17\t4\t0\t12\t18")
print("S\tT\tR\tE\tA\tM\tS")
print("So, the key is 'STREAMS'.\n")
key = "STREAMS"

# Decrypt the ciphertext
print("The decrypted text is:")
decrypt(key, ciphertext)
'''
The Department of Justice has been and will always be committed 
to protecting the liberty and security of those whom we serve. In recent 
months, however, we have on a new scale seen mainstream products and 
services designed in a way that gives users sole control over access
to their data. As a result, law enforcement is sometimes unable to recover 
the content of electronic communications from the technology provider 
even in response to a court order or duly-authorized warrant issued by 
a Federal Judge. For example, many communications services now encrypt 
certain communications by default, with the key necessary to decrypt the 
communications solely in the hands of the end user. This applies both 
when the data is not in motion over electronic networks, or at rest on an 
electronic device. If the communications provider is served with a warrant
 seeking those communications, the provider cannot provide the data because 
it has designed the technology such that it cannot be accessed by any 
third party. We do not have any silver bullets and the discussions with 
the Executive Branch are still ongoing. While there has not yet been a 
decision whether to seek legislation, we must work with Congress, industry, 
academics, privacy groups, and others to craft an approach that addresses 
all of the multiple competing concerns that have been the focus of so much 
debate. But we can all agree that we will need ongoing honest and informed 
public debate about how best to protect liberty and security in both our 
laws and our technology.
'''
print("\nAfter cleaning it up, the decrypted message is: ")
print("The Department of Justice has been and will always be committed \
to protecting ")
print("the liberty and security of those whom we serve. In recent months, ho\
wever, we ")
print("have on a new scale seen mainstream products and services designed in \
a way ")
print("that gives users sole control over access to their data. As a result,")
print("law enforcement is sometimes unable to recover the content of electronic ")
print("communications from the technology provider even in response to a court ")
print("order or duly-authorized warrant issued by a Federal Judge. For example, ")
print("many communications services now encrypt certain communications by ")
print("default, with the key necessary to decrypt the communications solely ")
print("in the hands of the end user. This applies both when the data is ")
print("not in motion over electronic networks, or at rest on an electronic ")
print("device. If the communications provider is served with a warrant ")
print("seeking those communications, the provider cannot provide the data ")
print("because it has designed the technology such that it cannot be accessed ")
print("by any third party. We do not have any silver bullets and the ")
print("discussions with the Executive Branch are still ongoing. While there ")
print("has not yet been a decision whether to seek legislation, we must work ")
print("with Congress, industry, academics, privacy groups, and others to ")
print("craft an approach that addresses all of the multiple competing ")
print("concerns that have been the focus of so much debate. But we can ")
print("all agree that we will need ongoing honest and informed public ")
print("debate about how best to protect liberty and security in both our ")
print("laws and our technology.")

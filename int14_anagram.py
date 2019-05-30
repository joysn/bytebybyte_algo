# 14. Anagrams
# Question: Given two strings, write a function to determine whether they are anagrams.

def isAnagram(s1,s2): #T = O(nlogn) S = O(n)

	if len(s1) != len(s2):
		return False
	s1_lower = s1.lower()
	s2_lower = s2.lower()
	
	s1_lower = sorted(s1_lower)
	s2_lower = sorted(s2_lower)
	
	if s1_lower == s2_lower:
		return True
	else:
		return False
	

print(isAnagram("", "")) #true
print(isAnagram("A", "A")) #true
print(isAnagram("A", "B")) #false
print(isAnagram("ab", "ba")) #true
print(isAnagram("AB", "ab")) #true
print("***********************")


def isAnagram(s1,s2): #T = O(n) S = O(n)

	if len(s1) != len(s2):
		return False
	s1_lower = s1.lower()
	s2_lower = s2.lower()

	char_dict = dict()
	for i in range(len(s1_lower)):
		if s1_lower[i] in char_dict.keys():
			char_dict[s1_lower[i]] += 1
		else:
			char_dict[s1_lower[i]] = 1
			
	for i in range(len(s2_lower)):
		if s2_lower[i] in char_dict.keys():
			char_dict[s2_lower[i]] -= 1
		else:
			char_dict[s2_lower[i]] = 1
			
	for key in char_dict.keys():
		if char_dict[key] != 0:
			return False
	return True
	

print(isAnagram("", "")) #true
print(isAnagram("A", "A")) #true
print(isAnagram("A", "B")) #false
print(isAnagram("ab", "ba")) #true
print(isAnagram("AB", "ab")) #true
print("***********************")



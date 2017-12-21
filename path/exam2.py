### 반 : 화 / 금
### 이름 :
### 학번 : 

#### 2 ####
# 문자열 내에 특정 문자가 나타나는 횟수를 내주는 함수

def occurred_in(char, string):
	occ = 0
	for c in string:
		if char == c:
			occ += 1
	return occ

# print(occurred_in('p', '')) # 0
# print(occurred_in('p', 'I love Python!')) # 0
# print(occurred_in('e', 'What happened to your college life?')) # 5

#### 3 ####

def numbers_art(n):
	for i in range(n):
		for j in range(n):
			print(j+1, end=' ')
		print()

# numbers_art(5)
# numbers_art(7)

# (1)
def numbers_art1(n):
	for i in range(n):
		for j in range(n):
			print(j+1, end=' ')
		n -= 1
		print()

# (2)
def numbers_art2(n):
	a = 1
	for i in range(n):
		for j in range(a):
			print(j+1, end=' ')
		a += 1
		print()

# (3)
def numbers_art3(n):
	k=''
	a=0
	for i in range(n):
		for j in range(n):
			if j+1>a:
				k += str(j+1)+str(' ')
			else:
				k += str('  ')
		a+=1
		print(k)
		k= ''
# (4)
def numbers_art4(n):
	k=''
	a=n-1
	for i in range(n):
		for j in range(n):
			if j+1>a:
				k += str(j+1)+str(' ')
			else:
				k += str('  ')
		a-=1
		print(k)
		k= ''
# numbers_art1(5)
# numbers_art2(5)
# numbers_art3(5)
# numbers_art4(5)

##### 4 #####

# 인수 n이 소수인지 확인하기
def is_prime(n):
	if n < 2:
		return False
	else:
		for i in range(2,n):
			if n % i == 0:
				return False
		return True

# for i in range(50):
# 	if is_prime(i):
# 		print(i)

# (1)
def is_prime(n):
	if n == 2:
		return True
	elif n < 2 or n%2==0:
		return False
	else:
		for i in range(2,n):
			if n % i == 0:
				return False
		return True		

# for i in range(50):
# 	if is_prime(i):
# 		print(i)

# (2)
# 자연수 n미만의 소수를 2부터 시작하여 모두 오름차순으로 나열한 리스트로 만들어 내주는 함수
def primes_less_than(n):
	p = []
	for i in range(n):
		if is_prime(i):
			p += [i]
	return p

# print(primes_less_than(2)) # []
# print(primes_less_than(3)) # [2]
# print(primes_less_than(10)) # [2, 3, 5, 7]
# print(primes_less_than(30)) # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# (3)
# k개의 소수를 2부터 시작하여 오름차순으로 리스트로 만들어 내주는 함수
def primes(k):
	p = []
	n = 2
	a=0
	while k > 0:
		if is_prime(a):
			p += [a]
			if len(p) == k:
				break
		a += 1
	return p

# print(primes(0)) # []
# print(primes(1)) # [2]
# print(primes(5)) # [2, 3, 5, 7, 11]
# print(primes(10)) # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# (4)
# 쌍둥이 소수 k 쌍 찾기 (차이가 2인 소수의 쌍)
def twin_primes(k):
	p = []
	q = []
	prev = 2
	n = 0
	a = 0
	while k > 0:
		if is_prime(a):
			p+=[a]
		for i in range(len(p)):
			if i != len(p)-1:
				if p[i+1]-p[i]==2:
					q += [(p[i],p[i+1])]
			n += 1
		a += 1
		if len(q) != k:
			q = []
		else:
			break
	return q

# print(twin_primes(0)) # []
# print(twin_primes(1)) # [(3, 5)]
# print(twin_primes(5)) # [(3, 5), (5, 7), (11, 13), (17, 19), (29, 31)]
# print(twin_primes(10)) 
# # q = [(3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43), (59, 61), (71, 73), (101, 103), (107, 109)]

#### 5 ####
# (1)
## generate all subsequences

def subsequences(ns):
	subs = [[]]
	for n in ns:
		newsubs = []
		for sub in subs:
			newsub = sub[:]
			newsub.append(n)
			newsubs.append(newsub)
		subs += newsubs
	return subs

# print(subsequences([])) 
# [[]]
# print(subsequences([1]))
# [[], [1]]
# print(subsequences([1,2]))
# [[], [1], 
#  [2], [1, 2]]
# print(subsequences([1,2,3]))
# [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
# print(subsequences([1,2,3,4]))
# [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3], 
#  [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]]

# (2)
# check if a list is increasing
def increasing(ns):
	return len(ns) < 2 or ns[0] < ns[1] and increasing(ns[1:]) # write a suitable boolean expression

# print(increasing([])) # True
# print(increasing([2])) # True
# print(increasing([1,2])) # True
# print(increasing([2,2])) # False
# print(increasing([3,2])) # False
# print(increasing([1,2,3])) # True
# print(increasing([1,3,2])) # False
# print(increasing([3,2,1])) # False

# (3)
# length of longest increasing subsequence
def longest_increasing_subsequence(ns):
	if len(ns) < 2:
		return len(ns)
	else:
		subs = subsequences(ns)
		longest = 1
		for sub in subs:
			if len(sub)>longest and increasing(sub):
				longest = len(sub)
		return longest

# print(longest_increasing_subsequence([])) # 0
# print(longest_increasing_subsequence([3])) # 1
# print(longest_increasing_subsequence([5,4])) # 1
# print(longest_increasing_subsequence([2,4])) # 2
# print(longest_increasing_subsequence([4,3,2])) # 1
# print(longest_increasing_subsequence([4,2,7,5,9])) # 3
# print(longest_increasing_subsequence([4,2,7,5,4,7,6,8,9,6])) # 5

#### 6 ####

# (1)
# 2진수를 10진수로 바꾸기

def bin2dec(bin):
	length = len(bin)
	dec = 0
	for i in range(length):
		if bin[-1-i] == '1':
			a = 2**i
			dec += a
	return dec

# print(bin2dec('0')) # 0
# print(bin2dec('1')) # 1
# print(bin2dec('110')) # 6
# print(bin2dec('10011')) # 19
# print(bin2dec('101010')) # 42

# (2)
# 10진수를 2진수로 바꾸기

def dec2bin(dec):
	bin = ''
	while not (dec == 0 or dec == 1):
		if dec%2==1:
			bin += '1'
		else:
			bin += '0'
		dec = dec//2
	if dec == 1:
		bin += '1'
	elif dec == 0:
		bin += '0'
	final_bin=''
	for i in range(len(bin)):
		final_bin += bin[-1-i]
	return final_bin

# print(dec2bin(0)) 
# # => '0'
# print(dec2bin(1)) 
# # => '1'
# print(dec2bin(6)) 
# # => '110'
# print(dec2bin(19)) 
# # => '10011'
# print(dec2bin(42)) 
# # => '101010'

# 문제#2 - countnumber
def countnumber(xss):
	counter = 0
	for i in xss:
		if isinstance(i,list):
			counter += countnumber(i)
		else:
			counter += 1
	return counter

# 테스트케이스
# print(countnumber([1,2,3]))
# print(countnumber([1,[],3]))
# print(countnumber([1,[1,2,[3,4]]]))
# print(countnumber([[[[[[[[1,2,3]]]]]]]]))
# print(countnumber([]))
# print(countnumber([[[[3]],[4]],5,6,[7]]))
# print(countnumber([1,[2,2],[[3],[4,4]],[[[5,5,5,5]]],6,[7,[[8],[[9]]]]]))

# 답
# 3
# 2
# 5
# 3
# 0
# 5
# 14

# 문제 #3: 정방행렬 검사
def issquare(mat):
	a=1
	for i in mat:
		if a!=len(mat):
			if len(i)>len(mat[a]):
				return False
			a += 1
		else:
			if i == []:
				return False
	return True



# print(issquare([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])) 
# print(issquare([])) 
# print(issquare([[]]))
# print(issquare([[1]])) 
# print(issquare([[1,1],[1]])) 
# print(issquare([[1,1],[1,1]])) 

# 답
# True
# True
# False
# True
# False
# True

# 문제 #4: 정방행렬 - 전치
def transpose(sqmat):
	final_sqmat = []
	middle_sqmat = []
	size = len(sqmat)
	for i in range(size):
		for j in range(size):
			middle_sqmat += [sqmat[j][i]]
		final_sqmat += [middle_sqmat]
		middle_sqmat = []
	return final_sqmat

# 테스트케이스
# xs0 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# xs1 = [[0, -3, 6, 4], [3, 0, -9, 8], [-6, 9, 0, 2], [-4, -8, -2, 0]]
# print(transpose(xs0))
# print(transpose(xs1))

# 답
# [[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]]
# [[0, 3, -6, -4], [-3, 0, 9, -8], [6, -9, 0, -2], [4, 8, 2, 0]]


# 문제 #5: 정방행렬 - 반대칭행렬 검사
def antisymmetric(sqmat):
	final_sqmat = []
	middle_sqmat = []
	size = len(sqmat)
	for i in range(size):
		for j in range(size):
			if sqmat[i][j] != -sqmat[j][i]:
				return False
	return True


# 테스트케이스
# xs0 = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
# xs1 = [[1,0,0,0],[0,2,0,0],[0,0,1,0],[0,0,0,1]]
# xs2 = [[0,-3,6,4],[3,0,-9,8],[-6,9,0,2],[-4,-8,-2,0]]
# print(antisymmetric(xs0))
# print(antisymmetric(xs1))
# print(antisymmetric(xs2))

# 답
# False
# False
# True

# 문제 #6: 순열 (난이도 높음)
def perm(xs):
	pass

# 테스트케이스
#xs0 = []
#xs1 = [1]
#xs2 = [1,2]
#xs3 = [1,2,3]
#xs4 = [1,2,3,4]
#print(perm(xs0))
#print(perm(xs1))
#print(perm(xs2))
#print(perm(xs3))
#print(perm(xs4))


# 문제#7: digit frequencies
def digit_freq(s):
	freqs = [0,0,0,0,0,0,0,0,0,0]
	count = 0
	for i in range(10):
		for j in range(len(s)):
			# print(s[j])
			if s[j] == str(i):
				count += 1
		freqs[i] = (str(i),count)
		count = 0
	dfreqs = []
	for i in range(len(freqs)):
		dfreqs += [freqs[i]]
	dfreqs.sort(key=lambda t: t[1],reverse=True)
	return dfreqs

# 테스트케이스
# print(digit_freq(""))
# print(digit_freq("0987654321"))
# print(digit_freq("30774378274672034827764362738473"))

# 답
# [('0', 0), ('1', 0), ('2', 0), ('3', 0), ('4', 0),
#  ('5', 0), ('6', 0), ('7', 0), ('8', 0), ('9', 0)]
# [('0', 1), ('1', 1), ('2', 1), ('3', 1), ('4', 1),
#  ('5', 1), ('6', 1), ('7', 1), ('8', 1), ('9', 1)]
# [('7', 9), ('3', 6), ('4', 5), ('2', 4), ('6', 3),
#  ('8', 3), ('0', 2), ('1', 0), ('5', 0), ('9', 0)]
    


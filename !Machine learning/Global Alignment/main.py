print("Enter the first sequence: ")
s1 = input()
print("Enter the second sequence: ")
s2 = input()
s1l = len(s1)
s2l = len(s2)
matrix = [[0 for i in range((s1l + 5) * 2)] for j in range((s2l + 5) * 2)]
matrix[0][0] = 0

f = 0
match = float(input("Enter the score for match : "))
mismatch = float(input("Enter the score for mismatch : "))
gap = float(input("Enter the score for gap penalty : "))
score = [0, 0, 0]
count = 0
matrix[1][1] = 0

for i in range(2, s1l + 2):
    f = f - gap
    matrix[i][1] = f
f = 0
for j in range(2, s2l + 2):
    f = f - gap
    matrix[1][j] = f
for j in range(s2l):
    for i in range(s1l):
        if (s2[j] == s1[i]):
            score[0] = matrix[i + 2 - 1][j + 2 - 1] + match
        else:
            score[0] = matrix[i + 2 - 1][j + 2 - 1] - mismatch
        score[1] = matrix[i + 2 - 1][j + 2] - gap
        score[2] = matrix[i + 2][j + 2 - 1] - gap
        matrix[i + 2][j + 2] = max(score)

seq1 = ""
seq2 = ""
mid = ""
i = s1l
j = s2l

while (i > 0 and j > 0):
        if (s1[i - 1] == s2[j - 1]):
            seq1 = seq1 + s1[i - 1]
            seq2 = seq2 + s2[j - 1]
            mid = mid + '|'
            i = i - 1
            j = j - 1
        else:
            seq1 = seq1 + s1[i - 1]
            seq2 = seq2 + s2[j - 1]
            mid = mid + ' '
            i = i - 1
            j = j - 1
print("The global alignment is : \n")
seq1 = seq1[::-1]
seq2 = seq2[::-1]
mid = mid[::-1]
print("########################################################################################################")
print("#                                         Score is :", matrix[s1l + 1][s2l + 1],"                                              #")
print("########################################################################################################\n")
for i in range(len(mid)):
    print(seq1[i], end=" ")
print("\n")
for i in range(len(mid)):
    print(mid[i], end=" ")
print("\n")
for i in range(len(mid)):
    print(seq2[i], end=" ")
print("\n")
print(
    "#########################################################################################################\n")

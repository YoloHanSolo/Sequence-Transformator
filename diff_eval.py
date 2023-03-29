import sys
import math

def is_prime(number):
    number = abs(number)
    if number < 2:
        return False 
    for i in range(2, int(number/2)+1):
        if (number % i) == 0:
            return False     
    return True

def fun_operation(seq_list, operation):
    result = []
    for i in range(len(seq_list)):
        result.append([])
    result[0] = seq_list.copy()
    for i in range(len(seq_list)):
        for k in range(len(seq_list) - i - 1):
            if operation == "diff":
                result[i+1].append(abs(result[i][k] - result[i][k+1]))
            elif operation == "neg":
                result[i+1].append(result[i][k+1] - result[i][k])       
            elif operation == "sum":
                result[i+1].append(result[i][k] + result[i][k+1])
            elif operation == "integral":
                if i == 0:
                    result[i+1].append(result[i][0])
                    continue
                sum = 0
                for j in range(k+1):
                    sum += result[i][j]
                result[i+1].append(sum)
            else:
                result[i+1].append(result[i][k] + result[i][k+1])
    return result

def fun_print(result):
    print("iteration {}".format(z))
    #for i in range(len(result)):
    #    for k in range(len(result[i])):
    #        result[i][k] = abs(result[i][k])
    for i in range(len(result)):
        string = "  "    
        for k in range(len(result[i])):
            string += "{}".format(str(round(result[i][k], 2)))
            if (k + 1) < len(result[i]):
                string += ", "
        print(string) 
    
sequences = [
    {"name": "primes", "sequence": [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]},
    {"name": "primes_inv", "sequence": [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]},
    {"name": "primes_seed", "sequence": [0, 1, 2, 2, 4, 2, 4, 2, 4, 6, 2, 6, 4, 2, 4, 6, 6, 2, 6, 4, 2, 6, 4, 6, 8, 4, 2, 4, 2, 4, 14, 4, 6, 2, 10, 2, 6, 6, 4, 6, 6, 2, 10, 2, 4, 2]},
    {"name": "21*", "sequence": [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]},
    {"name": "#div", "sequence": [1, 2, 2, 3, 2, 4, 2, 4, 3, 4, 2, 6, 2, 4, 4, 5, 2, 6, 2, 6, 4, 4, 2, 8, 3, 4, 4, 6, 2, 8, 2, 6, 4, 4, 4, 9, 2, 4, 4, 8, 2, 8, 2, 6, 6, 4, 2, 10, 3]},
    # FIB
    {"name": "011*", "sequence": [0, 1, 1, 0, 1, 1, 0, 1, 1, 0]},
    {"name": "022*", "sequence": [0, 2, 1, 0, 1, 1, 0, 1, 1, 0]},
    {"name": "fibonacci", "sequence": [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946]},
    {"name": "fibonacci_w", "sequence": [0, 1, 3, 8, 21, 55, 144, 377, 987, 2584, 6765, 17711, 46368, 121393, 317811, 832040, 2178309, 5702887, 14930352, 39088169, 102334155, 267914296, 701408733]},
    {"name": "fibonacciX2", "sequence": [0, 1, 3, 8, 21, 55, 144, 377, 987, 2584, 6765, 17711, 46368, 121393, 317811, 832040, 2178309, 5702887, 14930352]},
    # !N N!
    {"name": "factorial", "sequence": [1, 1, 2, 6, 24]},#, 40320, 362880, 3628800, 39916800]},
    {"name": "derangement", "sequence": [1, 0, 1, 2, 9, 44, 265, 1854, 14833, 133496, 1334961, 14684570]},
    # EXP
    {"name": "0exp", "sequence": [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},
    {"name": "1exp", "sequence": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]},
    {"name": "2exp", "sequence": [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]},
    {"name": "3exp", "sequence": [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049]},
    # POW
    {"name": "0power", "sequence": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]},
    {"name": "1power", "sequence": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]},
    {"name": "2power", "sequence": [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144]},
    {"name": "3power", "sequence": [0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728]},
    {"name": "4power", "sequence": [0, 1, 16, 81, 256, 625, 1296, 2401, 4096, 6561]},
    {"name": "5power", "sequence": [0, 1, 32, 243, 1024, 3125, 7776, 16807, 32768, 59049]},
    {"name": "6power", "sequence": [0, 1, 64, 3**6, 4**6, 5**6, 6**6, 7**6, 8**6, 9**6]},
    # POW BASE
    {"name": "0base", "sequence": [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},
    {"name": "1base", "sequence": [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]},
    {"name": "2base", "sequence": [0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0]},
    {"name": "3base", "sequence": [0, 1, 6, 6, 0, 0, 0, 0, 0, 0, 0]},
    {"name": "4base", "sequence": [0, 1, 14, 36, 24, 0, 0, 0, 0, 0, 0]},
    {"name": "5base", "sequence": [0, 1, 30, 150, 240, 120, 0, 0, 0, 0, 0]},
    {"name": "6base", "sequence": [0, 1, 62, 540, 1560, 1800, 720, 0, 0, 0, 0]},
    # MOD
    {"name": "xmod2", "sequence": [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]},
    {"name": "xmod3", "sequence": [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0]},
    {"name": "xmod4", "sequence": [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]},
    {"name": "xmod5", "sequence": [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]},
    {"name": "010*", "sequence": [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]},
    {"name": "x+1mod2", "sequence": [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]},
    {"name": "110*", "sequence": [1, 1, 0, 0, 0, 0, 0, 0, 0, 0]},
    {"name": "osc", "sequence": [-1]},
    #
    {"name": "odd", "sequence": [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]},
    {"name": "even", "sequence": [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]},
    {"name": "pascal", "sequence": [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]},
    {"name": "aliquot", "sequence": [2, 3, 3, 4, 3, 1, 3, 4, 5, 5, 3, 8, 3, 6, 6, 7, 3, 5, 3, 8, 4, 7, 3, 6, 2, 8, 4, 1, 3, 16, 3, 4, 7]},
    {"name": "default", "sequence": [2, 3, 3, 4, 3, 1, 3, 4, 5, 5, 3, 8, 3, 6, 6, 7, 3, 5, 3, 8, 4, 7, 3, 6, 2, 8, 4, 1, 3, 16, 3, 4, 7]},
    
    {"name": "catalan", "sequence": [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 742900, 2674440, 9694845]},
    {"name": "euler", "sequence": [1, -1, 5, -61, 1385, -50521, 2702765, -199360981, 19391512145, -2404879675441, 370371188237525, -69348874393137901, 15514534163557086905]},
    {"name": "lucas", "sequence": [2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, 322, 521, 843]},
    {"name": "partition", "sequence": [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42, 56, 77, 101, 135, 176, 231, 297, 385, 490, 627, 792]},
    {"name": "shapiro", "sequence": [0, 0, 0, 1, 0, 0, 1, 2, 0, 0, 0, 1, 1, 1, 2, 3]},
    {"name": "semiprime", "sequence": [4, 6, 9, 10, 14, 15, 21, 22, 25, 26, 33, 34, 35, 38, 39, 46, 49, 51, 55]},
    {"name": "bell", "sequence": [1, 1, 3, 13, 75, 541, 4683, 47293, 545835, 7087261, 102247563]},
    
    #{"name": "test", "sequence": [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]},
    {"name": "test", "sequence": [math.e**0, math.e**1, math.e**2, math.e**3]},
    {"name": "test2", "sequence": [1, 3, 4, 2, 4, 4, 8, 8, 16, 16, 32]},
    
    {"name": "func", "sequence": [0.0, 0.84, 0.91, 0.14]},
    {"name": "seed", "sequence": [0.0, 0.84, -0.77, -0.07]},
    
    #
    {"name": "1*", "sequence": [1, 1, 1, 1, 1, 1]},
    {"name": "0*", "sequence": [0, 0, 0, 0, 0, 0]},
    {"name": "[01]*", "sequence": [0, 1, 0, 1, 0, 1]},
    {"name": "[10]*", "sequence": [1, 0, 1, 0, 1, 0]},
    {"name": "[100]*", "sequence": [1, 0, 0, 1, 0, 0, 1, 0, 0]},
    {"name": "[010]*", "sequence": [0, 1, 0, 0, 1, 0, 0, 1, 0]},
    {"name": "[001]*", "sequence": [0, 0, 1, 0, 0, 1, 0, 0, 1]},
    {"name": "[011]*", "sequence": [0, 1, 1, 0, 1, 1, 0, 1, 1]},
    {"name": "[110]*", "sequence": [1, 1, 0, 1, 1, 0, 1, 1, 0]},
]

name = sys.argv[1]
operation = sys.argv[2]
s = None
for s in sequences:
    if name == s["name"]:
        sequence = s["sequence"]

#if len(sys.argv) > 3:
sequence = sequence[0:50]

iterations = 1
if len(sys.argv) > 3:
    iterations = int(sys.argv[3])

memory = []
memory.append(sequence.copy())

print("{}".format(name))

for z in range(iterations):
    result = fun_operation(sequence, operation)
    fun_print(result)
    # q
    sequence = []
    if operation == "integral":
        for i in range(1, len(result)):
            sum = 0
            for k in range(len(result)):
                if len(result[k]) < i:
                    continue
                sum += result[k][-i]
            sequence.insert(0, sum)
    else:
        for i in range(len(result)):
            sequence.append(result[i][0])
       
    memory.append(sequence.copy())


print()

string = ""
for m in range(len(memory)):
    string += "["
    for i in range(len(memory[m])):
        if i+1 == len(memory[m]):
            string += "{}".format(round(memory[m][i], 2))
        else:
            string += "{}, ".format(round(memory[m][i], 2))
    string += "]\n"
print(string)



print("\n\nFUNC EVAL")
import math
string = ""
string += "\n["
l = 6
for x in range(0, l, 1):
    if x+1 == l:
        string += "{}".format(round(math.sin(x), 2))
    else:
        string += "{}, ".format(round(math.sin(x), 2))
string += "]\n"
print(string)

print("\n\n")


exit()
"""
for i in range(len(result)):
    for k in range(len(result[i])):
        result[i][k] = abs(result[i][k])

for i in range(len(sequence)):
    string = "  "    
    for k in range(len(result[i])):
        if is_prime(result[i][k]):
            string += "{}".format(str(result[i][k]))
        else: 
            string += " "
        if (k + 1) < len(result[i]):
            string += ", "
    print(string)
"""
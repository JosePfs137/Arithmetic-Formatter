def arithmetic_formatter(problems, state = True):
    results = []
    fstRow = ''
    sndRow = ''
    trdRow = ''
    thRow = ''
    row1 = []
    row2 = []
    row3 = []
    row4 = []
    for problem in problems: #Loops in all of the problems in the 'problems' array
        if '+' in problem:
            ope = '+'
            problem = problem.split('+')
        elif '-' in problem:
            ope = '-'
            problem = problem.split('-')
        else:
            print('Error: Operator must be \'+\' or \'-\'.')
            quit()
            #Verifies if there is a plus sign or a subtraction sign, to then take it and split the string to obtain the numbers
        try:
            num1 = int(problem[0])
            num2 = int(problem[1])
        except:
            print('Error: Numbers must only contain digits.')
            quit()
        #See if the numbers have numeric characters or are anything more
        nuM = int(max(len(str(num1)), len(str(num2))))
        num = int(min(len(str(num1)), len(str(num2))))
        #Takes the length of the numbers and compares them.
        if nuM > 4:
            print('Error: Numbers cannot be more than four digits')
            quit()
            #Error message
        if ope == '+':
            res = num1 + num2
        if ope == '-':
            res = num1 - num2
        #Remembers the sign and computes the corresponding operation
        results.append((ope,num1,num2,res, nuM, num))
    for op in results:
        n1 = len(str(op[1]))
        n2 = len(str(op[2]))
        n3 = len(str(op[3]))
        #Takes the length of the result, first and second number
        line = str()
        space = str()
        s3 = str()
        for i in range(op[4] + 2): line = line + '-'
        for i in range(len(line) - op[5] - 1) : space = space + ' '
        for i in range(len(line) - n3): s3 = s3 + ' '
        #Creates the spaces and the lines needed so the operations print in the correct format.
        if n1 == n2:
            s1 = '  '
            s2 = ' '
        elif n1 > n2:
            s2 = space
            s1 = '  '
        elif n1 < n2:
            s1 = ' ' + space
            s2 = ' '
        #Complete the missing spaces due to the sign and the order of the numbers in the operation.
        row1.append((s1, op[1]))
        row2.append((s2, op[0], op[2]))
        row3.append(line)
        row4.append((s3, op[3]))
        #Saves the numbers, signs, and their spaces in rows so we can print it later per row.
    for r in row1:
        fstRow = fstRow + '{:}{:>}    '.format(r[0],str(r[1]))
        #Creates a string for the whole first row
    for r in row2:
        sndRow = sndRow + '{:<}{:}{:>}    '.format(r[1], r[0],str(r[2]))
        #Creates a string for the whole second row
    for r in row3:
        trdRow = trdRow + r + '    '
        #Creates a string for the whole third row
    for r in row4:
        thRow = thRow + '{:}{:>}    '.format(r[0],str(r[1]))
        #Creates a string for the whole fourth row
    if len(results) > 5:
        print('Error: Too many problems.')
        quit()
    print(fstRow)
    print(sndRow)
    print(trdRow)
    #Prints the rows
    if state:
        print(thRow)
        #Print the resuls row if the user wants to see it
#The calculator it self
def interface():
    problems = []
    while True:
        print('\nWelcome to MyCalculator')
        problem = input('Please give me a sum or a subtract, or write \'exit\': ')
        if problem == 'exit':
            quit()
        if '+' in problem:
            num = problem.split('+')

        elif '-' in problem:
            num = problem.split('-')
        else:
            print('\nError: Operator must be \'+\' or \'-\'.')
            continue
        if len(num[0]) > 4 or len(num[1]) > 4:
            print('\nError: Numbers cannot be more than four digits')
            continue
        try:
            n1 = int(num[0])
            n2 = int(num[1])
        except:
            print('\nError: Numbers must only contain digits.')
            continue

        problems.append(problem)
        state = input('If you want to see the results please write \'yes\' else press\'Enter\': ')

        if state == 'yes':
            arithmetic_formatter(problems, False)
            while True:
                s = input('\n\nPress \'Enter\' when you are ready to see the results')
                if s == '':
                    arithmetic_formatter(problems)
                    break
                else:
                    print('I cant understand you')
                    continue
            print('Bye!')
            break
        else:
            pass

        if len(problems) == 5:
            print('\n\nThe maximum number of problems is 5!')
            arithmetic_formatter(problems, False)
            while True:
                state = input('\n\nPress \'Enter\' when you are ready to see the results')
                if state == '':
                    arithmetic_formatter(problems)
                    break
                else:
                    print('I cant understand you')
                    continue
            print('Bye!')
            break
        #print(problems)
#A sequence of if statements and while loops that I've decided to call 'interface', helps the user to just type his computations
interface()

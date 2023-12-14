import random


class ArithmeticExam:

    def __init__(self):
        self.operation = None
        self.answer = None
        self.msg = None
        self.level = None
        pass

    def op_gen_1(self):
        self.a = random.randint(2, 9)
        self.b = random.randint(2, 9)
        self.opd = ["*", "+", "-"]
        self.op = random.choice(self.opd)
        self.operation = " ".join([str(self.a), str(self.op), str(self.b)])
        self.answer = eval(self.operation)
        return self.answer

    def op_gen_2(self):
        self.a = random.randint(11, 29)
        self.operation = self.a
        self.answer = self.a ** 2
        return self.answer

    def difficulty(self):
        while True:
            self.level = input(
                '''Which level do you want? Enter a number:\n1 - simple operations with numbers 2-9\n2 - integral squares of 11-29''')
            if self.level in ["1", "2"]:
                break
            else:
                print('Incorrect format.')
        return self.level

    def check_(self):
        if self.level == "1":
            self.op_gen_1()
            self.msg = "1 (simple operations with numbers 2-9)"
        else:
            self.op_gen_2()
            self.msg = "2 (integral squares 11-29)"
        print(self.operation)
        while True:
            self.ans = input()
            try:
                self.ans = int(self.ans)
                break
            except ValueError:
                print('Incorrect format.')
                pass
        if self.ans == self.answer:
            return 'Right!'
        elif self.ans != self.answer:
            return 'Wrong!'


exam = ArithmeticExam()
n = 0
exam.difficulty()
for i in range(5):
    result = exam.check_()
    print(result)
    if result == 'Right!':
        n += 1
response = input('your marks is {}/5. Would you like to save your result to the file? Enter yes or no.\n'.format(n))
if response in ['yes', 'YES', 'y', 'Yes']:
    name = input('What is your name?\n')
    file = open('results.txt', 'a', encoding="utf-8")
    file.write(f'{name}: {n}/5 in level {exam.msg}.')
    file.close()
    print('The results are saved in "results.txt".')
else:
    pass

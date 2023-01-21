""" My approach to practice question #7.1 """


class Prompt:
    def __init__(self, prompt):
        self.prompt = prompt

    def run(self):
        while True:
            cmd = input(self.prompt).strip()
            if len(cmd) == 0:
                continue

            if cmd == 'quit':
                break
            else:
                print(cmd[::-1])


cp = Prompt('AHD>')
cp.run()

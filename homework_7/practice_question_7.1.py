""" My approach to practice question #7.1 """


class Prompt:
    def __init__(self, prompt):
        self.prompt = prompt

    def run(self):
        while True:
            cmd = input(self.prompt)
            if len(cmd.strip()) == 0:
                continue

            if cmd.strip() == 'quit':
                break
            else:
                print(cmd[::-1])


cp = Prompt('AHD>')
cp.run()

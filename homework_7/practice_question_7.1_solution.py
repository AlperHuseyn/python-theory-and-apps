""" Instructor solution for practice question #7.1 """


class CommandPrompt:
    def __init__(self, prompt):
        self.prompt = prompt

    def run(self):
        while True:
            cmd = input(f'{self.prompt}>').strip()
            if cmd == '':
                continue
            elif cmd == 'quit':
                break
            print(cmd[::-1])


cp = CommandPrompt('CSD')
cp.run()

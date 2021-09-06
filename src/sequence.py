import subprocess

class Process:
    def __init__(self, commands):
        self.commands = commands
        self.process = None

    def __str__(self):
        return str(self.commands)

    def execute(self):
        self.process = subprocess.Popen(self.commands, shell=True)
        self.process.wait()


class Sequence:
    def __init__(self):
        self._seq = []
        self._failed = []

    def add_process(self, *commands):
        self._seq.append(Process(commands))

    def execute(self):
        for process in self._seq:
            process.execute()
            if process.process.poll() != 0:
                failed_proc = {
                    'commands': str(process),
                    'code': process.process.poll()
                }
                self._failed.append(failed_proc)

    def print_failed(self):
        for process in self._failed:
            print(f"Exit code: {process.code}, Commands: {process.commands}")



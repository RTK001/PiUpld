import subprocess
from json import loads

def get_devices():
    with subprocess.Popen(["platformio", "device", "list", "--json-output"],
                            stdout = subprocess.PIPE,
                            stderr = subprocess.PIPE,
                            universal_newlines=False) as proc:
        out, err = proc.communicate('')
        output = loads(out)
        if len(output) == 0:
            return None
        for device in output:
            device['Hardware ID'] = "<br>".join(device.pop('hwid').split(" "))
            device['Port'] = device.pop('port')
            device['Description'] = device.pop('description')
        return output


def write_project_to_device(project_dir):
    with subprocess.Popen(["platformio", "run", "upload",  "-d", project_dir,  "--json-output"],
                            bufsize = 1,
                            stdout = subprocess.PIPE,
                            stderr = subprocess.PIPE,
                            universal_newlines=False) as proc:
        pass

class WriteToDevice():
    def __init__(self):
        pass
        #self.projectDir = project_dir

    def __iter__(self):
        '''
        self.proc = subprocess.Popen(["platformio", "run", "upload",  "-d", self.projectDir,  "--json-output"],
                                bufsize = 1,
                                stdout = subprocess.PIPE,
                                stderr = subprocess.PIPE,
                                universal_newlines=True)
        '''
        self.proc = subprocess.Popen(["platformio", "device", "list", "--json-output"],
                                stdout = subprocess.PIPE,
                                stderr = subprocess.PIPE,
                                universal_newlines=False)
        return self

    def __next__(self):
        for line in self.proc.stdout:
            return "<br>" + line.decode("utf-8")
        raise StopIteration

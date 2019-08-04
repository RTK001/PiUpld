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
            return [{"Error": "No Devices Found"}]
        for device in output:
            device['Hardware ID'] = device.pop('hwid').split(" ")
            device['Port'] = device.pop('port')
            device['Description'] = device.pop('description')
        return output

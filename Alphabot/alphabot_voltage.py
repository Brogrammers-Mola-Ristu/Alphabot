import subprocess

voltage = subprocess.run(["vcgencmd"," measure_volts"], capture_output=True)
voltage = float(voltage.stdout.decode().split('=')[1][:-3])
print(voltage)
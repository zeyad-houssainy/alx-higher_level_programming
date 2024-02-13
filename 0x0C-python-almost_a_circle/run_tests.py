import subprocess
subprocess.run(["python.exe", "-m pip install", "--upgrade", "pip"])
  

# Run tests with coverage
subprocess.run(['coverage', 'run', '-m', 'unittest',
               'discover', '-p', 'test_*.py'])

# Generate coverage report
subprocess.run(['python', '-m', 'coverage', 'report'])

# Generate HTML coverage report
subprocess.run(['python', '-m', 'coverage', 'html'])

#Unittest
# subprocess.run(['python3', '-m', 'unittest', 'discover', 'tests'])
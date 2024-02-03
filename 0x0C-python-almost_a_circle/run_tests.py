import subprocess
subprocess.run(['pip', 'install', 'coverage'])
  

# Run tests with coverage
subprocess.run(['coverage', 'run', '-m', 'unittest',
               'discover', '-p', 'test_*.py'])

# Generate coverage report
subprocess.run(['python', '-m', 'coverage', 'report'])

# Generate HTML coverage report
subprocess.run(['python', '-m', 'coverage', 'html'])

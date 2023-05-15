import subprocess

def open_programs(programs):
    for program in programs:
        subprocess.Popen(program)

# List of programs you want to open
programs = [
    r"C:\Path\to\SQL Server Management Studio\Ssms.exe",
    r"C:\Path\to\Visual Studio 2022\Devenv.exe",
    r"C:\Path\to\PhpStorm\PhpStorm.exe",
    r"C:\Path\to\Visual Studio Code\Code.exe"
]

# Call the function to open the programs
open_programs(programs)

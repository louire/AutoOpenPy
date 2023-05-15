import subprocess

def open_programs(programs):
    for program in programs:
        subprocess.Popen(["open", "-a", program])

# List of programs you want to open
programs = [
    "Brave Browser",
    "Visual Studio Code",
    "Microsoft Teams",
    "Spotify"
]

# Call the function to open the programs
open_programs(programs)

import pyfiglet


def generate_title():
    bj_art = pyfiglet.figlet_format("Black Jack")
    for line in bj_art.split("\n"):
        print(line.center(100))
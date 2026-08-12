import sys
from time import sleep


def print_lyrics():
    lines = [
        ("Ku bertamu ke rumah barumu", 0.1),
        ("Tak ada kamu", 0.09),
        ("Hanya papan dan namamu", 0.09),
        ("Mana ocehan, wewangian khasmu?", 0.09),
        ("Jarak ini terlalu jauh", 0.09),
        ("Kalau rindu aku tak mampu", 0.09),
        ("Sesal hatiku tak sempat temani kamu...", 0.09),
        ("Harusnya ku bisikkan", 0.09),
        ("Kata ajaib ke telinga mu", 0.09),
        ("Soal ikhlas ternyata aku masih amatir", 0.09),
        ("Masih sangat amatir...", 0.09)
    ]
    
    for line, char_delay in lines:
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(char_delay)
        print()
        sleep(1.5)
        
print_lyrics()
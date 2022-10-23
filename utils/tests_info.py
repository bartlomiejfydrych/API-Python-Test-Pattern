# ------------------------------
# CONSOLE COLORS:
# ------------------------------
# Test colors:
c_blue = '\33[94m'
# End color:
c_end = '\033[0m'


def show_tests(*args):
    # Wkładanie argumentów do tablicy
    test_list = [item for item in args]
    # Wypisanie tekstu
    print(f"{c_blue}TESTS IN THAT TEST:{c_end}")
    for i in range(len(test_list)):
        print(f"{c_blue}[TEST-{i+1}] {test_list[i]}{c_end}")

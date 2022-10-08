def show_tests(*args):
    # Wkładanie argumentów do tablicy
    test_list = [item for item in args]
    # Ustawienia kolorów konsoli
    c_yellow = '\33[94m'
    c_end = '\033[0m'
    # Wypisanie tekstu
    print(f"{c_yellow}TESTS IN THAT TEST:{c_end}")
    for i in range(len(test_list)):
        print(f"{c_yellow}[TEST-{i+1}] {test_list[i]}{c_end}")

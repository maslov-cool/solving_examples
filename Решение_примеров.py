def examples():
    def greeting():
        print("                **    **  ********  **        **            **      ")
        print("               **    **  ********  **        **         **     **   ")
        print("              ********  **        **        **         **      **  ")
        print("             ********  ********  **        **         **      **  ")
        print("            **    **  **        **        **         **      **  ")
        print("           **    **  ********  ********  ********    **    **   ")
        print("          **    **  ********  ********  ********       **      ")
        print("Приветствую тебя программе для решения примеров на сложение и вычитание! ")
        start()

    def is_valid_(s):
        if str(s).isdigit():
            return True
        return False

    def generating_numbers_addition(r_border):
        import random
        a = random.randint(1, r_border)
        b = random.randint(1, r_border)
        while not a + b <= r_border:
            a = random.randint(1, r_border)
            b = random.randint(1, r_border)
        return a, b

    def generating_numbers_subtraction(r_border):
        import random
        a = random.randint(1, r_border)
        b = random.randint(1, r_border)
        while not b - a >= 0:
            a = random.randint(1, r_border)
            b = random.randint(1, r_border)
        return a, b

    def with_statistics():
        print('P.S. Если захотите завершить или решать примеры без статистики введите "restart"')
        while True:
            r_border = input('Введи число до которого ты умеешь считать ')
            if is_valid_(r_border) and int(r_border) > 0:
                r_border = int(r_border)
                break
            elif not is_valid_(r_border):
                print('А может быть все-таки введем натуральное число?')
                continue
        correctly_solved = 0
        attempts = 0
        flag = True

        while flag:
            a, b = generating_numbers_addition(r_border)
            while flag:
                n = input(f'{a} + {b} = ').strip().lower()
                if n == 'restart':
                    restart()
                    flag = False
                elif is_valid_(n) and int(n) == a + b:
                    correctly_solved += 1
                    attempts += 1
                    print('Молодец!')
                    print(f'Правильно решено {correctly_solved} из {attempts} примеров')
                else:
                    attempts += 1
                    print('Неправильно')
                    print(f'Правильно решено {correctly_solved} из {attempts} примеров')
                break

            a, b = generating_numbers_subtraction(r_border)
            while flag:
                n = input(f'{b} - {a} = ').strip().lower()
                if n == 'restart':
                    restart()
                    flag = False
                elif is_valid_(n) and int(n) == b - a:
                    correctly_solved += 1
                    attempts += 1
                    print('Молодец!')
                    print(f'Правильно решено {correctly_solved} из {attempts} примеров')
                else:
                    attempts += 1
                    print('Неправильно')
                    print(f'Правильно решено {correctly_solved} из {attempts} примеров')
                break

    def without_statistics():
        print('P.S. Если захотите завершить или решать примеры со статистикой введите "restart"')
        while True:
            r_border = input('Введи число до которого ты умеешь считать ')
            if is_valid_(r_border) and int(r_border) > 0:
                r_border = int(r_border)
                break
            elif not is_valid_(r_border):
                print('А может быть все-таки введем натуральное число?')
                continue
        flag = True

        while flag:
            a, b = generating_numbers_addition(r_border)
            while flag:
                n = input(f'{a} + {b} = ').strip().lower()
                if n == 'restart':
                    restart()
                    flag = False
                    break
                elif is_valid_(n) and int(n) == a + b:
                    print('Молодец!')
                    break
                else:
                    print('Неправильно, попробуй ещё раз')
                    continue

            a, b = generating_numbers_subtraction(r_border)
            while flag:
                n = input(f'{b} - {a} = ').strip().lower()
                if n == 'restart':
                    restart()
                    flag = False
                    break
                elif is_valid_(n) and int(n) == b - a:
                    print('Молодец!')
                    break
                else:
                    print('Неправильно, попробуй ещё раз')
                    continue

    def start():
        while True:
            print('Вы хотите решать со статистикой или без? ')
            choice = input().lower().strip()
            if choice == 'со статистикой' or choice == 'со':
                with_statistics()
                break
            elif choice == 'без статистики' or choice == 'без':
                without_statistics()
                break
            else:
                print('Я вас не понимаю')
                continue

    def restart():
        while True:
            print('Если вы хотите завершить решать примеры введите "end" ')
            print('Если вы хотите решать решать примеры со статистикой или без введите "again" ')
            restart_ = input().lower().strip()
            if restart_ == 'end':
                print('Возвращайся если ещё захочешь порешать примеры!')
                print('Пока!')
                break
            elif restart_ == 'again':
                start()
                break
            else:
                print('Я не понимаю ')
                continue
    greeting()


examples()

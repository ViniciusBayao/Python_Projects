from models.calculate import Calculate


def main() -> None:
    points: int = 0
    play(points)


def play(points: int) -> None:
    difficulty: int = int(input('Enter the desired difficulty level [1, 2, 3 or 4]: '))

    calc: Calculate = Calculate(difficulty)

    print('Report the result for the following operation: ')
    calc.show_operation()

    result: int = int(input())

    if calc.check_result(result):
        points += 1
        print(f'You have {points} points(s).')

    continue_op: int = int(input('Do you want to continue in the game? [1 - yes, 0 - no] '))

    if continue_op:
        play(points)
    else:
        print(f'you ended up with {points} point(s).')
        print('See you next time!')


if __name__ == '__main__':
    main()

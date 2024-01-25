
def mat_operation(inp1, operator, inp2):
    if operator == '+':
        return inp1 + inp2
    elif operator == '-':
        return inp1 - inp2
    elif operator == '/':
        if inp2 != 0:  # Check for division by zero
            return inp1 / inp2
        else:
            return 'Error: Division by zero'
    elif operator == '*':
        return inp1 * inp2
    else:
        return 'Error: Invalid operator'


def user_interface():
    while True:
        try:
            inp1 = int(input('Input 1: '))
            operator = input('Operator: ')
            inp2 = int(input('Input 2: '))

            result = mat_operation(inp1, operator, inp2)

            if isinstance(result, (int, float)):
                print(f'Result: {result}')
            else:
                print(result)
            print('Operation done')
            cont = input('Continue? (y/n): ')
            if cont.lower() != 'y':
                break
        except ValueError as ve:
            print(f'Error: Invalid input. Please enter valid numbers. - {ve}')
        except Exception as e:
            print(f'Error: {e}')


if __name__ == "__main__":
    user_interface()



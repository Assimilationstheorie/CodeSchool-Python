def f():
    try:
        print(1/0)
    except:
        print('ERROR ERROR!')
        return 0
    finally:
        print('FINAL!')

    print('Will not be printed!')
    return 1

print('Start')
f()
print('End')

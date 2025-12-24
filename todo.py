import argparse
import mainprog 

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('task',nargs = '+')
    args = parser.parse_args()

    main_work = ' '.join(args.task[1:])

    if args.task[0] == 'add':
        mainprog.add_task(main_work)

    elif args.task[0] == 'remove':
        mainprog.remove_task(main_work)

    elif args.task[0] =='display':
        mainprog.display_task()

if __name__ == '__main__':
    main()
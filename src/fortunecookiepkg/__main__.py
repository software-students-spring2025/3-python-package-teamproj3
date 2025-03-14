import argparse
from fortunecookiepkg.fortunecookie import (
    get_random_fortune,
    get_lucky_numbers,
    get_daily_fortune,
    get_custom_fortune,
    get_themed_fortune,
)

def main():
    """
    Recieve the fortune or lucky numbers
    """
    parser = argparse.ArgumentParser(description="Get your fortune!")
    parser.add_argument("--random", action="store_true", help="Get a random fortune.")
    parser.add_argument("--numbers", metavar="LEN", help="Get your lucky number(s). Choose how many numbers you want from 1-10 (inclusive).")
    parser.add_argument("--daily", action="store_true", help="Get today's fortune.")
    parser.add_argument("--custom", metavar="NAME", help="Get a personalized fortune.")
    parser.add_argument("--themed", metavar="THEME", help="Get a themed fortune. The themes are love, career, and happiness.")

    args = parser.parse_args()

    if args.random:
        print(get_random_fortune())
    elif args.numbers:
        lucky_numbers = get_lucky_numbers(args.numbers)
        len_nums = len(lucky_numbers)
        if len_nums > 0:
            print("Lucky Numbers:", lucky_numbers)
        else:
            parser.print_help();
        
    elif args.daily:
        print("Today's Fortune:", get_daily_fortune())
    elif args.custom:
        print(get_custom_fortune(args.custom))
    elif args.themed: 
        print(get_themed_fortune(args.themed))
    else:
        parser.print_help()

if __name__ == "__main__":
    #run main function
    main()
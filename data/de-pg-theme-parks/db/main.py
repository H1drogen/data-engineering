from seed import seed
from data.parks import parks
from data.foods import foods
from data.rides import rides
from data.stalls import stalls


def main():
    seed(parks, rides, stalls, foods)

if __name__ == "__main__":
    main()
def list_alphabets():
    """Lists the alphabets from Z to A horizontally."""
    print(*[chr(i) for i in range(ord('Z'), ord('A') - 1, -1)])

def main():
    list_alphabets()

if __name__ == "__main__":
    main()

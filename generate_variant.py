if __name__ == '__main__':
    email = "smail.t@phystech.edu"
    print("Variant: ", (hash(email) % 3) + 1)

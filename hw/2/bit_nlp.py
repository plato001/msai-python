def str_preprocessing(str_):
    try:
        return " ".join(str_.strip().split())
    except AttributeError:
        return "Error! Please enter string!"


if __name__ == "__main__":
    str_1 = "You will probably  need this     trick to   prepare data  for NLP tasks! "
    str_2 = "    Hi! My name   is John    "
    str_3 = "Hello!"
    str_4 = ""
    str_5 = None
    str_6 = 45
    print(str_preprocessing(str_1))
    print(str_preprocessing(str_2))
    print(str_preprocessing(str_3))
    print(str_preprocessing(str_4))
    print(str_preprocessing(str_5))
    print(str_preprocessing(str_6))

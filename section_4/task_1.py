def retry_if_none(f):
    def wrapper():
        wrapper.count += 1
        if f() is None and wrapper.count < 3:
            return wrapper()
    wrapper.count = 0
    return wrapper


@retry_if_none
def foo():
    print("foo")
    return None


@retry_if_none
def bar():
    print("bar")
    return 1


if __name__ == '__main__':
    foo()
    bar()

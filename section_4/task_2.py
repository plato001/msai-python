def retry_if_none_n_times(n=1):
    def retry_if_none(f):
        def wrapper():
            wrapper.count += 1
            if f() is None and wrapper.count < n:
                return wrapper()
        wrapper.count = 0
        return wrapper
    return retry_if_none


@retry_if_none_n_times(n=10)
def foo():
    print("foo")
    return None


@retry_if_none_n_times(n=10)
def bar():
    print("bar")
    return 1


if __name__ == '__main__':
    foo()
    bar()

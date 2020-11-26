from contextlib import contextmanager


@contextmanager
def file_open_helper(path, mode):
    file_ = open(path, mode)
    # ...
    yield file_
    # ...
    file_.close()


with file_open_helper("mycontacts.txt", "r") as file_:
    print(file_.read())

class Resource(object):
    def __init__(self):
        print("--- init Resource ---")

    def __enter__(self):
        print("--- enter Resource ---")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("--- exit Resource ---")

    def operate(self):
        print("--- operate Resource ---")


with Resource() as res:
    res.operate()

import time

IN_FILE = "log.txt"
OUT_FNAME_PREFIX = "dict-"

if __name__ == "__main__":
    with open(IN_FILE) as f:
        lines = f.readlines()

    lines = [l.lower() for l in lines]

    data = set(lines)
    data = list(data)
    data.sort()

    print(data)

    out_file = OUT_FNAME_PREFIX + str(time.time())

    with open(out_file, "w") as f:
        for i in data:
            f.write(i)

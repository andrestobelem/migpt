"""Build a character bigram model with counts. See docs/01-bigramas.md."""

import numpy as np


def main():

    text = "banana bandana"
    t = len(text)

    vocabulary = sorted(set(text))
    vocabulary = sorted(set(text))

    token_to_id = {v: k for k, v in enumerate(vocabulary)}
    id_to_token = {k: v for k, v in enumerate(vocabulary)}

    V = len(vocabulary)
    C = np.zeros([V, V], dtype=int)

    ids = [token_to_id[c] for c in text]

    ult = ids[:-1]
    prim = ids[1:]
    pairs = zip(ult, prim)

    np.add.at(C, (ult, prim), 1)

    t = C.sum()

    assert 13 == t

    C = (C + 1 / V * 2) / (C + 1 / V * 2).sum()

    C = C.sum()
    print(C)


if __name__ == "__main__":
    main()

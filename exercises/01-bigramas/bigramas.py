"""Build a character bigram model with counts. See docs/01-bigramas.md."""

import numpy as np


def main():

    text = "banana bandana"
    vocabulary = sorted(set(text))

    token_to_id = {v: k for k, v in enumerate(vocabulary)}
    id_to_token = {k: v for k, v in enumerate(vocabulary)}

    V = len(vocabulary)
    C = np.zeros([V, V], dtype=int)

    ids = [token_to_id[c] for c in text]

    current_ids = ids[:-1]
    next_ids = ids[1:]

    np.add.at(C, (current_ids, next_ids), 1)

    t = C.sum()

    assert 13 == t

    row_totals = C.sum(axis=1, keepdims=True)
    probabilities = np.full((V, V), 1 / V)
    np.divide(C, row_totals, out=probabilities, where=row_totals != 0)

    assert np.allclose(probabilities.sum(axis=1), 1)
    assert np.isclose(probabilities[token_to_id["a"], token_to_id["n"]], 4 / 5)
    assert np.isclose(probabilities[token_to_id["a"], token_to_id[" "]], 1 / 5)
    print(probabilities[token_to_id["a"]])


if __name__ == "__main__":
    main()

import argparse
from collections import OrderedDict
import os

import utils

def run(path_corpus, path_vocab, prune_at, min_count, special_words, with_unk=True):
    assert os.path.exists(path_corpus)
    assert not os.path.exists(path_vocab)
    assert path_vocab.endswith("vocab.txt")

    print("[textpreprocessor.create_vocabulary] Processing ...")
    print("[textpreprocessor.create_vocabulary] PRUNE AT=%d" % prune_at)
    print("[textpreprocessor.create_vocabulary] MINIMUM COUNT=%d" % min_count)
    print("[textpreprocessor.create_vocabulary] SPECIAL WORDS=%s" % special_words)

    # Counting
    counter = utils.get_word_counter(path_corpus)
    counter = counter.most_common()

    # Pruning
    counter = counter[:prune_at]
    frequencies = dict(counter)
    counter.sort(key=lambda x: (-x[1], x[0]))
    vocab_words = [w for w,freq in counter if freq >= min_count]

    # Adding special words
    for sw in special_words:
        if not sw in vocab_words:
            vocab_words = vocab_words + [sw]
            frequencies[sw] = 0 # TODO

    # Create a word-to-id dictionary
    vocab = OrderedDict()
    for w_id, w in enumerate(vocab_words):
        vocab[w] = w_id

    # Add a special unknown symbol
    if with_unk:
        if not "<UNK>" in vocab.keys():
            vocab["<UNK>"] = len(vocab)
            frequencies["<UNK>"] = 0 # TODO
        print("[textpreprocessor.create_vocabulary] Vocabulary size (w/ '<UNK>')=%d" % len(vocab))
    else:
        print("[textpreprocessor.create_vocabulary] Vocabulary size (w/o '<UNK>')=%d" % len(vocab))

    with open(path_vocab, "w") as f:
        for w, w_id in vocab.items():
            freq = frequencies[w]
            f.write("%s\t%d\t%d\n" % (w, w_id, freq))
    print("[textpreprocessor.create_vocabulary] Saved the vocabulary (text) to %s" % path_vocab)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--corpus", type=str, required=True)
    parser.add_argument("--vocab", type=str, required=True)
    parser.add_argument("--prune_at", type=int, default=1000000)
    parser.add_argument("--min_count", type=int, default=0)
    parser.add_argument("--special", type=str, nargs="+", default=[])
    args = parser.parse_args()

    path_corpus = args.corpus
    path_vocab = args.vocab
    prune_at = args.prune_at
    min_count = args.min_count
    special_words = args.special

    run(path_corpus=path_corpus,
        path_vocab=path_vocab,
        prune_at=prune_at,
        min_count=min_count,
        special_words=special_words)

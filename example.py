# -*- coding: utf-8 -*-

import preprocess

def main():
    # Your own text
    sents = open("preprocess.py")
    sents = [s.decode("utf-8") for s in sents]
    
    # Preprocess
    sents = preprocess.preprocess_sentences(
                            sents,
                            lowercase=True,
                            replace_digits=True,
                            append_eos=True,
                            replace_rare=True,
                            prune_at=1000000,
                            min_count=0)
    

if __name__ == "__main__":
    main()

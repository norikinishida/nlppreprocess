# A Tool for Preprocessing Natural Language Text #

## 1. Required Package ##

- nltk

NLTK is required for tokenization. 

## 2. Setting ##

```
$ cd /path/to/hoge
$ git clone https://github.com/norikinishida/nlppreprocess.git
$ vim ~/.zshrc
```

Please add the following line in your .zshrc (or .bashrc, etc.).

```
export PYTHONPATH=/path/to/hoge/nlppreprocess:$PYTHONPATH
```

## 3. How to use ##

### Tokenization ###

```python
import nlppreprocess.tokenizer
nlppreprocess.tokenizer.run(
    "/path/to/raw/raw_0000.txt",
    "/path/to/outdir/raw_0000.txt.tokenized")
```

However, I recommend using the Stanford CoreNLP or PTBTokenizer to tokenize text.

### Lowercasing ###

```python
import nlppreprocess.lowercase
nlppreprocess.lowercase.run(
    "/path/to/outdir/raw_0000.txt.tokenized",
    "/path/to/outdir/raw_0000.txt.tokenized.lowercased")
```

### Replacing digit to '7' ###

e.g., 
    - before: "$ 150 million of 8.55 % senior notes due oct. 15 , 2009 ,"
    - after:  "$ 777 million of 7.77 % senior notes due oct. 77 , 7777 ,"

```python
import nlppreprocess.replace_digits
nlppreprocess.replace_digits.run(
    "/path/to/outdir/raw_0000.txt.tokenized.lowercased",
    "/path/to/outdir/raw_0000.txt.tokenized.lowercased.replace_digits")
```

### Building a vocabulary ###

1. Please concatenate the documents to build a vocabulary. Here, we assume that 8,000 documents ```/path/to/outdir/rar_{0000〜7999}.txt.tokenized.lowercased.replace_digits``` are to used for training.

```python
import nlppreprocess.concat

# Get a list of paths to training documents
filepaths = aggregate_training_paths() # => ["/path/to/outdir/raw_0000.txt.tokenized.lowercased.replace_digits", .., "/path/to/outdir/raw_7999.txt.tokenized.lowercased.replace_digits"]

# Concatenate them into a single file
nlppreprocess.concat.run(
    filepaths,
    "/path/to/outdir/concat.tokenized.lowercased.replace_digits")
```

2. Then, build a vocabulary.

```python
import nlppreprocess.create_vocabulary
nlppreprocess.create_vocabulary.run(
    "/path/to/outdir/concat.tokenized.lowercased.replace_digits",
    "path/to/outdir/vocab",
    prune_at=100000, # the maximum number of vocab. size
    min_count=5, # threshold for filtering rare word types
    special_words=[]) # to avoid removing special word types such as <EOS>
```

If you set special_words as ["A", "B", "C"], the built vocabulary contains these three word types in it.

### Replacing rare word types ###

Replace tokens that are not contained in the built vocabulary with "\<UNK\>"

```python
import nlppreprocess.replace_rare_words
path_in = "/path/to/outdir/raw_0000.txt.tokenized.lowercased.replace_digits"
path_out = "/path/to/outdir/raw_0000.txt.preprocessed"
path_vocab = "/path/to/outdir/vocab"
nlppreprocess.replace_rare_words.run(
    path_in, path_out, path_vocab)
```

### Other functions ###
    - nlppreprocess.append_eos: appends "\<EOS\>" at the end of each line
    - nlppreprocess.conll2lines: converts CoNLL-format files to sentence-by-sentence files
    - nlppreprocess.split_corpus: randomly splits a single corpus (i.e., a list of sentences) into train/dev files
    - nlppreprocess.convert_textlines_to_characters: convert a corpus to character sequences (e.g., "H e l l o <SPACE> w o r l d <EOL>")


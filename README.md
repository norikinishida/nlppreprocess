# A Tool for Preprocessing Natural Language Text #

## 1. Required Package ##

- nltk (optional)

NLTK is required for tokenization. 

## 2. Setting ##

```
$ cd /path/to/hoge
$ git clone https://github.com/norikinishida/textpreprocessor.git
$ vim ~/.zshrc
```

Please add the following line in your .zshrc (or .bashrc, etc.).

```
export PYTHONPATH=/path/to/hoge/textpreprocessor:$PYTHONPATH
```

## 3. How to use ##

Please check ```./run.sh``` to see examples.

Here, we assume that we have 10,000 English raw documents (i.e., raw_0000.txt〜raw_9999.txt) each of which consists of multiple sentences.

### Tokenization ###

```python
import textpreprocessor.tokenizer
textpreprocessor.tokenizer.run(
    "/path/to/raw/raw_0000.txt",
    "/path/to/outdir/raw_0000.txt.tokenized")
```

However, for tokenization, I recommend using the Stanford CoreNLP or PTBTokenizer in stead of NLTK.

```
$ python textpreprocessor/make_filelist.py --input_dir /path/to/raw --output_dir /path/to/outdir --filelist_name filelist.txt --begin raw --end txt
$ ./corenlp.sh /path/to/outdir/filelist.txt /path/to/outdir
```

These commands will generate CoNLL-format files ```/path/to/outdir/raw_{0000〜9999}.txt.conll```.

```python
import textpreprocessor.conll2lines
textpreprocessor.conll2lines.run(
    "/path/to/outdir/raw_0000.txt.conll",
    "/path/to/outdir/raw_0000.txt.tokenized")
```

### Lowercasing ###

```python
import textpreprocessor.lowercase
textpreprocessor.lowercase.run(
    "/path/to/outdir/raw_0000.txt.tokenized",
    "/path/to/outdir/raw_0000.txt.tokenized.lowercased")
```

### Replacing digit to '7' ###

e.g.,
- before: "$ 150 million of 8.55 % senior notes due oct. 15 , 2009 ,"
- after:  "$ 777 million of 7.77 % senior notes due oct. 77 , 7777 ,"

```python
import textpreprocessor.replace_digits
textpreprocessor.replace_digits.run(
    "/path/to/outdir/raw_0000.txt.tokenized.lowercased",
    "/path/to/outdir/raw_0000.txt.tokenized.lowercased.replace_digits")
```

### Building a vocabulary ###

1. Please concatenate the documents to build a vocabulary. Here, we assume that 8,000 documents ```/path/to/outdir/rar_{0000〜7999}.txt.tokenized.lowercased.replace_digits``` are to used for training.

```python
import textpreprocessor.concat

# Get a list of paths to training documents
filepaths = aggregate_training_paths() # => ["/path/to/outdir/raw_0000.txt.tokenized.lowercased.replace_digits", .., "/path/to/outdir/raw_7999.txt.tokenized.lowercased.replace_digits"]

# Concatenate them into a single file
textpreprocessor.concat.run(
    filepaths,
    "/path/to/outdir/concat.tokenized.lowercased.replace_digits")
```

2. Then, build a vocabulary.

```python
import textpreprocessor.create_vocabulary
textpreprocessor.create_vocabulary.run(
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
import textpreprocessor.replace_rare_words
path_in = "/path/to/outdir/raw_0000.txt.tokenized.lowercased.replace_digits"
path_out = "/path/to/outdir/raw_0000.txt.preprocessed"
path_vocab = "/path/to/outdir/vocab"
textpreprocessor.replace_rare_words.run(
    path_in, path_out, path_vocab)
```

### Other functions ###
    - textpreprocessor.append_eos:
        - appends "<EOS>" at the end of each line
    - textpreprocessor.split_corpus
        - randomly splits a single corpus (i.e., a list of sentences) into train/test files
    - textpreprocessor.convert_textlines_to_characters
        - convert a corpus to character sequences (e.g., "H e l l o <SPACE> w o r l d <EOL>")


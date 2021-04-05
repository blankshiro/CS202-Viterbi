# Demo of Convolutional Encoding and Viterbi Decoding

The demo relies on a convolutional encoding and viterbi decoding algorithm by xukmin. The dependency repository is stored as a gitmodule, hence the `viterbi` folder is empty. To pull the that repo dependency, run the following commands in the directory above.

```sh
# At the root directory above:
git init
git submodule update --init
cd demo/viterbi
make
cd ..
python3 demo.py "Hello World"
```

## References

* Convolutional encoding and Viterbi decoding algorithm: https://github.com/xukmin/viterbi

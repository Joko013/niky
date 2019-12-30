## Sample processor

### What is this?

A simple pandas data processor that takes an input *xlsx* file from  the `/data` folder,
crunches the samples and modifies *vystup.xlsx* file with an appropriate result.  

### How to run it?

#### Prerequisites

First, install all the dependencies into your environment.

```
$ pip install -r requirements.txt
```

#### Run it

Execute the `process.py` file with the input file name (without the `.xlsx` extension) as a positional argument.

```
$ python process.py test_input
```

Profit! (ᵔᴥᵔ)

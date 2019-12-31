## Sample processor

### What is this?

A simple pandas data processor that takes an input *xlsx* file from  the `/data` folder,
crunches the samples and modifies *vystup.xlsx* file with an appropriate result.  

### How to run it?

#### Prerequisites

First, clone this repository or download the code into your machine.

After that, install all the dependencies into your environment.

```
$ pip install -r requirements.txt
```

Copy the `vystup.xlsx` file to the `/data` folder. Make sure the name is `vystup.xlsx`,
the code outputs into the file with this exact name.

Fill the `/data` folder with the sample files you want to process.

#### Run it

Execute the `process.py` file with the input file name (without the `.xlsx` extension) as a positional argument.

```
$ python process.py test_input
```

Profit! (ᵔᴥᵔ)

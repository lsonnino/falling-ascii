# falling-ascii
 Displays falling characters on the console like in movies

![Screenshot 2021-10-12 at 18.38.55](screenshots/default.png)

## Usage

To run it, simply type:

```bash
python main.py
```

Options can be provided as well as follow:

```bash
python main.py [options]
```

### Options

The supported options are the following:

* `--change | -C`: The probability from 0 to 100 that a column of chars will disapear.
* `--cols  | -c`: The probability from 0 to 100 that a column of chars will appear.
* `--help  | -h | -H`: Displays the help page.
* `--speed  | -s | -S`: Set the speed of the text.

They can be provided in any order followed by the respective value. For instance:

```bash
python main.py --speed 20 -c 1
```

The default values are:

* --change: 20
* --cols: 2
* --speed: 10

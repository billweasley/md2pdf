md2pdf
------

Convert single markdown file to pdf.

What For
--------

I create it to help me create pdf version resumes.

There are a lot of tools to do this, I also used one of them (gimli) at first,
but I have to fix many unexcepted errors.

Requirements
------------

Wkhtmltopdf: 

```bash
# Ubuntu
sudo apt-get install wkhtmltopdf

# on OSX
brew tap homebrew/boneyard
brew install wkhtmltopdf

```

Install
--------

    pip install git+git://github.com/hit9/md2pdf.git@master

Usage
-----

```
Usage:
  md2pdf <filepath> [-s <stylesheet>] [-o <output>]
  md2pdf [-h|-v]

Options:
  -h --help         show help
  -v --version      show version
```

Example usage:

```
md2pdf file.md   # output to `file.pdf` with default stylesheet
```

```
md2pdf file.md -s style.css  # output to `file.pdf` with `style.css`
```

```
md2pdf file.md -s style.css -o out.pdf  # output to `out.pdf` with `style.css`
```

License
--------

[LICENSE-BSD](LICENSE-BSD)

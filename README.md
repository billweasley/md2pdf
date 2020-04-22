md2pdf
------

Convert single markdown file to pdf.

What For
--------

Supportive lib for creating pdf version resumes. Credit to @hit9

This version was adapted to Python 3 and hence cannot be compatible with Python 2.

Pre-Requirements
------------
- python 3 dev with distutils (```sudo apt-get install python3-distutils python3-dev```)
- pip
- build essentials for ```make``` command (```sudo apt-get install build-essential```)
- Wkhtmltopdf: 
```bash
# Ubuntu
sudo apt-get install xvfb libfontconfig wkhtmltopdf

# on OSX (not tested)
brew tap homebrew/boneyard
brew install wkhtmltopdf

```

Install the lib
--------

    pip install git+git://github.com/billweasley/md2pdf.git@master

Chinese (or Non-English language) Resume
--------
To produce the non-English resume, you need the system to support the corresponding language display.

For Chinese, there is a step-by-step gist [here](https://gist.github.com/BoWang816/c2e9ce52ce03c59450bcf587b7d0f456).
The main steps are here:

```

首先，安装中文支持包language-pack-zh-hans：

$ sudo apt-get install language-pack-zh-hans
然后，修改/etc/environment（在文件的末尾追加）：

LANG="zh_CN.UTF-8"
LANGUAGE="zh_CN:zh:en_US:en"
再修改/var/lib/locales/supported.d/local(没有这个文件就新建，同样在末尾追加)：

en_US.UTF-8 UTF-8
zh_CN.UTF-8 UTF-8
zh_CN.GBK GBK
zh_CN GB2312
最后，执行命令：

$ sudo locale-gen
对于中文乱码是空格的情况，安装中文字体解决。

$ sudo apt-get install fonts-droid-fallback ttf-wqy-zenhei ttf-wqy-microhei fonts-arphic-ukai fonts-arphic-uming
以上，问题解决，中文显示正常。:)

```

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

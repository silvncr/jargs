<!-- omit from toc -->
# jargs

simplifying args jargon

![[publish status](https://github.com/silvncr/jargs/actions/workflows/python-publish.yml)](https://img.shields.io/github/actions/workflow/status/silvncr/jargs/python-publish.yml)
![[latest release](https://github.com/silvncr/jargs/releases/latest)](https://img.shields.io/github/v/release/silvncr/jargs)

## Summary

Provides a simpler way to create commandline arguments.

> Works on Python 3.6 and above. Tested on Windows 10.

## Contents

- [Summary](#summary)
- [Contents](#contents)
- [The story behind jargs](#the-story-behind-jargs)
- [Usage](#usage)

## The story behind jargs

I was inspired to make this library while developing a commandline application. I needed to parse user input, which was easy enough until I reached the part where I took booleans as input, which broke it every time. The solution was to create a `BooleanAction` class to parse the booleans separately. I then thought that it shouldn't be necessary for every commandline tool developer to rewrite the same class. Thus, jargs was born; the solution to all of your confusion regarding commandline arguments.

## Usage

Simply create a `Parser` object, pass your arguments, and you're ready to use the outputs.

```py
from jargs import Argument, Parser

args = Parser(
    [
        Argument(
            name = 'one',
            type = bool,
            help = 'provide a boolean'
        ),
        Argument(
            name = 'two',
            type = str,
            multiple = True,
            help = 'provide one or more strings'
        ),
    ]
)()

if args.one:
    print(args.two)
```

# Lease Amendment Letter

[![Build status](https://ci.appveyor.com/api/projects/status/j7vu25s6t6pp7xod?svg=true)](https://ci.appveyor.com/project/lcamichigan/lease-amendment-letter)
[![Build Status](https://travis-ci.org/lcamichigan/lease-amendment-letter.svg?branch=master)](https://travis-ci.org/lcamichigan/lease-amendment-letter)

This is a collection of resources for creating letters describing amendments to
[Sigma Alumni Association](https://lcamichigan.com) leases.

## Contents

* [Getting Started](#getting-started)
  * [On Windows](#on-windows)
  * [On macOS](#on-macos)
* [How to Make a Letter](#how-to-make-a-letter)

## Getting Started

To make a letter, you need [LuaTeX](http://www.luatex.org) and
[Python](https://www.python.org). Both of these are free and cross-platform. You
also need the fonts
[Libertinus](https://github.com/libertinus-fonts/libertinus) and
[Gillius](http://arkandis.tuxfamily.org/adffonts.html). These are also free, and
you’ll get them automatically when you install LuaTeX.

### On Windows

The most reliable way to install LuaTeX is probably to install
[TeX Live](https://www.tug.org/texlive/). To install TeX Live, visit
https://www.tug.org/texlive/acquire-netinstall.html, and then download and run
install-tl-windows.exe. Note that installing TeX Live can take a few hours.

To install Python, visit https://www.python.org/downloads/windows/, and then
download and run an installer for the latest release of Python 2 or 3 (you can
use either version). Make sure you add python.exe to your Windows PATH when you
install Python.

To view a letter, you need a PDF viewer. On Windows 10, you can view PDF files
in the built-in
[Microsoft Edge](https://www.microsoft.com/en-us/windows/microsoft-edge)
browser. On Windows 7 and later, you can use
[Adobe Acrobat Reader](https://get.adobe.com/reader/) or
[Google Chrome](https://www.google.com/chrome/).

### On macOS

The easiest way to install LuaTeX is probably to install
[MacTeX](https://www.tug.org/mactex/). To install MacTeX, visit
https://tug.org/mactex/mactex-download.html, download MacTeX.pkg, and then
double-click MacTeX.pkg.

Python is included with macOS.

## How to Make a Letter

First, download this repository as a ZIP archive. To do this, click
[here](https://github.com/lcamichigan/lease-amendment-letter/archive/master.zip).
Unzip the archive wherever you wish.

To make a letter, you enter commands in PowerShell or Command Prompt on Windows,
or in Terminal on macOS. Open PowerShell or Command Prompt on Windows, or
Terminal on macOS, and then `cd` to the folder you just unzipped.

If you’re making a letter for the first time, enter

```sh
python init.py
```

This runs the Python script [init.py](init.py). This script creates an info.tex
file.

Now, enter in PowerShell:

```powershell
foreach ($i in 1..2) { lualatex Letter.tex }
```

or in Command Prompt:

```batch
for /l %G in (1, 1, 2) do lualatex Letter.tex
```

or in Terminal:

```sh
for i in {1..2}; do lualatex Letter.tex; done
```

This will create a PDF file of a letter using the information in info.tex.
You’ll see placeholder information in the letter. You must update info.tex with
information about the letter you’re making.

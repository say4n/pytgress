"""Indeterminate progress bars

- simple_spinner
- dots_spinner
- arrow_spinner
- bars_spinner
- bars_spinner_v
- bars_spinner_h
- lt_spinner
- triangle_spinner
- square_spinner
- circle_spinner_v1
- circle_spinner_v2
- circle_spinner_v3
- braille_spinner

author - Sayan Goswami
email - goswami [dot] sayan47+pygress [at] gmail [dot] com

======= 
LICENSE
=======

Copyright 2017 Sayan Goswami

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated 
documentation files (the "Software"), to deal in the Software without restriction, including without 
limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies 
of the Software, and to permit persons to whom the Software is furnished to do so, subject to the 
following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial 
portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT 
NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


class simple_spinner:
    """Simple indeterminate spinner"""

    def __init__(self):
        self.choices = ["–", "\\", "|", "/", "-", "\\", "|", "/"]
        self.progress = 0

    def update(self):
        """Update progress to next state"""
        self.progress += 1
        self.progress %= len(self.choices)

    def show(self):
        """Show current progress"""
        res = " " + self.choices[self.progress]
        print(res, end="\r")


class dots_spinner(simple_spinner):
    """Indeterminate dots spinner"""

    def __init__(self):
        super().__init__()
        self.choices = "⠁ ⠂ ⠄ ⡀ ⢀ ⠠ ⠐ ⠈".split(' ')


class arrow_spinner(simple_spinner):
    """Indeterminate arrows spinner"""

    def __init__(self):
        super().__init__()
        self.choices = "← ↖ ↑ ↗ → ↘ ↓ ↙".split(' ')


class bars_spinner_v(simple_spinner):
    """Indeterminate growing bars spinner"""

    def __init__(self):
        super().__init__()
        self.choices = "▁ ▂ ▃ ▄ ▅ ▆ ▇ █ ▇ ▆ ▅ ▄ ▃ ▁".split(' ')


class bars_spinner_h(simple_spinner):
    """Indeterminate shrinking bars spinner"""

    def __init__(self):
        super().__init__()
        self.choices = "▉ ▊ ▋ ▌ ▍ ▎ ▏ ▎ ▍ ▌ ▋ ▊ ▉".split(' ')


class bars_spinner(simple_spinner):
    """Indeterminate bars spinner"""

    def __init__(self):
        super().__init__()
        self.choices = "▖ ▘ ▝ ▗".split(' ')


class lt_spinner(simple_spinner):
    """Indeterminate box characters spinner"""

    def __init__(self):
        super().__init__()
        self.choices = "┤ ┘ ┴ └ ├ ┌ ┬ ┐".split(' ')


class triangle_spinner(simple_spinner):
    """Indeterminate triangular spinner"""

    def __init__(self):
        super().__init__()
        self.choices = "◢ ◣ ◤ ◥".split(' ')


class sqaure_spinner(simple_spinner):
    """Indeterminate square spinner"""

    def __init__(self):
        super().__init__()
        self.choices = "◰ ◳ ◲ ◱".split(' ')


class circle_spinner_v1(simple_spinner):
    """Indeterminate circular spinner #1"""

    def __init__(self):
        super().__init__()
        self.choices = "◴ ◷ ◶ ◵".split(' ')


class circle_spinner_v2(simple_spinner):
    """Indeterminate circular spinner #2"""

    def __init__(self):
        super().__init__()
        self.choices = "◐ ◓ ◑ ◒".split(' ')


class circle_spinner_v3(simple_spinner):
    """Indeterminate circular spinner #3"""

    def __init__(self):
        super().__init__()
        self.choices = "◡◡ ⊙⊙ ◠◠".split(' ')


class braille_spinner(simple_spinner):
    """Indeterminate braille dots spinner"""

    def __init__(self):
        super().__init__()
        self.choices = "⣾ ⣽ ⣻ ⢿ ⡿ ⣟ ⣯ ⣷".split(' ')

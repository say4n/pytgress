"""Determinate progress bars

- simple_bar
- arrrow_bar

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


class simple_bar:
    """Simple progress bar showing #s"""

    def __init__(self):
        self.maximum = None
        self.minimum = None
        self.progress = None
        self.bar = None
        self.indicator = "#"
        self.blank = " "
        self.length = 10

    def set_maximum(self, maximum):
        """Set upper bound of progress"""
        if not isinstance(maximum, (int, float)):
            raise TypeError("`maximum` must be numeric")
        else:
            self.maximum = maximum

    def set_minimum(self, minimum):
        """Set lower bound of progress"""
        if not isinstance(minimum, (int, float)):
            raise TypeError("`minimum` must be numeric")
        else:
            self.minimum = minimum

    def update_progress(self, progress):
        """Update self.progress to progress"""
        if not isinstance(progress, (int, float)):
            raise TypeError("`progress` value must be numeric")

        elif self.maximum is None:
            raise ValueError("`maximum` is None")

        elif self.minimum is None:
            raise ValueError("`minimum` is None")

        elif not self.minimum <= progress <= self.maximum:
            raise ValueError(
                "`progress` value must lie between `maximum` and `minimum`")

        else:
            self.progress = progress

    def set_filled(self, indicator):
        """Set the progress indicator"""
        self.indicator = indicator

    def set_blank(self, blank):
        """Set blank character"""
        self.blank = blank

    def set_length(self, length):
        if not isinstance(length, (int, float)):
            raise TypeError("`progress` value must be numeric")
        else:
            self.length = length

    def show(self):
        """Print current state of the progress bar"""
        total = self.length
        percent = self.progress / (self.maximum - self.minimum)
        current = int(total * percent)
        res = " [ " + self.indicator * current + self.blank * \
            (total - current) + " ]\t\t{:.2f}%".format(100 * percent)

        if (self.progress != self.maximum):
            print(res, end="\r")
        else:
            print(res, end="\n")


class arrow_bar(simple_bar):
    """Simple progress bar with an arrow head"""

    def __init__(self):
        super().__init__()
        self.indicator = "="
        self.arrow_head = ">"

    def set_arrow_head(self, arrow_head):
        """Set the arrow head"""
        self.arrow_head = arrow_head[0]

    def show(self):
        """Print current state of the progress bar"""
        total = self.length
        percent = self.progress / (self.maximum - self.minimum)
        current = int(total * percent)
        if 1 <= current < self.length:
            res = " [ " + self.indicator * (current - 1) + self.arrow_head + self.blank * (total - current) +\
                " ]\t\t{:.2f}%".format(100 * percent)
        else:
            res = " [ " + self.indicator * current + self.blank * (total - current) +\
                " ]\t\t{:.2f}%".format(100 * percent)

        if (self.progress != self.maximum):
            print(res, end="\r")
        else:
            print(res, end="\n")

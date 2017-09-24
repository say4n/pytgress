# PytGress

[![forthebadge](http://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com)

### What is PytGress?

PytGress is short for **Pyt**hon Pro**gress**, a library that helps you use fancy spinner for all your command line project needs.

It support both determinate and indeterminate progress bars, has sanity checks pre-included.

### How do I get it ?

Just use `pip install pytgress` !

### What do I get ?

- Indeterminate (No fixed upper & lower bounds)
    + simple_spinner
    + dots_spinner
    + arrow_spinner
    + bars_spinner
    + bars_spinner_v
    + bars_spinner_h
    + lt_spinner
    + triangle_spinner
    + square_spinner
    + circle_spinner_v1
    + circle_spinner_v2
    + circle_spinner_v3
    + braille_spinner
- Determinate (Fixed upper & lower bounds)
    + simple_bar
    + arrrow_bar

### How do I use them ?

#### Determinate

Simple progress bar

    from pytgress import determinate
    
    bar = determinate.simple_bar() 
    bar.set_maximum(100)    # required
    bar.set_minimum(0)      # required
    bar.set_filled("▇")     # optional (default : '=')
    bar.set_blank('▒')      # optional (default : ' ')
    bar.set_length(15)      # optional (default : 10)
    
    bar.update_progress(i)  # update progress
    bar.show()              # show bar

Progress bar with an arrow (Inherits `simple_bar`)

    from pytgress import determinate
    
    b = determinate.arrow_bar()
    b.set_maximum(100)      # required
    b.set_minimum(0)        # required
    b.set_arrow_head(">")   # optional (default : '>')
    
    b.update_progress(i)    # update progress
    b.show()                # show bar


#### Indeterminate

    from pytgress import indeterminate

    spinner = indeterminate.simple_spinner()
    
    spinner.update()        # update after each time-step
    spinner.show()          # show current state

All other spinner inherit from `simple_spinner`

Note : For more examples, see "tests.py".


### Where's the license ?

Copyright 2017 Sayan Goswami

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


### How do I contribute ?

Fork and hack away !


### TODO 
- [ ] Add colors
- [ ] ~Add more spinners~



Sayan   ✌🏼


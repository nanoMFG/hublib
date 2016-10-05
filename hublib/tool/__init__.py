from IPython.display import display, HTML
from IPython.core.magic import (register_line_magic, register_cell_magic,
                                register_line_cell_magic)

# HTML5 code for a button
input_form = "<button name=\"%s,%s\" class=\"continue_button\" onclick=\"IPython.wait_button_clicked()\">%s</button>"

@register_line_magic
def wait(line):
    """ Set a waitpoint.  Optional line should contain a
    button name and wait name seperated by a comma"""
    line = line.split(',')
    if len(line) == 0:
        name = 'Run'
        wname = 'Running'
    elif len(line) == 1:
        name = line
        wname = 'Running'
    else:
        name, wname = line
    button = input_form % (name, wname, name)
    display(HTML(button))


@register_line_magic
def waitdone(line):
    """
    Does nothing now.  Might have a button to Restart.
    """
    display(HTML('DONE'))

# We delete these to avoid name conflicts for automagic to work
del wait
del waitdone

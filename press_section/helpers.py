# Needed to fix the relative file paths in the outputted css.
# https://stackoverflow.com/questions/10423159/django-compressor-using-lessc-in-debug-mode/14842293#14842293?newreg=191fc05bb3f940b491d3262b423d8be0

from compressor.filters.base import CompilerFilter
from compressor.filters.css_default import CssAbsoluteFilter

class ScssFilter(CompilerFilter):
    def __init__(self, content, attrs, **kwargs):
        super(ScssFilter, self).__init__(content, command='sass --scss {infile} {outfile}', **kwargs)

    def input(self, **kwargs):
        content = super(ScssFilter, self).input(**kwargs)
        return CssAbsoluteFilter(content).input(**kwargs)

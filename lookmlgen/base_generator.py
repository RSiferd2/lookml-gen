"""
    File name: base_generator.py
    Author: joeschmid
    Date created: 4/8/17
"""
import abc
import six

DEFAULT_WARNING_HEADER_COMMENT = \
    """# STOP! This file was generated by an automated process.
# Any edits you make will be lost the next time it is
# re-generated.\n"""


class GeneratorFormatOptions(object):
    def __init__(self, indent_spaces=2, newline_between_items=True,
                 omit_default_field_type=True,
                 warning_header_comment=DEFAULT_WARNING_HEADER_COMMENT):
        self.indent_spaces = indent_spaces
        self.newline_between_items = newline_between_items
        self.omit_default_field_type = omit_default_field_type
        self.warning_header_comment = warning_header_comment


@six.add_metaclass(abc.ABCMeta)
class BaseGenerator:
    def __init__(
            self, file=None, format_options=GeneratorFormatOptions()):
        self.file = file
        self.format_options = format_options

    @abc.abstractmethod
    def generate_lookml(self, file=None, format_options=None):
        raise NotImplementedError(
            'You must implement the generate_lookml() method')

    @classmethod
    def __subclasshook__(cls, C):
        if cls is BaseGenerator:
            if any("generate_lookml" in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented
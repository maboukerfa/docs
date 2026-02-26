"""Custom validators for the core app."""

import emoji
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def sub_validator(value):
    """Validate that the sub is ASCII only."""
    if not value.isascii():
        raise ValidationError("Enter a valid sub. This value should be ASCII only.")


def validate_unicode_emoji(value):
    """
    Validate that the string contains exactly one Unicode emoji using the 'emoji' library.
    """
    # emoji.is_emoji(value) returns True if the string is a single emoji.
    # We also want to ensure no other characters are present.
    if not emoji.is_emoji(value):
        raise ValidationError(
            _("%(value)s is not a single valid Unicode emoji."),
            params={"value": value},
        )

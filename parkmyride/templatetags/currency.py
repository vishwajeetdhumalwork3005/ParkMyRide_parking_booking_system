from django import template
import locale

register = template.Library()


@register.filter
def inr(value):
    """Format a number as INR currency with ₹ symbol.

    Falls back to a simple formatting if locale isn't available.
    """
    try:
        # try using locale for grouping
        locale.setlocale(locale.LC_ALL, '')
        # ensure float
        amount = float(value)
        # format with grouping
        s = f"{amount:,.2f}"
        return f"₹{s}"
    except Exception:
        try:
            return f"₹{float(value):.2f}"
        except Exception:
            return value

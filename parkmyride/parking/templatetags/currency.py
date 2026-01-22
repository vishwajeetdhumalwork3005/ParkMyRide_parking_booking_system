from django import template
import locale

register = template.Library()


@register.filter
def inr(value):
    """Format a number as INR currency with ₹ symbol.

    Simple, locale-aware grouping when possible.
    """
    try:
        amount = float(value)
        s = f"{amount:,.2f}"
        return f"₹{s}"
    except Exception:
        try:
            return f"₹{float(value):.2f}"
        except Exception:
            return value

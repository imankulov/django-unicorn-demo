from django_unicorn.components import UnicornView


class WrapperView(UnicornView):
    value: int = 0

from django_unicorn.components import UnicornView


class BaseComponentView(UnicornView):
    array = ["first", "second", "third"]

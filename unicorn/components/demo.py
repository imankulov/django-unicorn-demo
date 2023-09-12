from django_unicorn.components import UnicornView


class DemoView(UnicornView):
    name: str = "test"

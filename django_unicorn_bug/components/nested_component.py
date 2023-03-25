from django_unicorn.components import UnicornView


class NestedComponentView(UnicornView):
    def test_action(self):
        print("TEST ACTION")

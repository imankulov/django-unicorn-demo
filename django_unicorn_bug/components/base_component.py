from django_unicorn.components import UnicornView


class BaseComponentView(UnicornView):
    array = ["first", "second", "third"]
    display = False

    def test_action(self):
        print("TEST ACTION")

    def add_array(self):
        self.display = [1, 2, 3]
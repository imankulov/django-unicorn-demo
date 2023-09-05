from django_unicorn.components import UnicornView


class ButtonView(UnicornView):

    def increment(self):
        self.parent.value += 1

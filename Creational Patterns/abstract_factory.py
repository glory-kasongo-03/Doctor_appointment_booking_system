class WebButton:
    def render(self):
        return "Rendered Web Button"

class MobileButton:
    def render(self):
        return "Rendered Mobile Button"

class WebUIFactory:
    def create_button(self):
        return WebButton()

class MobileUIFactory:
    def create_button(self):
        return MobileButton()

# Abstract Factory usage
def render_ui(factory):
    button = factory.create_button()
    print(button.render())

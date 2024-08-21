import toga

def build(app):
    main_box = toga.Box()

    display = toga.Label('0', style=toga.style.Pack(font_size=50, alignment='left'))
    main_box.add(display)

    button_container = toga.Box()
    for button_text in ['7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', '.', '+', '=']:
        button = toga.Button(button_text, on_press=lambda widget: button_pressed(widget, display))
        button_container.add(button)
    main_box.add(button_container)

    main_window = toga.Window(title='Calculator')
    main_window.content = main_box

    return main_window

def button_pressed(widget, display):
    button_text = widget.label
    if button_text == '=':
        try:
            result = str(eval(display.text))
            display.text = result
        except:
            display.text = 'Error'
    elif button_text == 'C':
        display.text = '0'
    else:
        if display.text == '0':
            display.text = button_text
        else:
            display.text += button_text

def main():
    app = toga.App('Calculator', 'org.beeware.calculator')
    main_window = build(app)
    main_window.show()
    return app.main_loop()

if __name__ == '__main__':
    main()
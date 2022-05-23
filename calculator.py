from kivy.app import App
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from Useful_files.useful_functions import FloatPointGuard

# Builder.load_file('./calculator.kv')
Window.size = (550, 550)

class CalculatorWidget(Widget):
    counter = ''
    def clear(self):
        self.ids.input_box.text = '0'
        self.ids.result_box.text = '0'

    def button_value(self, number):
        prev_number = self.ids.input_box.text
        if len(prev_number) < 13:
            if prev_number == '0':
                self.ids.input_box.text = ''
                self.ids.input_box.text = f'{number}'
            else:
                self.ids.input_box.text = f'{prev_number}{number}'
        else:
            pass

    def signs(self, sign):
        global counter
        prev_number = self.ids.input_box.text
        self.ids.input_box.text = f'{prev_number}{sign}'
        counter = self.ids.input_box.text
        print(counter)
        self.ids.input_box.text = ''

    def remove_last(self):
        prev_number = self.ids.input_box.text
        prev_number = prev_number[:-1]
        self.ids.input_box.text = prev_number

    def print_result(self):
        global counter
        final_num = ''
        counter = counter + self.ids.input_box.text
        try:
            result = str(eval(counter))
            if len(result) > 13:
                for n in range(0, 14):
                    final_num = final_num + result[n]
            else:
                final_num = result
            self.ids.result_box.text = (FloatPointGuard.fix_float(final_num))
        except ValueError as e:
            self.ids.input_box.text = 'Error'
        except SyntaxError as e:
            self.ids.input_box.text = 'Error'
        except ZeroDivisionError as e:
            print(str(e))
            self.ids.input_box.text = str(e)

    def invert(self):
        number = self.ids.input_box.text
        if number[:1] != '-':
            number = f'-{number}'
        elif number[:1] == '-':
            number = number[1:]
        self.ids.input_box.text = number

class CalculatorApp(App):
    def build(self):
        return CalculatorWidget()

if __name__ == '__main__':
    CalculatorApp().run()
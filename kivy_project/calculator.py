from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
# from kivy.properties import ObjectProperty

Builder.load_file('calc.kv')
Window.size = (500,700)

class Mycalculator(Widget):
    #number press functoins
    def button_fun(self,button):
        pers = self.ids.calc.text
        if pers == "Error":
            pers = ''
        if pers == "0":
            self.ids.calc.text = ''    
            self.ids.calc.text = f'{button}' 
        else:
            self.ids.calc.text = f'{pers}{button}'   

    #clear function 
    def Cls(self):
        self.ids.calc.text = '0'

    # funtionality of addition
    def oprations(self, sign):
        pers = self.ids.calc.text
        self.ids.calc.text = f'{pers}{sign}'

    # remove funtion
    def remove(self):
        pers = self.ids.calc.text
        pers = pers[:-1]
        self.ids.calc.text = pers

    # dot funtion
    def dot(self):
        pers = self.ids.calc.text
        num_list = pers.split("+")
        if "+" in pers and "." not in num_list[-1]:
             self.ids.calc.text = f'{pers}.'
        elif "." in pers:
            pass
        else:
            self.ids.calc.text = f'{pers}.'

    # positive to negative number
    def pos_neg(self):
        pers = self.ids.calc.text
        if "-" in pers:
            self.ids.calc.text = f'{pers.replace("-","")}'
        else:
            self.ids.calc.text = f"-{pers}"

    # funtionality of equals
    def equals(self):
        pers = self.ids.calc.text
        # Error handling
        try:
            # Evaluate the math from the text box
            ans = eval(pers)
            #print the output in text box
            self.ids.calc.text = str(ans)
        except:
           self.ids.calc.text = str("Error") 


# runing the App 
class Calc(App):
    def build(self):
        # Window.clearcolor = (1,1,1,1) #for color the screen of windows
        return Mycalculator()


if __name__ == '__main__':
    Calc().run()
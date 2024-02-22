from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
# from kivy.properties import ObjectProperty

Builder.load_file('kivy.kv')
Window.size = (500,700)

class MyGrid(Widget):
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

        # # Addition
        # if "+" in pers:
        #     num_list = pers.split("+")
        #     ans = 0.0
        #     for num in num_list:
        #         ans += float(num)
        #     self.ids.calc.text = str(ans)
        # if "-" in pers:
        #     num_list = pers.split("-")
        #     ans = 0
        #     for num in num_list:
        #         ans -= int(num)
        #     self.ids.calc.text = str(ans)
            


######################################################
    # def press(self):
    #     name = self.ids.name_input.text
    #     print(name)
    #     self.ids.name_label.text = name
    #     self.ids.name_input.text = ''
######################################################
    # name = ObjectProperty(None)
    # age = ObjectProperty(None)
    # year = ObjectProperty(None)
    # def press(self):
    #     name = self.name.text
    #     age = self.age.text
    #     year = self.year.text
    #     #print message
    #     print(f'hello {name}')
    #     #clear text from screen
    #     self.name.text = ""
    #     self.name.age = ""
    #     self.name.year = ""

class KivyApp(App):
    def build(self):
        # Window.clearcolor = (1,1,1,1) #for color the screen of windows
        return MyGrid()


if __name__ == '__main__':
    KivyApp().run()
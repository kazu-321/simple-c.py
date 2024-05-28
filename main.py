CODE=[
"int a;",
"int b=10;",
"a=a+10;"
]

class compiler:
    def __init__(self):
        self.V_NAMES=[]
        self.V_TYPES=[]
        self.V_VALUE=[]
        self.OPERATION=["=","+","-","*","/","%"]
        self.COMPILE_LINE=1
        self.COMPILE_NOW=1

    def initialize_compiler(self):
        self.V_NAMES=[]
        self.V_TYPES=[]
        self.V_VALUE=[]
        self.OPERATION=["=","+","-","*","/","%"]
        self.COMPILE_LINE=1
        self.COMPILE_NOW=1

    def initialize_variable(self,V_TYPES,V_NAMES):
        if V_NAMES not in self.V_NAMES:
            self.V_TYPES.append(V_TYPES)
            self.V_NAMES.append(V_NAMES)
            self.V_VALUE.append()
    
    def assignment(self,V_NAMES,v_value):
        if V_NAMES in self.V_NAMES:
            self.V_VALUE[self.V_NAMES.find(V_NAMES)]=v_value
    
    def remote_variable(self,V_NAMES):
        rm=self.V_NAMES.find(V_NAMES)
        if len(self.V_NAMES)>rm:
            self.V_TYPES[rm]=self.V_TYPES[len(self.V_TYPES)]
            self.V_NAMES[rm]=self.V_NAMES[len(self.V_NAMES)]
            self.V_VALUE[rm]=self.V_VALUE[len(self.V_VALUE)]
        self.V_TYPES[len(self.V_TYPES)].pop(-1)
        self.V_NAMES[len(self.V_NAMES)].pop(-1)
        self.V_VALUE[len(self.V_VALUE)].pop(-1)
        
    

            

    def compile(self):
        self.initialize_compiler()

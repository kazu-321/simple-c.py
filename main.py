CODE=[
"int a;",
"int b=10;",
"a=a+10;"
]
# I have to convert this program to scratch.mit.edu.
# So, I must use easy(decreased in scratch) code.
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
        self.COMPILE_LINE=0
        self.COMPILE_NOW=0

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

    def increase(self,V_NAMES):
        self.assignment(V_NAMES,self.V_VALUE[self.V_NAMES.find(V_NAMES)]+1)

    def substr(self,value,start,end,return_variable):
        self.initialize_variable("int","__substr.counter")
        self.assignment("__substr.counter",start)
        self.assignment(return_variable,"")
        for _ in range(end-start+1):
            self.assignment(self.V_VALUE[self.V_NAMES.find(return_variable)],self.V_VALUE[self.V_NAMES.find(return_variable)]+value[self.V_VALUE[self.V_NAMES.find("__substr.counter")]])
            self.increase("__substr.counter")
        self.remote_variable("__substr.counter")

    def findchar(self,value,char,return_variable):
        self.initialize_variable("int","__findchar.counter")
        self.assignment("__findchar.counter",0)
        self.assignment(return_variable,-1)
        for _ in value:
            if value[self.V_VALUE[self.V_NAMES.find("__findchar.counter")]]==char:
                self.assignment(return_variable,self.V_VALUE[self.V_NAMES.find("__findchar.counter")])
                return
            self.increase("__findchar.counter")
        self.remote_variable("__findchar.counter")

    def is_string(self,value,return_variable):
        if value[0]=='"' and value[len(value)-1]=='"':
            self.assignment(return_variable,1)
        else:
            self.assignment(return_variable,0)
    
    def is_int(self,value,return_variable):
        
    def evaluate(self,value):
        self.initialize_variable("int","__evaluate.is_string")
        if self.is_string(value,"__evaluate.is_string")==1:
            self.substr(value,1,len(value)-2,value)
            self.remote_variable("__evaluate.is_string")
            return
        self.remote_variable("__evaluate.is_string")


    def compile_line(self,code):
        self.initialize_variable("int","__compile_line.counter")
        self.assignment("__compile_line.counter",0)
        for _ in range(len(self.OPERATION)):
            if self.OPERATION[self.V_VALUE[self.V_NAMES.find("__compile_line.counter")]] in code:
                self.initialize_variable("int","__compile_line.op_index")
                self.findchar(code,self.OPERATION[self.V_VALUE[self.V_NAMES.find("__compile_line.counter")]],"__compile_line.op_index")
                self.initialize_variable("int","__compile_line.var1")
                self.initialize_variable("int","__compile_line.var2")
                self.substr(code,0,self.V_VALUE[self.V_NAMES.find("__compile_line.op_index")],"__compile_line.var1")
                self.substr(code,self.V_VALUE[self.V_NAMES.find("__compile_line.op_index")]+1,len(code),"__compile_line.var2")

            self.increase("__compile_line.counter")
            

    def compile(self):
        self.initialize_compiler()

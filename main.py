CODE=[
"int a;",
"int b;",
"b=10;",
"a=b+10;"
]
# I have to convert this program to scratch.mit.edu.
# So, I must use easy(decreased in scratch) code.
class compiler:
    def __init__(self):
        self.initialize_compiler()

    def initialize_compiler(self):
        self.V_NAMES=[]
        self.V_TYPES=[]
        self.V_VALUE=[]
        self.OPERATIONS=["=","+","-","*","/","%"]
        self.TYPES=["int","string","float","double","char"]
        self.FUNKS=["printf","scanf","if","while","for","switch","case","break","continue","return","else"]
        self.COMPILE_LINE=0
        self.COMPILE_NOW=0

    def initialize_variable(self,V_TYPES,V_NAMES):
        if V_NAMES not in self.V_NAMES:
            self.V_TYPES.append(V_TYPES)
            self.V_NAMES.append(V_NAMES)
            self.V_VALUE.append(None)
    
    def assignment(self,V_NAMES,v_value):
        if V_NAMES in self.V_NAMES:
            self.V_VALUE[self.V_NAMES.index(V_NAMES)]=v_value
    
    def remove_variable(self,V_NAMES):
        rm=self.V_NAMES.index(V_NAMES)
        if len(self.V_NAMES)>rm:
            self.V_TYPES[rm]=self.V_TYPES[len(self.V_TYPES)-1]
            self.V_NAMES[rm]=self.V_NAMES[len(self.V_NAMES)-1]
            self.V_VALUE[rm]=self.V_VALUE[len(self.V_VALUE)-1]
        self.V_TYPES.pop(-1)
        self.V_NAMES.pop(-1)
        self.V_VALUE.pop(-1)

    def increase(self,V_NAMES):
        self.assignment(V_NAMES,self.V_VALUE[self.V_NAMES.index(V_NAMES)]+1)

    def substr(self,value,start,end,return_variable):
        self.initialize_variable("int","__substr.counter")
        self.assignment("__substr.counter",start)
        self.assignment(return_variable,"")
        for _ in range(end-start+1):
            self.assignment(self.V_VALUE[self.V_NAMES.index(return_variable)],self.V_VALUE[self.V_NAMES.index(return_variable)]+value[self.V_VALUE[self.V_NAMES.index("__substr.counter")]])
            self.increase("__substr.counter")
        self.remove_variable("__substr.counter")

    def indexchar(self,value,char,return_variable):
        self.initialize_variable("int","__indexchar.counter")
        self.assignment("__indexchar.counter",0)
        self.assignment(return_variable,-1)
        for _ in value:
            if value[self.V_VALUE[self.V_NAMES.index("__indexchar.counter")]]==char:
                self.assignment(return_variable,self.V_VALUE[self.V_NAMES.index("__indexchar.counter")])
                return
            self.increase("__indexchar.counter")
        self.remove_variable("__indexchar.counter")
    
    def indexstr(self,value,str,return_variable):
        self.initialize_variable("int","__indexstr.counter")
        self.assignment("__indexstr.counter",0)
        self.assignment(return_variable,-1)
        self.initialize_variable("string","__indexstr.sub")
        for _ in range(len(value)-len(str)):
            self.substr(value,self.V_VALUE[self.V_NAMES.index("__indexstr.counter")],len(str),"__indexstr.sub")
            if self.V_VALUE[self.V_NAMES.index("__indexstr.sub")]==str:
                self.assignment(return_variable,self.V_VALUE[self.V_NAMES.index("__indexstr.counter")])
                self.remove_variable("__indexstr.counter")
                self.remove_variable("__indexstr.sub")
                return
            self.increase("__indexstr.counter")
        self.remove_variable("__indexstr.counter")
        self.remove_variable("__indexstr.sub")

    def is_string(self,value,return_variable):
        if value[0]=='"' and value[len(value)-1]=='"':
            self.assignment(return_variable,1)
        else:
            self.assignment(return_variable,0)
    
    def is_int(self,value,return_variable):
        if value[0] in "-0123456789":
            self.initialize_variable("int","__is_int.counter")
            self.assignment("__is_int.counter",0)
            for _ in range(len(value)-1):
                if value[self.V_VALUE[self.V_NAMES.index("__is_int.counter")]] not in "0123456789":
                    self.assignment(return_variable,0)
                    self.remove_variable("__is_int.counter")
                    return
                self.increase("__is_int.counter")
            self.assignment(return_variable,1)
            self.remove_variable("__is_int.counter")
        else:
            self.assignment(return_variable,0)   

    def is_variable(self,value,return_variable):
        if value[0] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            self.initialize_variable("int","__is_variable.counter")
            self.assignment("__is_variable.counter",0)
            for _ in range(len(value)-2):
                if value[self.V_VALUE[self.V_NAMES.index("__is_variable.counter")]] not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-.":
                    self.assignment(return_variable,0)
                    self.remove_variable("__is_variable.counter")
                    return
                self.increase("__is_variable.counter")
            self.assignment(return_variable,1)
            self.remove_variable("__is_variable.counter")
            if value[len(value)] not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
                self.assignment(return_variable,0)
                self.remove_variable("__is_variable.counter")
                return
            self.assignment(return_variable,1)
            self.remove_variable("__is_variable.counter")
            return
        self.assignment(return_variable,0)
        self.remove_variable("__is_variable.counter")
    
    def operation(self,value1,value2,op,return_variable):
        self.initialize_variable("int","__operation.counter")
        self.assignment("__operation.counter",0)
        for _ in range(len(self.OPERATIONS)):
            if self.OPERATIONS[self.V_VALUE[self.V_NAMES.index("__operation.counter")]]==op:
                if op=="=":
                    self.assignment(value1,value2)
                    self.remove_variable("__operation.counter")
                    return
                if op=="+":
                    self.assignment(return_variable,value1+value2)
                    self.remove_variable("__operation.counter")
                    return
                if op=="-":
                    self.assignment(return_variable,value1-value2)
                    self.remove_variable("__operation.counter")
                    return
                if op=="*":
                    self.assignment(return_variable,value1*value2)
                    self.remove_variable("__operation.counter")
                    return
                if op=="/":
                    self.assignment(return_variable,value1/value2)
                    self.remove_variable("__operation.counter")
                    return
                if op=="%":
                    self.assignment(return_variable,value1%value2)
                    self.remove_variable("__operation.counter")
                    return
            self.increase("__operation.counter")
        self.remove_variable("__operation.counter")

    def evaluate(self,value,id,return_variable):
        self.initialize_variable("int","__evaluate.is_int")
        self.is_int(value,"__evaluate.is_int")
        if self.V_VALUE[self.V_NAMES.index("__evaluate.is_int")]==1:
            self.assignment(return_variable,int(value))
            self.remove_variable("__evaluate.is_int")
            return
        self.remove_variable("__evaluate.is_int")
        self.initialize_variable("int","__evaluate.is_string")
        self.is_string(value,"__evaluate.is_string")
        if self.V_VALUE[self.V_NAMES.index("__evaluate.is_string")]==1:
            self.substr(value,1,len(value)-2,return_variable)
            self.remove_variable("__evaluate.is_string")
            return
        self.remove_variable("__evaluate.is_string")
        self.initialize_variable("int","__evaluate.is_variable")
        self.is_variable(value,"__evaluate.is_variable")
        if self.V_VALUE[self.V_NAMES.index("__evaluate.is_variable")]==1:
            if value in self.V_NAMES:
                self.assignment(return_variable,self.V_VALUE[self.V_NAMES.index(value)])
                self.remove_variable("__evaluate.is_variable")
                return
            self.remove_variable("__evaluate.is_variable")
            return
        self.remove_variable("__evaluate.is_variable")
        self.initialize_variable("int","__evaluate.operation_counter"+str(id))
        self.assignment("__evaluate.operation_counter"+str(id),0)
        for _ in range(len(self.OPERATIONS)):
            if self.OPERATIONS[self.V_VALUE[self.V_NAMES.index("__evaluate.operation_counter"+str(id))]] in value:
                self.initialize_variable("string","__evaluate.value1"+str(id))
                self.initialize_variable("string","__evaluate.value2"+str(id))
                self.initialize_variable("int","__evaluate.op_index" +str(id))
                self.indexchar(value,self.OPERATIONS[self.V_VALUE[self.V_NAMES.index("__evaluate.operation_counter")]],"__evaluate.op_index"+str(id))
                self.substr(value,0,self.V_VALUE[self.V_NAMES.index("__evaluate.op_index"+str(id))],"__evaluate.value1"+str(id))
                self.substr(value,self.V_VALUE[self.V_NAMES.index("__evaluate.op_index"+str(id))]+1,len(value),"__evaluate.value2"+str(id))
                self.evaluate(self.V_VALUE[self.V_NAMES.index("__evaluate.value1"+str(id))],id+1,"__evaluate.value1"+str(id))
                self.evaluate(self.V_VALUE[self.V_NAMES.index("__evaluate.value2"+str(id))],id+1,"__evaluate.value2"+str(id))
                self.operation(self.V_VALUE[self.V_NAMES.index("__evaluate.value1"+str(id))],self.V_VALUE[self.V_NAMES.index("__evaluate.value2"+str(id))],self.OPERATIONS[self.V_VALUE[self.V_NAMES.index("__evaluate.operation_counter"+str(id))]],return_variable)
                self.remove_variable("__evaluate.value1"+str(id))
                self.remove_variable("__evaluate.value2"+str(id))
                self.remove_variable("__evaluate.op_index"+str(id))
                self.remove_variable("__evaluate.operation_counter"+str(id))
                return
            self.increase("__evaluate.operation_counter"+str(id))
        self.remove_variable("__evaluate.operation_counter"+str(id))


    def compile_line(self,code):
        self.initialize_variable("int","__compile.types_counter")
        self.assignment("__compile.types_counter",0)
        self.initialize_variable("string","__compile.code_sub")
        for _ in range(len(self.TYPES)):
            self.substr(code,0,len(self.OPERATIONS[self.V_VALUE[self.V_NAMES.index("__compile.types_counter")]])+1,"__compile.code_sub")
            if self.V_VALUE[self.V_NAMES.index("__compile.code_sub")]==self.OPERATIONS[self.V_VALUE[self.V_NAMES.index("__compile.types_counter")]]+" ":
                self.initialize_variable("string","__compile.variable")
                if "=" in code:
                    pass
                self.substr(code,len(self.OPERATIONS[self.V_VALUE[self.V_NAMES.index("__compile.types_counter")]])+1,len(code),"__compile.variable")
                self.initialize_variable(self.OPERATIONS[self.V_VALUE[self.V_NAMES.index("__compile.types_counter")]],self.V_VALUE[self.V_NAMES.index("__compile.variable")])
                self.remove_variable("__compile.variable")
                self.remove_variable("__compile.code_sub")
                self.remove_variable("__compile.types_counter")
                return
            self.increase("__compile.types_counter")
        self.evaluate(code,0,"")

    def compile(self):
        global CODE
        self.initialize_compiler()
        self.initialize_variable("int","__compile.counter")
        self.assignment("__compile.counter",0)
        for _ in range(len(CODE)):
            self.compile_line(CODE[self.V_VALUE[self.V_NAMES.index("__compile.counter")]])
            self.increase("__compile.counter")
        self.remove_variable("__compile.counter")

c=compiler()
c.compile()
print(c.V_NAMES)
print(c.V_VALUE)
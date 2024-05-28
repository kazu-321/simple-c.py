CODE=[
"int a;",
"int b=10;",
"a=a+10;"
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
        self.OPERATION=["=","+","-","*","/","%"]
        self.TYPES=["int","string","float","double","char"]
        self.FUNKS=["printf","scanf","if","while","for","switch","case","break","continue","return","else"]
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
    
    def remove_variable(self,V_NAMES):
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
        self.remove_variable("__substr.counter")

    def findchar(self,value,char,return_variable):
        self.initialize_variable("int","__findchar.counter")
        self.assignment("__findchar.counter",0)
        self.assignment(return_variable,-1)
        for _ in value:
            if value[self.V_VALUE[self.V_NAMES.find("__findchar.counter")]]==char:
                self.assignment(return_variable,self.V_VALUE[self.V_NAMES.find("__findchar.counter")])
                return
            self.increase("__findchar.counter")
        self.remove_variable("__findchar.counter")
    
    def findstr(self,value,str,return_variable):
        self.initialize_variable("int","__findstr.counter")
        self.assignment("__findstr.counter",0)
        self.assignment(return_variable,-1)
        self.initialize_variable("string","__findstr.sub")
        for _ in range(len(value)-len(str)):
            self.substr(value,self.V_VALUE[self.V_NAMES.find("__findstr.counter")],len(str),"__findstr.sub")
            if self.V_VALUE[self.V_NAMES.find("__findstr.sub")]==str:
                self.assignment(return_variable,self.V_VALUE[self.V_NAMES.find("__findstr.counter")])
                self.remove_variable("__findstr.counter")
                self.remove_variable("__findstr.sub")
                return
            self.increase("__findstr.counter")
        self.remove_variable("__findstr.counter")
        self.remove_variable("__findstr.sub")

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
                if value[self.V_VALUE[self.V_NAMES.find("__is_int.counter")]] not in "0123456789":
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
                if value[self.V_VALUE[self.V_NAMES.find("__is_variable.counter")]] not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-.":
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
        for _ in range(len(self.OPERATION)):
            if self.OPERATION[self.V_VALUE[self.V_NAMES.find("__operation.counter")]]==op:
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
        if self.V_VALUE[self.V_NAMES.find("__evaluate.is_int")]==1:
            self.assignment(return_variable,int(value))
            self.remove_variable("__evaluate.is_int")
            return
        self.remove_variable("__evaluate.is_int")
        self.initialize_variable("int","__evaluate.is_string")
        self.is_string(value,"__evaluate.is_string")
        if self.V_VALUE[self.V_NAMES.find("__evaluate.is_string")]==1:
            self.substr(value,1,len(value)-2,return_variable)
            self.remove_variable("__evaluate.is_string")
            return
        self.remove_variable("__evaluate.is_string")
        self.initialize_variable("int","__evaluate.is_variable")
        self.is_variable(value,"__evaluate.is_variable")
        if self.V_VALUE[self.V_NAMES.find("__evaluate.is_variable")]==1:
            if value in self.V_NAMES:
                self.assignment(return_variable,self.V_VALUE[self.V_NAMES.find(value)])
                self.remove_variable("__evaluate.is_variable")
                return
            self.remove_variable("__evaluate.is_variable")
            return
        self.remove_variable("__evaluate.is_variable")
        self.initialize_variable("int","__evaluate.operation_counter"+str(id))
        self.assignment("__evaluate.operation_counter"+str(id),0)
        for _ in range(len(self.OPERATION)):
            if self.OPERATION[self.V_VALUE[self.V_NAMES.find("__evaluate.operation_counter"+str(id))]] in value:
                self.initialize_variable("string","__evaluate.value1"+str(id))
                self.initialize_variable("string","__evaluate.value2"+str(id))
                self.initialize_variable("int","__evaluate.op_index" +str(id))
                self.findchar(value,self.OPERATION[self.V_VALUE[self.V_NAMES.find("__evaluate.operation_counter")]],"__evaluate.op_index"+str(id))
                self.substr(value,0,self.V_VALUE[self.V_NAMES.find("__evaluate.op_index"+str(id))],"__evaluate.value1"+str(id))
                self.substr(value,self.V_VALUE[self.V_NAMES.find("__evaluate.op_index"+str(id))]+1,len(value),"__evaluate.value2"+str(id))
                self.evaluate(self.V_VALUE[self.V_NAMES.find("__evaluate.value1"+str(id))],id+1,"__evaluate.value1"+str(id))
                self.evaluate(self.V_VALUE[self.V_NAMES.find("__evaluate.value2"+str(id))],id+1,"__evaluate.value2"+str(id))
                self.operation(self.V_VALUE[self.V_NAMES.find("__evaluate.value1"+str(id))],self.V_VALUE[self.V_NAMES.find("__evaluate.value2"+str(id))],self.OPERATION[self.V_VALUE[self.V_NAMES.find("__evaluate.operation_counter"+str(id))]],return_variable)
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
        for _ in range(len(self.TYPES)):
            if self.TYPES[self.V_VALUE[self.V_NAMES.find("__compile.types_counter")]] in code:
                self.initialize_variable("string","__compile.variable")
                self.initialize_variable("string","__compile.value")
                self.initialize_variable("int","__compile.variable_index")
                self.findstr
                self.evaluate(self.V_VALUE[self.V_NAMES.find("__compile.variable")],0,"__compile.value")
                self.initialize_variable(self.TYPES[self.V_VALUE[self.V_NAMES.find("__compile.types_counter")]],self.V_VALUE[self.V_NAMES.find("__compile.variable")])
                self.assignment(self.V_VALUE[self.V_NAMES.find("__compile.variable")],self.V_VALUE[self.V_NAMES.find("__compile.value")])
                self.remove_variable("__compile.variable")
                self.remove_variable("__compile.value")
                self.remove_variable("__compile.variable_index")
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
            self.compile_line(CODE[self.V_VALUE[self.V_NAMES.find("__compile.counter")]])
            self.increase("__compile.counter")
        self.remove_variable("__compile.counter")

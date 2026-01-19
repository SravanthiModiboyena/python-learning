# Dictionary stores data in key:value pairs

student={"name":"Shasra","age":24,"course":"DataAnalyst"}
# student is a dictionary

print(student) # {'name':'Shasra', 'age':24,'course':'DataAnalyst'}
print(student.keys()) # (['name','age','course'])
print(student.values()) # (['Shasra',24,'DataAnalyst'])
print(student.items()) # ([('name','Shasra'),('age',24),('course','DataAnalyst')])
print(student.get("age")) # 24
print(student.get("salary")) # none
student.update({"age": 25,"city":"Venkatagiri"})
print(student) # {'name':'Shasra','age':25,'course':'DataAnalyst','city':'Venkatagiri'}



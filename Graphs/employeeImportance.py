"""
return the importance of an employee: own importance + importance of all subordinates

emp[0]: employee.id
emp[1]: employee.importance
emp[2]: employee.subordinates

"""

employees = [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]

def getImportance(emp, id):
    employee_dict = {}
    for emp in employees:
        employee_dict[emp[0]] = [emp[1], emp[2]]

    def dfs(id, emp_dict):
        imp = emp_dict[id][0]
        for subs in emp_dict[id]:
            imp += dfs(subs, emp_dict)
        return imp

    res = dfs(id, employee_dict)
    return res
id = 1
res = getImportance(employees, id)
print(res)


# [1: [5, [2, 3]]]
# [2: [3, []]]
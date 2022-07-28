from . import Expense

class BudgetList():
    
    def __inti__(self, budget):
        self.budget=budget
        self.sum_expenses=0
        self.expenses=[]
        self.sum_overages=0
        self.overages=[]
    
    def __len__(self):
        return self.expenses+self.overages

    def append(self, item):
        if self.sum_expenses+item<self.budget:
            self.expenses.append(item)
            self.expenses+=item
        else:
            self.overages.append(item)
            self.overages+=item

def main():
    myBudgetList=BudgetList(1200)
    expenses=Expense.Expenses()
    expenses.read_expenses("data/spending_data.csv")
    for expense in expenses.list:
        expense.amount.append(myBudgetList)
        print('The count of all expenses: '+str(len(myBudgetList)))

if __name__=="__main__":
    main()
class BankAccount:
    # __accountBalance; # public access modifier - Can be accessible from anywhere.
    # _customerId; # protected access modifier - Can be accessible by the child classes.
    # accountNumber; # private access modifier
    # accountHolderName; # private access modifier - Can be accessible only within the class.
    # minBalanceRequired; # private access modifier

    def __init__(self, *args):
        # default constructor
        if len(args) == 0:
            print("Executing the default constructor")
        # parameterized constructor
        elif len(args) == 5:
            self.__accountNumber = args[0]
            self.__accountBalance = args[1]
            self.__accountHolderName = args[2]
            self.__customerId = args[3]
            self.__minBalanceRequired = args[4]
        # copy constructor - using the old object information to create the new object
        elif len(args) == 1:
            self.__accountNumber = args[0].__accountNumber + "NEW"
            self.__accountBalance = args[0].__accountBalance + 1000
            self.__accountHolderName = args[0].__accountHolderName
            self.__customerId = args[0].__customerId
            self.__minBalanceRequired = args[0].__minBalanceRequired

    def get_account_balance(self):
        return self.__accountBalance

    def get_account_number(self):
        return self.__accountNumber

    def is_below_min_balance(self):
        if self.__accountBalance < self.__minBalanceRequired:
            return True
        else:
            return False

    def print_details(self):
        print("Account Number: " + self.__accountNumber)
        print("Account Balance: " + str(self.__accountBalance))
        print("Account holder Name: " + self.__accountHolderName)
        print("Customer Id: " + self.__customerId)

from selenium.webdriver.common.by import By



class Search_Cadidate:
    
    #locators
    
    def __init__(self, driver):
        self.driver = driver
        
    #methods
    
    "//*[@class='oxd-table-body' and @role='rowgroup']child::div"
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from DataBase import create_database,create_table,set_data,get_data



headers = {
"cookie": "orioks_session=ab13391656fd1190f9b9eb52b1ae3007; _csrf=34e9fb8b4c9b9cb577d80faf0132b96a286d0b22ee6b86fca953a6f75eb6fa3aa%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22l9yP4wBLkXx7DQ1Zax7zrkyTTUcUdjLf%22%3B%7D",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 YaBrowser/22.7.3.787 Yowser/2.5 Safari/537.36"
}

headers_str = ""
for i in headers:
    headers_str += i+headers[i]+","
    

options = Options()
options.binary_location = "C:\\Users\\Valerian\\AppData\\Local\\Yandex\YandexBrowser\\Application\\browser.exe" #указываем путь до yandex
options.add_argument(headers_str)
WebDriver = webdriver.Chrome(chrome_options = options, executable_path=r'C:\\Users\\Valerian\Documents\\OneDrive\\Python\\Binance Parser\\chromedriver.exe') #путь до драйвера


try:
    Table = "MATANAL1"

    url_login = "https://orioks.miet.ru/user/login"
    url_test = "https://orioks.miet.ru/student/student/test?modID=91&kafID=33&idKM=1170605&debt=0"
    url_test_MatAnal1 = "https://orioks.miet.ru/student/student/test/?kafID=9&modID=179&idKM=1154589&debt=0"
    WebDriver.get(url_login)#авторизация

    login = WebDriver.find_element(By.NAME,"LoginForm[login]")
    login.send_keys("8211708")
    password = WebDriver.find_element(By.NAME,"LoginForm[password]")
    password.send_keys("Advicemietusers4")
    button_auth = WebDriver.find_element(By.ID,"loginbut")
    button_auth.click()
    time.sleep(0.5)

    WebDriver.get(url_test_MatAnal1)#заходим в тест

    def enter_to_question_page():
        try:
            question = WebDriver.find_element(By.XPATH,"/html/body/div[3]/div")
            print("----------------------------------")
            question = question.text.split(":")

            #answers[i-1] = WebDriver.find_element(By.XPATH,f"//*[@id='testform-answer']/label[i]/input")   #выбор варианта ответа

            answers = question[6].split("\n") #переменная со всеми вариантами ответов
            answers.pop(0)
            answers.remove("Продолжить")
            question = question[4]
            print("Вариантов ответов: ",len(answers))

            for i in range(0,4):
                try:
                    answers[i] = answers[i]
                except:
                    answers.append("0")
            for i in range(len(answers)):
                set_data(Table,question,answers[i],"True")#заполнение бд вариантами ответов и вопросоами

        except Exception as Ex:
            print("-Ошибка: ",Ex)
    #if answer.get_property("type") == "checkbox":
        
    def sampling_on_all_issues(num_question):
        print("hui")

    def first_sampling_on_all_issues():
        #create_table()
        for i in range(0,20):
            try:    
                WebDriver.find_element(By.XPATH,"/html/body/div[3]/div/a/button").click()# если это последняя страница, то повторить тест
                WebDriver.switch_to.alert.accept()
                time.sleep(5)
            except:
                print()
            num_question = WebDriver.find_element(By.XPATH,"/html/body/div[3]/div/div[2]/p")#номер решаемого впроса
            num_question = int(num_question.text.removeprefix("Текущий вопрос: "))
            question = WebDriver.find_element(By.XPATH,"/html/body/div[3]/div")#текст вопроса
            question = question.text.split(":")
            question = question[4]

            if num_question > 20:   #на случай,если тест начинается не с первого вопроса
                break
            answer = get_data(Table,question,1)
            if answer == "0":
                break

            enter_to_question_page()
            WebDriver.find_element(By.XPATH,f"//*[@id='testform-answer']/label[1]/input").click()  #выбор первого варианта ответа
            WebDriver.find_element(By.XPATH,"/html/body/div[3]/div/form/button").click() 
            time.sleep(5)
        return WebDriver.find_element(By.XPATH,"/html/body/div[3]/div/p[1]").text

    correct_answers = first_sampling_on_all_issues()
    print("Correct answer = ",correct_answers)

    def find_answer(question):
        for i in range(1,5):
            answer = get_data(Table,question,"True")
            if answer != "0":
                break

        WebDriver.find_element(By.XPATH,f"//*[@id='testform-answer']/label[1]/input").click() #выбор первого варианта ответа
    #print("-----------------=------------------")
    #print(answer.click)
    #print("-----------------=------------------")
    time.sleep(500)
except Exception as ex: 
    print(ex)
finally:
    WebDriver.close()
    WebDriver.quit()
    


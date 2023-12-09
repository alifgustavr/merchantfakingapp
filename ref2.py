from selenium import webdriver
import csv
import time

def isimercon():
    with open("D:/Familia/merchantapps/data.csv") as csv_file:
        csv_reader = csv.reader(csv_file)
        for merch in csv_reader:
            driver = webdriver.Edge()
            driver.get('https://subsiditepatlpg.mypertamina.id/merchant/auth/login')

            time.sleep(2)
            imel = driver.find_element("xpath", '//*[@id="mantine-r0"]')
            imel.click()
            imel.send_keys('alif.gustav@gmail.com')
            time.sleep(0.5)
            
            nip = driver.find_element("xpath", '//*[@id="mantine-r1"]')
            nip.click()
            nip.send_keys('573593')
            time.sleep(0.5)

            logon = driver.find_element("xpath", '//*[@id="__next"]/div[1]/div[1]/form/div[4]/button')
            logon.click()
            time.sleep(0.5)

            inputNik = driver.find_element("xpath", '//*[@id="mantine-r5"]')
            inputNik.send_keys(merch[0])
            time.sleep(0.5)

            okNik = driver.find_element("xpath", '//*[@id="__next"]/div[1]/div/main/div/div/div/div/div[2]/div/div[1]/form/div[2]/button')
            okNik.click()
            time.sleep(5)

            if merch[1] == "1" :
                jmlOk = driver.find_element("xpath", '//*[@id="__next"]/div[1]/div/main/div/div/div/div/div/div/form/div[3]/div/button')
                jmlOk.click()
                time.sleep(1)
            elif merch[1] == "2" :    
                jml2 = driver.find_element("xpath", '//*[@id="__next"]/div[1]/div/main/div/div/div/div/div/div/form/div[1]/div[2]/button[2]')
                jml2.click()
                time.sleep(1)
                jmlOk2 = driver.find_element("xpath", '//*[@id="__next"]/div[1]/div/main/div/div/div/div/div/div/form/div[3]/div/button') 
                jmlOk2.click()
            elif merch[1] == "3" :    
                jml3 = driver.find_element("xpath", '//*[@id="__next"]/div[1]/div/main/div/div/div/div/div/div/form/div[1]/div[2]/button[2]')
                jml3.click()
                time.sleep(1)
                jml3.click()
                time.sleep(1)
                jmlOk3 = driver.find_element("xpath", '//*[@id="__next"]/div[1]/div/main/div/div/div/div/div/div/form/div[3]/div/button') 
                jmlOk3.click()


            time.sleep(5)


        #    nik = data.iloc[i]['nik']
        #     inputNik = driver.find_element("xpath", '//*[@id="mantine-r2"]')
        #     for j in nik:
        #         inputNik.send_keys(j)
        #         time.sleep(0.5) 

        # cek = driver.find_element("xpath", '//*[@id="__next"]/div[1]/div/main/div/div/div/div/div[2]/div/div[1]/form/div[2]/button')
        # cek.click()
        # time.sleep(1)

        # submit = driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
        # submit.click()
        # time.sleep(0.5)

        # backForm = driver.find_element("xpath",'/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        # backForm.click()
        # time.sleep(0.5)

isimercon()
time.sleep(10)
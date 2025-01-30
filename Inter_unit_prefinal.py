# %%
import os  
import sys
import shutil
import pandas as pd 
import glob
import pymysql
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from datetime import datetime
import time
import re 
import os
import sys
import shutil
import pandas as pd
import glob
from datetime import datetime, timedelta
import pymysql
import openpyxl
from openpyxl import load_workbook
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import time
import re
import argparse
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email import encoders
from email.header import Header


# Server---------------------
# %%
USERNAME = 'root'
DATABASE = 'automatrix'

def connect_db():
	return pymysql.connect(
		host="localhost", user = USERNAME, database = DATABASE,
		autocommit = True, charset = 'utf8mb4',
		cursorclass = pymysql.cursors.DictCursor
	)

cursor = connect_db().cursor()

# %%
excelPath = r"C:\Users\mkt-admin2\Documents\process_automation\p2_debit_credit_automation\excel_dir"
today = datetime.today().strftime('%d/%m/%Y')
# %%
f_options = Options()
f_options.add_argument('--headless')  # Run Firefox in headless modef

# Create a Firefox profile with specific preferences
profile = FirefoxProfile()

# Set download preferences
download_directory = r"C:\Users\mkt-admin2\Documents\process_automation\p2_debit_credit_automation\excel_dir"
profile.set_preference("browser.download.folderList", 2)  # 2 means custom location
profile.set_preference("browser.download.dir", download_directory)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")  # Set MIME types if needed
profile.set_preference("browser.download.manager.showWhenStarting", False)  # Do not show download manager

# Allow popups during load
profile.set_preference("dom.disable_open_during_load", False)

# Firefox-specific options to mimic Chrome settings
f_options.set_preference("security.certerrors.mitm.auto_enable_enterprise_roots", True)  # Accept insecure SSL certificates
f_options.set_preference("browser.startup.page", 1)  # Start Firefox maximized

selenium_path = r"C:\Users\admin2\Documents\process_automation\geckodriver-v0.30.0-win64\geckodriver"

def deriverFunction_tcsion():
	try:
		driver = webdriver.Firefox(executable_path=selenium_path, firefox_profile=profile, options=f_options)
		driver.maximize_window()
		action = ActionChains(driver)
		print("driverI-S")
		return driver
	except Exception as e:
		return "driverI-E"


# Local----------------------
# today = datetime.now().date()
# USERNAME = 'root'
# PASSWORD = '94743@Outlook.Com'
# DATABASE = 'p1_research_table'
# def connect_db():
# 	return pymysql.connect(
# 		host="localhost", user = USERNAME, passwd = PASSWORD, database = DATABASE,
# 		autocommit = True, charset = 'utf8mb4',
# 		cursorclass = pymysql.cursors.DictCursor
# 	)
# cursor = connect_db().cursor()
# excelPath = r"C:\Users\rajad\Desktop\automatrix\automation_projects\p2_debit_credit_automation\excel_dir"
# today = datetime.today().strftime('%d/%m/%Y')

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.action_chains import ActionChains


# def deriverFunction_tcsion():
#     try:
#         c_options = Options()
#         prefs = {"download.default_directory": excelPath}
#         c_options.add_experimental_option("prefs", prefs)
#         c_options.add_argument('--ignore-certificate-errors')  # Accept insecure SSL certificates
#         c_options.add_argument('--start-maximized')  # Start Chrome maximized
#         c_options.add_argument('--disable-popup-blocking')  # Prevent popup windows from opening

#         # c_options.add_argument('--headless')  # Run Chrome in headless mode
#         c_options.add_argument('--no-sandbox')  # Required for running as root in some environments
#         c_options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource issues in headless mode
#         # c_options.add_argument('--window-size=1920,1080') 

#         driver = webdriver.Chrome(options=c_options)

#         # Optionally maximize the window (if not using --start-maximized)
#         # driver.maximize_window()
#         action = ActionChains(driver)

#         return driver
#     except Exception as e:
#         print("Error during driver initialization =======", e)
#         return None


# %%
# Function used to search for the excel file which will be downloaded by the 
def fileSearching(folder):
	try:
		allFiles = glob.glob(folder + "*")
		allFileName = []

		for files in allFiles:
			filename = os.path.basename(files) 
			allFileName.append(filename)

		return allFileName
		
	except Exception as e:
		print("fileSearching error >>>>>>>>>",e)
		return 'error'

# %%
# key Press funtions
def KeyPress(driver, key):
	try:
		time.sleep(5)
		action = ActionChains(driver)
		action.key_down(key).key_up(key).perform()

		return 'success'
	except Exception as e:
		print("KeyPress error >>>>>>", e)


# Scroll into view and move the mouse to that element
def moveToElement(driver,element):
	try:
		driver.execute_script("arguments[0].scrollIntoView();", element)
		# actions = ActionChains(driver)
		# actions.move_to_element(element).perform()
	except Exception as e:
		print("moveToElement error >>>>>>>>>.>", e)

# %%
def delete_all_files_in_directory(directory_path):

	for filename in os.listdir(directory_path):
		file_path = os.path.join(directory_path, filename)
		try:
			if os.path.isfile(file_path) or os.path.islink(file_path):
				os.unlink(file_path)
			elif os.path.isdir(file_path):
				shutil.rmtree(file_path)
		except Exception as e:
			print(f"Failed to delete {file_path}. Reason: {e}")

# %%

def logIn_tcsion(driver):
	try:
		driver.get("https://www4.tcsion.com/dotcom/TCSSMB/Login/login.html")
		WebDriverWait(driver, 20).until(
		EC.invisibility_of_element_located((By.XPATH,"//div[@class='blockUI blockOverlay']"))
		)
		time.sleep(2)
		WebDriverWait(driver, 10).until(
			EC.element_to_be_clickable((By.XPATH, "//span[text()='Accept All Cookies']"))
		).click()

		user_ele= driver.find_element(By.XPATH, f'//input[@id="accountname"]')
		user_ele.send_keys('automatrix3@srmbsteel.com')

		pass_ele= driver.find_element(By.XPATH, f'//input[@id="password"]')
		pass_ele.send_keys('2023@Srmb')
		# pass_ele.send_keys('2023#Srmb')
		# pass_ele.send_keys('2023-Srmb')
		# pass_ele.send_keys('Srmb-2023')

		WebDriverWait(driver, 10).until(
			EC.element_to_be_clickable((By.XPATH, '//a[@class="n-login"]'))
		).click()

		WebDriverWait(driver, 20).until(
		EC.invisibility_of_element_located((By.XPATH,"//div[@class='blockUI blockOverlay']"))
		)            
		time.sleep(2)

		try:
			if not WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//a[@id="start"]'))):
				driver.get("https://g01m18.tcsion.com/SMBPortal/Start")
		except:
			print("page frame not broken!")
				
		WebDriverWait(driver, 10).until(
			EC.element_to_be_clickable((By.XPATH, '//a[@id="start"]'))
		).click()
		time.sleep(5)
		WebDriverWait(driver, 10).until(
			EC.element_to_be_clickable((By.XPATH, '//li[@name= "Finance and Accounting"]'))
		).click()
		time.sleep(5)
		WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="app_26_content"]')))
		time.sleep(5)
		print("login success...")
		return "login-S"
	except:
		print("Password Changed or Prev Session Not Closed")
		return "login-E"


# %%
def afterLogin(driver):
    try:
        delete_all_files_in_directory(excelPath)
        time.sleep(5)
        driver.switch_to.default_content()
        WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="app_26_content"]')))
        driver.switch_to
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//li[@id= "M_70003"]'))
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@id= "menu-Drill Down Reports"]/ul/li/a/label'))
        ).click()
        time.sleep(10)

        WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//iframe[@id="iframe_id"]')))
        
        ##########################################################################################
        WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//h4[text()= "Party Outstanding Detail "]'))
        ).click()
        ##########################################################################################

        WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//mat-select[@id= "accountingSiteid"]'))
        )
        acc_site= driver.find_element(By.XPATH, '//mat-select[@id= "accountingSiteid"]')
        driver.execute_script("arguments[0].click();", acc_site)
        time.sleep(3)
        WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//span[contains(text(), "22 (SRMB Srijan Pvt Ltd - Durgapur)")]'))  
        ).click()
        time.sleep(1)
        WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//span[contains(text(), "31 (SRMB Srijan Pvt Ltd - Tripura Branch. .")]'))  
        ).click()
        time.sleep(1)
        WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//span[contains(text(), "76 (TECH NIRMAN ISPAT PRIVATE LIMITED-TR. .")]'))  
        ).click()

        KeyPress(driver, Keys.ESCAPE)

        WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//label[text()="Basic Filter "]'))
        ).click()

        WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//mat-card[@class="mat-card mat-focus-indicator advanceFilterElements commanRemoveMatCard"][1]/div/div[1]'))
        ).click()
        driver.execute_script("return document.activeElement;").send_keys(Keys.CONTROL + 'a')
        
        KeyPress(driver, Keys.ESCAPE)

        WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//label[text()= "Advance Filter "]'))
        ).click()
        
        WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//mat-card[@class= "mat-card mat-focus-indicator advanceFilterElements commanRemoveMatCard"][2]/div[@class= "advanceFilterDiv"]/div[@class= "iON_Col_Md_3"][1]'))
        ).click()

        try:
            ad_optionNBH = WebDriverWait(driver, 10).until(
                EC.visibility_of_all_elements_located((By.XPATH, '//span[contains(text(), "NBH")]'))  
            )
            for ad_option in ad_optionNBH:
                ad_option.click()
        except:
            print("NBH Not found")

        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//span[contains(text(), "AB-ADM(AB-ADM)")]'))  
            ).click()
        except:
            print("ADM Not found")

        KeyPress(driver, Keys.ESCAPE)

        export = driver.find_element(By.XPATH,'//button[@id= "directExportExcel"]')
        driver.execute_script("arguments[0].scrollIntoView();", export)
        driver.execute_script("arguments[0].click();", export)
        
        time.sleep(4)
        
        def_temp = driver.find_element(By.XPATH,'//mat-card-content[@class= "mat-card-content"]/descendant::span[text()= "Default Template"]')
        driver.execute_script("arguments[0].click();", def_temp)
        time.sleep(2)
        WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//span[text()= " All Columns Template "]'))  
        )
        all_cols= driver.find_element(By.XPATH,'//span[text()= " All Columns Template "]')
        driver.execute_script("arguments[0].click();", all_cols)
        time.sleep(2)
        WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//div[@class="searchFilterFooter; selectTemplateFilter"]/button[1]'))  
        ).click()
        return "afterLIn-S"

    except:
        return "afterLIn-E"


# %%
def logOut(driver):
	# driver.execute_script("window.scroll(0, 0);")
	driver.switch_to.default_content()
	WebDriverWait(driver, 10).until(
	EC.element_to_be_clickable((By.XPATH, '//a[@id= "logoff"]'))  
	).click()
	time.sleep(5)
	# WebDriverWait(driver, 10).until(
	# EC.element_to_be_clickable((By.XPATH, '//*[@id="yesBtn"]'))  
	# ).click() # normal Xpath cant reach the element but javascript dom function reach through that
	
	button_logout_click = driver.find_element(By.XPATH,'//*[@id="yesBtn"]')
	driver.execute_script("arguments[0].click();", button_logout_click)
	# arguments is an array-like object available within all functions.
	# arguments[0]: This accesses the first argument passed to the function.this is the element you want to interact with.
	time.sleep(5)
	driver.close()
	driver.quit()

# %%
def search_for_file(directory):
	for i in range(5):
		files = os.listdir(directory)
		
		if len(files) > 0:
			print("File found!")
			return "file-S"
		else:
			print("File not found. Checking again in 40 seconds...")
		
		time.sleep(40)
	print("file not found waited for 200 sec...")
	return

# %%
def download_filter_excel():
	ll= os.listdir(excelPath)
	wb = load_workbook(filename=os.path.join(excelPath, ll[0]))
	fileOriginalName, file_extension = os.path.splitext(ll[0])
	print(fileOriginalName,file_extension)
	wb.save(os.path.join(excelPath,ll[0]))
	file = os.path.join(excelPath,ll[0])
	df = pd.read_excel(file,sheet_name='Party Outstanding Detail Report',engine='openpyxl')
	# print("col>>>",df.columns)
	time.sleep(5)
	filter_df= df[['Transaction Site', 'Party Category', 'Party Account Code', 'Party Account Description', 'Party Code', 'Party Description', 'Voucher Type', 'Voucher Number','Voucher Date','Supplier Invoice No or Customer PO No','Outstanding or Unadjusted Amount in Domestic Currency','Header Narration']]
	filter_df = filter_df[
		~filter_df['Party Code'].str.startswith('CUST00257', na=False) &
		~filter_df['Voucher Number'].str.startswith('Summary:', na=False) &
		filter_df['Voucher Number'].notna() &
		filter_df['Voucher Number'].astype(str).str.startswith(('3136', '7636'))
	].reset_index(drop=True)

	

	return filter_df

# %%
def insertDB(filter_df):
	try:
		truncate_sql = "TRUNCATE TABLE p2_bot_table"
		cursor.execute(truncate_sql)
		for index, row in filter_df.iterrows():
			insert_sql = """
				INSERT INTO p2_bot_table
				(`Transaction Site`, `Party Category`, `Party Account Code`, `Party Account Description`, 
				`Party Code`, `Party Description`, `Voucher Type`, `Voucher Number`, `Voucher Date`, 
				`Supplier Invoice No or Customer PO No`, `Outstanding or Unadjusted Amount in Domestic Currency`, `Header Narration`) 
				VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
			"""
			insert_data = (
				None if pd.isna(row['Transaction Site']) else row['Transaction Site'],
				None if pd.isna(row['Party Category']) else row['Party Category'],
				None if pd.isna(row['Party Account Code']) else row['Party Account Code'],
				None if pd.isna(row['Party Account Description']) else row['Party Account Description'],
				None if pd.isna(row['Party Code']) else row['Party Code'],
				None if pd.isna(row['Party Description']) else row['Party Description'],
				None if pd.isna(row['Voucher Type']) else row['Voucher Type'],
				None if pd.isna(row['Voucher Number']) else row['Voucher Number'],
				None if row['Voucher Date'] is pd.NaT else row['Voucher Date'],
				None if pd.isna(row['Supplier Invoice No or Customer PO No']) else row['Supplier Invoice No or Customer PO No'],
				None if pd.isna(row['Outstanding or Unadjusted Amount in Domestic Currency']) else row['Outstanding or Unadjusted Amount in Domestic Currency'],
				None if pd.isna(row['Header Narration']) else row['Header Narration']
			)
			cursor.execute(insert_sql, insert_data)

		return "insertDB-S"
	except:
		return "insertDB-E"
# %%
# Master Logic MF
def if_vn(str):
	if not str:
		str= ""
	pattern = r"\d{4}/\d{2}/\d{1,6}"
	match = re.search(pattern, str)
	# print(match.group(0))
	return match.group(0) if match else ""

def mainAdjustmentFunction(driver):
	try:
		inter_unit_voucher_code= ('3136', '7636')
		inter_unit_po= ('3122', '7622')

		select_query = "Select * from p2_bot_table where status= 0"
		cursor.execute(select_query)
		results = cursor.fetchall()
		# print("results>>>>>>>>>>>>", results)
		for result in results:
			if result is None:
				print("break")
				break
			if str(result['Voucher Number']).startswith(inter_unit_voucher_code):
				vn= if_vn(result['Voucher Number'])
				v_date= result['Voucher Date']
				if v_date:
					v_date = v_date.strftime('%d/%m/%Y')
				else:
					v_date = ''
				v_amount= str(result['Outstanding or Unadjusted Amount in Domestic Currency'])
				po_no= result['Supplier Invoice No or Customer PO No']
				print("Details>>>>>>",vn, po_no, v_amount, v_date)
				po_no= if_vn(po_no)
				print(po_no)

				if po_no.startswith(inter_unit_po):
					try:
						interUnit_Manual(driver, v_date, vn, po_no, v_amount) 
					except:
						print("interUnit manual error.")
						break
				else:
					try:
						interUnit_Auto(driver, v_date, vn, v_amount)
					except:
						print("interUnit auto errror...")
						break
					
			r_query= '''update p2_bot_table
					set Status= 1
					where id= %s;
				'''
			cursor.execute(r_query, result.get('id'))

		return "process-S"
	except Exception as e:
		print(e)
		return "process-E"

# %%
def matchAmount(amt1, amt2):
	amt1 = amt1.replace(',', '')
	amt2 = amt2.replace(',', '')
	try: 
		return abs(float(amt1))== abs(float(amt2))
	except:
		print("amt not matched!!")
##############################
def interUnit_Manual(driver, v_date, vn, po_no, amount):
	print("interUnit Manual...............")
	driver.switch_to.default_content()
	WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="app_26_content"]')))
	for i in range(3):
		try:
			acc = driver.find_element(By.XPATH,'//span[text()= "Accounts Receivable"]')
			driver.execute_script("arguments[0].click();", acc)
			time.sleep(3)
			WebDriverWait(driver, 20).until(
			EC.invisibility_of_element_located((By.XPATH,"//div[@class='blockUI blockOverlay']"))
			)
			drcr = driver.find_element(By.XPATH,'//label[text()= "Inter-Unit Dr/ Cr Notes"]')
			driver.execute_script("arguments[0].click();", drcr)
			break
		except:
			...
	
	try:
		time.sleep(2)
		WebDriverWait(driver, 20).until(
		EC.invisibility_of_element_located((By.XPATH,"//div[@class='blockUI blockOverlay']"))
		)
		driver.find_element(By.XPATH,'//span[text()= "Modify Search"]').click()

	except: 
		print("Modify Search Not found")

	time.sleep(2)
	input_box= WebDriverWait(driver, 10).until(
	EC.element_to_be_clickable((By.XPATH, '//input[@name= "S_apvvouchernumber"]'))  
	)
	driver.execute_script("arguments[0].value = '';", input_box)
	input_box.send_keys(vn)

	fromDate= WebDriverWait(driver, 10).until(
	EC.element_to_be_clickable((By.XPATH, '//input[@id= "fromDate"]'))  
	)
	fromDate.click()
	driver.execute_script("arguments[0].value = '';", fromDate)
	fromDate.send_keys(v_date)
	KeyPress(driver, Keys.ENTER)

	toDate= WebDriverWait(driver, 10).until(
	EC.element_to_be_clickable((By.XPATH, '//input[@id= "toDate"]'))  
	)
	toDate.click()
	driver.execute_script("arguments[0].value = '';", toDate)
	toDate.send_keys(v_date)
	KeyPress(driver, Keys.ENTER)

	for i in range(0, 3):
		try:
			search= WebDriverWait(driver, 10).until(
			EC.element_to_be_clickable((By.XPATH, '//button[@value= "Search"]'))  
			)
			driver.execute_script("arguments[0].click()", search)
			break
		except:
			print("searching prob...")

	try: ## not found out data point
		time.sleep(5)
		WebDriverWait(driver, 20).until(
		EC.invisibility_of_element_located((By.XPATH,"//div[@class='blockUI blockOverlay']"))
		)
		WebDriverWait(driver, 10).until(
		EC.visibility_of_any_elements_located((By.XPATH, '//td[text()= "NO RECORD EXISTS"]'))  
		)
		return
	except:
		...
		# print(f"Working on mf: {vn}")
	
	try:
		time.sleep(2)
		WebDriverWait(driver, 20).until(
		EC.invisibility_of_element_located((By.XPATH,"//div[@class='blockUI blockOverlay']"))
		)
		WebDriverWait(driver, 10).until(
			EC.element_to_be_clickable((By.XPATH, f'//a[text()= "{vn}"]'))
		).click()
	except:
		print(f"MF: {vn} not found!")
		return 
	time.sleep(5)
	for i in range(0, 3):
		try:
			WebDriverWait(driver, 20).until(
			EC.invisibility_of_element_located((By.XPATH,"//div[@class='blockUI blockOverlay']"))
			)
			driver.switch_to.default_content()
			WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="app_26_content"]')))
			# xyz= driver.find_element(By.XPATH, '//button[text()= "Auto Clear Voucher"]')
			xyz= WebDriverWait(driver, 10).until(
					EC.element_to_be_clickable((By.XPATH, '//button[text()= "Auto Clear Voucher"]'))
				)
			driver.execute_script("arguments[0].click();", xyz)
			print("auto clear voucher ?")
			driver.switch_to.default_content()
			WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="app_26_content"]')))
			WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="popupid_content"]')))
			time.sleep(3)
			WebDriverWait(driver, 20).until(
			EC.invisibility_of_element_located((By.XPATH,"//div[@class='blockUI blockOverlay']"))
			)
		
			WebDriverWait(driver, 10).until(
				EC.element_to_be_clickable((By.XPATH, '//input[@value= "Search"]'))
			).click()
			break
		except:
			print("auto clear voucher inloop")
	# time.sleep(40)
	# Works GOOD

	time.sleep(5)
	driver.switch_to.default_content()
	WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="app_26_content"]')))
	WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="popupid_content"]')))

	WebDriverWait(driver, 80).until(
	EC.invisibility_of_element_located((By.XPATH,'//*[contains(text(), "Processing")]'))
	)
	time.sleep(5)
	
	####################################################
	try:
		WebDriverWait(driver, 10).until(
		EC.visibility_of_any_elements_located((By.XPATH, '//div[text()= "No Record Exists"]'))  
		)
		print("No Record Exists: PO")
	except:
		...

	####################################################

	try:
		input_amount= WebDriverWait(driver, 10).until(
			EC.element_to_be_clickable((By.XPATH, '//input[@name= "ToBeAdjusted"]'))
		)
		time.sleep(2)
		copied_amt = input_amount.get_attribute("value")
		if not matchAmount(copied_amt, amount):
			dead_close(driver)
			return 
		time.sleep(1)
		WebDriverWait(driver, 10).until(
			EC.element_to_be_clickable((By.XPATH, '//input[@id= "radio"][2]'))
		).click() # Manual 

		WebDriverWait(driver, 20).until(
		EC.invisibility_of_element_located((By.XPATH,"//div[@class='blockUI blockOverlay']"))
		)
		filter= WebDriverWait(driver, 10).until(
			EC.element_to_be_clickable((By.XPATH, '//input[@id= "selectallnumber"]'))
		)
		actions = ActionChains(driver)
		actions.click(filter).perform()
		driver.execute_script("arguments[0].value = '';", filter)
		filter.send_keys(po_no)
		tbody = driver.find_element(By.XPATH, '//tbody[@id="dynamictable"]')
		elements_with_no_display_set = driver.execute_script("""
			let tbody = arguments[0];
			return Array.from(tbody.querySelectorAll('tr')).filter(element => 
				!element.hasAttribute('style') || !element.style.display
			);
		""", tbody)
		try:
			pending_amt= elements_with_no_display_set[1].find_element(By.XPATH, './/td[6]/input')
			p_amt= pending_amt.get_attribute("value")
			if not matchAmount(p_amt, amount):
				print("pending amt not matched>>>>>>>", p_amt)
				dead_close(driver)
				return 
			checkbox = elements_with_no_display_set[1].find_element(By.XPATH, './/td/input[@type="checkbox"]')
			checkbox.click()
			adjusted_amt_input= elements_with_no_display_set[1].find_element(By.XPATH, './/td[7]/input')
			actions = ActionChains(driver)
			actions.click(adjusted_amt_input).perform()
			driver.execute_script("arguments[0].value = '';", adjusted_amt_input)
			adjusted_amt_input.send_keys(amount)
		except:
			WebDriverWait(driver, 10).until(
			EC.element_to_be_clickable((By.XPATH, '//input[@id="Cancel"]'))
			).click()
			print("Search: PO not exists...")
			return
		adj= driver.find_element(By.XPATH, "//input[@id= 'Adjust']")
		driver.execute_script('arguments[0].click();', adj)
		
		suc= driver.find_element(By.XPATH, '//input[@value= "Save"]')
		driver.execute_script('arguments[0].click();', suc)
		time.sleep(3)
		print("vn>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", vn)
		print("amount>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", amount)

		adj_insert_query= "INSERT INTO adjusted_record (voucher_number, po_number, amount, date, adjustment_date) VALUES (%s,%s,%s, %s, %s)"
		adj_data= (vn, po_no, amount, v_date, today)
		cursor.execute(adj_insert_query, adj_data)

		cancel= driver.find_element(By.XPATH, '//input[@id="Cancel"]')
		driver.execute_script('arguments[0].click();', cancel)
		# print("Succ")

	except:
		dead_close(driver)
		return 

# %%
def interUnit_Auto(driver, v_date, vn, amount):
	print("interUnit Auto.........")
	driver.switch_to.default_content()
	WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="app_26_content"]')))
	for i in range(3):
		try:
			acc = driver.find_element(By.XPATH,'//span[text()= "Accounts Receivable"]')
			driver.execute_script("arguments[0].click();", acc)
			time.sleep(2)
			WebDriverWait(driver, 20).until(
			EC.invisibility_of_element_located((By.XPATH,"//div[@class='blockUI blockOverlay']"))
			)
			drcr = driver.find_element(By.XPATH,'//label[text()= "Inter-Unit Dr/ Cr Notes"]')
			driver.execute_script("arguments[0].click();", drcr)
			break
		except:
			...
	try:
		time.sleep(2)
		WebDriverWait(driver, 20).until(
		EC.invisibility_of_element_located((By.XPATH,"//div[@class='blockUI blockOverlay']"))
		)
		driver.find_element(By.XPATH,'//span[text()= "Modify Search"]').click()

	except: 
		print("Modify Search Not found")
	print("vn/dn")
	time.sleep(2)
	WebDriverWait(driver, 20).until(
	EC.invisibility_of_element_located((By.XPATH,"//div[@class='blockUI blockOverlay']"))
	)
	input_box= WebDriverWait(driver, 10).until(
	EC.element_to_be_clickable((By.XPATH, '//input[@name= "S_apvvouchernumber"]'))  
	)
	driver.execute_script("arguments[0].value = '';", input_box)
	input_box.send_keys(vn)

	fromDate= WebDriverWait(driver, 10).until(
	EC.element_to_be_clickable((By.XPATH, '//input[@id= "fromDate"]'))  
	)
	fromDate.click()
	driver.execute_script("arguments[0].value = '';", fromDate)
	fromDate.send_keys(v_date)
	KeyPress(driver, Keys.ENTER)

	toDate= WebDriverWait(driver, 10).until(
	EC.element_to_be_clickable((By.XPATH, '//input[@id= "toDate"]'))  
	)
	toDate.click()
	driver.execute_script("arguments[0].value = '';", toDate)
	toDate.send_keys(v_date)
	KeyPress(driver, Keys.ENTER)
	for i in range(0, 3):
		try:
			search= WebDriverWait(driver, 10).until(
			EC.element_to_be_clickable((By.XPATH, '//button[@value= "Search"]'))  
			)
			driver.execute_script("arguments[0].click()", search)
			break
		except:
			print("searching prob...")
	try: 
		time.sleep(5)
		WebDriverWait(driver, 20).until(
		EC.invisibility_of_element_located((By.XPATH,"//div[@class='blockUI blockOverlay']"))
		)
		WebDriverWait(driver, 10).until(
		EC.visibility_of_any_elements_located((By.XPATH, '//td[text()= "NO RECORD EXISTS"]'))  
		)
		return
	except:
		...
		# print(f"Working on mf: {vn}")
	
	try:
		time.sleep(2)
		WebDriverWait(driver, 20).until(
		EC.invisibility_of_element_located((By.XPATH,"//div[@class='blockUI blockOverlay']"))
		)
		WebDriverWait(driver, 10).until(
			EC.element_to_be_clickable((By.XPATH, f'//a[text()= "{vn}"]'))
		).click()
		print("voucher click")
	except:
		print(f"MF: {vn} not found!")
		return 

	for i in range(3):
		try:
			time.sleep(5)
			WebDriverWait(driver, 20).until(
			EC.invisibility_of_element_located((By.XPATH,"//div[@class='blockUI blockOverlay']"))
			)
			####################
			driver.switch_to.default_content()
			WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="app_26_content"]')))
			# xyz= driver.find_element(By.XPATH, '//button[text()= "Auto Clear Voucher"]')
			# driver.execute_script("arguments[0].click();", xyz)
			xyz= WebDriverWait(driver, 10).until(
					EC.element_to_be_clickable((By.XPATH, '//button[text()= "Auto Clear Voucher"]'))
				)
			driver.execute_script("arguments[0].click();", xyz)
			print("Auto Clear Voucher clicked... ")

			driver.switch_to.default_content()
			WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="app_26_content"]')))
			WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="popupid_content"]')))
			time.sleep(2)
			WebDriverWait(driver, 20).until(
			EC.invisibility_of_element_located((By.XPATH,"//div[@class='blockUI blockOverlay']"))
			)
		
			WebDriverWait(driver, 10).until(
				EC.element_to_be_clickable((By.XPATH, '//input[@value= "Search"]'))
			).click()
			break
		except:
			print("Auto Clear Voucher inloop...")
	# time.sleep(40)
	# print("search")
	# Works GOOD
	
	time.sleep(5)
	driver.switch_to.default_content()
	WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="app_26_content"]')))
	WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="popupid_content"]')))

	WebDriverWait(driver, 80).until(
	EC.invisibility_of_element_located((By.XPATH,'//*[contains(text(), "Processing")]'))
	)
	time.sleep(5)

	
	####################################################
	try:
		WebDriverWait(driver, 10).until(
		EC.visibility_of_any_elements_located((By.XPATH, '//div[text()= "No Record Exists"]'))  
		)
		print("No Record Exists: PO")
	except:
		...

	####################################################


	try:
		input_amount= WebDriverWait(driver, 10).until(
			EC.element_to_be_clickable((By.XPATH, '//input[@name= "ToBeAdjusted"]'))
		)
		copied_amt = input_amount.get_attribute("value")
		if not matchAmount(copied_amt, amount):
			dead_close(driver)
			return 
		WebDriverWait(driver, 10).until(
			EC.element_to_be_clickable((By.XPATH, '//input[@id= "radio"][1]'))
		).click()
		print("auto")
		adj= driver.find_element(By.XPATH, "//input[@id= 'Adjust']")
		driver.execute_script('arguments[0].click();', adj)
		
		suc= driver.find_element(By.XPATH, '//input[@value= "Save"]')
		driver.execute_script('arguments[0].click();', suc)
		time.sleep(3)
		print("vn>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", vn)
		print("amount>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", amount)

		adj_insert_query= "INSERT INTO adjusted_record (voucher_number, po_number, amount, date, adjustment_date) VALUES (%s,%s,%s, %s, %s)"
		adj_data= (vn, "not_found", amount, v_date, today)
		cursor.execute(adj_insert_query, adj_data)

		can= driver.find_element(By.XPATH, '//input[@id="Cancel"]')
		driver.execute_script('arguments[0].click();', can)
		print("save")
		# print("Succ")

	except:
		print("")
		dead_close(driver)
		return 
	
# interUnit_Auto(driver, '3136/25/137', '-2,773,180.00')


def dead_close(driver):
	script = '''
		(function() {
			window.top.document.defaultView.focus();

			function waitForIframeAndSwitchToIt(xpath, callback) {
				const interval = setInterval(function() {
					const iframe = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
					if (iframe) {
						clearInterval(interval);
						console.log('Iframe found:', iframe);
						callback(iframe);
					}
				}, 100);
			}

			function waitForElementInIframe(iframe, xpath, callback) {
				const interval = setInterval(function() {
					const element = iframe.contentDocument.evaluate(xpath, iframe.contentDocument, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
					if (element) {
						clearInterval(interval);
						console.log('Element found:', element);
						callback(element);
					}
				}, 100);
			}

			waitForIframeAndSwitchToIt('//*[@id="app_26_content"]', function(iframe) {
				waitForElementInIframe(iframe, "//div[@id='popupid_close'][2]", function(cross) {
					cross.click();
					console.log('Element clicked:', cross);
				});
			});
		})();
		'''
	driver.switch_to.default_content() 
	driver.execute_script(script)

def getStatus(process):
	query= "SELECT * FROM process_status where process_name= %s;"
	cursor.execute(query, process)
	res= cursor.fetchone()
	print(res)
	return res.get('status')

def modStatus(status, process):
	query= 'UPDATE process_status SET status = %s WHERE process_name= %s;'
	data= (status, process)
	try:
		cursor.execute(query, data)
		return True
	except:
		return False

def modStatusCond2(p_name):
	q1= "select * from p2_bot_table where Status= 0"
	cursor.execute(q1)
	res= cursor.fetchall()
	if not res:
		modStatus(2, p_name)
	print("Process Completed and Status Changed...")


def export_excel(cursor):
	curr_date = datetime.now().strftime('%d/%m/%Y')
	print(curr_date)
	# curr_date= "14/10/2024"
	curr_date__ = datetime.now().strftime('%d-%m-%Y')
	# curr_date__= "14-10-2024"
	print(curr_date__)
	# auto_dc_voucher_code= ('2233', '2234', '3133', '3134', '7633', '7634','2265', '3165', '7665')
	inter_voucher_code= ('3136', '7636')
	totaldf= pd.DataFrame()
	for vn in inter_voucher_code:
		query= "select * from adjusted_record where voucher_number like %s  and adjustment_date= %s"
		cursor.execute(query, (vn+"%", curr_date))
		res= cursor.fetchall()
		df = pd.DataFrame(res)
		totaldf = pd.concat([totaldf, df], ignore_index=True)

	# Save the DataFrame to an Excel file (corrected file extension to .xlsx)
	if not totaldf.empty:
		totaldf.to_excel(fr"C:\Users\mkt-admin2\Documents\process_automation\p2_debit_credit_automation\log\InterUnit_adjusted_record_{curr_date__}.xlsx", index=False)



def send_email():
	curr_date__ = datetime.now().strftime('%d-%m-%Y')
	# curr_date__= "14-10-2024"
	print(curr_date__)
	print("Report Sending >>>>>>>>>>>>>>> starts")
	from_email = 'bot-support@automatrix.co.in'
	mail_password = 'RobotBOT@1234'
	
	# Recipients
	to_email = ["commercialproject1@srmbsteel.com", "projectcommercial2@srmbsteel.com", "anjan.chaudhuri@srmbsteel.com"]
	cc_emails = ["shubhrajyoti.poddar@automatrix-innovation.com", "arijit.chowdhury@automatrix.co.in", "nirmalya.sarkar@automatrix.co.in", "arnab.halder@automatrix.co.in"]
	
	# to_email= ["rajadjrocks@gmail.com"]
	# cc_emails= ["rajadjrocks+bot@gmail.com"]

	subject = 'InterUnit Adjusted Report'
	body = "Adjusted report attached."
	
	# File path to the attachment
	attachment_path = fr"C:\Users\mkt-admin2\Documents\process_automation\p2_debit_credit_automation\log\InterUnit_adjusted_record_{curr_date__}.xlsx"
	
	# Create the email message object
	msg = MIMEMultipart()
	msg['From'] = from_email
	msg['To'] = ', '.join(to_email)
	msg['Cc'] = ', '.join(cc_emails)
	msg['Subject'] = subject
	
	# Adding the attachment
	try:
		filename = os.path.basename(attachment_path)
		with open(attachment_path, "rb") as attachment:
			part = MIMEBase('application', 'octet-stream')
			part.set_payload(attachment.read())
			encoders.encode_base64(part)
			part.add_header('Content-Disposition', f"attachment; filename= {filename}")
			msg.attach(part)
	except Exception as e:
		print(f"Error while attaching file: {e}")
		body = "Sir, This is to Inform that we have not found any records for adjustment today."
	finally:
		msg.attach(MIMEText(body, 'plain'))
	
	# Combine the recipients (To + Cc)
	recipients = to_email + cc_emails

	try:
		# Create SMTP session
		session = smtplib.SMTP('smtp.gmail.com', 587)
		session.starttls()
		session.login(from_email, mail_password)
		text = msg.as_string()
		session.sendmail(from_email, recipients, text)
		session.quit()
		print("Message sent successfully")
	except Exception as e:
		print(f"Mail sending error: {e}")



print("Process started")
def todoList():
	status= getStatus("inter_unit")
	if status== 3:
		return
	elif status== 0 :
		driver= deriverFunction_tcsion()
		if driver:
			print("driver Created...")
			lIn= logIn_tcsion(driver)
			if lIn== "login-S":
				print("login successfull...")
				aLIn= afterLogin(driver)
				if aLIn== "afterLIn-S":
					print("XLS clicked!")
					sfile= search_for_file(excelPath) 
					if sfile== "file-S":
						filter_df= download_filter_excel()
						print(insertDB(filter_df))
						modStatus(1, "inter_unit")
						mainF= mainAdjustmentFunction(driver)
						if mainF== "process-S":
							print("Main F Exited!")
							modStatusCond2("inter_unit")
							# modStatus(2, "inter_unit")
							logOut(driver)
							print("logout Successful...")
							status= getStatus("inter_unit")
							if status== 2:
								print("Sending Email")
								export_excel(cursor)
								send_email()
								modStatus(3,"inter_unit")
							else:
								print('not downloaded or not finished or ???...')
						else:
							print("main function not completed...")
							logOut(driver)
					else:
						print("waited for > 200 secs not downloaded, exiting...")
						logOut(driver)
				else:
					print("file not downloaded...")
					logOut(driver)
			else:
				print("login Failed")
				driver.close()
				driver.quit()
		else:
			print("driver not created...")

	elif status== 1:
		driver= deriverFunction_tcsion()
		if driver:
			print("driver Created...")
			lIn= logIn_tcsion(driver)
			if lIn== "login-S":
				print("login successfull...")
				mainF= mainAdjustmentFunction(driver)
				if mainF== "process-S":
					print("process Completed!")
					# modStatus(2, "inter_unit")
					modStatusCond2("inter_unit")
					
					logOut(driver)
					print("logout Successful...")
					status= getStatus("inter_unit")
					if status== 2:
						print("Sending Email")
						export_excel(cursor)
						send_email()
						modStatus(3,"inter_unit")
					else:
						print('not downloaded or not finished or ???...')
				else:
					print("main function not completed...")
					logOut(driver)
			else:
				print("login Failed")
				driver.close()
				driver.quit()
		else:
			print("driver not created...")

	elif status== 2:
		print("Sending Email")
		export_excel(cursor)
		send_email()
		modStatus(3,"inter_unit")


todoList()








# driver= deriverFunction_tcsion()
# logIn_tcsion(driver)
# afterLogin(driver)
# search_for_file(excelPath)   
# filter_df= download_filter_excel()
# print(filter_df)
# print(insertDB(filter_df))
# mainAdjustmentFunction(driver)
# logOut(driver)
# try:
#     driver.close()
#     driver.quit()
# except:
#     ...
# print("Exited mainAdjustmentFunction...")
# export_excel(cursor)


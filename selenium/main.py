'''
Created on 2024年2月27日

@author: ericluo
'''

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
path_current_dir = os.path.dirname(os.path.abspath(__file__))

# selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select   # 使用 Select 對應下拉選單
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#pyautoit
import autoit

import csv
import time
from normal import method
# from normal.method import PyConfigParser

def RunSelenium(config, driver, config_data, **kwargs):
    
    timeout = kwargs.get('timeout', '20')
    freq = kwargs.get('freq', '0.5')
    xpath = kwargs.get('xpath', '')
    item = kwargs.get('item', '') 
    data = kwargs.get('data', '') 
    section = kwargs.get('section', 'section')
    option = kwargs.get('option', 'option')
    source = kwargs.get('source', '')
    target = kwargs.get('target', '')
    xoffset = kwargs.get('xoffset', '')
    yoffset = kwargs.get('yoffset', '')
    element = kwargs.get('yoffset', '')
    id = kwargs.get('id', '')  # @ReservedAssignment
    skip_fail = kwargs.get('skip_fail', '')  # @ReservedAssignment
    title = kwargs.get('title', '')
    send_text = kwargs.get('send_text', '')
    result = False
    
    try:
        
        for i in range(1):  # @UnusedVariable

            if item == 'sleep':
                #normal
                time.sleep(float(data)) #等待(秒)。

            else:
                if 'autoit' in item:
                    #selenium
                    if item == 'autoit_win_activate':
                        autoit.win_activate(title)
                    elif item == 'autoit_send':
                        autoit.send(send_text)
                    elif item == 'autoit_win_close':
                        autoit.win_close(title)
                    elif item == 'autoit_win_kill':
                        autoit.win_kill(title)
                    else:
                        continue
                else:
                    #selenium
                    if item == 'get': #開啟網址。
                        driver.set_page_load_timeout(int(timeout))
                        driver.set_script_timeout(int(timeout))
                        driver.get(data)
                    elif item == 'refresh':
                        driver.refresh() #網頁重整。
                    elif item == 'back':   
                        driver.back()#前往上一項瀏覽紀錄。
                    elif item == 'forward':   
                        driver.forward()#前往下一項瀏覽紀錄。
                    elif item == 'execute_script':
                        driver.execute_script(data)#執行JavaScript語法
                        #window.scrollTo(0,500) # 瀏覽器視窗捲動到 500px 位置
                        #window.open("https://192.168.127.253/asqc.asp") #瀏覽器視窗開啟分頁。
                    elif item == 'switch_to.frame':
                        driver.switch_to.frame(data)#切換frame。
                    elif item == 'switch_to.default_content':   
                        driver.switch_to.default_content()#切換frame到預設值。
                    elif item == 'switch_to.parent_frame':   
                        driver.switch_to.parent_frame()#切換frame到前一個。
                    elif item == 'switch_to.window':          
                        driver.switch_to.window(driver.window_handles[int(data)])#切換分頁。             
                    elif item == 'switch_to.alert.accept':
                        driver.switch_to.alert.accept()#點擊警告視窗確定鍵。
                    elif item == 'switch_to.alert.dismiss':
                        driver.switch_to.alert.dismiss()#點擊警告視窗取消鍵。
                    elif item == 'close': 
                        try:  
                            driver.close()# 關閉瀏覽器視窗。
                        except Exception as e:
                            raise e
                    elif item == 'quit': 
                        try:  
                            driver.quit()# 離開瀏覽器
                        except Exception as e:
                            raise e                 
                    elif item == 'WebDriverWait':   
                        if xpath: WebDriverWait(driver, float(timeout), float(freq)).until(expected_conditions.presence_of_element_located((By.XPATH, xpath)), '找不到指定的元素')
                        elif id: WebDriverWait(driver, float(timeout), float(freq)).until(expected_conditions.presence_of_element_located((By.ID, id)), '找不到指定的元素')
                    elif item == 'quit':
                        try:  
                            driver.quit()
                        except Exception as e:
                            print(e)
                    elif item == 'maximize_window':
                        driver.maximize_window()#瀏覽器視窗最大化
                    elif item == 'minimize_window':
                        driver.minimize_window()#瀏覽器視窗最小化
                    elif item == 'fullscreen_window':
                        driver.fullscreen_window()#瀏覽器視窗全屏
                    elif item == 'frame':
                        
                        driver.switch_to.frame('contents')
                        control = driver.find_element(By.XPATH, '//*[@id="folder62"]/tbody/tr/td[2]/a/font')
                        control.click()
                        control = driver.find_element(By.XPATH, '//*[@id="item65"]/tbody/tr/td[2]/a/font')
                        control.click()
                        driver.switch_to.default_content()
                        driver.switch_to.frame('main')
                        control = driver.find_element(By.XPATH, '//*[@id="file_upload"]/table[1]/tbody/tr[1]/td[2]/input')
                        control.send_keys('D:\\Ericluo Documents\\Desktop\\MultipleStationV2\\MW-AWK1132C\\MOXA\\Moxa 產測資料\\FW\\出貨\\AWK1137C_1.8_Build_23010916.rom')
                        
                    else:
                        
                        if item == 'select_by_index':
                            if xpath:
                                control = Select(driver.find_element(By.XPATH, xpath))
                            elif id:
                                control = Select(driver.find_element(By.ID, id))
                        else:
                            if xpath:
                                control = driver.find_element(By.XPATH, xpath)
                            elif id:
                                control = driver.find_element(By.ID, id).send_keys(data)
                                
                        if element :
                            if item == 'select_by_index':
                                if xpath:
                                    control = Select(driver.find_element(By.XPATH, element))
                            else:
                                if xpath:
                                    control = driver.find_element(By.XPATH, element)

                        if item == 'click':
                            control.click()#按下滑鼠左鍵。
                        elif item == 'click_and_hold':
                            control.click_and_hold()#滑鼠左鍵按著不放。
                        elif item == 'double_click':
                            control.double_click()#連續按兩下滑鼠左鍵。
                        elif item == 'context_click':
                            control.context_click()#按下滑鼠右鍵 ( 需搭配指定元素定位 )。
                        elif item == 'drag_and_drop':
                            control.drag_and_drop(source, target)#點擊 source 元素後，移動到 target 元素放開。
                        elif item == 'drag_and_drop_by_offset':
                            control.drag_and_drop_by_offset(source, int(xoffset), int(yoffset))#點擊 source 元素後，移動到指定的座標位置放開。
                        elif item == 'release':
                            control.release(data)#放開滑鼠。
                        elif item == 'send_keys':
                            control.send_keys(data)#送出某個鍵盤按鍵值。
                        elif item == 'send_keys_to_element':
                            control.send_keys_to_element(element, data)#向某個元素發送鍵盤按鍵值。
                        elif item == 'key_down':
                            control.key_down(data)#按著鍵盤某個鍵。
                        elif item == 'key_up':
                            control.key_up(data)#按著鍵盤某個鍵。
                        elif item == 'pause':
                            control.pause(int(data))#暫停動作(秒seconds)。
                        elif item == 'perform':
                            control.perform()#執行儲存的動作。
                        elif item == 'text':
                            method.Logging(config, path_current_dir, 'INFO', '{} = {}'.format(option, control.text))
                            method.ConfigAdd(config_data, section, option, control.text)#元素的內容文字。
                        elif item == 'get_attr_name':
                            method.ConfigAdd(config_data, 'Selenium', 'get_attr_name', control.get_attr_name(data))#元素的某個 HTML 屬性值。
                        elif item == 'id':
                            method.ConfigAdd(config_data, 'Selenium', 'id', control.id())#元素的 id。
                        elif item == 'tag_name':
                            method.ConfigAdd(config_data, 'Selenium', 'tag_name', control.tag_name())#元素的 tag 名稱。
                        elif item == 'size':
                            method.ConfigAdd(config_data, 'Selenium', 'size', control.size())#元素的 tag 名稱。
                        elif item == 'screenshot':
                            control.screenshot()#將某個元素截圖並儲存為 png。
                        elif item == 'select_by_index':
                            control.select_by_index(int(data))#下拉式選單選取
                        elif item == 'clear':
                            control.clear() #清除文字       
                        elif item == 'current_url':
                            method.ConfigAdd(config_data, 'Selenium', 'current_url', control.current_url())# 取得當前瀏覽器網址
                        elif item == 'current_window_handle':
                            method.ConfigAdd(config_data, 'Selenium', 'current_window_handle', control.current_window_handle())# 取得當前瀏覽器handle
                        elif item == 'title':
                            method.ConfigAdd(config_data, 'Selenium', 'title', control.title())# 取得當前瀏覽器title
                        elif item == 'is_selected':
                            result = control.is_selected()# 元素是否被選取。
                            continue
                        elif item == 'is_enabled':
                            result = control.is_enabled()# 元素是否可用。
                            continue
                        elif item == 'is_displayed':
                            result = control.is_displayed()# 元素是否顯示在網頁上。
                            continue
                        elif item == 'parent':
                            result = control.parent()# 元素的父元素。
                            continue
                
            result = True
        
    except Exception as e:
        method.Logging(config, path_current_dir, 'ERROR', '{}'.format(e))    
    finally:
        if method.PathIsExist(method.PathJoin(path_current_dir, 'STOP')) == True: result = False
        if skip_fail == 'True':
            result = True
        return result
    
if __name__ == '__main__':
    pass

    try:       

        driver = None
        
        method.FileDelete(method.PathJoin(path_current_dir, 'PASS'))
        method.FileDelete(method.PathJoin(path_current_dir, 'FAIL'))
        method.FileDelete(method.PathJoin(path_current_dir, 'STOP'))
        
        config_data = method.PyConfigParser()
        config = method.PyConfigParser()
        config.read(method.PathJoin(path_current_dir, 'config.ini'))
        #[env]
        browser = method.ConfigGet(config, 'env', 'browser', 'chrome')
        output_file_name = method.ConfigGet(config, 'env', 'output_file_name', 'output.txt')
        method.FileDelete(method.PathJoin(path_current_dir, output_file_name))
        #[logger]
        logger_file_name = method.ConfigGet(config, 'logger', 'file_name', 'sys.log')
        method.FileDelete(method.PathJoin(path_current_dir, logger_file_name))
        #[chrome_options]
        disable_notifications = method.ConfigGet(config, 'chrome_options', 'disable_notifications', 'False')#禁用彈跳視窗
        headless = method.ConfigGet(config, 'chrome_options', 'headless', 'False')#隱藏瀏覽器視窗
        maximized = method.ConfigGet(config, 'chrome_options', 'maximized', 'False')#瀏覽器視窗最大化
        minimized = method.ConfigGet(config, 'chrome_options', 'minimized', 'False')#瀏覽器視窗最小化
        ChromeDriverManager = method.ConfigGet(config, 'chrome_options', 'ChromeDriverManager', 'False')#啟用Chrome更新
        
        if browser == 'chrome':
            chrome_options = webdriver.ChromeOptions()
            if disable_notifications == 'True': chrome_options.add_argument("--disable-notifications")
            if headless == 'True': chrome_options.add_argument('--headless')
            if maximized == 'True': chrome_options.add_argument('--start-maximized')
            if minimized == 'True': chrome_options.add_argument('--start-minimized')
            chrome_options.add_argument('--ignore-certificate-errors')
            if ChromeDriverManager == 'False':
                driver = webdriver.Chrome(options=chrome_options)
            else:
                driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        elif browser == 'ie':
            ie_options = webdriver.IeOptions();
            #忽略保護模式
            ie_options.ignore_protected_mode_settings = True
            driver = webdriver.Ie(options = ie_options)
        
        result = True
        output = False
        with open(method.PathJoin(path_current_dir, 'script.txt'), newline='', encoding='utf-8') as csvfile:
            rows = csv.reader(csvfile)
            for row in rows:
                if method.PathIsExist(method.PathJoin(path_current_dir, 'STOP')) == True: 
                    result = False
                    break
                data = ', '.join(row)
                if not data or data[0] == '#': continue
                if "item' : 'text'" in data:
                    output = True
                res = eval(data)
                method.Logging(config, path_current_dir, 'INFO', '{}'.format(res))
                if RunSelenium(config, driver, config_data, **res) == False:
                    result = False
                    break
        
        if method.PathIsExist(method.PathJoin(path_current_dir, 'STOP')) == True:
            method.Logging(config, path_current_dir, 'ERROR', 'User Stop.')
             
        if result == True:
            method.FileCreate(method.PathJoin(path_current_dir, 'PASS'))
            method.Logging(config, path_current_dir, 'INFO', 'Result : PASS')
        else:
            method.FileCreate(method.PathJoin(path_current_dir, 'FAIL'))
            method.Logging(config, path_current_dir, 'INFO', 'Result : FAIL')
            
        if output == True: method.ConfigWrite(config_data, method.PathJoin(path_current_dir, output_file_name))
        
    except Exception as e:
        method.Logging(config, path_current_dir, 'ERROR', '{}'.format(e))
        pass
    
    finally:
        try:
            if driver != None:
                driver.close()# 關閉瀏覽器視窗
                driver.quit() # 離開瀏覽器
        except Exception as e:
            method.Logging(config, path_current_dir, 'ERROR', '{}'.format(e))
            
        method.Logging(config, path_current_dir, 'INFO', 'Finish.')
    
        
    #ERROR
    #unterminated string literal (detected at line 1) (<string>, line 1) //scritp 字串(string)無法轉換成字典(dict)
        
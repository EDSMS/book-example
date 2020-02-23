from selenium import webdriver

__browser_url = r'C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe'

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = __browser_url
chrome_options.add_argument(r'--lang=zh-CN')

browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get('http://localhost:8000')

assert 'Django' in browser.title


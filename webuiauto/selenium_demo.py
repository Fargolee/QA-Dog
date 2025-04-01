from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# 创建 Options 选项对象
opt = Options()
opt.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"	# 指定 Chrome 浏览器的路径

# 创建 Service 对象
ser = Service()
ser.executable_path = r"D:\Chrome\Webdriver\134\chromedriver.exe"	# 指定 ChromeDriver 的路径

# 初始化 WebDriver，使用之前创建的 Options 和 Service 对象
driver = webdriver.Chrome(options=opt, service=ser)

# 打开网页
driver.get('http://localhost/ecshop/admin/index.php')

# 关闭浏览器
# driver.quit()
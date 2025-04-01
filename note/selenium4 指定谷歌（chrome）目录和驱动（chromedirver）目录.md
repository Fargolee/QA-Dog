很多博客的`selenium`是3，会使用`chrome_options`,`chrome_options`，这样会报错，因为在4中，这两个参数已经被弃用
注：

-   在默认路径下的`chrome`会自动更新，如果是大版本更新需要重新下载对应版本的`chromedriver`
-   不在默认路径下的`chrome`则不会自动更新

环境：

-   selenium：4.19.0
    
-   python：3.12.0
    
-   windows 10
    

这里针对下列四种不同的情况，给出相应的解决方式

-   两个都不缺
-   `chrome`不是默认路径
-   缺少`chromedriver`路径（可以通过指定环境变量解决，这里给出代码解决方案）
-   两个缺少

1、`chrome`为默认路径，`chromedriver`已经设为环境变量

```python
from selenium  import webdriver

driver = webdriver.Chrome()	# 初始化 WebDriver
driver.get('http://www.baidu.com')	# 打开网页
driver.quit()	# 关闭浏览器

```

2、`chrome`不在默认路径，`chromedriver`已经设为环境变量

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 创建 Options 选项对象
opt = Options()
opt.binary_location = r'F:\Chrome\Application\chrome.exe'	# 指定 Chrome 浏览器的路径

# 初始化 WebDriver，使用之前创建 Options 对象
driver = webdriver.Chrome(options=opt)  

# 打开网页
driver.get('http://www.baidu.com')

# 关闭浏览器
driver.quit()

```

3、`chrome`为默认路径，`chromedriver`没有设为环境变量

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 创建 Service 对象
ser = Service()
ser.executable_path = r'F:\Chrome\chromedriver\chromedriver.exe'	# 指定 ChromeDriver 的路径

# 初始化 WebDriver，使用之前创建 Service 对象
driver = webdriver.Chrome(service=ser)

# 打开网页
driver.get('http://www.baidu.com')

# 关闭浏览器
driver.quit()

```

4、`chrome`不在默认路径，`chromedriver`没有设为环境变量

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# 创建 Options 选项对象
opt = Options()
opt.binary_location = r'F:\Chrome\Application\chrome.exe'	# 指定 Chrome 浏览器的路径

# 创建 Service 对象
ser = Service()	
ser.executable_path = r'F:\Chrome\chromedriver\chromedriver.exe'	# 指定 ChromeDriver 的路径

# 初始化 WebDriver，使用之前创建的 Options 和 Service 对象
driver = webdriver.Chrome(options=opt, service=ser)

# 打开网页
driver.get('http://www.baidu.com')

# 关闭浏览器
driver.quit()

```
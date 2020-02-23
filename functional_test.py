from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        __browser_url = r'C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe'
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = __browser_url
        chrome_options.add_argument(r'--lang=zh-CN')

        self.browser = webdriver.Chrome(chrome_options=chrome_options)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 伊迪丝听说有一个很酷的在线代办事项应用
        # 她去看了这个应用的首页
        self.browser.get('http://localhost:8000')

        # 她注意到网页的标题和头部都包含"To-Do"这个词
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # 应用邀她输入一个代办事项

        # 她在一个文本框中输入了"Buy peacock feathers" (购买孔雀羽毛)
        # 伊迪丝的爱好是使用假蝇做饵钓鱼

        # 她按了回车键后，界面更新了
        # 代办事项表格中显示了"1: Buy peacock feathers"

        # 界面中又显示了一个文本框可以输入其他待办事项
        # 她又输入了"User peacock feathers to make a fly" (使用孔雀羽毛做假蝇)
        # 伊迪斯做事很有条理

        # 界面再次更新，她的清单中显示了这两个待办事项

        # 伊迪斯箱知道这个网站是否会记住她的清单
        # 她看到网站为她生成了一个唯一的URL
        # 而且界面中有一些文字解说这个功能


        # 她访问那个URL，发现她的待办事项列表还在

        # 她很满意，去睡觉了

if __name__ == '__main__':
    unittest.main(warnings='ignore')
    
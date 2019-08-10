# 导包
import unittest
import HTMLTestRunnerPlugins
import time

# 获取测试用例的文件路径
test_case_dir = "./scripts"
# 获取测试报告的路径
test_report_dir = "./test_report"
# 将测试用例添加到测试套件中
discover = unittest.defaultTestLoader.discover(test_case_dir,pattern="test_*.py")
# discover = unittest.defaultTestLoader.discover(test_case_dir,pattern="test_register.py")
# 给测试报告命名
now_time = time.strftime("%Y-%m-%d %H-%M-%S")
file = open(test_report_dir+"//"+now_time+"report.html","wb")
# 执行测试并生成测试报告
runner = HTMLTestRunnerPlugins.HTMLTestRunner(title="自动化测试报告",
                                     description="详细描述",
                                     stream=file,
                                     verbosity=2,
                                     retry=0
)
runner.run(discover)
# 关闭测试报告
file.close()
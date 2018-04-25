[cn_stock_holidays](https://github.com/rainx/cn_stock_holidays) is a another repo which can help you find trade-day of market

```python
from datetime import date
import cnholiday

print(cnholiday.isHoliday(date(2018, 1, 1)))
print(cnholiday.isHoliday(date(2018, 2, 1)))
```




## Official document
- [国务院办公厅关于2018年部分节假日安排的通知](http://www.gov.cn/zhengce/content/2017-11/30/content_5243579.htm) 国办发明电〔2017〕12号
- [国务院办公厅关于2017年部分节假日安排的通知](http://www.gov.cn/zhengce/content/2016-12/01/content_5141603.htm) 国办发明电〔2016〕17号
- [国务院办公厅关于2016年部分节假日安排的通知](http://www.gov.cn/zhengce/content/2015-12/10/content_10394.htm) 国办发明电〔2015〕18号
- [国务院办公厅关于2015年部分节假日安排的通知](http://www.gov.cn/zhengce/content/2014-12/16/content_9302.htm) 国办发明电〔2014〕28号

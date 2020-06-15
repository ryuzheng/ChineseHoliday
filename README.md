# Chinese Holiday

中国节假日静态json数据

使用来替换Jubal的快捷指令「中国法定节假日自动关闹钟 1.1」中的API接口，目前调用格式 [https://cdn.jsdelivr.net/gh/ryuzheng/ChineseHoliday/holiday/年/月/日.json](https://cdn.jsdelivr.net/gh/ryuzheng/ChineseHoliday/holiday/年/月/日.json)（jsdelivr CDN，国内推荐）或者[https://raw.githubusercontent.com/ryuzheng/ChineseHoliday/master/holiday/年/月/日.json](https://raw.githubusercontent.com/ryuzheng/ChineseHoliday/master/holiday/年/月/日.json)

修改后的快捷指令链接为[中国法定节假日自动关闹钟 1.1.1](https://www.icloud.com/shortcuts/6553fb19483543b4a147bfdb06b36df2)，只修改了调用的API地址，设置方法请参考[不用羡慕安卓！iOS13.1 + 快捷指令 原生实现中国法定节假日闹钟](https://zhuanlan.zhihu.com/p/85984676)，感谢Jubal。

另外Jubal已更新基于日历的本地版本，[iOS 自定义闹钟 —— 中国法定节假日 (升级版）](https://zhuanlan.zhihu.com/p/138316230)

-----

json格式参照[http://timor.tech/api/holiday/info](http://timor.tech/api/holiday/info)的数据格式，但该接口目前已不可访问，因此自己手动生成了2020年的json；

原接口的数据定义

```json
{
  "code": 0,              // 0服务正常。-1服务出错
  "type": {
    "type": enum(0, 1, 2, 3), // 节假日类型，分别表示 工作日、周末、节日、调休。
    "name": "周六",         // 节假日类型中文名，可能值为 周一 至 周日、假期的名字、某某调休。
    "week": enum(1 - 7)    // 一周中的第几天。值为 1 - 7，分别表示 周一 至 周日。
  },
  "holiday": {
    "holiday": false,     // true表示是节假日，false表示是调休
    "name": "国庆前调休",  // 节假日的中文名。如果是调休，则是调休的中文名，例如'国庆前调休'
    "wage": 1,            // 薪资倍数，1表示是1倍工资
    "after": false,       // 只在调休下有该字段。true表示放完假后调休，false表示先调休再放假
    "target": '国庆节'     // 只在调休下有该字段。表示调休的节假日
  }
}
```

同时参考了[https://github.com/gentlyxu/holiday](https://github.com/gentlyxu/holiday)项目的json存储方式；但该项目是19年11月抓取的以上接口的数据，部分数据如国庆节前调休日期不正确，因此自行实现。

感谢[https://github.com/NateScarlet/holiday-cn](https://github.com/NateScarlet/holiday-cn)项目提供的静态节假日json文件，但该项目只保留了节假日及调休当天的信息，所以从[https://www.iamwawa.cn/holiday.html](https://www.iamwawa.cn/holiday.html)等网站补充了薪资倍数，另外手动补充调休的部分描述，具体文件参考db文件夹下的json。


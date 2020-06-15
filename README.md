# Chinese Holiday

中国节假日静态json数据

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


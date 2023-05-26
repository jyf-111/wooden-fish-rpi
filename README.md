# wooden-fish-rpi
树莓派实现的电子木鱼

![wakatime](https://wakatime.com/badge/user/cfee0eb2-658b-4917-a1ed-9801e76b961f/project/a15c4e2c-1782-4ebe-8562-53108f3a8e1f.svg)

![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)

![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)

[视频演示](https://www.bilibili.com/video/BV1zT41147gn/)

## :sparkles: Features

- :musical_keyboard: 蓝牙键盘
- :unlock: 蓝牙配对免pin
- :game_die: 多进程,多线程,协程
- :bread: 使用`python-dotenv`读取环境变量

## :zap: Requirements

| 物料清单          | 
| ----------------- | 
| 树莓派4b          | 
| 真实木鱼一个      | 
| rfp402压力传感器+信号转换模块  | 
| pcf8591数模转换器 | 
| ws2812b灯带       | 


```                                                 
 rfp402       pcf8591               树莓派                      ws2812b
┌─────┐    ┌─────────────┐   ┌─────────────────┐              ┌─────────┐
                              +3V           +5V ────┬───────┐            
  AO  ───── AIN0      SDA ─── P02[SDA1]     +5V ────^────┐  └──── red    
  DO        AIN1      SCL ─── P03[SCL1]     GND ────^──┬─^──┐     
  GND ────┐ AIN2      VCC ──┐  ...          ...     │  │ │  └──── white
  VCC ──┐ │ AIN3      GND ──^─ GND          P18 ────^──^─^──┐
        │ │ AOUT            │                       │  │ │  └──── green
        │ │ INPUT0          │                       │  │ │
        │ │ INPUT1          │                       │  │ │
        │ │ INPUT2          │                       │  │ │
        │ │ GND             └───────────────────────┘  │ │
        │ │ GND                                        │ │
        │ └────────────────────────────────────────────┘ │
        └────────────────────────────────────────────────┘
```

## :rocket: Run

```bash
sudo apt install -y bluetooth pi-bluetooth bluez blueman
sudo apt install -y libdbus-1-dev libcairo2-dev libgirepository1.0-dev
sudo pip3 install -r requirements.txt
sudo raspi-config # 选择 i2c 和 serial port 开启

cd wooden-fish-rpi
sudo ./run.sh
```

## :bulb: Note

- 运行项目前请确保蓝牙正常使用
- 如果不指定环境变量`FILENAME`,默认输出文本为`woodfish`目录下每个文件的代码
所有支持的环境变量[.env.example](./.env.example)
- 同一设备第二次连接木鱼蓝牙需要把之前的配对记录删除

## :green_heart: Thanks

- [`feiyirenPt`](https://github.com/feiyirenPt)和他的朋友们提供的资金支持

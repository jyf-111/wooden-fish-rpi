---
# try also 'default' to start simple
theme: seriph
# random image from a curated Unsplash collection by Anthony
# like them? see https://unsplash.com/collections/94734566/slidev
background: https://source.unsplash.com/collection/94734566/1920x1080
# apply any windi css classes to the current slide
class: 'text-center'
# https://sli.dev/custom/highlighters.html
highlighter: shiki
# show line numbers in code blocks
lineNumbers: false
# some information about the slides, markdown enabled
info: |
  ## Slidev Starter Template
  Presentation slides for developers.

  Learn more at [Sli.dev](https://sli.dev)
# persist drawings in exports and build
drawings:
  persist: false
# page transition
transition: slide-left
# use UnoCSS
css: unocss
---
# 基于压力反馈的电子木鱼

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Press Space for next page <carbon:arrow-right class="inline"/>
  </span>
</div>

---
layout: image-right
image: https://ae01.alicdn.com/kf/HTB1TEjqQXXXXXXHXVXXq6xXFXXXb/3-3V-5V-MB102-Breadboard-power-module-MB-102-830-points-Solderless-Prototype-Bread-board-kit.jpg
---

# 连接面包板

<br>
<br>

- 在准备好所需材料后，接下来需要将它们连接到面包板上。

- 将面包板连接到树莓派的 GPIO 引脚上，使用杜邦线来连接。

- 连接完所有的元件后，检查连接来验证电路是否正确连接。


---
transition: fade-out
---

# 准备材料

<br>

在制作电子木鱼之前，需要准备以下材料：
| 材料           | 用途                                     |
| -------------- | ---------------------------------------- |
| **树莓派**     | 整个项目的实现平台                       |
| **面包板**     | 使电路设计和调试变得更加方便             |
| **压力传感器** | 将压力转化为电信号输出，以便于测量和控制 |
| **LED 灯**     | 使用 LED灯来计数                         |
| **蜂鸣器**     | 发出周期性振动声音                       |
| **杜邦线**     | 在面包板中使用杜邦线连接各个元件         |
| **外壳**       | 构成木鱼外壳                             |

---
transition: slide-up

level: 2
---
<style>
li {
  font-size: 1em;
}
blockquote {
  code {
    @apply text-teal-500 dark:text-teal-400;
  }
}
</style>

# 编写程序

<br>

- 在连接完所有的元件后，接下来需要编写程序来控制电子木鱼的运行。
- 可以使用 Python 编写控制程序，程序可以在树莓派上运行，并通过 GPIO 引脚来控制各个元件


```py
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)  # 设置GPIO引脚编号方式
GPIO.setwarnings(False)  # 禁用警告提示

pressure_pin = 11  # 压力传感器连接的GPIO引脚
GPIO.setup(pressure_pin, GPIO.IN)  # 设置GPIO引脚为输入模式

while True:
    if GPIO.input(pressure_pin) == GPIO.HIGH:  # 如果传感器输出高电平
        print("有压力")
    else:
        print("无压力")
    time.sleep(0.1)  # 暂停0.1秒，避免读取速度过快
```

---
class: px-20
---

# 添加随机变化

<br>

为了让电子木鱼更加有趣和生动，我们可以添加一些随机变化。
例如，可以使用 Python 的 random 模块生成随机数，并根据随机数的值来改变 LED 灯和蜂鸣器的状态。

```py
import RPi.GPIO as GPIO
import random

GPIO.setmode(GPIO.BCM) # 设置 GPIO 模式为 BCM
led_pin = 18 # 设置 GPIO 引脚号
buzzer_pin = 23
GPIO.setup(led_pin, GPIO.OUT) # 设置 GPIO 引脚为输出
GPIO.setup(buzzer_pin, GPIO.OUT)

while True: # 生成随机数并控制 LED 灯和蜂鸣器的状态
    random_num = random.random()
    if random_num < 0.5:
        GPIO.output(led_pin, GPIO.HIGH)
        GPIO.output(buzzer_pin, GPIO.HIGH)
    else:
        GPIO.output(led_pin, GPIO.LOW)
        GPIO.output(buzzer_pin, GPIO.LOW)
    time.sleep(1)
```

---
layout: image-right
image: https://th.bing.com/th/id/OIP.Pszy-JD0Dq8D-9IBVIYDPAHaFe
---

# 连接扬声器

<br>

要连接扬声器，需要使用一个数字输出引脚，并使用一个放大器来放大树莓派输出的信号。

- 连接树莓派的 GPIO 引脚到音频放大器电路板的输入端。
- 连接电路板的输出端到扬声器的正负极。
- 在程序中使用 GPIO 引脚来输出音频信号。

---

# 使用电子木鱼

<br>

![muyu](https://image.lceda.cn/avatars/2022/6/WNa594jMw2gmVbQKL0PfbAhiWasgkQDx6I2I0EgG.png)
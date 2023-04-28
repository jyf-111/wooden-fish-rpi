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
# 基于压力反馈的--电子木鱼制作

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Press Space for next page <carbon:arrow-right class="inline"/>
  </span>
</div>

---
transition: fade-out
---

# 准备材料

在制作电子木鱼之前，需要准备以下材料：

- **树莓派**
- **面包板**
- **压敏电阻**
- **LED 灯**
- **蜂鸣器**
- **按键**
- **杜邦线**

<br>
<br>

---
layout: default
---

# 连接面包板

- 在准备好所需材料后，接下来需要将它们连接到面包板上。
- 将面包板连接到树莓派的 GPIO 引脚上，可以使用杜邦线来连接。确保正确地连接元件和面包板，并按照电路图进行正确的连接。
- 连接完所有的元件后，检查连接来验证电路是否正确连接。

---
transition: slide-up

level: 2
---

# 编写程序

- 在连接完所有的元件后，接下来需要编写程序来控制电子木鱼的运行。
- 可以使用 Python 编写控制程序，程序可以在树莓派上运行，并通过 GPIO 引脚来控制各个元件

---
class: px-20
---

# 添加随机变化

为了让电子木鱼更加有趣和生动，我们可以添加一些随机变化。
例如，可以使用 Python 的 random 模块生成随机数，并根据随机数的值来改变 LED 灯和蜂鸣器的状态。

---

# 连接扬声器

要连接扬声器，需要使用一个数字输出引脚，并使用一个放大器来放大树莓派输出的信号。

- 连接树莓派的 GPIO 引脚到音频放大器电路板的输入端。
- 连接电路板的输出端到扬声器的正负极。
- 在程序中使用 GPIO 引脚来输出音频信号。

---

# 使用电子木鱼

![muyu](https://image.lceda.cn/avatars/2022/6/WNa594jMw2gmVbQKL0PfbAhiWasgkQDx6I2I0EgG.png)

---
layout: end
---

# 总结

- 使用树莓派制作电子木鱼
- 连接面包板、LED灯、蜂鸣器、按键等元件
- 使用Python编写控制程序，添加随机变化
- 连接扬声器，开始使用电子木鱼

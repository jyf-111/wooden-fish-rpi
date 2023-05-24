# wooden-fish-rpi
树莓派实现的电子木鱼

![wakatime](https://wakatime.com/badge/user/cfee0eb2-658b-4917-a1ed-9801e76b961f/project/a15c4e2c-1782-4ebe-8562-53108f3a8e1f.svg)

![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)
![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)

## Run

```bash
sudo apt install -y bluetooth pi-bluetooth bluez blueman
sudo apt install -y libdbus-1-dev libcairo2-dev libgirepository1.0-dev
sudo pip3 install -r requirements.txt
sudo raspi-config # 选择 i2c 和 serial port 开启

cd wooden-fish-rpi
sudo python3 woodfish/main.py
```

## Reference

- https://oshwhub.com/oldtreee/dian-zi-mu-yu

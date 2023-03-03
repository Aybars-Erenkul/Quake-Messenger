# Quake-Messenger
![Made With Python](http://ForTheBadge.com/images/badges/made-with-python.svg) ![Made with love](http://ForTheBadge.com/images/badges/built-with-love.svg)

Quake Messenger scrapes the Turkey's earthquake data from a trusted source, and then uses Selenium to automate the process of sending messages through the WhatsApp Web interface. With this program, you can stay up-to-date on any seismic activity that may affect you or your loved ones.

The program is easy to use and can be customized to your preferences. You can specify the minimum magnitude threshold for alerts, as well as the method of receiving notifications. The notifications include important details such as the location, magnitude, and time of the earthquake.

## Turkish
Quake Messenger, Turkiye'deki deprem verilerini güvenilir bir kaynaktan alır ve ardından WhatsApp Web arabirimi aracılığıyla mesaj gönderme sürecini otomatikleştirmek için Selenium'u kullanır. 

Programın kullanımı kolaydır ve tercihlerinize göre özelleştirilebilir. Uyarılar için minimum büyüklük eşiğini ve ayrıca bildirim alma yöntemini belirleyebilirsiniz. Bildirimler, depremin yeri, büyüklüğü ve zamanı gibi önemli detayları içeriyor.

## Requirements
```bash
beautifulsoup4==4.11.2
gTTS==2.3.1
PyQt6==6.4.2
requests==2.28.2
selenium==4.8.2
webdriver_manager==3.8.5
```

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install necessary libraries.

```bash
pip install -r requirements.txt
```

## Usage

```bash
python quake_messenger.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.


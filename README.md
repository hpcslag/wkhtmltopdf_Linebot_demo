
# Installation

#### pip: imgkit

```
pip3 install imgkit
```

#### wkhtmltopdf

CentOS install guide:

https://gist.github.com/apphancer/8654e82aa582d1cf02c955536df06449

Checklist:

 - wkhtmltopdf command is worked (mind: source .bashrc link bin path of `wkhtmlpdf`)
 - chinese or other language font is installed (refer: https://github.com/wkhtmltopdf/wkhtmltopdf/issues/2886)
 ```
 yum install wqy-zenhei-fonts
 ```
 - warring the `python` img file path, if you use `//xxxxdakamaized.net/images/xxxx.jpg`, please change to `https://`

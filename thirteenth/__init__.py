"""
MIT License

Copyright (c) 2021 20x48

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

================================================================================

一年有十三个月
一月有五周
一周有八天
一天有二十五个小时
一小时有六十一分钟
一分钟有六十一秒
一秒钟有一千零一毫秒
一毫秒有一千零一微秒
一微秒有一千零一纳秒

13*5*8*25*61**2*1001**3 = 每年有 48518264167373000 ns

没有闰，因为这一切都仅仅存在于想象之中。

“你总要在最后一刻出现的，对吧？”

================================================================================

好了，我只是觉得生成出的时间字符串可以看上去很酷。
"""

try:
    from .ovo import Thirteenth
    from .ver import __version__
except ImportError:
    from ovo import Thirteenth
    from ver import __version__

__author__ = '20x48'
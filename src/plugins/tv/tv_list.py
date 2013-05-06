#! /usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (C) 2013 XXX, Inc.
#               2013 www.bsyx.net
#
# Author:   王波 <249772961@qq.com>
# Maintainer:  王波 <249772961@qq.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

cn_tv = \
'''
CCTV5体育 = mms://112.230.192.196/zb10,
江苏卫视 = mms://112.230.192.196/zb11,
凤凰卫视资讯台 = mms://112.230.192.196/zb12,
上海卫视 = mms://112.230.192.196/zb17,
济南新闻 = mms://112.230.192.196/zb20,
济南都市 = mms://112.230.192.196/zb21,
济南影视 = mms://112.230.192.196/zb22,
济南娱乐 = mms://112.230.192.196/zb23,
济南生活 = mms://112.230.192.196/zb24,
济南商务 = mms://112.230.192.196/zb25,
济南少儿 = mms://112.230.192.196/zb26,
厦门卫视 = mms://mediasrv2.iptv.xmg.com.cn/tvhaixia,
厦门新闻 = mms://mediasrv2.iptv.xmg.com.cn/tvxinwen,
厦门纪实 = mms://mediasrv2.iptv.xmg.com.cn/tvjishi,
厦门生活 = mms://mediasrv2.iptv.xmg.com.cn/tvshenghuo,
厦门影视 = mms://mediasrv2.iptv.xmg.com.cn/tvyingshi,
青岛新闻综合频道 = mms://221.0.188.40/35,
青岛生活频道 = mms://221.0.188.40/37,
青岛影视 = mms://221.0.188.40/38,
CCTV新闻 = mms://221.0.188.40/39,
青岛党建 = mms://221.0.188.40/40,
长春一 = mms://221.8.74.26:8080,
长春三 = mms://221.8.74.28/ctv,
烟台一台 = mms://av1.jiaodong.net/tv1,
烟台二台 = mms://av1.jiaodong.net/tv2,
湖州新闻综合 = mms://live.hugd.com/xwzh.wmv,
湖州公共民生 = mms://live.hugd.com/ggms.wmv,
湖州文化娱乐 = mms://live.hugd.com/whyl.wmv,
东南卫视 = mms://video.fjtv.net/setv,
福建综合 = mms://video.fjtv.net/fjtv1,
福建公共 = mms://video.fjtv.net/fjtv3,
福建新闻 = mms://video.fjtv.net/fjtv4,
福建都市 = mms://video.fjtv.net/fjtv6,
福建经济 = mms://video.fjtv.net/fjtv7,
海峡卫视 = mms://video.fjtv.net/fjtv10,
延边网络台 = mms://202.111.175.222/playlist
'''

if __name__ == "__main__":
    for url in cn_tv.split(","):
        print url
    

# 多线程下载youtube高清视频(+字幕)和封面
## 主要的库和工具youtube-dl ，ffmpeg(搭配使用，将音频和视频自动整合)

### 项目安装
1.将需要下载的链接地址放在url.txt，每行一条

2.运行 python youtube.py

3.视频、封面默认保存在download目录下，可在代码中修改目录

4.默认支持3个视频同时下载，可修改参数 THREAD_POOSIZE

### youtube-dl食用方法 https://github.com/ytdl-org/youtube-dl
    
### 1.安装python
推荐3.7以上版本

### 2.下载youtube-dl
下载地址：https://github.com/rg3/youtube-dl/releases

### 3.安装ffmpeg
可选，不安装的话视频、音频将不会自动合并。

### 4.用法
使用帮助命令查看其用法：

youtube-dl -h

一些常用的参数：

youtube-dl --list-extractors  #查看支持网站列表
youtube-dl -U  #程序升级
youtube-dl --get-format URL #获取视频格式
youtube-dl -F URL #获取所有格式（目前仅支持YouTube），例如：

 

youtube-dl -F http://www.youtube.com/watch?v=n-BXNXvTvV4
 

[youtube] Setting language

[youtube] n-BXNXvTvV4: Downloading video webpage

[youtube] n-BXNXvTvV4: Downloading video info webpage

[youtube] n-BXNXvTvV4: Extracting video information

Available formats:

37      :       mp4     [1080x1920]

46      :       webm    [1080x1920]

22      :       mp4     [720x1280]

45      :       webm    [720x1280]

35      :       flv     [480x854]

44      :       webm    [480x854]

34      :       flv     [360x640]

18      :       mp4     [360x640]

43      :       webm    [360x640]

5       :       flv     [240x400]

36      :       3gp     [240x320]

17      :       3gp     [144x176]

137     :       mp4     [1080p] (DASH Video)

136     :       mp4     [720p] (DASH Video)

135     :       mp4     [480p] (DASH Video)

134     :       mp4     [360p] (DASH Video)

133     :       mp4     [240p] (DASH Video)

160     :       mp4     [192p] (DASH Video)

141     :       mp4     [256k] (DASH Audio)

172     :       webm    [256k] (DASH Audio)

140     :       mp4     [128k] (DASH Audio)

171     :       webm    [128k] (DASH Audio)

139     :       mp4     [48k] (DASH Audio)

第一栏数字用来选择下载具体某个音视频格式

youtube-dl -f format URL #下载指定格式的视频，这里以下载1080p原画质量的视频格式为例:

youtube-dl -f 137 http://www.youtube.com/watch?v=n-BXNXvTvV4

### 5.代理
推荐使用SS代理。非全局模式，请在命令后面加  --proxy ‘socks5://127.0.0.1:1080‘  (1080是端口号，我的端口是1080，您的端口请按照您自己设置的填写)

例如： youtube-dl --proxy ‘socks5://127.0.0.1:1080‘ [URL] 

注：2016年4月以前的版本是不支持socks代理的，具体过程请见：https://github.com/rg3/youtube-dl/issues/402

### 6.下载YouTube视频
1) 查看视频所有类型,只看不下载
youtube-dl -F [url]
或者
youtube-dl --list-formats [url]

这是一个列清单参数，执行后并不会下载视频，但能知道这个目标视频都有哪些格式存在，这样就可以有选择的下载啦！

### 7.关于音频和视频的合并
下载指定质量的视频和音频并自动合并
youtube-dl -f [format code] [url]

通过上一步获取到了所有视频格式的清单，最左边一列就是编号对应着不同的格式.
由于YouTube的1080p及以上的分辨率都是音视频分离的,所以我们需要分别下载视频和音频,可以使用137+140这样的组合.
如果系统中安装了ffmpeg的话, youtube-dl 会自动合并下下好的视频和音频, 然后自动删除单独的音视频文件

### 8.下载字幕
youtubd-dl --write-sub [url] //这样会下载一个vtt格式的英文字幕和mkv格式的1080p视频下来
youtube-dl --write-sub --skip-download [url] //下载单独的vtt字幕文件,而不会下载视频
youtube-dl --write-sub --all-subs [url] //下载所有语言的字幕(如果有的话)
youtube-dl --write-auto-sub [url] //下载自动生成的字幕(YouTube only)

### 9.关于youtube的字幕接口
获取所有语言的字幕列表：‘http://video.google.com/timedtext?hl=en&v=hRfHcp2GjVI&type=list‘
获取字幕，在视频有官方字幕的情况下：‘http://www.youtube.com/api/timedtext?lang=%s&v=%s&name=%s‘

「上传字幕」和「机器字幕」是不互相「兼容」的，有「上传字幕」的视频是没有「机器字幕」的，当然一个视频也可能「上传字幕」和「机器字幕」都没有

### 10.webvtt字幕转srt字幕方法
直接修改后缀名：直接将*.vtt文件的后缀名改为*.srt。然后删除最前方的类型标识符：WEBVTT，保存即可载入srt字幕正常使用。
附上知乎讨论贴：https://www.zhihu.com/question/29789259

 

### 11.直接使用youtubd-dl转字幕的方法

youtubd-dl 自带一个  --convert-subs FORMAT  参数。

具体用法见例子：

youtube-dl -f 137+140  --convert-subs "srt" --all-subs https://www.youtube.com/watch?v=hRfHcp2GjVI
需要注意的是，不能带上 --skip-download 参数。

详见：https://github.com/rg3/youtube-dl/issues/9073


### 12.下载视频列表
youtube-dl -f [format code] [palylist_url] //这种方式可以下载制定清晰度的mp4视频
youtube-dl [playlist_url] //下载视频列表,这种方式下载的视频可能是mkv格式或者webm格式
youtube-dl -cit [playlist_url] //下载视频列表,这种方式下载的视频可能是mkv格式或者webm格式
youtube-dl --yes-playlist [url] //当链接为视频列表,则下载该列表视频,跟上面的一样,可能是mkv或者webm格式


youtube-dl支持的网站很多,大家可以从作者整理的这个列表里查看支持的网站(不过由于有的网站接口改变,可能当初支持的网站现在不能很好的支持了),如果您要下载的视频网站现在不能用youtube-dl下载的,不妨试试另外一个同样基于Python开发的下载工具You-Get

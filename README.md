# ResetProvisioningProfileTool
用于清空iOS Provisioning Profiles文件下的所有文件
## Getting Started
我们在苹果开发者中心新添加一台测试设备的 UDID 之后，紧接着打出一份 Adhoc 包，却发现新添加的设备还是无法安装。这是因为 Xcode 没有及时更新云端的 Provisioning Profile。这时可以清除本地目录 ~/Library/MobileDevice/Provisioning 下的所有内容，然后打包时勾选 Automatically manage signing 选项，Xcode会自动下载云端的最新 Provisioning Profile。
[传送门](https://weibo.com/3656155132/G8cQfkXFz?type=comment) - 原问题链接
### How to use
In terminal
```
python resetProvisioningProfile.py
```
## Built With
Python 2.7.10 

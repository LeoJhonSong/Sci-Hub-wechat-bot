#! /usr/bin/env python3
import os
import glob
import itchat


# check fo cache folder
if not os.path.exists('./cache'):
    os.system('mkdir cache')

# for private message
@itchat.msg_register(itchat.content.TEXT)
def private_download_paper(msg):
    if msg.text[:2] == '下载':
        print('正在下载!')
        itchat.send_msg(msg='正在下载!', toUserName=msg.fromUserName)
        os.system('./scihub.py -o cache -d ' + msg.text[2:])
        fileDir = glob.glob('./cache/*.pdf')[0]
        itchat.send_file(fileDir, msg.fromUserName)
        os.system('rm -rf ./cache/*')
        print('已发送')


# for group message
@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def group_download_paper(msg):
    if msg.isAt:
        # if '下载' in msg.text:
        print('正在下载!')
        msg.user.send_msg(msg='正在下载!')
        os.system('./scihub.py -o cache -d ' + msg.text[msg.text.find('下载') + 2:])
        fileDir = glob.glob('./cache/*.pdf')[0]
        itchat.send_file(fileDir)
        os.system('rm -rf ./cache/*')
        print('已发送')


itchat.auto_login(enableCmdQR=2)
itchat.run()

# coding: utf-8
#ライブラリの読み込み
from slackbot.bot import Bot

def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    #実行したときにターミナルにメッセージを表示させる
    print('*** start slackbot ***') 
    main()

# coding: utf-8

# *** 時間を確認する ***
# ライブラリの読み込み
from slackbot.bot import respond_to # @botname: で反応するデコレータ
from slackbot.bot import listen_to # チャネル内発言で反応するデコレータ
from slackbot.bot import default_reply # 該当する応答がない場合に反応するデコレータ
import datetime #現在日時を取得する

#メンションするとき
@respond_to('いまなんじ？')
# 「現在時刻」のときのみメンションなしで応答
@listen_to('現在時刻')
def mention_func(message):
  # 現在日時を取得
  dt_now = datetime.datetime.now()
  # メンションをつけて現在の時刻を投稿
  message.reply('現在の時刻は ' + dt_now.strftime('%H時%M分%S秒') + ' です！') 

#メンションしないとき
@listen_to('いまなんじ？')
def listen_func(message):
  # 通常の投稿
  message.send('時間を知りたいのですか？')
  # 相手にメンションをつけて投稿
  message.reply('メンションをつけて聞いてください')

# *** 天気を確認する ***
# 作成した天気情報モジュールを読み込む
import weather

#メンションありで天気を聞く
#京都の天気(デフォルトは京都)
@respond_to('京都の天気')
@respond_to('今日の天気')
def whether_1(message):
    w = weather.get_weather(260010)
    t = w['forecasts'][0]
    # 相手にメンションをつけて投稿
    message.reply('今日の京都の天気は ' + t['telop'] + ' です！') 

#東京の天気
@respond_to('東京の天気')
def whether_1(message):
    w = weather.get_weather(130010)
    t = w['forecasts'][0]
    # 相手にメンションをつけて投稿
    message.reply('今日の東京の天気は ' + t['telop'] + ' です！') 

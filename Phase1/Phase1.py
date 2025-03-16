from ast import Continue
import time
import random

class Def_Constants:

  @staticmethod
  def playLevelValidation(playLevel, playerName):
    if playLevel == "Level1" or playLevel == "Level１":

      print("Level1用キャラクターステータスを設定しています...")
      # Level1用敵キャラクターステータス設定
      eHP = 1000
      eATName = ["破砕の一撃", "雷鳴斬", "頭突き", "くっつき"]
      eATP = [150, 90, 100, 200]
      print(f"敵のHPは{eHP}です。")

      # Level1用自キャラクターステータス設定
      mHP = 3000
      mATName = ["疾風斬", "雷鳴撃", "氷結拳", "火焰斬"]
      mATP = [110, 200, 140, 115]
      print(f"あなたのHPは{mHP}です。")

      time.sleep(3)
      print("キャラクターステータスの設定が完了しました。Level1で遊びます。")
      play_Game = PlayBody(mHP, mATName, mATP, eHP, eATName, eATP, playerName)
      play_Game.PlayOP1()
      return True

    elif playLevel == "Level2" or playLevel == "Level２":
      print("Level2用キャラクターステータスを設定しています...")
      # Level2用敵キャラクターステータス設定
      eHP = 3000
      eATName = ["大地の怒り", "火焰の呪文", "氷結の旋律", "闇夜の呪縛"]
      eATP = [500, 600, 200, 300]

      # Level2用自キャラクターステータス設定
      mHP = 5000
      mATName = ["聖光の祈り", "風精の加護", "覇王の爪", "不死の突撃"]
      mATP = [200, 40, 50, 250]

      time.sleep(3)
      print("キャラクターステータスの設定が完了しました。Level2で遊びます。")
      play_Game = PlayBody(mHP, mATName, mATP, eHP, eATName, eATP, playerName)
      play_Game.PlayOP1()
      return True
    elif playLevel == "Level3" or playLevel == "Level３":
      print("Level3用キャラクターステータスを設定しています...")
      # Level3用敵キャラクターステータス設定
      eHP = 4000
      eATName = ["連撃の舞", "爆裂斬", "大地を割る一撃", "猛進アタック"]
      eATP = [600, 700, 300, 400]

      # Level3用自キャラクターステータス設定
      mHP = 7000
      mATName = ["ファイアボール", "氷結の霧", "雷撃", "暗黒の波動"]
      mATP = [300, 50, 60, 350]
      time.sleep(3)
      print("キャラクターステータスの設定が完了しました。Level3で遊びます。")
      play_Game = PlayBody(mHP, mATName, mATP, eHP, eATName, eATP, playerName)
      play_Game.PlayOP1()
      return True
    else:
      print("レベル１～３で入力をしてください。もしくは、スペルミスによりレベル選択ができませんでした。")
      return False

class PlayBody:
  def __init__(self, mHP, mATName, mATP, eHP, eATName, eATP, playerName):
    self.mHP = mHP
    self.mATName = mATName
    self.mATP = mATP
    self.eHP = eHP
    self.eATName = eATName
    self.eATP = eATP
    self.playerName = playerName

  def PlayOP1(self):
    while self.eHP > 0 and self.mHP > 0:
      print("攻撃する技名を選んでください。")
      for index1, attack1 in enumerate(self.mATName, 1):
        print(f"{index1}: {attack1}")

      try:
        choice = int(input("選んだ攻撃技の番号を入力してください：")) -1
        if 0 <= choice < len(self.mATName):
          critical_Attack = random.randrange(100)
          if critical_Attack < 50:
            self.eHP -= self.mATP[choice]
            print(f"敵に{self.mATP[choice]}のダメージを与えました。")
            print(f"敵の残HPは{self.eHP}です。")
            if self.eHP <= 0:
              print("あなたの勝利です！")
              break
          else:
            self.eHP -= self.mATP[choice] + critical_Attack
            print(f"クリティカルヒット！敵に{self.mATP[choice] + critical_Attack}のダメージを与えました。")
            if self.eHP <= 0:
              print("あなたの勝利です！")
              break

        print("敵の攻撃ターンです。")

        for index2, attack2 in enumerate(self.eATName, 1):
          print(f"{index2}: {attack2}")

        enemy_Attack = random.randrange(4)
        if 0 <= enemy_Attack < len(self.eATName):
          enemy_Critical_Attack = random.randrange(100)
          if enemy_Critical_Attack < 50:
            self.mHP -= self.eATP[enemy_Attack]
            print(f"敵は{self.playerName}に{self.eATP[enemy_Attack]}のダメージを与えました。")
            if self.mHP <= 0:
              print("敵の勝利です。")
              break

          else:
            self.mHP -= self.eATP[enemy_Attack] + enemy_Critical_Attack
            print(f"クリティカルヒット！{self.playerName}に{self.eATP[enemy_Attack] + enemy_Critical_Attack}のダメージを与えました。")
            if self.mHP <= 0:
              print("敵の勝利です。")
              break

      except ValueError:
        print("無効な入力です。1～4の数字を入力してください。")

class Initialize:
  # Tabataスラッシャーズプレイ概要説明
  print("===============================================================================================================================================")
  print("ようこそ！Tabataスラッシャーズへ")
  print("このゲームは「IT・プログラミング勉強会」で扱うPh1演習課題である「ハクスラを作ってみよう」のサンプルプログラムとなります。")
  print("プレイヤーは開発者であるあなた！ゲームバランスの調整やゲーム全体のカスタマイズ、世界観の構築は全てあなた次第です！！")
  print("より高いレベルのプログラミングスキル獲得に向けて楽しみながらPython言語を学習していきましょう！！")
  print("===============================================================================================================================================")

  # 要求レベル及び要件定義概要説明
  print("")
  print("===============================================================================================================================================")
  print("■ 要求されるプログラミングスキルレベル")
  print("   Python初学者")
  print("   プログラミングの3大処理であり基礎中の基礎のレベルである以下項目をマスターしていただきます。")
  print("     １：逐次処理")
  print("         - プログラミングの世界ではできて当たり前とされる上から下に順番に実行される処理方式")
  print("     ２：繰り返し処理")
  print("         - ある特定の条件下で繰り返し同じ条件で同じ処理を繰り返すことができる処理方式")
  print("     ３：条件分岐処理")
  print("         - ある特定の条件式に従い「真」ならAの処理を、「偽」ならBの処理を実行することができる処理方式")
  print("")
  print("■ 皆さんに作っていただく「Tabataスラッシャーズ」のゲーム概要")
  print("   １：自らが操作するキャラクターのニックネームをコンソールより入力できること")
  print("   ２：自らが操作するキャラクターと敵キャラクターを戦わせて、どちらかのHP（ヒットポイント）が0になったらプログラムを終了すること")
  print("   ３：敵キャラクター、自らが操作するキャラクターの攻撃時、クリティカルヒットを乱数で調整することができること")
  print("以上")
  print("===============================================================================================================================================")

  # プレイヤー名コンソール入力
  playerName = input("プレイヤー名を入力してください。：")

  # プレイレベルコンソール入力
  for attempt in range(2):
    playLevel = input("RPGのプレイレベルを選択してください。（Level1, Level2, Level3）：")

    # プレイレベルバリデーション関数呼び出しプレイキャラクターステータス調整
    if Def_Constants.playLevelValidation(playLevel, playerName):
      break
    else:
      if attempt == 1:
        print("処理を中断します。")
        break
      print("再度プレイレベルを選択してください。")

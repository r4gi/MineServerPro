import os
import requests
from datetime import datetime

def download_server(server_type, version, folder_path, ram_size):
    try:
        # サーバータイプを小文字に変換
        server_type = server_type.lower()

        # サーバータイプに基づいてURLを設定
        if server_type == "paper":
            url = f"https://api.papermc.io/v2/projects/paper/versions/{version}/builds/121/downloads/paper-{version}-121.jar"
        elif server_type == "fabric":
            url = f"https://meta.fabricmc.net/v2/versions/loader/{version}/0.16.10/1.0.1/server/jar"
        else:
            print(f"サーバータイプ「{server_type}」はサポートされていません。")
            return

        # ダウンロードを開始
        print(f"ダウンロード開始: {url}")
        response = requests.get(url)
        response.raise_for_status()  # ステータスコードが200でない場合、エラーを発生させる

        # ダウンロードしたファイルを指定フォルダに保存
        os.makedirs(folder_path, exist_ok=True)  # フォルダが存在しない場合は作成
        server_file = os.path.join(folder_path, f"{server_type}_{version}.jar")
        with open(server_file, 'wb') as file:
            file.write(response.content)

        print(f"{server_type.capitalize()} サーバーが正常にダウンロードされ、フォルダに配置されました: {folder_path}")

        # eula.txtを生成
        create_eula_file(folder_path)

        # run.batを生成
        create_run_bat(folder_path, server_file, ram_size)
        return server_file  # ダウンロードしたファイルのパスを返す

    except requests.exceptions.RequestException as e:
        print(f"エラーが発生しました: {e}")
        return None

def create_eula_file(folder_path):
    try:
        eula_content = (
            "#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://aka.ms/MinecraftEULA).\n"
            f"#{datetime.utcnow().strftime('%a %b %d %H:%M:%S UTC %Y')}\n"
            "eula=true\n"
        )
        eula_path = os.path.join(folder_path, "eula.txt")
        with open(eula_path, 'w') as eula_file:
            eula_file.write(eula_content)
        print(f"eula.txt が生成されました: {eula_path}")
    except Exception as e:
        print(f"eula.txt の生成中にエラーが発生しました: {e}")
        
def create_run_bat(folder_path, jar_file, ram_size):
    try:
        # RAMサイズを指定したバッチファイルの内容
        bat_content = f"java -Xmx{ram_size}G -Xms{ram_size}G -jar {os.path.basename(jar_file)}\n"
        bat_content += "pause\n"  # コンソールを閉じないためにpauseを追加
        run_bat_path = os.path.join(folder_path, "run.bat")
        with open(run_bat_path, 'w') as bat_file:
            bat_file.write(bat_content)
        print(f"run.bat が生成されました: {run_bat_path}")
    except Exception as e:
        print(f"run.bat の生成中にエラーが発生しました: {e}")

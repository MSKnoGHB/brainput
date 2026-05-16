#OS指定
FROM ubuntu:26.04 

#Pythonインストール
RUN apt update && apt install -y \
  python3 \
  python3-pip \
  python3-venv \
  && rm -rf /var/lib/apt/lists/*

#仮想環境を作成・有効化
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

#作業ディレクトリを作成
WORKDIR /app

#コンテナにコピー(requirementsファイル)
COPY requirements.txt .

#ライブラリをインストール(requirementsファイル内記載部)
RUN pip install -r requirements.txt

#ソースコードをコンテナにコピー
COPY . .

#Django起動
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
#Python3で実行  manage.pyを使用  runserverコマンドで  どこからでもアクセス可能

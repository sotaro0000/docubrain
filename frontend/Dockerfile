FROM node:20-slim

WORKDIR /app

# パッケージ定義をコピーしてインストール
COPY package*.json ./
RUN npm install

# ソースコードをコピー
COPY . .

# 開発サーバー起動
CMD ["npm", "run", "dev"]
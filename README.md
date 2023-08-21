# addresss-to-coordinate
住所データから緯度経度を取得する

## Requirements
- Poetry
- Google Map API Key
    - https://developers.google.com/maps/documentation/javascript/get-api-key?hl=ja

## Usage
住所データを標準入力する

```
poetry install
export = GOOGLE_API_KEY="<YOUR GOOGLE API KEY>"
cat <住所データ.txt> | poetry run python main.py
```

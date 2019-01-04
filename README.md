# json_viewer

特定の形式のJsonファイルを閲覧するサイト。  
形式はdata/sample.jsonを見てください。  
素早く見やすく検索しやすいものを少ないのコードで書いてみました。  
表の列はJsonファイルのキーを動的に読み込みます。  
  
JqueryのDatatableを使用しサーチと表示件数を変えられます。  
データを一度読み込んだあとに表示を整形するので、  
巨大なファイルを読み込むと遅くなります。  

ドロップダウンのSelectは
サイトを読み込んだときにdataディレクトリを読みに行くので、
ファイルをdataディレクトリに置くだけで動的にメニューに表示してくれます。
  
### require  

Python3 

pip3 install flask  

### start
python3 json_read.py  

##  access
http://localhost:5000/json  


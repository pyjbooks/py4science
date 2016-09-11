===========================
Pythonのインストール全般
===========================

ディストリビューションパッケージ
===================================

主なディストリビューションパッケージには以下のようなものがあります。

- Anaconda（一部のサービスが有償）
- WinPython
- Python(x,y)
- Enthought Canopy（無償のExpress版と有償版がある）

この中で一番のお勧めは、Anacondaです。
科学技術計算や、（ビッグ）データ解析などに使われる多くのパッケージを一度にインストールできて、
NumPyもIntel MKLにリンクされており、動作が高速です。ごく一部のパッケージが有償で提供されて
いますが、ほとんどの主要なパッケージはオープンソースプロジェクトですので無償で利用できます。

Anacondaのインストール
-----------------------------

`Anaconda`_ は、400を超える `パッケージ`_ を提供しており、そのうち標準インストールの対象となっている
パッケージ全体をまとめたインストーラがダウンロード可能です。Anacondaは、Linux、OS X、Windowsの
全てのプラットフォームに対応しており、OSが32bitでも64bitでも使えます（別々のインストーラが用意してあります）。全体がまとめられたインストーラをダウンロードしてインストールするだけなので、非常に簡単です。

.. _`Anaconda`: https://www.continuum.io/downloads
.. _`パッケージ`: https://docs.continuum.io/anaconda/pkg-docs


個別のパッケージのインストール
==================================

line_profilerのインストールと設定
----------------------------------------

計算負荷のプロファイリングにおいて、行ごとのプロファイルを行うには、「line_profiler」というパッケージ（ライブラリ）
を利用すると便利です。pipによって、以下のように簡単にインストールできます。pipにパスが通っている状態で、
シェル（Windowsの場合「コマンドプロンプト」、Linuxの場合Bashなど）を開いて、以下のようにコマンドを入力します。::

 $ pip install line_profiler

line_profilerは、Anacondaのパッケージとしても用意されています（2016年9月現在）ので、
Anacondaを使っている方は、condaを使って簡単にインストールできます。
line_profilerは、Anacondaのインストーラには含まれていないので、手動でインストールする必要があります。::

 $ conda install line_profiler

line_profilerをIPythonで利用する際、line_proifler用のマジックコマンドを使うには、
IPythonの拡張機能として登録しておく必要があります。それには、IPythonの設定ファイルである
「ipython_config.py」に、以下のように書いておきます。::

 c.InteractiveShellApp.extensions = [
     'line_profiler',   # ←この行がline_profiler用の設定
     'memory_profiler',
     'cython',
 ]

なお、IPythonの設定ファイルは、通常「~/.ipython/profile_default/」というフォルダに置いてあります。
「~」（チルダ）はホームディレクトリの意味です。WindowsでAnacondaをインストールした場合は、
「C:\\users\\<UserName>」(<UserName>はアカウント名に置き換え)というフォルダが該当する場合が
多いと思います。

また、設定ファイルをまだ作成していない場合には、設定ファイルを含む「プロファイル」をまず生成する必要があります。
それには、「Anaconda Prompt」（Anaconda関係のコマンドにパスが通ったシェル
（Windowsのコマンドプロンプトなど））を起動して、次のようにします。::

 ipython profile create [profilename]

デフォルトの設定だけ用意すれば良い場合は、[profilename]を省略できます。
このようにして自動生成された「ipython_config.py」に対して、上記のような設定を行います。

memory_profilerのインストールと設定
----------------------------------------------

Pythonプログラムのメモリ利用量の変化を把握するには、memory_profilerを利用すると便利です。
memory_profilerのインストールと設定に関する説明は、line_profilerの場合と全く同じになります。
上記の説明で、line_profilerをmemory_profilerと読み替えていただければ結構です。

Windows用パッケージの見つけ方
===================================

Anacondaなどのディストリビューションパッケージでは、実に多くの主要パッケージ（ライブラリ）をWindowsでも利用可能にしてくれていますが、それでもなお、Windows向けには提供されていないものがあります。
そのような場合に、役に立つのが `Christoph Gohlke氏が提供している非公式パッケージ`_ です。「非公式」と言っても、
非常に多くのパッケージを網羅していますので、Windowsを使っている方は、まずはこちらにパッケージが置いてないかどうか、探してみると良いでしょう。インストールに苦労しないためにも、このようなサイトに準備されているwheelと呼ばれるパッケージをインストールするのが賢明です。筆者も、basemapパッケージなどをこちらからダウンロードして使わせていただいています。

.. _`Christoph Gohlke氏が提供している非公式パッケージ`: http://www.lfd.uci.edu/~gohlke/pythonlibs/

なお、ダウンロードしたwheelファイルは次のようにしてpipを使ってインストールします。::

 $ pip install SomePackage-1.0-py2.py3-none-any.whl

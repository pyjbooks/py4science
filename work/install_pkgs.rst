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


basemapのインストール
----------------------------------------------

本書で例題として挙げた `PyRockSim`_ を利用するには、地図描画用に basemap というパッケージが必要となります。

.. _`PyRockSim`: https://github.com/pyjbooks/PyRockSim

2017年2月の時点では、 Linux/OS X用のパッケージがAnaconda（Python 2.7/3.4/3.5/3.6の全てのバージョンでbasemap 1.0.7が使えます）に
用意されています。LinuxまたはOS Xを利用している方は、::

 $ conda install basemap

とすればインストール可能です。

また、 Windowsの場合、`Christoph Gohlkeが公開しているWindows用パッケージ`_ を使えばほぼ問題なく使えると思われます。
Christoph GohlkeはWheel形式のパッケージを配布していますので、PythonのバージョンとOSの種類（32bit OS/64bit OS）に対応するWheelをダウンロードして、
例えば以下のようにインストールします(32bit版 WindowsでPython 3.5を使う場合)。::

 $ pip install basemap-1.0.8-cp35-none-win32.whl

.. _`Christoph Gohlkeが公開しているWindows用パッケージ`: http://www.lfd.uci.edu/~gohlke/pythonlibs/

なお、2017年2月時点で最新のAnaconda 4.3.0(Python 3.6版)を使っている場合は、依存関係のあるパッケージも同時にインストールする必要（適切にC/C++コンパイラがインストールされて
おり、適切に環境設定されていれば、basemapのインストールをpipに指示するだけで、あとはpipが勝手に必要なパッケージをダウンロードして、コンパイル後にインストールしてくれます。
しかし、下記のように必要なコンパイル済みパッケージを全てダウンロードしてインストールする方がトラブルに遭遇する可能性は低くなります。）が
あるので、まずChristoph Gohlkeのパッケージから以下の3つのパッケージを取得します。::

 pyproj-1.9.5.1-cp36-cp36m-win_amd64.whl
 pyshp-1.2.10-py2.py3-none-any.whl
 basemap-1.0.8-cp36-cp36m-win_amd64.whl

これらの3つのwheelパッケージを、pipを使ってインストールしていきます。
（以下、"Anaconda Prompt"(DOSコマンドプロンプト)のプロンプトを > で表します）

具体的には、3つのwheelパッケージを保存したフォルダにおいて、
以下の3つのコマンドを実行します。::

 > pip install pyproj-1.9.5.1-cp36-cp36m-win_amd64.whl
 > pip install pyshp-1.2.10-py2.py3-none-any.whl
 > pip install basemap-1.0.8-cp36-cp36m-win_amd64.whl

以上でインストール終了です。

ところで、Windowsユーザがbasemapをインストールする方法にはもう一つあります。
それは、conda（Anacondaのパッケージマネージャ）を使ってインストールする方法です。
先に述べたように、AnacondaはWindows用のbasemapパッケージを提供していませんが、`conda-forge`_
のconda用のパッケージレポジトリに、Windows用（32bit/64bit両方）の
パッケージが用意されているのです。

.. _`conda-forge`: https://conda-forge.github.io/

具体的には、以下の2つのインストールコマンドを実行します。「-c conda-forge」は、パッケージを「conda-forge」から取得してくる
ことを意味します。2つ目のコマンドでは、詳細な精度の高い地図データをインストールしています。::

 > conda install -c conda-forge basemap=1.0.8.dev0
 > conda install -c conda-forge basemap-data-hires

これらを実行するだけで、インストール完了です。ただし、上記のコマンドで「1.0.8.dev0」とあるところは、
適宜最新のバージョンを指定するといいでしょう。最新のバージョンは、`ここ`_ で確認できます。

.. _`ここ`: https://anaconda.org/conda-forge/basemap

なお、basemapインストールの際に、conda自体のバージョンが古いものに変わってしまう場合があります。
他のパッケージの管理に影響すると考えられる場合は、次のようにしてcondaのバージョンを戻してしまいましょう。::

 > conda update conda

これでcondaのバージョンを元に戻しても、basemapの利用上はなんら問題ありません。


Windows用パッケージの見つけ方
===================================

Anacondaなどのディストリビューションパッケージでは、実に多くの主要パッケージ（ライブラリ）をWindowsでも利用可能にしてくれていますが、それでもなお、Windows向けには提供されていないものがあります。
そのような場合に、役に立つのが `Christoph Gohlke氏が提供している非公式パッケージ`_ です。「非公式」と言っても、
非常に多くのパッケージを網羅していますので、Windowsを使っている方は、まずはこちらにパッケージが置いてないかどうか、探してみると良いでしょう。インストールに苦労しないためにも、このようなサイトに準備されているwheelと呼ばれるパッケージをインストールするのが賢明です。筆者も、basemapパッケージなどをこちらからダウンロードして使わせていただいています。

.. _`Christoph Gohlke氏が提供している非公式パッケージ`: http://www.lfd.uci.edu/~gohlke/pythonlibs/

なお、ダウンロードしたwheelファイルは次のようにしてpipを使ってインストールします。::

 $ pip install SomePackage-1.0-py2.py3-none-any.whl

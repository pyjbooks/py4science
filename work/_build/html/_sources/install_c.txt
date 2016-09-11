=========================
C/C++コンパイラのインストール
=========================

ここでは、C言語で実装されたPythonの参照実装であるCPythonを使う場合を前提として話をします。
python.orgが配布しているPythonや、主要なディストリビューションパッケージに含まれるPython
はCPythonですので、良く分からない方は、CPythonを使っていると思ってください。

どういう場合にC/C++コンパイラが必要となるか？
=======================================

PythonでC/C++コンパイラが必要となる場面は、次のような場合です。

- ライブラリ（パッケージ）のインストール時に、C/C++のソースコードをコンパイルする必要がある場合
- Cythonを使う場合

まず、最初に挙げた例では、インストール時に必要になる例です。
関数がC/C++で実装されていて、それをPythonから呼び出して使う仕組みになっている場合には、
インストール時にそのC/C++のソースコードをコンパイルする必要が場合があります。
コンパイル自体は、インストールスクリプトが自動的に行ってくれますが、コンパイラは事前に準備して
おかないと、そのライブラリ（パッケージ）をインストールすることができません。
そのため、様々なライブラリを独自にインストールして試してみたいと考えている方は、C/C++コンパイラを
インストールしておくことを強くお勧めします。

２つ目の例は、PythonコードをC言語化して高速化を図るCythonを使う場合です。
科学技術計算にPythonを使う方は、プログラムの高速化が必須であり、NumPyの機能だけでは
十分に高速化が図れない場合には、Cythonの利用が必要となる場合もあるでしょう。
そのような場合、適切なC/C++コンパイラをあらかじめインストールしておく必要があります。

注意が必要なC/C++コンパイラのインストール
========================================

C/C++コンパイラは、何でも良いわけではありません。OS XやLinuxでは、gccを使えば良いのですが、
問題はWindowsの場合です。Windowsの場合も、MinGWというgcc実装があるのですが、このgccを
使うとうまく動かない場合があります。一番良いのは、Python本体がコンパイルされたコンパイラに、
バージョンを含めて合わせることです。Windows向けのPython本体（CPython）は、Microsoft社の
Visual C++を使ってコンパイルされています。Pythonのバージョンによって、使われている
Visual C++のバージョンが異なりますので、そのバージョンに合わせたC/C++コンパイラを用意する必要があります。

Python本体と、Cythonを使ってコンパイルしたプログラムが、異なるバージョンの
Visual C++ランタイムを呼び出すようになっていると、`いろいろと不都合が生じてしまうようです`_。

.. _`いろいろと不都合が生じてしまうようです`: http://p-nand-q.com/python/building-python-33-with-vs2013.html


WindowsにおけるC/C++コンパイラのインストール
========================================

Windowsでは、Microsoft社のVisual C++（Visual Studio）をインストールします。
その際、上記のようにPython本体がコンパイルされたコンパイラのバージョンに合わせる必要があります。

.. csv-table:: Pythonのバージョンと対応するVisual C++のバージョン
    :header: "Pythonのバージョン","VC++ version","_MSC_VER","開発環境名","C runtime","C++ runtime"
    :widths: 12, 10, 15, 20, 20, 20

    2.7, 9.0, 1500, Visual Studio 2008, MSVCR90.DLL, MSVCP90.DLL
    3.4, 10.0, 1600, Visual Studio 2010, MSVCR100.DLL, MSVCP100.DLL
    3.5, 14.0, 1900, Visual Studio 2015, 注１, MSVCP140.DLL

注１）Universal CRTが導入されています。`詳しくはこちら`_。

.. _`詳しくはこちら`: https://blogs.msdn.microsoft.com/vcblog/2015/03/03/introducing-the-universal-crt/

これからPythonをインストールされる方は、Python 2.7もしくは、Python 3.5を使われると思いますので、
これらについて、以下のようにインストールすべきコンパイラパッケージを示します。「Visual Studio 2015 Community」に
ついては、ライセンス上の制限があり、要件を満たす方しか使えませんのでご注意ください。
また、Professional版などの有料版コンパイラを使われている方は、そちらでも問題なく使えるはずです。
なお、下記の表の中のコンパイラパッケージ名は、リンクになっています。インストールパッケージは、そのリンク先からダウンロード可能です。

.. csv-table:: VC++を含むコンパイラパッケージと、対応するPythonのバージョン
    :header: "","Python 2.7(32bit)", "Python 2.7(64bit)", "Python 3.5(32bit)", "Python 3.5(64bit)"
    :widths: 35, 13, 13, 13, 13

    `Visual C++ Compiler for Python 2.7`_, "     〇", "     〇", ,
    `Visual C++ Build Tools 2015`_, , , "     〇", "     〇"
    `Visual Studio 2015 Express for Windows Desktop`_, , , "     〇",
    `Visual Studio 2015 Community`_, , , "     〇", "     〇"

.. _`Visual C++ Compiler for Python 2.7`: https://www.microsoft.com/en-us/download/details.aspx?id=44266
.. _`Visual C++ Build Tools 2015`: http://landinghub.visualstudio.com/visual-cpp-build-tools
.. _`Visual Studio 2015 express for Windows Desktop`: https://www.visualstudio.com/ja-jp/products/visual-studio-express-vs.aspx
.. _`Visual Studio 2015 Community`: https://www.visualstudio.com/ja-jp/products/visual-studio-community-vs.aspx

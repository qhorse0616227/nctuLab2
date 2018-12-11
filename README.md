# Network Topology with Mininet

This repository is lab for NCTU course "Introduction to Computer Networks 2018".

---
## Abstract

In this lab, we are going to write a Python program which can generate a network topology using Mininet and use iPerf to measure the bandwidth of the topology.

---
## Objectives

1. Learn how to create a network topology with Mininet
2. Learn how to measure the bandwidth in your network topology with iPerf

---
## Execution

> * 先cd到那個檔案的位置，再改成可以執行topology.py的模式（chmod +x topology.py），然後執行topology.py（./topology.py）  
    
> * ![螢幕快照 2018-12-06 下午2.53.45.png](https://github.com/nctucn/lab2-qhorse0616227/blob/master/%E8%9E%A2%E5%B9%95%E5%BF%AB%E7%85%A7%202018-12-06%20%E4%B8%8B%E5%8D%882.53.45.png)
        
---
## Description

### Mininet API in Python

> * Mininet : Network emulation with hosts spawned in network namespaces
> * Topo : Data center network representation for structured multi-trees
> * OVSController : Open vSwitch controller
> * TCLink : Link with symmetric TC interfaces configured via opts
> * dumpNodeConnections : Dump every hosts’ connections
> * setLogLevel : Set new log level
> * CLI : Simple command-line interface to talk to nodes
        

### iPerf Commands

    h2 iperf -s -u -i 1 > ./out/result &   
    將h2以server的模式啟動(使用UDP協議)，並將狀態每隔1秒顯示出來，再把結果傳到out資料夾裡    
    
    h6 iperf -c 10.0.0.2 -u -i 1  
    將h2以client的模式啟動(使用UDP協議)，並連接到ＩＰ地址為10.0.0.2的server，然後每隔1秒要顯示一次狀態
    

### Tasks

1. **Environment Setup**
   先把自己的repository clone到“Network_Topology”

2. **Example of Mininet**
   在執行example.py前要先把模式轉成可以執行的模式 ＝> chmod +x example.py  
   然後才能執行那個檔案 ＝> ./example.py

3. **Topology Generator**
   照著example.py寫自己的topology.py(topo0.png)
   詳細的寫法code裡有註解

4. **Measurement**
   用iperf來測試網路性能
---
## References

> * [Iperf使用說明](http://m1016c.pixnet.net/blog/post/145780230-iperf%E4%BD%BF%E7%94%A8%E8%AA%AA%E6%98%8E)
> * [Mininet筆記](https://blog.laszlo.tw/?p=81)
> * [Mininet Python API Reference Manual](http://mininet.org/api/annotated.html)
> * [SDN軟體定義網路](https://sites.google.com/site/sdnruantidingyiwanglu/home/sdn-lab/lab1)

* **Mininet**
    * [Mininet Walkthrough](http://mininet.org/walkthrough/)
    * [Introduction to Mininet](https://github.com/mininet/mininet/wiki/Introduction-to-Mininet)
    * [Mininet Python API Reference Manual](http://mininet.org/api/annotated.html)
    * [A Beginner's Guide to Mininet](https://opensourceforu.com/2017/04/beginners-guide-mininet/)
    * [GitHub/OSE-Lab - 熟悉如何使用 Mininet](https://github.com/OSE-Lab/Learning-SDN/blob/master/Mininet/README.md)
    * [菸酒生的記事本 – Mininet 筆記](https://blog.laszlo.tw/?p=81)
    * [Hwchiu Learning Note – 手把手打造仿 mininet 網路](https://hwchiu.com/setup-mininet-like-environment.html)
    * [阿寬的實驗室 – Mininet 指令介紹](https://ting-kuan.blog/2017/11/09/%E3%80%90mininet%E6%8C%87%E4%BB%A4%E4%BB%8B%E7%B4%B9%E3%80%91/)
    * [Mininet 學習指南](https://www.sdnlab.com/11495.html)
* **Python**
    * [Python 2.7.15 Standard Library](https://docs.python.org/2/library/index.html)
    * [Python Tutorial - Tutorialspoint](https://www.tutorialspoint.com/python/)
* **Others**
    * [iPerf3 User Documentation](https://iperf.fr/iperf-doc.php#3doc)
    * [Cheat Sheet of Markdown Syntax](https://www.markdownguide.org/cheat-sheet)
    * [Vim Tutorial – Tutorialspoint](https://www.tutorialspoint.com/vim/index.htm)
    * [鳥哥的 Linux 私房菜 – 第九章、vim 程式編輯器](http://linux.vbird.org/linux_basic/0310vi.php)

---
## Contributors

* [Tingyu Chen](https://github.com/qhorse0616227)
* [David Lu](https://github.com/yungshenglu)

---
## License

GNU GENERAL PUBLIC LICENSE Version 3

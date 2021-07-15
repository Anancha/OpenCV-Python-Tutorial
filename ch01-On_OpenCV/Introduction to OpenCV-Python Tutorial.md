# 关于OpenCV

# Translate (Anucha- goolge tranalTE)
OpenCV was started by Gary Bradsky at Intel in 1999, and the first version was released in 2000. Vadim Pisarevsky joined Gary Bradsky and is responsible for managing Intel’s Russian software OpenCV team.

In 2005, OpenCV was used to win the [2005 DARPA Grand Challenge] (https://en.wikipedia.org/wiki/DARPA_Grand_Challenge_(2005)) vehicle. Later, its active development continued to lead the project with Gary Bradsky and Vadim Pisarevsky with the support of Willow Garage. OpenCV now supports many algorithms related to computer vision and machine learning, and it is expanding day by day.

OpenCV supports a variety of programming languages, such as C++, Python, Java, etc., and can be used on different platforms including Windows, Linux, OS X, Android and iOS. The high-speed GPU operating interface based on CUDA and OpenCL is also actively developing. 
-----------------------------------------------------------------------------------------------------------------------------------
OpenCV-Python是OpenCV的Python API，结合了OpenCV C ++ API的最佳特性和Python语言。
OpenCV-Python is OpenCV's Python API, which combines the best features of OpenCV C++ API and the Python language. 

## OpenCV中的Python

OpenCV-Python is a Python binding library for solving computer vision problems.

Python is a common programming language started by Guido van Rossum, which is very popular mainly because of its simplicity and code readability. It enables programmers to express ideas in fewer lines of code without reducing readability.

Python is slower than languages such as C/C. That is, Python can be easily extended through C /C, which allows us to write compute-intensive code in C /C? and create python packaging that can be used as a Python module. This gives us two advantages: first, the code is as fast as the original C/C?code (because it actually works in the background), and second, it is easier to code than Python C/C? OpenCV-Python is the original OpenCV C-plus implementation of the Python wrapper.

OpenCV-Python使用Numpy，它是一个高度优化的库，用于使用MATLAB风格的语法进行数值运算。所有OpenCV阵列结构都转换成Numpy数组。这也使得与使用Numpy的其他库（如SciPy和Matplotlib）更容易集成。
-------------------------------------------------------------------------------------------------------------------------------------
# [Comment Translate] Google

OpenCV-Python is a Python binding library for solving computer vision problems.

Python is a general-purpose programming language started by Guido van Rossum. It is very popular mainly because of its simplicity and code readability. It enables programmers to express ideas in fewer lines of code without reducing readability.

Compared with languages ​​such as C/C++, Python is slower. That is, Python can be easily extended through C/C++, which allows us to write computationally intensive code in C/C++ and create Python wrappers that can be used as Python modules. This gives us two advantages: first, the code is as fast as the original C/C++ code (because it is the actual C++ code working in the background), and second, it is easier to code than Python C/C++ . OpenCV-Python is a Python wrapper for the original OpenCV C++ implementation.

OpenCV-Python uses Numpy, which is a highly optimized library for numerical operations using MATLAB-style syntax. All OpenCV array structures are converted to Numpy arrays. This also makes it easier to integrate with other libraries that use Numpy (such as SciPy and Matplotlib). 
---------------------------------------------------------------------------------------------------------------------------------------


## OpenCV-Python Tutorial

OpenCV has introduced a new set of tutorials that will guide you through the various functions available in OpenCV-Python. This guide focuses on the OpenCV 3.x version (although most tutorials will also be used with OpenCV 2.x).

Previous knowledge of Python and Numpy is recommended, as this guide will not cover it. Proficiency in Numpy is necessary in order to write optimized code using OpenCV-Python.

This tutorial was originally started by Abid Rahman K. as part of the "Google Summer Code" project under the direction of Alexander Mordvintsev. 
________________________________________________________________________________________________________________________________________
## OpenCV需要你！



Since OpenCV is an open source project, everyone is welcome to contribute to the library, documentation and tutorials. If you find any errors in this tutorial (from minor spelling errors to serious errors in the code or concept), please feel free to correct them by cloning OpenCV in GitHub and submitting a citation request. The OpenCV developers will check your pull request and give you important feedback (once approved by the reviewers), it will be merged into OpenCV. Then you will become an open source contributor :-)

As new modules are added to OpenCV-Python, this tutorial will have to be extended. If you are familiar with a specific algorithm and can write a tutorial that includes the basic principles of the algorithm and the code used by the example, please do so.

Remember, together we can make this project a complete success! 


## 贡献者

以下是向OpenCV-Python提交教程的贡献者列表。

* Alexander Mordvintsev（GSoC-2013导师）
* Abid Rahman K.（GSoC-2013实习生）

## 其他资源
* Python的快速指南 - Python的[一个字节](http://swaroopch.com/notes/python/)
* [基本的Numpy教程](http://wiki.scipy.org/Tentative_NumPy_Tutorial)
* [Numpy示例列表](http://wiki.scipy.org/Numpy_Example_List)
* [OpenCV文档](http://docs.opencv.org/)
* [OpenCV论坛](http://answers.opencv.org/questions/)

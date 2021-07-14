# 关于OpenCV

OpenCV于1999年由Gary Bradsky在英特尔启动，2000年第一个版本发布。Vadim Pisarevsky加入了Gary Bradsky，负责管理英特尔的俄罗斯软件OpenCV团队。

2005年，OpenCV被用于赢得[2005年DARPA大挑战赛](https://en.wikipedia.org/wiki/DARPA_Grand_Challenge_(2005))的车辆。后来，它的积极发展继续在Willow Garage的支持下与Gary Bradsky和Vadim Pisarevsky领导该项目。OpenCV现在支持与计算机视觉和机器学习相关的许多算法，并且日益扩大。

OpenCV支持各种各样的编程语言，如C ++，Python，Java等，并且可以在包括Windows，Linux，OS X，Android和iOS在内的不同平台上使用。基于CUDA和OpenCL的高速GPU操作接口也在积极的发展。
--------------------------------------------------------------------------------------------------------------------------------
# Translate (Anucha- goolge tranalTE)
OpenCV was started by Gary Bradsky at Intel in 1999, and the first version was released in 2000. Vadim Pisarevsky joined Gary Bradsky and is responsible for managing Intel’s Russian software OpenCV team.

In 2005, OpenCV was used to win the [2005 DARPA Grand Challenge] (https://en.wikipedia.org/wiki/DARPA_Grand_Challenge_(2005)) vehicle. Later, its active development continued to lead the project with Gary Bradsky and Vadim Pisarevsky with the support of Willow Garage. OpenCV now supports many algorithms related to computer vision and machine learning, and it is expanding day by day.

OpenCV supports a variety of programming languages, such as C++, Python, Java, etc., and can be used on different platforms including Windows, Linux, OS X, Android and iOS. The high-speed GPU operating interface based on CUDA and OpenCL is also actively developing. 
-----------------------------------------------------------------------------------------------------------------------------------
OpenCV-Python是OpenCV的Python API，结合了OpenCV C ++ API的最佳特性和Python语言。
OpenCV-Python is OpenCV's Python API, which combines the best features of OpenCV C++ API and the Python language. 

## OpenCV中的Python

OpenCV-Python是一个用于解决计算机视觉问题的Python绑定库。

Python是由Guido van Rossum开始的通用编程语言，它非常流行，主要是因为它的简单性和代码可读性。它使程序员能够在更少的代码行中表达想法，而不会降低可读性。

与C / C ++等语言相比，Python速度较慢。也就是说，Python可以通过C / C ++轻松扩展，这使得我们可以在C / C ++中编写计算密集型代码，并创建可用作Python模块的Python包装。这给了我们两个优点：第一，代码与原始C / C ++代码一样快（因为它是实际的C ++代码在后台工作），其次，它比Python C / C ++更容易编码。OpenCV-Python是原始OpenCV C ++实现的Python包装器。

OpenCV-Python使用Numpy，它是一个高度优化的库，用于使用MATLAB风格的语法进行数值运算。所有OpenCV阵列结构都转换成Numpy数组。这也使得与使用Numpy的其他库（如SciPy和Matplotlib）更容易集成。
-------------------------------------------------------------------------------------------------------------------------------------
# [Comment Translate] Google

OpenCV-Python is a Python binding library for solving computer vision problems.

Python is a general-purpose programming language started by Guido van Rossum. It is very popular mainly because of its simplicity and code readability. It enables programmers to express ideas in fewer lines of code without reducing readability.

Compared with languages ​​such as C/C++, Python is slower. That is, Python can be easily extended through C/C++, which allows us to write computationally intensive code in C/C++ and create Python wrappers that can be used as Python modules. This gives us two advantages: first, the code is as fast as the original C/C++ code (because it is the actual C++ code working in the background), and second, it is easier to code than Python C/C++ . OpenCV-Python is a Python wrapper for the original OpenCV C++ implementation.

OpenCV-Python uses Numpy, which is a highly optimized library for numerical operations using MATLAB-style syntax. All OpenCV array structures are converted to Numpy arrays. This also makes it easier to integrate with other libraries that use Numpy (such as SciPy and Matplotlib). 
---------------------------------------------------------------------------------------------------------------------------------------
## OpenCV-Python教程

OpenCV引入了一套新的教程，它将引导您了解OpenCV-Python中可用的各种功能。本指南主要集中在OpenCV 3.x版本（尽管大多数教程也将与OpenCV 2.x一起使用）。

推荐使用Python和Numpy的以前的知识，因为本指南将不会介绍。熟练使用Numpy是必须的，以便使用OpenCV-Python编写优化的代码。

本教程最初由Abid Rahman K.开始，是Alexander Mordvintsev指导下的“Google Summer Code”计划的一部分。

## OpenCV-Python Tutorial

OpenCV has introduced a new set of tutorials that will guide you through the various functions available in OpenCV-Python. This guide focuses on the OpenCV 3.x version (although most tutorials will also be used with OpenCV 2.x).

Previous knowledge of Python and Numpy is recommended, as this guide will not cover it. Proficiency in Numpy is necessary in order to write optimized code using OpenCV-Python.

This tutorial was originally started by Abid Rahman K. as part of the "Google Summer Code" project under the direction of Alexander Mordvintsev. 
________________________________________________________________________________________________________________________________________
## OpenCV需要你！

由于OpenCV是一个开源计划，欢迎所有人对图书馆，文档和教程做出贡献。如果您在本教程中发现任何错误（从小的拼写错误到代码或概念中的严重错误），请通过在GitHub中克隆OpenCV 并提交引用请求来随意更正。OpenCV开发人员将检查您的拉动请求，给您重要的反馈意见（一旦通过审核人员的批准），它将被合并到OpenCV中。然后，您将成为一个开源的贡献者 :-)

随着新模块被添加到OpenCV-Python，本教程将不得不进行扩展。如果您熟悉一个特定的算法，并且可以编写一个教程，包括算法的基本原理和示例使用的代码，请执行此操作。

记住，我们一起可以使这个项目取得圆满成功！

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
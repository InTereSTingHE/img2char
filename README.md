# **img2char**
图片生成字符画  

## **参数设置**
* --width 字符画输出宽度，默认120  
* --height  字符画输出宽度，默认80  

## **运行**  
直接运行使用默认宽高度  
```bash
python img2char
```
### 指定宽度高度  
```bash
python img2char --width=100
```  
*or*  
```bash
python img2char --height=60
```  
*or*  
```bash
python img2cgar --width=100 --height=60
```  
### 指定文件及输出路径  
弹窗选择图片及输出位置，输出文件名为*图片名_output.txt*  

## 示例  
### 原图  
![image](https://github.com/InTereSTingHE/img2char/blob/main/pikachu.jpg)  
```bash
python img2char --width=120 --height=60
``` 
### 输出  
![image](https://github.com/InTereSTingHE/img2char/blob/main/output_example.PNG)

# 流程

setting sliding window and threshold -> two sequence(a, b) -> store in list -> align two sequence -> print result

# 具体功能

1. 一个列表用来存储结果矩阵
   1. 一个二维列表
2. 比对的函数
   1. if a~i~ = b~j~, dot; else blank
   2. sliding window(sw) and threshold(th) 
3. 输出结果
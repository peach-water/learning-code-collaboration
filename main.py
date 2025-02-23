from __future__ import annotations

AUTHOR = "cjw"

class ComplexNumber:
    """
    复数类，用于表示和操作复数。

    成员变量:
    real -- 复数的实部
    imag -- 复数的虚部
    """

    def __init__(self, real: float, imag: float):
        """
        初始化复数对象。

        参数:
        real -- 实部
        imag -- 虚部
        """
        self.real = real
        self.imag = imag

    def getReal(self) -> float:
        """
        获取复数的实部。

        返回值
        ---
        self.real: float
            返回复数的实部
        """
        return self.real

    def getImag(self) -> float:
        """
        获取复数的虚部。

        返回值
        ---
        self.imag: float
            返回复数的虚部
        """
        return self.imag

    def setReal(self, real: float) -> None:
        """
        设置复数的实部。

        输入参数
        ---
        real: float
            要修改为的复数的实部
        """
        self.real = real

    def setImag(self, imag: float) -> None:
        """
        设置复数的虚部。

        输入参数
        ---
        imag: float
            要修改为的复数的虚部
        """
        self.imag = imag

    def add(self, other: ComplexNumber) -> ComplexNumber:
        """
        将另一个复数与当前复数相加，返回一个新的复数对象

        输入参数
        ---
        other: ComplexNumber
            另一个复数对象
        
        返回值
        ---
        result: ComplexNumber
            新的复数对象
        """
        result = ComplexNumber(self.real + other.real, self.imag + other.imag)
        return result

if __name__ == "__main__":
    author = AUTHOR
    print("hello world")
    print("This is %s's version." % author)

    # 创建两个复数对象
    c1 = ComplexNumber(1, 2)
    c2 = ComplexNumber(3, 4)

    # 调用加法方法
    c3 = c1.add(c2)

    # 输出结果
    print("c3: real= %s, imag=%s" % (c3.getReal(), c3.getImag()))
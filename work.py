import os


# ------------------------------------文件节点定义-----------------------------
class fileNode():
    def __init__(self, originPath, filename):
        self.originPath = originPath
        self.fileName = filename
        self.floders = []
        self.files = []


# -------------------------------------输入路径--------------------------------
# filesPath = input("请输入路径")

# -------------------------------------主函数--------------------------------
def main():
    inputPath = "/Users/gitfub/Downloads/IphoneMail"

    # 处理输入进来的路径，将路径拆分为起始路劲和文件名
    inputPathlist = inputPath.split("/")
    fileName = inputPathlist[-1]
    del inputPathlist[-1]
    originPath = "/".join(inputPathlist)

    # 返回主节点
    originNode = getFileNodes(originPath, fileName)
    print(originNode.files)
    print(len(originNode.floders))


# -------------------------------------功能函数--------------------------------
# 获取所有文件的文件路径
#
def getFileNodes(originPath, fileName):
    node = fileNode(originPath, fileName)
    completePath = node.originPath + "/" + node.fileName # 文件完成路径
    itmes = os.listdir(completePath)
    for itme in itmes:
        filePath = completePath + "/" + itme
        if os.path.isfile(filePath):
            node.files.append(itme)
        elif os.path.isdir(filePath):
            node.floders.append(getFileNodes(completePath,itme))

    return node


# -------------------------------------主函数调用--------------------------------
if __name__ == '__main__':
    main()

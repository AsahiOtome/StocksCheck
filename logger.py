import logging.handlers

"""
logging.basicConfig函数各参数：
    format：指定输出的格式和内容，format可以输出很多有用的信息;
    level：设置日志级别，默认为logging.WARNING;
    datefmt：指定时间格式，同time.strftime();
    filename：指定日志文件名;
    filemode：和file函数意义相同，指定日志文件的打开模式，'w'或者'a';
        %(name)s:           日志的名称
        %(asctime)s:        可读时间，默认格式‘2003-07-08 16:49:45,896’，逗号之后是毫秒
        %(filename)s:       文件名，pathname的一部分
        %(levelname)s:      日志的等级
        %(module)s:         模块名
        %(funcName)s:       调用日志输出函数的函数名
        %(thread)d:         线程的ID
        %(threadName)s:     线程的名称
        %(processName)s:    进程的名称
        %(message)s:        获取到的字符串信息
    logging.Formatter(fmt='', datefmt='')
"""

# 设置日志格式（全局）
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# 创建日志对象
logger = logging.getLogger()


def setLogger():
    logger.setLevel(logging.INFO)  # 设置日志默认级别为INFO级
    # 设置日志格式
    formatter = logging.Formatter(fmt='[%(asctime)s] %(module)s.%(funcName)s %(levelname)s: %(message)s',
                                  datefmt='%Y-%m-%d %T')

    """
    StreamHandler 控制台输出日志
    FileHandler 日志输出到文件
    TimedRotatingFileHandler 按时间日志分割
    RotatingFileHandler 回滚式输出到文件
    """
    sh = logging.StreamHandler()    # 添加StreamHandler输出规则
    sh.setLevel(logging.INFO)
    sh.setFormatter(formatter)
    logger.addHandler(sh)

    # fh = logging.FileHandler('./Database\\StocksCheck.log', encoding='utf-8')
    # fh.setLevel(logging.INFO)
    # fh.setFormatter(formatter)
    # logger.addHandler(fh)

    # 添加回滚文件保存规则
    rh = logging.handlers.RotatingFileHandler(
        './Database\\StocksCheck.log', maxBytes=10485760, backupCount=5, encoding='utf-8')
    rh.setLevel(logging.INFO)
    rh.setFormatter(formatter)
    logger.addHandler(rh)


setLogger()


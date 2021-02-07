import logging
import datetime
import pandas as pd


def logger(log_file, mode='a'):
    '''
    :param log_file: 日志存储路径和文件名，类型string；
    :param mode: 日志添加方式；
    :param : ，类型；
    :return:
    '''
    # 创建一个loggger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    # 创建一个handler，用于写入日志文件
    fh = logging.FileHandler(filename=log_file, encoding='utf-8', mode=mode)
    fh.setLevel(logging.DEBUG)
    # 创建一个handler，用于将日志输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # 定义handler的输出格式
    formatter = logging.Formatter('%(asctime)s-%(name)s-%(filename)s-[line:%(lineno)d]''-%(levelname)s-[日志信息]: %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # 给logger添加handler
    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger


def get_hist_date(day, x):
    '''
    计算给定日期前x天的日期
    :param day: 分区日期，类型int；
    :param x: 时间窗，类型lint；
    :param : ，类型；
    :return:
    '''
    each_dt = datetime.date(int(str(day)[: 4]), int(str(day)[4:6]), int(str(day)[6:8]))
    dt_xd = int(str(each_dt - datetime.timedelta(x)).replace('-', ''))

    return dt_xd


def get_future_date(day, x):
    '''
    计算给定日期后x天的日期
    :param day: 分区日期，类型int；
    :param x: 时间窗，类型lint；
    :param : ，类型；
    :return:
    '''
    each_dt = datetime.date(int(str(day)[: 4]), int(str(day)[4:6]), int(str(day)[6:8]))
    dt_xd = int(str(each_dt + datetime.timedelta(x)).replace('-', ''))

    return dt_xd



def get_period_day_lst(dt_start, dt_end):
    '''
    获取一段连续日期列表
    :param dt_start: 起始日期yyyymmdd，类型int
    :param dt_end: 截止日期yyyymmdd，类型int
    :return:
    '''
    dt_start, dt_end = str(dt_start), str(dt_end)
    dt_start = dt_start[:4] + '-' + dt_start[4:6] + '-' + dt_start[6:8]
    dt_end = dt_end[:4] + '-' + dt_end[4:6] + '-' + dt_end[6:8]
    df_dt_range = pd.date_range(start=dt_start, end=dt_end).to_frame().rename(columns={0: 'dt'})
    df_dt_range['dt'] = df_dt_range['dt'].astype('str').str.replace('-', '').astype('int')

    return df_dt_range['dt'].tolist()


def make_dir(dir, recursion=True):
    '''
    创建文件路径
    :param dir: 路径，类型string
    :param recursion: 是否递归创建，类型boolean
    :return:
    '''
    if not os.path.exists(dir):
        if recursion:
            os.makedirs(dir)
        else:
            os.mkdir(dir)

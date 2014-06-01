# coding=utf8

from os.path import dirname, join, normpath


def normjoin(*pathes):
    return normpath(join(*pathes))


def path_to(*pathes):
    """the path to md2pdf's file"""
    file_dir_path = dirname(__file__)
    return normjoin(file_dir_path, *pathes)

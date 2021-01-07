# ROOT = '/Users/jackz/Documents/P Macbook/Laptop/Git Workspace/'
# MY_ML_ROOT = f'{ROOT}DataScience/MachineLearning/my_machine_learning/'
# MY_ML_DATA = f'{MY_ML_ROOT}my_nn/my_data/data/'
#
#
# def make_file_name(dataset_name="xsum", dataset_type="train", dataset_size=60, maxlen=30, extra=None,
#                    file_ext=".csv"):
#     """
#     serialize name format example for xsum, train, subset 60, maxlen 30, with .csv format: 'xsum_train60_maxlen30.csv'
#     :param dataset_name:
#     :param dataset_type:
#     :param dataset_size:
#     :param maxlen:
#     :param file_ext:
#     :return:
#     """
#     separator = "_"
#     file_name = f"{dataset_name}{separator}{dataset_type}{dataset_size}{separator}maxlen{maxlen}"
#     if extra:
#         file_name = f"{dataset_name}{separator}{dataset_type}{dataset_size}{separator}maxlen{maxlen}{separator}{extra}"
#     if file_ext:
#         file_name = file_ext + file_ext
#     return file_name
#
#
# def file_path(file_name, root=MY_ML_DATA):
#     data_dir = f"{root}{file_name}"
#     return data_dir
#
#
# def make_file_names(dataset_name="xsum", dataset_size=60, maxlen=30, extra="", file_ext=".csv"):
#     train_name = make_file_name(dataset_name=dataset_name, dataset_size=dataset_size, dataset_type="train",
#                                 maxlen=maxlen, extra=extra, file_ext=file_ext)
#     valid_name = make_file_name(dataset_name=dataset_name, dataset_size=dataset_size, dataset_type="valid",
#                                 maxlen=maxlen, extra=extra, file_ext=file_ext)
#     test_name = make_file_name(dataset_name=dataset_name, dataset_size=dataset_size, dataset_type="test",
#                                maxlen=maxlen, extra=extra, file_ext=file_ext)
#     return train_name, valid_name, test_name
#
#
# def file_paths(file_names=[], root=MY_ML_DATA):
#     if file_names:
#         train_path = file_path(file_names[0], root)
#         valid_path = file_path(file_names[1], root)
#         test_path = file_path(file_names[2], root)
#         return train_path, valid_path, test_path
import os


class XsumPath():
    ROOT = '/Users/jackz/Documents/P Macbook/Laptop/Git Workspace/DataScience/MachineLearning/MyForks/joeynmt/gitignored/data/sample/'
    MY_ML_ROOT = f'{ROOT}DataScience/MachineLearning/my_machine_learning/'
    MY_ML_DATA = f'{MY_ML_ROOT}my_nn/my_data/data/'
    # MY_XSUM_SAMPLE = f'{MY_ML_DATA}/xsum/'
    MY_XSUM_SAMPLE = os.path.join('..', 'gitignored', 'data', 'sample')

    def __init__(self):
        self.create_file_names_paths()

    # def make_file_name(self, dataset_name="xsum", dataset_type="train", dataset_size=60, maxlen=30, extra=None,
    #                    file_ext=".csv"):
    #     """
    #     serialize name format example for xsum, train, subset 60, maxlen 30, with .csv format: 'xsum_train60_maxlen30.csv'
    #     :param dataset_name:
    #     :param dataset_type:
    #     :param dataset_size:
    #     :param maxlen:
    #     :param file_ext:
    #     :return:
    #     """
    #     separator = "_"
    #     file_name = f"{dataset_name}{separator}{dataset_type}{dataset_size}{separator}maxlen{maxlen}"
    #     if extra:
    #         file_name = f"{dataset_name}{separator}{dataset_type}{dataset_size}{separator}maxlen{maxlen}{separator}{extra}"
    #     if file_ext:
    #         file_name = file_ext + file_ext
    #     return file_name
    #
    # def file_path(self, file_name, root=MY_ML_DATA):
    #     data_dir = f"{root}{file_name}"
    #     return data_dir
    #
    # def make_file_names(self, dataset_name="xsum", dataset_size=60, maxlen=30, extra="", file_ext=".csv"):
    #     train_name = self.make_file_name(dataset_name=dataset_name, dataset_size=dataset_size, dataset_type="train",
    #                                      maxlen=maxlen, extra=extra, file_ext=file_ext)
    #     valid_name = self.make_file_name(dataset_name=dataset_name, dataset_size=dataset_size, dataset_type="valid",
    #                                      maxlen=maxlen, extra=extra, file_ext=file_ext)
    #     test_name = self.make_file_name(dataset_name=dataset_name, dataset_size=dataset_size, dataset_type="test",
    #                                     maxlen=maxlen, extra=extra, file_ext=file_ext)
    #     return train_name, valid_name, test_name
    #
    # def file_paths(self, file_names=[], root=MY_ML_DATA):
    #     if file_names:
    #         train_path = self.file_path(file_names[0], root)
    #         valid_path = self.file_path(file_names[1], root)
    #         test_path = self.file_path(file_names[2], root)
    #         return train_path, valid_path, test_path
    def make_file_name(self, dataset_name="xsum", dataset_type="train", dataset_size=60, maxlen=30, extra=None,
                       file_ext=".csv"):
        """
        serialize name format example for xsum, train, subset 60, maxlen 30, with .csv format: 'xsum_train60_maxlen30.csv'
        :param dataset_name:
        :param dataset_type:
        :param dataset_size:
        :param maxlen:
        :param file_ext:
        :return:
        """
        separator = "_"
        file_name = f"{dataset_name}{separator}{dataset_type}{dataset_size}{separator}maxlen{maxlen}"
        if extra:
            file_name = f"{dataset_name}{separator}{dataset_type}{dataset_size}{separator}maxlen{maxlen}{separator}{extra}"
        if file_ext:
            file_name = file_name + file_ext
        return file_name

    def file_path(self, file_name, root=MY_XSUM_SAMPLE):
        data_path = os.path.join(root, file_name)
        return data_path

    def get_file_names(self, dataset_name="xsum", dataset_size=60, maxlen=30, extra="", file_ext=".csv"):
        train_name = self.make_file_name(dataset_name=dataset_name, dataset_size=dataset_size, dataset_type="train",
                                         maxlen=maxlen, extra=extra, file_ext=file_ext)
        valid_name = self.make_file_name(dataset_name=dataset_name, dataset_size=dataset_size, dataset_type="valid",
                                         maxlen=maxlen, extra=extra, file_ext=file_ext)
        test_name = self.make_file_name(dataset_name=dataset_name, dataset_size=dataset_size, dataset_type="test",
                                        maxlen=maxlen, extra=extra, file_ext=file_ext)
        return train_name, valid_name, test_name

    def file_paths(self, file_names=['train', 'valid', 'test'], root=MY_ML_DATA):
        if file_names:
            train_path = self.file_path(file_names[0], root)
            valid_path = self.file_path(file_names[1], root)
            test_path = self.file_path(file_names[2], root)
            return train_path, valid_path, test_path

    def create_file_names_paths(self):
        ## maxlen 30
        self.XSUM_TRAIN60_MAXLEN30, self.XSUM_VALID60_MAXLEN30, self.XSUM_TEST60_MAXLEN30 = self.get_file_names()
        self.XSUM_TRAIN100_MAXLEN30, self.XSUM_VALID100_MAXLEN30, self.XSUM_TEST100_MAXLEN30 = self.get_file_names(
            dataset_size=100)
        self.XSUM_TRAIN500_MAXLEN30, self.XSUM_VALID500_MAXLEN30, self.XSUM_TEST500_MAXLEN30 = self.get_file_names(
            dataset_size=500)

        self.XSUM_TRAIN60_MAXLEN30_REVERSED, self.XSUM_VALID60_MAXLEN30_REVERSED, self.XSUM_TEST60_MAXLEN30_REVERSED = self.get_file_names(
            extra="reversed")
        self.XSUM_TRAIN100_MAXLEN30_REVERSED, self.XSUM_VALID100_MAXLEN30_REVERSED, self.XSUM_TEST100_MAXLEN30_REVERSED = self.get_file_names(
            dataset_size=100, extra="reversed")
        self.XSUM_TRAIN500_MAXLEN30_REVERSED, self.XSUM_VALID500_MAXLEN30_REVERSED, self.XSUM_TEST500_MAXLEN30_REVERSED = self.get_file_names(
            dataset_size=500, extra="reversed")

        ## maxlen 100
        self.XSUM_TRAIN60_MAXLEN100, self.XSUM_VALID60_MAXLEN100, self.XSUM_TEST60_MAXLEN100 = self.get_file_names()
        self.XSUM_TRAIN100_MAXLEN100, self.XSUM_VALID100_MAXLEN100, self.XSUM_TEST100_MAXLEN100 = self.get_file_names(
            dataset_size=100)
        self.XSUM_TRAIN500_MAXLEN100, self.XSUM_VALID500_MAXLEN100, self.XSUM_TEST500_MAXLEN100 = self.get_file_names(
            dataset_size=500)

        self.XSUM_TRAIN60_MAXLEN100_REVERSED, self.XSUM_VALID60_MAXLEN100_REVERSED, self.XSUM_TEST60_MAXLEN100_REVERSED = self.get_file_names(
            extra="reversed")
        self.XSUM_TRAIN100_MAXLEN100_REVERSED, self.XSUM_VALID100_MAXLEN100_REVERSED, self.XSUM_TEST100_MAXLEN100_REVERSED = self.get_file_names(
            dataset_size=100, extra="reversed")
        self.XSUM_TRAIN500_MAXLEN100_REVERSED, self.XSUM_VALID500_MAXLEN100_REVERSED, self.XSUM_TEST500_MAXLEN100_REVERSED = self.get_file_names(
            dataset_size=500, extra="reversed")

        ## data serialize path
        # maxlen30
        self.PATH_XSUM_TRAIN60_MAXLEN30 = self.file_path(self.XSUM_TRAIN60_MAXLEN30)
        self.PATH_XSUM_VALID60_MAXLEN30 = self.file_path(self.XSUM_VALID60_MAXLEN30)
        self.PATH_XSUM_TEST60_MAXLEN30 = self.file_path(self.XSUM_TEST60_MAXLEN30)

        self.PATH_XSUM_TRAIN100_MAXLEN30 = self.file_path(self.XSUM_TRAIN100_MAXLEN30)
        self.PATH_XSUM_VALID100_MAXLEN30 = self.file_path(self.XSUM_VALID100_MAXLEN30)
        self.PATH_XSUM_TEST100_MAXLEN30 = self.file_path(self.XSUM_TEST100_MAXLEN30)

        self.PATH_XSUM_TRAIN500_MAXLEN30 = self.file_path(self.XSUM_TRAIN500_MAXLEN30)
        self.PATH_XSUM_VALID500_MAXLEN30 = self.file_path(self.XSUM_VALID500_MAXLEN30)
        self.PATH_XSUM_TEST500_MAXLEN30 = self.file_path(self.XSUM_TEST500_MAXLEN30)

        self.PATH_XSUM_TRAIN60_MAXLEN30_REVERSED = self.file_path(self.XSUM_TRAIN60_MAXLEN30_REVERSED)
        self.PATH_XSUM_VALID60_MAXLEN30_REVERSED = self.file_path(self.XSUM_VALID60_MAXLEN30_REVERSED)
        self.PATH_XSUM_TEST60_MAXLEN30_REVERSED = self.file_path(self.XSUM_TEST60_MAXLEN30_REVERSED)

        self.PATH_XSUM_TRAIN100_MAXLEN30_REVERSED = self.file_path(self.XSUM_TRAIN100_MAXLEN30_REVERSED)
        self.PATH_XSUM_VALID100_MAXLEN30_REVERSED = self.file_path(self.XSUM_VALID100_MAXLEN30_REVERSED)
        self.PATH_XSUM_TEST100_MAXLEN30_REVERSED = self.file_path(self.XSUM_TEST100_MAXLEN30_REVERSED)

        self.PATH_XSUM_TRAIN500_MAXLEN30_REVERSED = self.file_path(self.XSUM_TRAIN500_MAXLEN30_REVERSED)
        self.PATH_XSUM_VALID500_MAXLEN30_REVERSED = self.file_path(self.XSUM_VALID500_MAXLEN30_REVERSED)
        self.PATH_XSUM_TEST500_MAXLEN30_REVERSED = self.file_path(self.XSUM_TEST500_MAXLEN30_REVERSED)

        ## maxlen 100
        self.PATH_XSUM_TRAIN60_MAXLEN100 = self.file_path(self.XSUM_TRAIN60_MAXLEN100)
        self.PATH_XSUM_VALID60_MAXLEN100 = self.file_path(self.XSUM_VALID60_MAXLEN100)
        self.PATH_XSUM_TEST60_MAXLEN100 = self.file_path(self.XSUM_TEST60_MAXLEN100)

        self.PATH_XSUM_TRAIN100_MAXLEN100 = self.file_path(self.XSUM_TRAIN100_MAXLEN100)
        self.PATH_XSUM_VALID100_MAXLEN100 = self.file_path(self.XSUM_VALID100_MAXLEN100)
        self.PATH_XSUM_TEST100_MAXLEN100 = self.file_path(self.XSUM_TEST100_MAXLEN100)

        self.PATH_XSUM_TRAIN500_MAXLEN100 = self.file_path(self.XSUM_TRAIN500_MAXLEN100)
        self.PATH_XSUM_VALID500_MAXLEN100 = self.file_path(self.XSUM_VALID500_MAXLEN100)
        self.PATH_XSUM_TEST500_MAXLEN100 = self.file_path(self.XSUM_TEST500_MAXLEN100)

        self.PATH_XSUM_TRAIN60_MAXLEN100_REVERSED = self.file_path(self.XSUM_TRAIN60_MAXLEN100_REVERSED)
        self.PATH_XSUM_VALID60_MAXLEN100_REVERSED = self.file_path(self.XSUM_VALID60_MAXLEN100_REVERSED)
        self.PATH_XSUM_TEST60_MAXLEN100_REVERSED = self.file_path(self.XSUM_TEST60_MAXLEN100_REVERSED)

        self.PATH_XSUM_TRAIN100_MAXLEN100_REVERSED = self.file_path(self.XSUM_TRAIN100_MAXLEN100_REVERSED)
        self.PATH_XSUM_VALID100_MAXLEN100_REVERSED = self.file_path(self.XSUM_VALID100_MAXLEN100_REVERSED)
        self.PATH_XSUM_TEST100_MAXLEN100_REVERSED = self.file_path(self.XSUM_TEST100_MAXLEN100_REVERSED)

        self.PATH_XSUM_TRAIN500_MAXLEN100_REVERSED = self.file_path(self.XSUM_TRAIN500_MAXLEN100_REVERSED)
        self.PATH_XSUM_VALID500_MAXLEN100_REVERSED = self.file_path(self.XSUM_VALID500_MAXLEN100_REVERSED)
        self.PATH_XSUM_TEST500_MAXLEN100_REVERSED = self.file_path(self.XSUM_TEST500_MAXLEN100_REVERSED)
    # ## data serialize names
    # XSUM_TRAIN60_MAXLEN30 = 'xsum_train60_maxlen30.csv'
    # XSUM_VALID60_MAXLEN30 = 'xsum_valid60_maxlen30.csv'
    # XSUM_TEST60_MAXLEN30 = 'xsum_test60_maxlen30.csv'
    #
    # # data serialize names
    # XSUM_TRAIN60_MAXLEN30 = make_file_name()
    # XSUM_VALID60_MAXLEN30 = make_file_name(dataset_type="valid")
    # XSUM_TEST60_MAXLEN30 = make_file_name(dataset_type="test")

    # ## maxlen 30
    # XSUM_TRAIN60_MAXLEN30, XSUM_VALID60_MAXLEN30, XSUM_TEST60_MAXLEN30 = make_file_names()
    # XSUM_TRAIN100_MAXLEN30, XSUM_VALID100_MAXLEN30, XSUM_TEST100_MAXLEN30 = make_file_names(dataset_size=100)
    # XSUM_TRAIN500_MAXLEN30, XSUM_VALID500_MAXLEN30, XSUM_TEST500_MAXLEN30 = make_file_names(dataset_size=500)
    #
    # XSUM_TRAIN60_MAXLEN30_REVERSED, XSUM_VALID60_MAXLEN30_REVERSED, XSUM_TEST60_MAXLEN30_REVERSED = make_file_names(
    #     extra="reversed")
    # XSUM_TRAIN100_MAXLEN30_REVERSED, XSUM_VALID100_MAXLEN30_REVERSED, XSUM_TEST100_MAXLEN30_REVERSED = make_file_names(
    #     dataset_size=100, extra="reversed")
    # XSUM_TRAIN500_MAXLEN30_REVERSED, XSUM_VALID500_MAXLEN30_REVERSED, XSUM_TEST500_MAXLEN30_REVERSED = make_file_names(
    #     dataset_size=500, extra="reversed")
    #
    # ## maxlen 100
    # XSUM_TRAIN60_MAXLEN100, XSUM_VALID60_MAXLEN100, XSUM_TEST60_MAXLEN100 = make_file_names()
    # XSUM_TRAIN100_MAXLEN100, XSUM_VALID100_MAXLEN100, XSUM_TEST100_MAXLEN100 = make_file_names(dataset_size=100)
    # XSUM_TRAIN500_MAXLEN100, XSUM_VALID500_MAXLEN100, XSUM_TEST500_MAXLEN100 = make_file_names(dataset_size=500)
    #
    # XSUM_TRAIN60_MAXLEN100_REVERSED, XSUM_VALID60_MAXLEN100_REVERSED, XSUM_TEST60_MAXLEN100_REVERSED = make_file_names(
    #     extra="reversed")
    # XSUM_TRAIN100_MAXLEN100_REVERSED, XSUM_VALID100_MAXLEN100_REVERSED, XSUM_TEST100_MAXLEN100_REVERSED = make_file_names(
    #     dataset_size=100, extra="reversed")
    # XSUM_TRAIN500_MAXLEN100_REVERSED, XSUM_VALID500_MAXLEN100_REVERSED, XSUM_TEST500_MAXLEN100_REVERSED = make_file_names(
    #     dataset_size=500, extra="reversed")
    #
    # ## data serialize path
    # # maxlen30
    # PATH_XSUM_TRAIN60_MAXLEN30 = file_path(XSUM_TRAIN60_MAXLEN30)
    # PATH_XSUM_VALID60_MAXLEN30 = file_path(XSUM_VALID60_MAXLEN30)
    # PATH_XSUM_TEST60_MAXLEN30 = file_path(XSUM_TEST60_MAXLEN30)
    #
    # PATH_XSUM_TRAIN100_MAXLEN30 = file_path(XSUM_TRAIN100_MAXLEN30)
    # PATH_XSUM_VALID100_MAXLEN30 = file_path(XSUM_VALID100_MAXLEN30)
    # PATH_XSUM_TEST100_MAXLEN30 = file_path(XSUM_TEST100_MAXLEN30)
    #
    # PATH_XSUM_TRAIN500_MAXLEN30 = file_path(XSUM_TRAIN500_MAXLEN30)
    # PATH_XSUM_VALID500_MAXLEN30 = file_path(XSUM_VALID500_MAXLEN30)
    # PATH_XSUM_TEST500_MAXLEN30 = file_path(XSUM_TEST500_MAXLEN30)
    #
    # PATH_XSUM_TRAIN60_MAXLEN30_REVERSED = file_path(XSUM_TRAIN60_MAXLEN30_REVERSED)
    # PATH_XSUM_VALID60_MAXLEN30_REVERSED = file_path(XSUM_VALID60_MAXLEN30_REVERSED)
    # PATH_XSUM_TEST60_MAXLEN30_REVERSED = file_path(XSUM_TEST60_MAXLEN30_REVERSED)
    #
    # PATH_XSUM_TRAIN100_MAXLEN30_REVERSED = file_path(XSUM_TRAIN100_MAXLEN30_REVERSED)
    # PATH_XSUM_VALID100_MAXLEN30_REVERSED = file_path(XSUM_VALID100_MAXLEN30_REVERSED)
    # PATH_XSUM_TEST100_MAXLEN30_REVERSED = file_path(XSUM_TEST100_MAXLEN30_REVERSED)
    #
    # PATH_XSUM_TRAIN500_MAXLEN30_REVERSED = file_path(XSUM_TRAIN500_MAXLEN30_REVERSED)
    # PATH_XSUM_VALID500_MAXLEN30_REVERSED = file_path(XSUM_VALID500_MAXLEN30_REVERSED)
    # PATH_XSUM_TEST500_MAXLEN30_REVERSED = file_path(XSUM_TEST500_MAXLEN30_REVERSED)
    #
    # ## maxlen 100
    # PATH_XSUM_TRAIN60_MAXLEN100 = file_path(XSUM_TRAIN60_MAXLEN100)
    # PATH_XSUM_VALID60_MAXLEN100 = file_path(XSUM_VALID60_MAXLEN100)
    # PATH_XSUM_TEST60_MAXLEN100 = file_path(XSUM_TEST60_MAXLEN100)
    #
    # PATH_XSUM_TRAIN100_MAXLEN100 = file_path(XSUM_TRAIN100_MAXLEN100)
    # PATH_XSUM_VALID100_MAXLEN100 = file_path(XSUM_VALID100_MAXLEN100)
    # PATH_XSUM_TEST100_MAXLEN100 = file_path(XSUM_TEST100_MAXLEN100)
    #
    # PATH_XSUM_TRAIN500_MAXLEN100 = file_path(XSUM_TRAIN500_MAXLEN100)
    # PATH_XSUM_VALID500_MAXLEN100 = file_path(XSUM_VALID500_MAXLEN100)
    # PATH_XSUM_TEST500_MAXLEN100 = file_path(XSUM_TEST500_MAXLEN100)
    #
    # PATH_XSUM_TRAIN60_MAXLEN100_REVERSED = file_path(XSUM_TRAIN60_MAXLEN100_REVERSED)
    # PATH_XSUM_VALID60_MAXLEN100_REVERSED = file_path(XSUM_VALID60_MAXLEN100_REVERSED)
    # PATH_XSUM_TEST60_MAXLEN100_REVERSED = file_path(XSUM_TEST60_MAXLEN100_REVERSED)
    #
    # PATH_XSUM_TRAIN100_MAXLEN100_REVERSED = file_path(XSUM_TRAIN100_MAXLEN100_REVERSED)
    # PATH_XSUM_VALID100_MAXLEN100_REVERSED = file_path(XSUM_VALID100_MAXLEN100_REVERSED)
    # PATH_XSUM_TEST100_MAXLEN100_REVERSED = file_path(XSUM_TEST100_MAXLEN100_REVERSED)
    #
    # PATH_XSUM_TRAIN500_MAXLEN100_REVERSED = file_path(XSUM_TRAIN500_MAXLEN100_REVERSED)
    # PATH_XSUM_VALID500_MAXLEN100_REVERSED = file_path(XSUM_VALID500_MAXLEN100_REVERSED)
    # PATH_XSUM_TEST500_MAXLEN100_REVERSED = file_path(XSUM_TEST500_MAXLEN100_REVERSED)

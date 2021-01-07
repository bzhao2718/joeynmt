# from scripts.data.HfXsumDataLoader import XsumHfLoader
from HfXsumDataLoader import XsumHfLoader
import os
import csv
import pandas as pd
# from scripts.data.XsumPath import XsumPath
from XsumPath import XsumPath


need_clean = True

MAX_NEWS_LEN = 30
xsumDataPath: XsumPath = XsumPath()

# def test_df():
#     df = pd.read_csv(names.abs_test_path)
#     news = df['news']
#     print(df.head())


def clean_seq(seq):
    import re
    seq = re.sub('[^a-zA-Z0-9]', ' ', seq)  # remove special characters
    seq = re.sub(r'\n', '', seq)  # remove newline character
    return seq


def create_sen_from_csv(file_name, size=30, maxlen=30, clean_text=True):
    df = pd.read_csv(file_name)
    sen_list = []
    i = 0
    for idx, x in df.iterrows():
        x = x[1]  # summary at index 1
        if i == size:
            break
        if len(x.split()) > maxlen:
            continue

        summary = x
        if clean_text:
            summary = clean_seq(summary)
        sen_list.append(summary)
        i += 1
    return sen_list


def senlist_from_csv_single_field(file_name, size=30, maxlen=30, field_name="summary", clean_text=True):
    field_src = "src"
    field_trg = "trg"
    field_len_src = "src_lens"
    field_len_trg = "trg_lens"

    df = pd.read_csv(file_name)
    sen_list = []
    i = 0
    cols = df.columns
    test = df[field_name]
    type = type(test)
    for x in df[field_name]:
        if i == size:
            break
        sentence = x
        if clean_text:
            sentence = clean_seq(sentence)
        if len(sentence.split()) > maxlen:
            continue
        sen_list.append(sentence)
        i += 1
    return sen_list


# def writeToCsv(file_name, dataset, split, maxlen=None):
#     # check if the directory exists
#     if not os.path.exists(XSUAM_DATA_PATH):
#         os.makedirs(XSUAM_DATA_PATH, exist_ok=True)
#
#     with open(file_name, mode='w') as data_file:
#         data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#         for example in dataset:
#             document = example[split]
#             if maxlen and len(document.split()) > maxlen:  # filter news based on news len
#                 continue
#             data_writer.writerow([document])


def writeSenToCsv(data_dir, file_path, sen_list, trg_reverse=False):
    # check if the directory exists
    if not os.path.exists(data_dir):
        os.makedirs(data_dir, exist_ok=True)
    headers = ['src', 'trg', 'src_lens', 'trg_lens']
    with open(file_path, mode='w') as data_file:
        data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        data_writer.writerow(headers)
        for src in sen_list:
            trg = " ".join(src.split()[::-1]) if trg_reverse else src
            data_writer.writerow([src, trg, len(src.split()), len(trg.split())])


def write_one_csv_file(data_path, file_path, sen_list, reverse=False):
    if not os.path.exists(file_path):
        writeSenToCsv(data_path, file_path, sen_list, trg_reverse=reverse)


def create_sen_list(hfLoader: XsumHfLoader, dataset_size, maxlen, reverse=False, clean_text=True):
    data_path = xsumDataPath.MY_XSUM_SAMPLE
    data_field = "summary"
    if maxlen and maxlen > 60:
        data_field = "document"
    extra = ""
    if reverse:
        extra = "Reverse"
    senlist_train = hfLoader.create_sentences(size=dataset_size, maxlen=maxlen, dataset_type="train",
                                              data_filed=data_field,
                                              clean_text=clean_text)
    senlist_valid = hfLoader.create_sentences(size=dataset_size, maxlen=maxlen, dataset_type="valid",
                                              data_filed=data_field,
                                              clean_text=clean_text)
    senlist_test = hfLoader.create_sentences(size=dataset_size, maxlen=maxlen, dataset_type="test",
                                             data_filed=data_field,
                                             clean_text=clean_text)
    file_path_train = xsumDataPath.file_path(
        xsumDataPath.make_file_name(dataset_type="train", dataset_size=dataset_size, maxlen=maxlen, extra=extra))
    file_path_valid = xsumDataPath.file_path(
        xsumDataPath.make_file_name(dataset_type="valid", dataset_size=dataset_size, maxlen=maxlen, extra=extra))
    file_path_test = xsumDataPath.file_path(
        xsumDataPath.make_file_name(dataset_type="test", dataset_size=dataset_size, maxlen=maxlen, extra=extra))
    write_one_csv_file(data_path, file_path_train, senlist_train, reverse)
    write_one_csv_file(data_path, file_path_valid, senlist_valid, reverse)
    write_one_csv_file(data_path, file_path_test, senlist_test, reverse)


def create_samples():
    hfLoader = XsumHfLoader()
    # sen_list60 = hfLoader.create_sentences(str_len=60, dataset_type="train",clean_text=True)
    # sen_list30 = hfLoader.create_sentences(str_len=30, clean_text=True)
    size_list = [50]
    maxlen_list = [30, 30]
    for s in size_list:
        for l in maxlen_list:
            create_sen_list(hfLoader, s, l)
            create_sen_list(hfLoader, s, l, reverse=True)


# def write_samples():
#     hfLoader = HuggingFaceDataLoader()
#     dataset = hfLoader.get_dataset()
#     split = "summary"
#     if not os.path.exists(TRAIN_DATA_PATH):
#         writeToCsv(f'{TRAIN_DATA_PATH}', dataset, split)
#         writeToCsv(f'{VALID_DATA_PATH}', dataset, split)
#         writeToCsv(f'{TEST_DATA_PATH}', dataset, split)


if __name__ == '__main__':
    # write_sentences()
    # test_df()
    # senlist = senlist_from_csv_single_field(TRAIN_DATA_PATH)
    create_samples()

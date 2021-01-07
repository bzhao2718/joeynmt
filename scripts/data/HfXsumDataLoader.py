from datasets import load_dataset


#     for x in train_data:
#         train_writer.writerow([x['document'],x['summary']])


class XsumHfLoader():
    def __init__(self):
        self.ini = "inited"

    def get_dataset(self, name="xsum", dataset_split=None):
        if dataset_split:
            data = load_dataset(name, split=dataset_split)
        else:
            data = load_dataset(name)
        return data

    def clean_seq(self, seq):
        import re
        seq = re.sub('[^a-zA-Z0-9]', ' ', seq)  # remove special characters
        seq = re.sub(r'\n', '', seq)  # remove newline character
        return seq

    def senlist_from_dataset(self, dataset, size=30, maxlen=30, data_filed="summary", clean_text=False):
        sen_list = []
        filed_name = data_filed
        i = 0
        for x in dataset:
            if i == size:
                break
            sentence = x[filed_name]
            if clean_text:
                sentence = self.clean_seq(sentence)
            if len(sentence.split()) > maxlen:
                continue
            sen_list.append(sentence)
            i += 1
        return sen_list

    def create_sentences(self, size=30, maxlen=30, dataset_name="xsum", dataset_split=None, data_filed="summary",
                         clean_text=False, dataset_type="test"):
        """
        create a list of sentences with str_len and maxlen sepecified from the dataset_name.
        :param size:
        :param maxlen:
        :param dataset_name:
        :param dataset_split:
        :param clean_text:
        :return:
        """
        data_split = ['train[:30%]', 'validation[:30%]', 'test[:30%]']
        if dataset_split:
            data_split = dataset_split

        dataset_all = self.get_dataset(dataset_name, dataset_split=data_split)
        if dataset_type == "train":
            dataset = dataset_all[0]
        elif dataset_type == "valid":
            dataset = dataset_all[1]
        elif dataset_type == "test":
            dataset = dataset_all[2]

        sen_list = self.senlist_from_dataset(dataset, size=size, maxlen=maxlen, data_filed=data_filed,
                                             clean_text=clean_text)
        return sen_list


if __name__ == '__main__':
    test = XsumHfLoader()
    result = test.create_sentences()

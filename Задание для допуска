from math import log

class CountVectorizer():
    '''
    Преобразует список строк в терм-документную матрицу

    '''
    def __init__(self) -> None:
        self.list_of_dict= []

    @staticmethod
    def get_dict_matrix(text:list[str]) -> list[dict]:
        '''
        Функция из списка строк создает список словарей (один словарь для каждой строчки)
        Ключи каждого словаря - все слова, которые встречались в заданном списке строк
        Значения i-го словаря - количество раз, которое слово-ключ встречалось в i-ой строчке

        Аргумент: список строк

        '''

        words = set()
        for string in text:
            words.update([w.lower() for w in string.split()])
        words = list(words)
        list_of_dict = []
        for string in text:
            d = dict.fromkeys(words, 0)
            for word in string.split():
                if word.lower() in words:
                    d[word.lower()] += 1
            list_of_dict.append(d)
        return list_of_dict




    def fit_transform(self, text:list[str]) ->list[list[int]]:
        '''
        Возвращает терм-документную матрицу

        Аргумент: список строк
        '''

        return [list(l.values()) for l in self.get_dict_matrix(text) ]

    def get_feature_names(self, text:list[str]) -> list[str]:
        '''
        Возвращает список всех слов, коортые встречалась в списке строк

        Аргумент: список строк
        '''

        return self.get_dict_matrix(text)[0].keys()



class TfidfTransformer():
    '''
    Преобразует терм-документную матрицу в матрицу, значения которой вычисляются по формуле tf*idf, где

    tf = количество поовторений слова/(сумма всех повторений всех слов)

    idf = ln((всего документов+1)/(документов со словом +1)) + 1

    '''
    def __init__(self) -> None:
        self.matrix= []

    @staticmethod
    def tf_transform(count_matrix:list[list[int]])->list[list[float]]:
        '''
        Возвращает матрицу, значения которой вычисляется по формуле:

        tf = количество поовторений слова/(сумма всех повторений всех слов)

        Аргумент: терм-документную матрица (в формате: список списков)

        '''
        result = []
        for vec in count_matrix:
            sum_vec = sum(vec)
            tf = []
            for symb in vec:
                tf.append(symb/sum_vec)

            result.append(tf)
        return result



    @staticmethod
    def idf_tranform(count_matrix:list[list[int]])->list[list[float]]:
        '''
        Возвращает матрицу, значения которой вычисляется по формуле:

        idf = ln((всего документов+1)/(документов со словом +1)) + 1

        Аргумент: терм-документную матрица (в формате: список списков)

        '''
        result = []
        n = len(count_matrix[0])
        idf = [sum([1 if row[i] else 0 for row in count_matrix]) for i in range(n)]
        idf = [
                log((len(count_matrix)+1)/(el+1))+1 for el in idf
            ]
        return idf



    def fit_transform(self,count_matrix:list[list[int]])->list[list[float]]:
        '''
        Преобразует терм-документную матрицу в матрицу, значения которой вычисляются по формуле tf*idf, где

        tf = количество поовторений слова/(сумма всех повторений всех слов)

        idf = ln((всего документов+1)/(документов со словом +1)) + 1

        аргумент: терм-документную матрица (в формате: список списков)

        '''
        matrix_tf = self.tf_transform(count_matrix)
        idf = self.idf_tranform(count_matrix)
        res = []
        for r in matrix_tf:
            res.append([round(a*b,3) for a,b in zip(r, idf)])
        return res









class TfidfVectorizer(CountVectorizer):
    '''
    Преобразует текст в матрицу, значения которой вычисляются по формуле tf*idf, где

    tf = количество поовторений слова/(сумма всех повторений всех слов)

    idf = ln((всего документов+1)/(документов со словом +1)) + 1

    '''
    def __init__(self) -> None:
        self.count_matrix= []


    def fit_transform(self,text:list[str])->list[list[float]]:
        '''
        Преобразует текст в матрицу, значения которой вычисляются по формуле tf*idf, где

        tf = количество поовторений слова/(сумма всех повторений всех слов)

        idf = ln((всего документов+1)/(документов со словом +1)) + 1

        аргумент: Текст (в формате: список строк)

        '''
        count_matrix = super().fit_transform(text)
        return TfidfTransformer().fit_transform(count_matrix)












if __name__ == "__main__":
    text =  ['Crock Pot Pasta Never boil pasta again',
    'Pasta Pomodoro Fresh ingredients Parmesan to taste']
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(text)
    print(tfidf_matrix)
    print(vectorizer.get_feature_names(text))


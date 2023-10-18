

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


if __name__ == "__main__":
    vectorizer = CountVectorizer()
    text =  ['Crock Pot Pasta Never boil pasta again',
     'Pasta Pomodoro Fresh ingredients Parmesan to taste']
    print(vectorizer.fit_transform(text))
    print(vectorizer.get_feature_names(text))


import os
import pandas as pd

class DataLoader:

    def _validate_file_path(self, filename):
        """Валидация файла."""
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Файл '{filename}' не найден!")
        if os.path.isdir(filename):
            raise FileNotFoundError(f"'{filename}' является директорией, а не файлом!")

    def load_data(self, filename):
        """Загрузка CSV-файла."""
        self._validate_file_path(filename)
        self.df = pd.read_csv(filename)
        self.filename = filename
        return self.df
     
    def get_basic_info(self):
        """Вывод информации о CSV-файле."""
        shape = self.df.shape
        columns = ', '.join(self.df.columns.to_list())
        missing_values = self.df.isnull().sum()
        all_info = f'Форма датасета: {shape}\n Названия столбцов с датасете: {columns}\n Пропущенные значения в столбцах:\n {missing_values}'
        return all_info 
   
    
loader = DataLoader()
df = loader.load_data("sales_data.csv") # Пример файла
info = loader.get_basic_info()
print(info)

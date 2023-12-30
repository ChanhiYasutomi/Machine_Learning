#特殊な値が入っている場合は0で置換
import unicodedata
import re

dataframe['Years of service'] = dataframe['Years of service'].astype(str).apply(lambda s: unicodedata.normalize('NFKC', s))
dataframe['Years of service'] = dataframe['Years of service'].apply(lambda x: x if re.fullmatch('[0-9]{4}.*', x) else 0)
dataframe['Years of service'] = dataframe['Years of service'].str[:4].fillna(0).astype('int64')

#勤務年数80年以上はNULLで置換する。
dataframe['Years of service'] = np.where((2023 - dataframe['Years of service']) < 80, 2023 - dataframe['Years of service'], np.nan)

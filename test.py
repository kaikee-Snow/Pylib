class Province(object):
        country = '中国'

        def __init__(self, name):
                self.name = name


obj = Province('河北省')
print(obj.name)

print(Province.country)

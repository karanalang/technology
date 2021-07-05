from collections import defaultdict

d = defaultdict(str)

d = {}
d.setdefault('missing_key', 'DefaultValue')

d.setdefault('missing_key', 'change the DefaultValue - does not affect the value of existing key')


print(" d -> ", d)
try:
    print("missing_key -> ", d['missing_key'])
except:
    print(" missing key ")

d1 = {}
print(d1.get('missingKey','defaultValue set in get call, does not change the dictionary'))

print(" d1.get(missing2) -> ", d1.get("missing2"))

print(" d1 -> ", d1)

print(" USING DEFAULT DICT")

# not passing anything as .default_factory
defdict = defaultdict()
print(" defauldicy issubclass of dict -> ", issubclass(defaultdict, dict))
defdict['1'] = 1
print(" dd -> ", defdict)
# print(" missing_key in d -> ", defdict['missing_key'])

dd_str = defaultdict(str)
print("dd_str['missing_key'] -> ", dd_str['missing_key'])

dd_list = defaultdict(list)
print("dd_list['missing_key'] -> ", dd_list['missing_key'])
dd_list['missing_list'].append('missing_val')
print(" dd_list, after adding value to listvalue ", dd_list)



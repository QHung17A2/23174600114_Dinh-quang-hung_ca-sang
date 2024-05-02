
inventory={
    'gold':500,
    'pouch':['flint','twine','gemstone'],
    'backpack':['xylophone','dagger','bedroll','bread loaf']
}
#them key'pocket'
inventory["pocket"]=['seashell', 'strange berry',  'lint']
print("Từ điển trên khi thêm  là:",inventory)
# sắp xếp "backpack"
inventory['backpack']=sorted(inventory['backpack'])
print("Từ điển khi sắp xếp lại là:",inventory)
# loại bỏ biến'dagger'
if 'dagger' in inventory['backpack']:
    inventory['backpack'].remove('dagger')
print("Từ điển khi đã xóa là:",inventory)
# thêm giá trị 50 vào 'gold'
inventory['gold']+=50
print("Từ điểm khi thêm là:",inventory)

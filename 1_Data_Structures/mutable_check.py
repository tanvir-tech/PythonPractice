
# var = input("Enter any variable value : ")
var = [1,2,3,'hi']

old_id = id(var)
print(old_id)

var = var.append(5)
new_id = id(var)
print(new_id)


if(new_id==old_id):
    print('Mutable!')
else:
    print('Immutable')









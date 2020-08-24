# Input
array = [1,5,6,7,3,5]
sum = 10
# Output
#[7,3] or [5,5]

def findPair(newArray,sum):
    #clonamos nuestra lista para no afectar a la lista original
    array = newArray[:] 
    for item in newArray:         
        #restamos el elemento actual al parametro suma
        res = sum - item
        #Ahora buscamos si el resultado de la resta existe en la lista
        if res in array:           
            #Si existe entonces cremos una lista nueva
            LIST = []
            #obtenemos el indice que le corresponde al valor de la resta
            position = array.index(res)
            #agregamos a la lista nueva el item y su compelmento para formar la suma
            LIST.append(item)
            LIST.append(array[position])                       
            #print(item,array[position])
            #imprimimos la nueva lista
            print(LIST)
            #eliminamos el item y su complemento para no duplicar busquedas
            array.pop(array.index(item))
            array.pop(position)
        
           
       

findPair(array,sum)




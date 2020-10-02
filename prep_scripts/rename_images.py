
f2 = open('label_data/annot_realValidation.txt','r')
filedata = f2.read()
f2.close()

newdata = filedata.replace(".png", ".jpg")

f2o = open('label_data/annot_realValidation.txt','w')
f2o.write(newdata)
f2o.close()

# f1 = open('label_data/annot_synthetic.txt','r')
# filedata = f1.read()
# f1.close()

# newdata = filedata.replace(".png", ".jpg")

# f1o = open('label_data/annot_synthetic.txt','w')
# f1o.write(newdata)
# f1o.close()


# f2 = open('label_data/annot_realTest.txt','r')
# filedata = f2.read()
# f2.close()

# newdata = filedata.replace(".png", ".jpg")

# f2o = open('label_data/annot_realTest.txt','w')
# f2o.write(newdata)
# f2o.close()


# f3 = open('label_data/annot_realTrain.txt','r')
# filedata = f3.read()
# f3.close()

# newdata = filedata.replace(".png", ".jpg")

# f3o = open('label_data/annot_realTrain.txt','w')
# f3o.write(newdata)
# f3o.close()
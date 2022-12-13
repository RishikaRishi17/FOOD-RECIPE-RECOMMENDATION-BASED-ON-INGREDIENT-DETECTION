imgs=[r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Bean\0001.jpg",r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Bitter_Gourd\1201.jpg",r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Bottle_Gourd\1001.jpg",r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Brinjal\0871.jpg",r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Broccoli\1001.jpg",r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Cabbage\0929.jpg",r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Capsicum\1001.jpg",r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Carrot\1001.jpg",r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Cauliflower\1048.jpg",r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Cucumber\1001.jpg",r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Papaya\1198.jpg",r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Potato\1001.jpg",r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Pumpkin\1001.jpg",r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Radish\1001.jpg",r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Tomato\1001.jpg"
    ,r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Bean\0002.jpg",r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Bitter_Gourd\1202.jpg",r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Bottle_Gourd\1002.jpg",r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Brinjal\0886.jpg",r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Broccoli\1002.jpg",r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Cabbage\0952.jpg",r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Cabbage\0952.jpg",r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Carrot\1002.jpg",r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Cauliflower\1049.jpg",r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Cucumber\1002.jpg",r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Papaya\1199.jpg",r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Potato\1002.jpg",r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Pumpkin\1002.jpg",r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Radish\1002.jpg",r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Tomato\1002.jpg"
    ,r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Bean\0150.jpg",r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Bitter_Gourd\1252.jpg",r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Bottle_Gourd\1017.jpg",r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Brinjal\1009.jpg",r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Broccoli\1018.jpg",r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Cabbage\1012.jpg",r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Capsicum\1018.jpg",r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Carrot\1018.jpg",r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Cauliflower\1065.jpg",r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Cucumber\1017.jpg",r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Papaya\1211.jpg",r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Potato\1019.jpg",r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Pumpkin\1017.jpg",r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Radish\1016.jpg",r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\test\Tomato\1017.jpg"]
oput=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]



import tensorflow as tf
import sys
import os


# Disable tensorflow compilation warnings
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
# Loads label file, strips off carriage return
label_lines = [line.rstrip() for line
                   in tf.gfile.GFile("static/logs/output_labels.txt")]

# Unpersists graph from file
with tf.gfile.FastGFile("static/logs/output_graph.pb", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')

def predct(fn):
    # image_path = sys.argv[1]
    # image_path="C:\\Users\\ELCOT-Lenovo\\Documents\\images\\sign_dataset\\test\\A\\color_0_0016"
    # Read the image_data
    image_data = tf.gfile.FastGFile(fn, 'rb').read()




    with tf.Session() as sess:
        # Feed the image_data as input to the graph and get first prediction
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

        predictions = sess.run(softmax_tensor, \
                 {'DecodeJpeg/contents:0': image_data})

        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

        a = {}
        for node_id in top_k:
            human_string = label_lines[node_id]
            score = predictions[0][node_id]
            # print('%s (score = %.5f)' % (human_string, score))

            if score >= 0.1:
                a[human_string]=score
        return a
cn=["Bean","Bitter_Gourd","Bottle_Gourd","Brinjal","Broccoli","Cabbage","Capsicum","Carrot","Cauliflower","Cucumber","Papaya","Potato","Pumpkin","Radish","Tomato"]

yp=[]
cn1=[]
for i in cn:
    cn1.append(i.lower().replace("_"," "))
for i in imgs:
    res=predct(i)
    print(type(res))
    res=str(res).split("'")
    yp.append(cn1.index(res[1]))

print(oput)
print(yp)
from sklearn.metrics import classification_report
target_names = cn
print("For testing")
print(classification_report(oput, yp, target_names=target_names))

from sklearn import metrics
cf=metrics.confusion_matrix(oput,yp)
print(cf)
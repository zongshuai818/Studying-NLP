from tqdm import tqdm
import jieba
import os

basedir = './THUCNews/' # 数据集文件夹位置
dir_list = ['affairs','constellation','economic','edu','ent','fashion','game','home','house','lottery','science','sports','society','stock']
# 统计数据集中每类样本的数量
for dir_name in dir_list:
    indir = basedir + dir_name + '/'
    print(dir_name, ':', len(os.listdir(indir)))

ftrain = open("news_fasttext_train.txt","w")
ftest = open("news_fasttext_test.txt","w")

train_max_num = 10000 #训练数据数量
test_max_num = 5000 #测试数据数量
for dir_name in tqdm(dir_list):
    count = 0
    indir = basedir + dir_name + '/'
    files = os.listdir(indir)
    for fileName in tqdm(files):
        count += 1
        filepath = indir + fileName
        with open(filepath,'r') as fr:
            text = fr.read()
        text = str(text.encode("utf-8"),'utf-8')
        text = ' '.join(text.replace('\n', ' ').split())
        
        seg_text = jieba.cut(text)
        
        outline = ' '.join(seg_text)
        outline = outline + "\t__label__" + dir_name + "\n"
        if count<= train_max_num:
            ftrain.write(outline)
            ftrain.flush()
            continue
        elif count<= train_max_num + test_max_num:
            ftest.write(outline)
            ftest.flush()
            continue
        else:
            break
            
ftrain.close()
ftest.close()
print('数据预处理完毕')
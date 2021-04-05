from bleurt import score
import os

checkpoint = "my_new_bleurt_checkpoint/export/bleurt_best/1616137291"

scorer = score.BleurtScorer(checkpoint)
def cac_bl(references, candidates):
    
    scores = scorer.score(references, candidates)
    assert type(scores) == list and len(scores) == 1
    return scores

# 求平均数
def cac_avg(l):
    s = 0
    for i in l:
        s+=float(i)
    return s/len(l)
    
# 计算bleurt的函数
def cal_bleurt(references, candidate):
    scores = []
    for ref in references:
        scores.append(cac_bl([ref], [candidate])[0])
    return cac_avg(scores)

# 获取参考答案
refs = []
with open("./references/EC/1.EC ref.txt", encoding="utf8") as f:
    refs.append(f.readlines())
with open("./references/EC/2.EC ref.txt", encoding="utf8") as f:
    refs.append(f.readlines())
with open("./references/EC/3.EC ref.txt", encoding="utf8") as f:
    refs.append(f.readlines())
with open("./references/EC/4.EC ref.txt", encoding="utf8") as f:
    refs.append(f.readlines())
# with open("./references/Ref_sentence_New.txt", encoding="utf8") as f:
#     refs.append(f.readlines())
p_refs = []
n=0
for ref in refs:
    t = []
    n+=1
    for s in ref:
        if len(s)>1:
            a=s[s.index(".")+1:].strip().lower()
            t.append(a)
    p_refs.append(t)
refs = p_refs

# 测试文件夹    
file_path = "./E-C transcripts-sentence-txt/"

# 遍历文件夹，获取文件名，存放在列表files中
files = []
for i,j,k in os.walk(file_path):
    files.extend(k)

bleurt={}
# 遍历测试文件
for fn in files:
    # 打开文件
    with open(file_path+fn, "r", encoding="utf8") as f:
        # 获取文本
        pgs = f.readlines()
        t=[]
        for s in pgs:
            if len(s)>1:
                a=s[s.index(".")+1:].strip().lower()
                t.append(a)
        pgs = t

        key = fn.split(".")[0]
        bleurt[key] = {"bleurt_val":[],"avg_bleurt":0}           
        # 获取每段话的bleurt值
        for i in range(len(pgs)):
            # 获取每句话的ref
            p_refs =[] 
            for j in range(len(refs)):         
                p_refs.append(refs[j][i])
            print(p_refs, pgs[i])
            bleurt_scores = cal_bleurt(p_refs, pgs[i])
            bleurt[key]["bleurt_val"].append(bleurt_scores)
        bleurt[key]["avg_bleurt"] = cac_avg(bleurt[key]["bleurt_val"])
# 保存结果
import json
with open("ec_bleurt_4ref_score.json", "w", encoding="utf8") as f:
    json.dump(bleurt, f, indent=4,sort_keys=True)



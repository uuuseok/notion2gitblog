from datetime import datetime
from pytz import timezone
from glob import glob
import os
import shutil
import zipfile
import re
import argparse


yfm = """---
layout: post
title: {}
subtitle: {}
author: useok
banner:
  image: assets/images/banners/home.jpeg
  opacity: 0.618
  background: "#000"
  height: "40vh"
  min_height: "10vh"
  heading_style: "font-size: 2.5rem; font-weight: bold;"
  subheading_style: "color: gold"
categories: [{}]
tags: [{}]
sidebar: [article-menu,category-list] 
---
"""

parser = argparse.ArgumentParser()
parser.add_argument("--title", "-t", type=str, default="",help="title")
parser.add_argument("--subtitle", "-s", type=str, default="",help="subtitle")
parser.add_argument("--categories", "-c", type=str, default="",help="categories")
parser.add_argument("--tags", "-tag", type=str, default="",help="tags")
args,_ = parser.parse_known_args()





def notion2gitblog(title:str, subtitle:str, categories:str, tags:str):
    # date & fileName #
    fileName = datetime.now(timezone("Asia/seoul")).strftime("%Y-%m-%d-%H%M%S-")+title+".md"

    # notion2gitblog, exportNotionPage, {username}.github.io 디렉토리가가 있는 경로의 부모 디렉토리
    parDir = os.path.abspath(os.path.join(os.getcwd(),os.pardir))


    ##### unzip & remove zip file #####
    # notion에서 export 한 zip 파일 경로
    zip_path = glob(parDir+"/exportNotionPage/*.zip")[0]

    # 압축 해제
    notion_zip = zipfile.ZipFile(zip_path)
    notion_zip.extractall(parDir+"/exportNotionPage")
    notion_zip.close()

    # zip 파일 삭제
    os.remove(zip_path)


    ##### 경로 이동 #####
    # 이미지 폴더 경로
    folder_path = glob(parDir+"/exportNotionPage/*[!.md]")


    #폴더를 블로그 내부 경로로 이동
    if folder_path == []:
        pass # 이미지 폴더가 없다면 pass
    else:
        # 이미지 폴더를 블로그 내부 경로로 이동
        img_path = glob(parDir+"/[!notion2gitblog|!exportNotionPage]*")[0]+"/assets/images/postImages/{}".format(fileName[:-3])
        shutil.move(folder_path[0], img_path)

        # 폴더 조회를 위한 폴더처음 %Y-%m-%d-%H%M%S 문자
        createTime = "-".join(img_path.split('/')[-1].split('-')[:4])

        # 폴더 안 이미지를 순서대로 정렬 [Untitled.png, Untitled 1.png, Untitled 2.png, ...]
        sorted_img_path = glob(os.path.abspath(os.path.join(img_path,os.pardir))+"/{}*/*".format(createTime))
        ordered_li = list(map(lambda x : x.split('/')[-1].split('.')[0][9:], sorted_img_path))
        ordered_li[-1] = '0'
        ordered_li = list(map(int,ordered_li))
        sorted_img_path = sorted(sorted_img_path, key=lambda x: dict(zip(sorted_img_path,ordered_li))[x])


    # md 파일 경로
    md_path = glob(parDir+"/exportNotionPage/*md")[0]

    # md 파일 읽기
    with open(md_path) as f:
        text = f.read()
    
    # md 파일 삭제
    os.remove(md_path)


    # md 파일에서 작성된 이미지 첨부 문자 조회
    start = [x.start() for x in re.finditer("!\[Untitled\]\(",text)] # 이미지 첨부 문자 시작 위치
    end = [x.end() for x in re.finditer("png[)]",text)] # 이미지 첨부 문자 끝 위치
    old_path_li = [text[start[x]:end[x]] for x in range(len(start))] 


    # md 파일에서 첨부된 이미지를 변경된 이미지의 경로로 변환
    try:
        for i in range(len(start)): 
            text = text.replace(old_path_li[i], "![Untitled]("+"/"+"/".join(sorted_img_path[i].split('/')[-5:])+")")
    except:
        print("이미지 없음")
        pass


    # 내 테마에서만 그런건지 모르겠지만, header가 ## 부터 시작함. # 하나를 추가
    text = text.replace("####",'❶❶❶❶❶').replace("###","❷❷❷❷").replace("##","❸❸❸").replace("#",'❹❹').\
    replace("❶❶❶❶❶","#####").replace("❷❷❷❷","####").replace("❸❸❸","###").replace("❹❹",'##')


    # yfm 
    global yfm
    yfm = yfm.format(title, subtitle, categories, tags)
    text = yfm + text

    # .../_posts 디렉토리에 변경된 md파일 저장
    with open(glob(parDir+"/[!notion2gitblog|!exportNotionPage]*")[0]+"/_posts/"+fileName,'w') as f:
        f.write(text)


if __name__ == "__main__":
    notion2gitblog(args.title, args.subtitle, args.categories, args.tags)
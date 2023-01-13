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
  heading_style: "font-size: 4em; font-weight: bold;"
  subheading_style: "color: gold"
categories: [{}]
tags: [{}]
sidebar: [article-menu,category-list] 
---
"""



parser = argparse.ArgumentParser()
parser.add_argument("--title", "-t", type=str, default="제목없음",help="title")
parser.add_argument("--subtitle", "-s", type=str, default="부제없음",help="subtitle")
parser.add_argument("--categories", "-c", type=str, default="카테고리없음",help="categories")
parser.add_argument("--tags", "-tag", type=str, default="태그없음",help="tags")


args,_ = parser.parse_known_args()



def notion2gitblog(title:str, subtitle:str, categories:str, tags:str):
    
    ##### date & fileName #####
    fileName = datetime.now(timezone('Asia/Seoul')).strftime("%Y-%m-%d-")+title+".md"

    ##### unzip #####
    # zip 파일 경로
    zip_path = glob("/Users/factorysunny/Desktop/useok/gitBlog/exportNotionPage/*.zip")[0]    
    
    # 압축 해제
    notion_zip = zipfile.ZipFile(zip_path)
    notion_zip.extractall('/Users/factorysunny/Desktop/useok/gitBlog/exportNotionPage')
    notion_zip.close()
    
    # zip 파일 삭제
    os.remove(zip_path)
    
    ##### 경로 이동 #####
    #이미지,파일 폴더 경로
    folder_path = glob("/Users/factorysunny/Desktop/useok/gitBlog/exportNotionPage/[!uuuseok]*[!.md]")

    #폴더를 블로그 내부 경로로 이동
    if folder_path == []:
        pass
    else:
        # 폴더 이동
        shutil.move(folder_path[0], "/Users/factorysunny/Desktop/useok/gitBlog/uuuseok.github.io/assets/images/postImages/{}".format(fileName[:-3]))

        #폴더 안 이미지를 순서대로 정렬
        image_path = sorted(glob("/Users/factorysunny/Desktop/useok/gitBlog/uuuseok.github.io/assets/images/postImages/{}/*".format(fileName[:-3])))



        img_li = list(map(lambda x : x.split('/')[-1].split('.')[0][9:], image_path))
        img_li[-1] = '0'
        img_li = list(map(lambda x: int(x), img_li))
        sorted_img_li = sorted(image_path, key=lambda x: dict(zip(image_path,img_li))[x])
        
        
    #md 파일 경로
    md_path = glob("/Users/factorysunny/Desktop/useok/gitBlog/exportNotionPage/[!uuuseok]*.md")[0]
    
    
    ##### open file #####
    with open(md_path) as f:
        text = f.read()
    
    # md 파일 삭제
    os.remove(md_path)
    
    ##### 수정 #####
    
    # 이미지 첨부 수정
    start = [x.start() for x in re.finditer("!\[Untitled\]\(",text)] # 이미지 첨부 문자 시작 위치
    end = [x.end() for x in re.finditer("png[)]",text)] # 이미지 첨부 문자 끝 위치
    
    old_path_li = [text[start[x]:end[x]] for x in range(len(start))] 
    
    try:
        for i in range(len(start)): 
            text = text.replace(old_path_li[i], "![Untitled]("+"/"+"/".join(sorted_img_li[i].split('/')[7:])+")") # 새 경로로 변환
    except:
        print("이미지 없음")
        pass
    
    # "#"+1 
    text = text.replace("####",'❶❶❶❶❶').replace("###","❷❷❷❷").replace("##","❸❸❸").replace("#",'❹❹').\
    replace("❶❶❶❶❶","#####").replace("❷❷❷❷","####").replace("❸❸❸","###").replace("❹❹",'##')
    
    
    
    ##### yfm #####
    global yfm
    yfm = yfm.format(title, subtitle, categories, tags)
    text = yfm + text
    
    
    
    
    ##### save #####
    with open("/Users/factorysunny/Desktop/useok/gitBlog/uuuseok.github.io/_posts/"+fileName,'w') as f:
        f.write(text)
    

if __name__ == "__main__":
    notion2gitblog(args.title, args.subtitle, args.categories, args.tags)
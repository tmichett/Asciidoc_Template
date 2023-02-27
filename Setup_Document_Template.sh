#!/bin/bash

echo "**********************************************"
echo "************ Create Chapters *****************"
echo "**********************************************"

echo "How many Chapters in this Book"
read CHAPTERS

for ((i=2;i<=$CHAPTERS;i++))
do
  cp ChapterTMP.adoc Chapter$i.adoc
done

echo "**********************************************"
echo "***** Create Chapters Sections/Folders *******"
echo "**********************************************"

cd Chapters
for ((i=2;i<=$CHAPTERS;i++))
do
  cp -avR CH_TMP CH$i
done

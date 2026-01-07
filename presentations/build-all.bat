@echo off
echo Building all presentations...

cd lectures\week01
pdflatex week01-intro-rag.tex
cd ..\..

cd lectures\week02
pdflatex week02-git-python.tex
cd ..\..

cd lectures\week03
pdflatex week03-docker-opensearch.tex
cd ..\..

cd lectures\week04
pdflatex week04-fastapi.tex
cd ..\..

cd lectures\week05
pdflatex week05-opensearch.tex
cd ..\..

cd lectures\week06
pdflatex week06-embeddings.tex
cd ..\..

cd lectures\week07
pdflatex week07-rag-llm-streamlit.tex
cd ..\..

cd lectures\week08
pdflatex week08-docker-compose.tex
cd ..\..

cd lectures\week09
pdflatex week09-cicd.tex
cd ..\..

echo Done!
pause

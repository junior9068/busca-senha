#!/bin/bash

# REPOSITORIO = sevir/autobots.git

REPOSITORIO=$1

DIRETORIO=`echo $REPOSITORIO | awk -F/ '{print $2}' | awk -F. '{print $1}'`

SETOR=`echo $REPOSITORIO | awk -F/ '{print $1}'`

git clone https://${token}@git.camara.gov.br/$REPOSITORIO.git

cd $DIRETORIO
a=`code `

if [[ ! -z $a ]]; then
   echo "ESTE REPOSITÓRIO TEM SENHA EM TEXTO"
   echo $REPOSITORIO >> ../lista-projetos-$SETOR.txt
fi
cd ..

rm -rf $DIRETORIO


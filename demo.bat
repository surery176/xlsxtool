:start
@echo off
color 0A


::Ҫ�����Ŀ¼
SET execPath=./demoxlsx

::ǰ�˵���json·��
SET saveClientJsonSrc=./out/client.json

::ǰ��tsģ��·��
SET templateClientSrc=./template/template_xy.ts

::ǰ�˵���ts·��
SET saveClientSrc=./out/client.ts

::����������json·��
SET saveServerJsonSrc=./out/server.json

::������pyģ��·��
SET templateServerSrc=./template/template.py

::����������py·��
SET saveServerSrc=./out/resobj.py

::�����������ṹ���pack��
SET gopack=main

::��ͼ�༭������������·��
SET mapSrc=./demoxlsx/map/


newxlsxtool.exe -idir=%execPath% -clientojson=%saveClientJsonSrc% -clientitemp=%templateClientSrc% -clientotemp=%saveClientSrc% -pkgn=%gopack% -serverojson=%saveServerJsonSrc% -serveritemp=%templateServerSrc% -serverotemp=%saveServerSrc% -mapSrc=%mapSrc%

set choice=
set /p choice=  ��������˳�


:start
@echo off
color 0A


::要处理的目录
SET execPath=./demoxlsx

::前端导出json路径
SET saveClientJsonSrc=./out/client.json

::前端ts模板路径
SET templateClientSrc=./template/template_xy.ts

::前端导出ts路径
SET saveClientSrc=./out/client.ts

::服务器导出json路径
SET saveServerJsonSrc=./out/server.json

::服务器py模板路径
SET templateServerSrc=./template/template.py

::服务器导出py路径
SET saveServerSrc=./out/resobj.py

::服务器导出结构体的pack名
SET gopack=main

::地图编辑器导出的配置路径
SET mapSrc=./demoxlsx/map/


newxlsxtool.exe -idir=%execPath% -clientojson=%saveClientJsonSrc% -clientitemp=%templateClientSrc% -clientotemp=%saveClientSrc% -pkgn=%gopack% -serverojson=%saveServerJsonSrc% -serveritemp=%templateServerSrc% -serverotemp=%saveServerSrc% -mapSrc=%mapSrc%

set choice=
set /p choice=  按任意键退出


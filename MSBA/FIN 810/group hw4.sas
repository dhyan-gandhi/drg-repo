proc import out=all_stocks
datafile='/home/u37563288/my_content/FIN810/all_stocks.csv' 
dbms=csv replace;
getnames=yes;
datarow=2;
run;

data dis;
set all_stocks;
where Symbol='DIS';
run;

data fb;
set all_stocks;
where Symbol='FB';
run;

data goo;
set all_stocks;
where Symbol='GOO';
run;

data jnj;
set all_stocks;
where Symbol='JNJ';
run;

data rok;
set all_stocks;
where Symbol='ROK';
run;

data dis1;
set dis;
ret_dis=AdjClose/lag(AdjClose)-1;
run;

data fb1;
set fb;
ret_fb=AdjClose/lag(AdjClose)-1;
run;

data goo1;
set goo;
ret_googl=AdjClose/lag(AdjClose)-1;
run;

data jnj1;
set jnj;
ret_jnj=AdjClose/lag(AdjClose)-1;
run;

data rok1;
set rok;
ret_roku=AdjClose/lag(AdjClose)-1;
run;

proc means data=fb1;
var ret_fb;
run;

proc means data=goo1;
var ret_googl;
run;

proc means data=dis1;
var ret_dis;
run;

proc means data=jnj1;
var ret_jnj;
run;

proc means data=rok1;
var ret_roku;
run;

proc import
out=ff
datafile='/home/u37563288/my_content/FIN810/F-F_Research_Data_5_Factors_2x3_daily.CSV'
dbms=csv replace;
getnames=yes;
datarow=2;
run;

proc contents data=ff;
run;

data ff1;
set ff;
DATE1 = INPUT(PUT(var1,8.),YYMMDD8.);
format DATE1 YYMMDD10.;
year=year(date1);
mkt_rf_d=mkt_rf/100;
smb_d=smb/100;
hml_d=hml/100;
rmw_d=rmw/100;
cma_d=cma/100;
rf_d=rf/100;
run;

data ff2018;
set ff1;
where year=2018;
run;

proc sort data=dis1;
by date;
run;

proc sort data=fb1;
by date;
run;

proc sort data=goo1;
by date;
run;

proc sort data=jnj1;
by date;
run;

proc sort data=rok1;
by date;
run;

proc sort data=ff2018;
by date1;
run;

proc sql;
create table dis_ff_reg as
select *
from dis1, ff2018
where dis1.date=ff2018.date1;
quit;

proc sql;
create table fb_ff_reg as
select *
from fb1, ff2018
where fb1.date=ff2018.date1;
quit;

proc sql;
create table googl_ff_reg as
select *
from goo1, ff2018
where goo1.date=ff2018.date1;
quit;

proc sql;
create table jnj_ff_reg as
select *
from jnj1, ff2018
where jnj1.date=ff2018.date1;
quit;

proc sql;
create table roku_ff_reg as
select *
from rok1, ff2018
where rok1.date=ff2018.date1;
quit;

data dis_ff_reg1;
set dis_ff_reg;
rp=ret_dis-rf_d;
run;

data fb_ff_reg1;
set fb_ff_reg;
rp=ret_fb-rf_d;
run;

data googl_ff_reg1;
set googl_ff_reg;
rp=ret_googl-rf_d;
run;

data jnj_ff_reg1;
set jnj_ff_reg;
rp=ret_jnj-rf_d;
run;

data roku_ff_reg1;
set roku_ff_reg;
rp=ret_roku-rf_d;
run;

proc reg data=fb_ff_reg1;
ff_5factor: model rp = mkt_rf_d smb_d hml_d rmw_d cma_d;
run;

proc reg data=googl_ff_reg1;
ff_5factor: model rp = mkt_rf_d smb_d hml_d rmw_d cma_d;
run;

proc reg data=dis_ff_reg1;
ff_5factor: model rp = mkt_rf_d smb_d hml_d rmw_d cma_d;
run;

proc reg data=jnj_ff_reg1;
ff_5factor: model rp = mkt_rf_d smb_d hml_d rmw_d cma_d;
run;

proc reg data=roku_ff_reg1;
ff_5factor: model rp = mkt_rf_d smb_d hml_d rmw_d cma_d;
run;
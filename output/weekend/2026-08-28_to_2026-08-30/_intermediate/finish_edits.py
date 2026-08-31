from pathlib import Path
p=Path(__file__).parent
f=p/'finalize_report.py'
t=f.read_text(encoding='utf-8')
t=t.replace('于8月28日开启EP02第二轮测试；融合','于8月28日开启EP02第二轮测试，现有公布信息未区分端游或手游；融合')
t=t.replace('AI反扫：覆盖全部行业候选，GIGA、巨人研发AI与游族创作工具转入AI','AI反扫：覆盖全部行业候选，GIGA、Vox与游族创作工具转入AI；巨人披露优先保留发行合作')
t=t.replace('产品日历反扫：','产品日历漏挂反查：')
t=t.replace('维度覆盖自检：','E×R+M：行业只按总分≥7筛选，无条数上限，按分数降序。时间无法定位的滚动目录/展会综述单独排除，不以采集时间冒充事件时间。维度覆盖自检：')
f.write_text(t,encoding='utf-8')
f=p/'repair_calendar.py';t=f.read_text(encoding='utf-8')
t=t.replace("elif p=='Zomline Survival':change(n,event_date='2026-06-01');reject(n,'正文只写6月上线；日期仅作月份边界标识，不用于发表')", "elif p=='Zomline Survival':change(n,date_precision='month_only',event_month='2026-06');reject(n,'正文只写6月上线；不补具体日期，不用于发表')")
f.write_text(t,encoding='utf-8')

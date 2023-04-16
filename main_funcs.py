from enum_keys import EnumKeys as ek
from TSC_utility import TscUtility as tu
import tableauserverclient as TSC
import py_utility as pu
import datetime

def get_job_info(window, values):
    if not tu.login():
        return

    jobId = str(values[ek.JOB_ID_INPUT]).strip()
    jobInfo = tu.server.jobs.get_by_id(jobId)
    targetId = ''
    nameHeader = ''
    all_contents = []

    if jobInfo.type == 'RunFlow':
        targetId = jobInfo.flow_run.flow_id
        nameHeader = 'フロー名：'
        all_contents = list(TSC.Pager(tu.server.flows, tu.request_options))
    else:
        targetId = jobInfo.datasource_id
        nameHeader = 'データソース名：'
        all_contents = list(TSC.Pager(tu.server.datasources, tu.request_options))

    status = ''
    note = ''
    if jobInfo.finish_code == TSC.JobItem.FinishCode.Success:
        status = '成功'
    elif jobInfo.finish_code == TSC.JobItem.FinishCode.Failed:
        status = '失敗'
        note = jobInfo.notes[0]
    elif jobInfo.finish_code == TSC.JobItem.FinishCode.Cancelled:
        status = 'キャンセル'
        note = jobInfo.notes[0]
    else:
        status = '実行中'
        if jobInfo.started_at is None:
            status = '保留中'
    
    start_time = '-'
    if jobInfo.created_at is not None:
        start_time = (jobInfo.created_at + datetime.timedelta(hours=9)).strftime('%X')

    end_time = '-'
    if jobInfo.completed_at is not None:
        end_time = (jobInfo.completed_at + datetime.timedelta(hours=9)).strftime('%X')
    
    run_time = '-'
    if jobInfo.started_at is not None:
        if jobInfo.completed_at is not None:
            run_time = pu.get_diff_time_str(jobInfo.started_at, jobInfo.completed_at)
        else:
            run_time = pu.get_diff_time_str(jobInfo.started_at, datetime.datetime.now(datetime.timezone.utc))

    que_time = '-'
    if jobInfo.created_at is not None:
        if jobInfo.started_at is not None:
            que_time = pu.get_diff_time_str(jobInfo.created_at, jobInfo.started_at)
        else:
            que_time = pu.get_diff_time_str(jobInfo.created_at, datetime.datetime.now(datetime.timezone.utc))
    
    total_time = '-'
    if jobInfo.created_at is not None:
        if jobInfo.completed_at is not None:
            total_time = pu.get_diff_time_str(jobInfo.created_at, jobInfo.completed_at)
        else:
            total_time = pu.get_diff_time_str(jobInfo.created_at, datetime.datetime.now(datetime.timezone.utc))

    info = ''
    for content in all_contents:
        if content.id == targetId:
            info  = 'ジョブ情報取得時刻：' + datetime.datetime.now().strftime('%X') + '\n'
            info += 'プロジェクト名：' + content.project_name + '\n'
            info += nameHeader + content.name + '\n'
            info += 'ステータス：' + status + '\n'
            if note != '':
                info += '理由：' + note + '\n'
            
            info += '開始時刻：' + start_time + '\n'
            info += '終了時刻：' + end_time + '\n'
            info += '実行時間：' + run_time + '\n'
            info += '保留時間：' + que_time + '\n'
            info += '合計時間：' + total_time
            break
    
    if info == '':
        info = '入力されたLUIDで該当がありませんでした'

    window[ek.JOB_INFO_MULTILINE].update(value=info)
NEXT_TASK=`task rc.verbose: rc.report.next.columns:description rc.report.next.labels:1 limit:1 next`
NEXT_TASK_ID=`task rc.verbose: rc.report.next.columns:id rc.report.next.labels:1 limit:1 next`
echo "${NEXT_TASK_ID}: ${NEXT_TASK^}"

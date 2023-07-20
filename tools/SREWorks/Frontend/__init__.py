
from typing import Dict,List,Optional

class Column(TypedDict):
    dataIndex: str
    label: str
    filters: Optional[List[str]]
    render: Optional[str]
    defaultSortOrder: Optional[str]

def table(columns: List[Column]) -> Dict:
    """This tool can generate low-code tables json schema"""
    return {"columns": columns}


class Table():
    """This tool can generate low-code tables json schema"""
    columns = []
    title = ""
    def __init__(self, title: str):
        self.title = title

    def add_column(self, dataIndex: str, label: str) -> Dict:
        

        if host == None or self._client_host == host:
            stdin, stdout, stderr = self._client.exec_command(command)
        else:
            stdin, stdout, stderr = self._client.exec_command("ssh " +  host +  " '" + command + "'")

        retcode  = stdout.channel.recv_exit_status()
        output_stdout = stdout.read().decode('utf-8')
        output_stderr = stderr.read().decode('utf-8')

        stdin = None
        stdout = None
        stderr = None

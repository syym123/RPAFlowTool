# flow_step.py
from dataclasses import dataclass

@dataclass
class FlowStep:
    id: int
    type: str                     # 新增 'upload'
    name: str = ""
    selector: str = ""
    selector_type: str = "xpath"
    value: str = ""
    field_name: str = ""
    extract_attr: str = "text"
    timeout: int = 5000
    pre_wait_seconds: int = 0
    pre_wait_element: bool = False
    pre_wait_xpath: str = ""
    date_format: str = ""
    use_today: bool = True
    fixed_date: str = ""
    js_code: str = ""
    upload_file_path: str = ""    # 上传文件路径，支持占位符 {download:...}
    python_code: str = ""
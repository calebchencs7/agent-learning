"""本地开发接口：将页面请求转交给已有的文本模型。"""

import importlib.util
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

def load_model(name, filename):
    path = Path(__file__).resolve().parent.parent / filename
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


model = load_model('financial_classification', '案例2_基于金融文本_分类项目.py')
extraction_model = load_model('financial_extraction', '案例3_基于金融文本_抽取项目.py')
matching_model = load_model('financial_matching', '案例4_基于金融文本_匹配项目.py')


class Handler(BaseHTTPRequestHandler):
    def send_json(self, status, payload):
        data = json.dumps(payload, ensure_ascii=False).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_POST(self):
        if self.path not in ('/api/classify', '/api/extract', '/api/match'):
            return self.send_json(404, {'error': '接口不存在'})
        try:
            length = int(self.headers.get('Content-Length', '0'))
            if length <= 0 or length > 300_000:
                return self.send_json(400, {'error': '请求内容为空或过长'})
            body = json.loads(self.rfile.read(length))
            text = body.get('text') if isinstance(body, dict) else None
            if not isinstance(text, str) or not text.strip():
                return self.send_json(400, {'error': '请输入文本'})
            if self.path == '/api/match':
                text2 = body.get('text2')
                if not isinstance(text2, str) or not text2.strip():
                    return self.send_json(400, {'error': '请输入第二段文本'})
                result = matching_model.match_model([(text.strip(), text2.strip())])
                return self.send_json(200, {'result': result[0]})
            if self.path == '/api/extract':
                result = extraction_model.extract_model([text.strip()])
                return self.send_json(200, {'result': result[0]})
            result = model.classify_model([text.strip()])
            return self.send_json(200, {'category': result[0]})
        except (ValueError, UnicodeDecodeError):
            return self.send_json(400, {'error': '请求格式不正确'})
        except Exception as exc:
            print(f'模型请求失败: {exc}', flush=True)
            return self.send_json(
                502, {'error': '模型调用失败，请检查后端配置和网络连接。'}
            )


if __name__ == '__main__':
    server = ThreadingHTTPServer(('127.0.0.1', 8000), Handler)
    print('文本分析接口运行于 http://127.0.0.1:8000', flush=True)
    server.serve_forever()

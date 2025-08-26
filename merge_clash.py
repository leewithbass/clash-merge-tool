import requests
import base64
import yaml
from urllib.parse import urlparse, unquote
import re
from rich.console import Console
from rich.prompt import Prompt
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table

# 初始化 rich 控制台
console = Console()

def get_subscription_urls():
    """获取用户输入的订阅链接"""
    urls = []
    console.print("[bold cyan]请输入订阅链接，每行一个。输入空行或 'done' 结束:[/bold cyan]")
    while True:
        try:
            url = input().strip()
            if not url or url.lower() == 'done':
                break
            if url.startswith("http"):
                urls.append(url)
            else:
                console.print("[bold red]无效的链接，请确保以 http 或 https 开头。[/bold red]")
        except (EOFError, KeyboardInterrupt):
            # 如果遇到EOF或中断信号，跳出循环
            break
    return urls

def decode_subscription_content(content):
    """解码 Base64 编码的订阅内容"""
    # 首先检查内容是否已经是明文（不是Base64编码）
    try:
        # 如果内容可以被解析为URL或包含明显的明文特征，则认为它已经是明文
        if content.startswith("ss://") or "://" in content:
            return content
    except:
        pass
    
    # 确保内容是字节类型
    if isinstance(content, str):
        # 先尝试直接编码为ASCII
        try:
            content = content.encode('ascii')
        except UnicodeEncodeError:
            # 如果包含非ASCII字符，可能已经解码过了
            return content
    
    # 尝试直接解码
    try:
        # 修复Base64填充
        missing_padding = len(content) % 4
        if missing_padding:
            content += b'=' * (4 - missing_padding)
        decoded_bytes = base64.b64decode(content)
        return decoded_bytes.decode('utf-8')
    except Exception as e1:
        try:
            # 如果直接解码失败，尝试 URL 安全的解码
            missing_padding = len(content) % 4
            if missing_padding:
                content += b'=' * (4 - missing_padding)
            decoded_bytes = base64.urlsafe_b64decode(content)
            return decoded_bytes.decode('utf-8')
        except Exception as e2:
            console.print(f"[bold red]解码失败: {e1} | {e2}[/bold red]")
            return content  # 如果所有解码都失败，返回原始内容

def parse_ss_url(ss_url):
    """解析 Shadowsocks URL"""
    try:
        if ss_url.startswith("ss://"):
            parsed = urlparse(ss_url)
            
            # 获取 userinfo@server:port 部分
            netloc = parsed.netloc
            fragment = unquote(parsed.fragment)  # 解码URL编码的片段
            
            # 分离 userinfo@server:port 和可能的查询参数
            if '#' in netloc:
                userinfo_server_port = netloc.split('#')[0]
            else:
                userinfo_server_port = netloc
            
            # 分离 userinfo 和 server:port
            if '@' in userinfo_server_port:
                userinfo, server_port = userinfo_server_port.split('@', 1)
            else:
                return None
            
            # 解码 userinfo (这部分是 base64 编码的)
            try:
                # 修复填充
                missing_padding = len(userinfo) % 4
                if missing_padding:
                    userinfo += '=' * (4 - missing_padding)
                decoded_userinfo = base64.b64decode(userinfo).decode('utf-8')
            except Exception as e:
                return None
            
            # 分离 method:password
            if ':' in decoded_userinfo:
                method, password = decoded_userinfo.split(':', 1)
            else:
                return None
            
            # 分离 server 和 port
            if ':' in server_port:
                server, port_str = server_port.rsplit(':', 1)
                try:
                    port = int(port_str)
                except ValueError:
                    return None
            else:
                return None
            
            # 使用片段作为名称，如果没有则使用服务器和端口
            name = fragment if fragment else f"{server}:{port}"
            # 清理节点名称中的特殊字符
            name = re.sub(r'[,;:$]', '-', name)
            
            return {
                "name": name,
                "type": "ss",
                "server": server,
                "port": port,
                "cipher": method,
                "password": password
            }
        return None
    except Exception as e:
        console.print(f"[bold red]解析 ss 链接时出错: {e}[/bold red]")
        return None

def fetch_and_parse_subscriptions(urls):
    """获取并解析所有订阅链接"""
    all_nodes = []
    
    # 添加请求头来模拟真实浏览器请求
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        task = progress.add_task("[cyan]正在获取订阅...", total=len(urls))
        
        for url in urls:
            try:
                response = requests.get(url, headers=headers)
                response.raise_for_status()
                
                # 解码内容
                decoded_content = decode_subscription_content(response.text)
                if not decoded_content:
                    console.print(f"[bold yellow]警告: 无法解码订阅内容 {url}[/bold yellow]")
                    continue
                
                # 按行分割
                lines = decoded_content.splitlines()
                
                # 解析每个节点
                for line in lines:
                    if line.startswith("ss://"):
                        node = parse_ss_url(line)
                        if node:
                            # 过滤掉信息性节点（检查节点名称是否包含典型的服务器信息）
                            name = node["name"]
                            if not any(keyword in name for keyword in ["剩余流量", "距离下次", "套餐到期", "重置", "到期"]):
                                all_nodes.append(node)
                            
                progress.update(task, advance=1)
            except Exception as e:
                console.print(f"[bold red]获取或解析订阅 {url} 时出错: {e}[/bold red]")
                
    return all_nodes

def extract_region(name):
    """从节点名称中提取地区"""
    # 转换为大写以便匹配
    name_upper = name.upper()
    
    # 常见地区代码映射
    region_mapping = {
        # 亚洲
        "HK": "HK", "HONG KONG": "HK", "香港": "HK", "🇭🇰": "HK",
        "SG": "SG", "SINGAPORE": "SG", "新加坡": "SG", "🇸🇬": "SG",
        "JP": "JP", "JAPAN": "JP", "日本": "JP", "🇯🇵": "JP",
        "KR": "KR", "KOREA": "KR", "韩国": "KR", "🇰🇷": "KR",
        "TW": "TW", "TAIWAN": "TW", "台湾": "TW", "🇨🇳": "TW",
        "IN": "IN", "INDIA": "IN", "印度": "IN", "🇮🇳": "IN",
        
        # 欧洲
        "UK": "UK", "UNITED KINGDOM": "UK", "英国": "UK", "🇬🇧": "UK",
        "DE": "DE", "GERMANY": "DE", "德国": "DE", "🇩🇪": "DE",
        "FR": "FR", "FRANCE": "FR", "法国": "FR", "🇫🇷": "FR",
        "NL": "NL", "NETHERLANDS": "NL", "荷兰": "NL", "🇳🇱": "NL",
        "RU": "RU", "RUSSIA": "RU", "俄罗斯": "RU", "🇷🇺": "RU",
        
        # 北美
        "US": "US", "USA": "US", "UNITED STATES": "US", "美国": "US", "🇺🇸": "US",
        "CA": "CA", "CANADA": "CA", "加拿大": "CA", "🇨🇦": "CA",
        
        # 大洋洲
        "AU": "AU", "AUSTRALIA": "AU", "澳大利亚": "AU", "🇦🇺": "AU",
    }
    
    # 尝试匹配地区代码
    for keyword, region in region_mapping.items():
        if keyword in name_upper:
            return region
            
    # 如果没有匹配到，返回默认值
    return "OTHER"

def group_nodes_by_region(nodes):
    """按地区对节点进行分组"""
    groups = {}
    
    for node in nodes:
        region = extract_region(node["name"])
        if region not in groups:
            groups[region] = []
        groups[region].append(node)
        
    return groups

def generate_config(nodes, output_file):
    """生成 Clash 配置文件"""
    # 按地区分组
    region_groups = group_nodes_by_region(nodes)
    
    # 基础配置
    config = {
        "port": 7890,
        "socks-port": 7891,
        "allow-lan": False,
        "mode": "rule",
        "log-level": "info",
        "external-controller": "127.0.0.1:9090",
        "proxies": nodes,
        "proxy-groups": [],
        "rules": [
            "MATCH,PROXY"
        ]
    }
    
    # 创建代理组
    proxy_groups = []
    
    # 手动选择组，包含所有节点
    manual_group = {
        "name": "MANUAL-SELECT",
        "type": "select",
        "proxies": [node["name"] for node in nodes]
    }
    proxy_groups.append(manual_group)
    
    # 地区分组
    region_group_names = []
    for region, region_nodes in region_groups.items():
        if region_nodes:  # 确保有节点
            group_name = f" {region}"  # 前面加空格以符合 Clash 命名习惯
            region_group_names.append(group_name)
            
            group = {
                "name": group_name,
                "type": "url-test",
                "url": "http://www.gstatic.com/generate_204",
                "interval": 300,
                "proxies": [node["name"] for node in region_nodes]
            }
            proxy_groups.append(group)
    
    # 主选择组
    main_group = {
        "name": "PROXY",
        "type": "select",
        "proxies": region_group_names + ["MANUAL-SELECT"]
    }
    proxy_groups.insert(0, main_group)  # 将主选择组放在最前面
    
    config["proxy-groups"] = proxy_groups
    
    # 写入配置文件
    with open(output_file, 'w', encoding='utf-8') as f:
        yaml.dump(config, f, allow_unicode=True, default_flow_style=False)
    
    console.print(f"[bold green]配置文件已生成: {output_file}[/bold green]")
    
    # 显示节点统计信息
    table = Table(title="节点统计")
    table.add_column("地区", style="cyan")
    table.add_column("节点数量", style="magenta")
    
    for region, region_nodes in region_groups.items():
        table.add_row(region, str(len(region_nodes)))
        
    console.print(table)

def main():
    """主函数"""
    console.print("[bold blue]欢迎使用 Clash 订阅合并工具![/bold blue]")
    
    # 获取订阅链接
    urls = get_subscription_urls()
    if not urls:
        console.print("[bold yellow]没有输入任何有效的订阅链接。[/bold yellow]")
        return
    
    # 获取输出文件名
    output_file = Prompt.ask("[bold cyan]请输入输出配置文件名[/bold cyan]", default="config.yaml")
    
    # 确保输出文件在脚本同一目录下
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(script_dir, output_file)
    
    # 获取并解析订阅
    nodes = fetch_and_parse_subscriptions(urls)
    if not nodes:
        console.print("[bold yellow]没有解析到任何有效的节点。[/bold yellow]")
        return
    
    # 生成配置文件
    generate_config(nodes, output_file)
    
    console.print("[bold green]所有操作已完成！[/bold green]")

if __name__ == "__main__":
    main()
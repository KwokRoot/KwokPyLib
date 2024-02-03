# #快速执行和管理子进程
# pip install envoy
import envoy

# 运行 'git config' 命令
r = envoy.run('git config', timeout=2)

print(r.status_code)  # 输出：129
print(r.std_out)      # 输出：'usage: git config [options]'
print(r.std_err)      # 输出：''


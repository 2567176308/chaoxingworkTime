import yaml

# 存入config.yaml
def save_id_pwd(id,pwd, file='config.yaml'):
    data = {}
    data['id'] = id
    data['pwd'] = pwd
    
    with open(file, 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)
# 从config.yaml中取出

def load_data(file='config.yaml'):
    with open(file, 'r') as stream:
        data = yaml.safe_load(stream)
        return data['id'], data['pwd']
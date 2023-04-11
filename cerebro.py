import requests, os, subprocess

TOKEN = os.environ["token"]
HEADERS = {'Authorization': f'token {TOKEN}'}

# logging.basicConfig(filename='log.txt',
#                     filemode='a',
#                     format='%(asctime)s %(name)s %(levelname)s %(message)s',
#                     datefmt='%H:%M:%S',
#                     level=logging.DEBUG)


def lista_organizacoes():
    try:
        r = requests.get(url=f"https://git.camara.gov.br/api/v1/orgs")
        orgs = r.json()
        lista = []
        for org in orgs:
            lista.append(org["username"])
        return lista
    except:
        return "ERRO"


def lista_repositorios(organizacao):
    try:
        r = requests.get(url=f"https://git.camara.gov.br/api/v1/orgs/{organizacao}/repos?limit=10000", headers=HEADERS)
        repos = r.json()
        lista = []
        for repo in repos:
            lista.append(repo["full_name"])
        return lista
    except:
        return "ERRO"

def lista_repositorios_privados():
    r = requests.get(url=f"https://git.camara.gov.br/api/v1/user/repos?limit=10000", headers=HEADERS)
    repos = r.json()
    lista = []
    for repo in repos:
        if repo["private"] != False:
            lista.append(repo["full_name"])
    return lista


if __name__ == "__main__":
    repositorios = lista_repositorios("sevir")
    for repositorio in repositorios:
        subprocess.call(["./busca-senha.sh", repositorio])

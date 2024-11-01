import asyncio
from enum import Enum

from quart import Quart, render_template
import requests


# Define the NERSC systems enum
class Resource(str, Enum):
    perlmutter = "perlmutter"
    cori = "cori"
    dna = "dna"
    dtns = "dtns"
    global_homes = "global_homes"
    global_common = "global_common"
    community_filesystem = "community_filesystem"
    iris = "iris"
    globus = "globus"
    jupyter = "jupyter"
    nersc_center = "nersc_center"
    helpportal = "helpportal"
    website = "website"
    rstudio = "rstudio"
    sgns = "sgns"
    network = "network"
    ldap = "ldap"
    integ_datalanguage = "integ_datalanguage"
    mathematica = "mathematica"
    spin = "spin"
    mongodb = "mongodb"
    matlab = "matlab"
    jgi_int_webservers = "jgi_int_webservers"
    jgidb = "jgidb"
    _int = "int"
    webservers = "webservers"
    ssh_proxy = "ssh-proxy"
    sciencedatabases = "sciencedatabases"
    myproxy = "myproxy"
    nomachine = "nomachine"
    newt = "newt"
    regent = "regent"
    archive = "archive"


Resource.__str__ = lambda self: self.value


# Function to fetch status for each system individually
def fetch_system_status():
    base_url = "https://api.nersc.gov/api/v1.2/status/"
    systems_status = {}
    for system in Resource:
        try:
            response = requests.get(f"{base_url}{system}")
            response.raise_for_status()
            systems_status[system] = response.json()
            print(system, systems_status[system])
        except requests.RequestException as e:
            systems_status[system] = {"status": "unknown", "error": str(e)}
    return systems_status


# Quart app setup
app = Quart(__name__)


@app.route('/')
async def index():
    loop = asyncio.get_event_loop()
    systems_status = await loop.run_in_executor(None, fetch_system_status)
    return await render_template('index.html', systems_status=systems_status)

if __name__ == '__main__':
    app.run(debug=True)

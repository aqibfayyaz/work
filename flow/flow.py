from prefect import Flow, task
from prefect.storage import GitHub
from prefect.run_configs import KubernetesRun
#from prefect.client import Secret
from prefect.tasks.secrets import PrefectSecret

FLOW_NAME = "flow"
STORAGE = GitHub(
    repo="aqibfayyaz/work",
    path=f"flows/{FLOW_NAME}.py",
    access_token_secret=PrefectSecret("MYTOKEN"),  # required with private repositories
)


@task(log_stdout=True)
def hello_world():
    text = f"hello from {FLOW_NAME}"
    print(text)
    return text


with Flow(
    FLOW_NAME, storage=STORAGE, run_config=KubernetesRun()
) as flow:
    hw = hello_world()

#flow.register(project_name="tutorial")
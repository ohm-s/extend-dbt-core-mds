# Set up 

## Install dependencies

Create a virtual environment, using conda for example

```bash
conda create -n extend-dbt python=3.10
conda activate extend-dbt
```

Install dependencies

```bash
pip install -r requirements.txt
```

Then you can use dbt.sh to run dbt commands

```bash
./dbt.sh list
```

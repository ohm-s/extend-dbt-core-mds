{#```doc
description: |
    This macro will loop over all SQL files in the project macros
    and generate docs in the format which DBT expects
```#}

{% macro prepare_macro_docs() %}
    {% set module_loaded = modules.dynamic.load_module('docs', env_var('DBT_PROJECT_DIR') ~ '/macros/__dynamic_modules__/docs/docs.py') %}
    {% do modules.dynamic.inc["docs"].extract_dbt_docs(env_var('DBT_PROJECT_DIR') ~ '/macros')  %}
{% endmacro %}
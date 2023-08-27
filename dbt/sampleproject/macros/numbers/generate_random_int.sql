{#```doc
description: |
    Generate a random int between 0 and provided scale
arguments:
    - name: scale
      type: int
      description: The maximum value of the random int
```#}

{% macro generate_random_int(scale=100) %}
    {% if execute %}
        {{ modules.dynamic.inc['sample'].generate_random_int(scale) }}
    {% endif %}
{% endmacro %}
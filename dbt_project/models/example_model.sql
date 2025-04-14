{{ config(materialized='table') }}

SELECT
  s.id,
  s.name,
  CURRENT_TIMESTAMP AS updated_at
FROM {{ ref('sample_seed') }} s
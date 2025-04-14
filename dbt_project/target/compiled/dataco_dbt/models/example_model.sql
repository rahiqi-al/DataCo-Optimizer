

SELECT
  s.id,
  s.name,
  CURRENT_TIMESTAMP AS updated_at
FROM dataco.public.sample_seed s
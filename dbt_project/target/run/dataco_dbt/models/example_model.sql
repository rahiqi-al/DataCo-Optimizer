
  
    

        create or replace transient table dataco.public.example_model
         as
        (

SELECT
  s.id,
  s.name,
  CURRENT_TIMESTAMP AS updated_at
FROM dataco.public.sample_seed s
        );
      
  
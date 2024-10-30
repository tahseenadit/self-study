In this setup, you won’t be able to access `ENV_NAME` in the `test` job as it’s currently written. The reason is that **environment variables set within a job (like `ENV_NAME` in `extract-environment-name`) are not automatically shared as outputs to other jobs**. When `ENV_NAME` is set in `extract-environment-name` using `echo "ENV_NAME=..." >> $GITHUB_ENV`, it’s available only within that job, not passed to other jobs.

To make `ENV_NAME` accessible in the `test` job, you need to:
1. Capture `ENV_NAME` as an output in `extract-environment-name`.
2. Reference that output in `test`.

However, currently, you’re trying to set `ENV_NAME` as an output with `outputs: environment: ${{ env.ENV_NAME }}`, but `env.ENV_NAME` won’t have the updated value because `outputs` in a job are evaluated before any commands run.

### Solution: Set `ENV_NAME` as an Output

1. **Update the `extract-environment-name` Job**: Store the `ENV_NAME` value in an output file and reference it in `outputs` so that it’s passed to the next job.

   ```yaml
   jobs:
     extract-environment-name:
       runs-on: ubuntu-latest
       name: "Extract Environment Name"
       steps:
         - name: Set environment variables
           id: set-env
           run: |
             if [[ ${GITHUB_REF} == "master" ]]
             then
               echo "ENV_NAME=prod" >> $GITHUB_ENV
               echo "::set-output name=environment::prod"
             else
               echo "ENV_NAME=dev" >> $GITHUB_ENV
               echo "::set-output name=environment::dev"
             fi
       outputs:
         environment: ${{ steps.set-env.outputs.environment }}

     test:
       runs-on: ubuntu-latest
       needs:
         - extract-environment-name
       environment:
         name: ${{ needs.extract-environment-name.outputs.environment }}
       env:
         ENV_NAME: ${{ needs.extract-environment-name.outputs.environment }}
         DBT_KEYFILE: /tmp/dbt-secret.json
         DBT_DATASET: movebox_data_dev
         IS_TEST: True
       steps:
         - name: Print environment name
           run: echo "Environment Name: $ENV_NAME"
   ```

### Explanation

- **Setting Outputs**: The `Set environment variables` step includes `echo "::set-output name=environment::prod"` (or `dev`) to set an output variable `environment`.
- **Using the Output in `test` Job**: In the `test` job, `ENV_NAME` is now accessible via `env: ENV_NAME: ${{ needs.extract-environment-name.outputs.environment }}`, making it available to any `steps` within `test`.

This will allow you to reference `ENV_NAME` as an environment variable within the `test` job, and you should see it printed as expected in the `Print environment name` step.

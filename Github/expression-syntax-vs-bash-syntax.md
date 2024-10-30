In GitHub Actions, conditional expressions within `if` statements don’t use `bash` syntax. Instead, GitHub Actions requires that you use its **expression syntax** directly in the `if` statement. This means you need to omit `[[ ... ]]` and simply write the condition directly.

Here’s how to write your conditional `if` statement correctly:

```yaml
- name: DBT run
  working-directory: ./dbt
  run: dbt run --target dev
  if: ${{ env.ENV_NAME == 'dev' }}
```

### Explanation

- **`${{ env.ENV_NAME == 'dev' }}`**: This is the correct GitHub Actions syntax for evaluating conditions. It checks if the environment variable `ENV_NAME` is equal to `dev`.
- **No `[[ ... ]]`**: GitHub Actions automatically interprets expressions in `${{ ... }}`, so you don’t need `[[ ... ]]` as you would in `bash`.
  
In this setup, the step will execute `dbt run --target dev` only if `ENV_NAME` equals `'dev'`.

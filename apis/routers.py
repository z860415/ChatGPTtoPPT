from apis import gpt_to_ptt


def init_apis(app):
    app.include_router(gpt_to_ptt.router, prefix="/get_ppt", tags=['get_ppt'])
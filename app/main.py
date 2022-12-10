from service import read_logss

from dto.request import GetAvregeBodyRequest

from fastapi import FastAPI , Query

app = FastAPI()

@app.get("/{type}/average")
def read_logs(type: str , froma: str = Query(default=None ,  max_length=16), to: str = Query(default=None ,  max_length=16)):
    return read_logss(type, froma, to)


@app.post("/average")
def read_item(item: GetAvregeBodyRequest):
    return read_logss(item.type, item.froma, item.to)

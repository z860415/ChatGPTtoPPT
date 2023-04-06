from fastapi import APIRouter
from starlette.responses import FileResponse
from interface.chatGPT_to_ppt import ChatgptToPpt
from utility.chatgpt import generate_notes
from utility.requestToMindsow import markdownToPPT


router = APIRouter()
@router.post('/get_ppt_file')
def get_ppt_file(data: ChatgptToPpt):
    generate_notes(data.title)
    markdownToPPT()
    return FileResponse(f'{data.title}主題課程.pptx')

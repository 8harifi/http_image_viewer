from fastapi import (
    FastAPI,
    Query,
    Body,
    HTTPException
)
from pydantic import BaseModel
from typing import Optional
from pathlib import Path
from fastapi.responses import (
    HTMLResponse,
    Response
)
from PIL import Image
import io

app = FastAPI()

IMAGE_DIR = Path("./images").resolve()


class RequestItem(BaseModel):
    file_height: Optional[int] = None
    file_width: Optional[int] = None


@app.get("/", response_class=HTMLResponse)
def list_files(path: str = ""):
    dir_path = IMAGE_DIR / path
    dir_path = dir_path.resolve()

    if not str(dir_path).startswith(str(IMAGE_DIR)):
        raise HTTPException(status_code=404, detail="Invalid directory path")

    if not dir_path.exists() or not dir_path.is_dir():
        raise HTTPException(status_code=404, detail="Directory not found")

    items = []
    for item in dir_path.iterdir():
        if item.is_dir():
            items.append(f'<li><a href="/?path={path + "/" + item.name if path else item.name}">{item.name}/</a></li>')
        elif item.is_file():
            items.append(f'<li><a href="/{path + "/" + item.name if path else item.name}">{item.name}</a></li>')

    file_list_html = f"<h1>Listing of /{path}</h1><ul>{''.join(items)}</ul>"
    return HTMLResponse(content=file_list_html)


@app.api_route("/{file_path:path}", methods=["GET", "POST"])
def process_file(
        file_path: str,
        file_height: Optional[int] = Query(None),
        file_width: Optional[int] = Query(None),
        body: Optional[RequestItem] = Body(None)
):
    if body:
        file_height = file_height or body.file_height
        file_width = file_width or body.file_width

    image_path = (IMAGE_DIR / file_path).resolve()

    if not str(image_path).startswith(str(IMAGE_DIR)):
        raise HTTPException(status_code=404, detail="Invalid image path")

    if not image_path.is_file():
        raise HTTPException(status_code=404, detail="Image not found")

    try:
        with Image.open(image_path) as img:
            if file_height is None or file_width is None:
                file_width, file_height = img.size  # Get original size

            img_resized = img.resize((file_width, file_height))
            img_bytes = io.BytesIO()
            img_resized.save(img_bytes, format="PNG")
            img_bytes.seek(0)
            return Response(content=img_bytes.getvalue(), media_type="image/png")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing image: {str(e)}")

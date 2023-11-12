from fastapi import FastAPI, Body, HTTPException
from fastapi.responses import RedirectResponse

def facefusion_api(_: gr.Blocks, app: FastAPI):
    @app.post("/facefusion/image")
    async def facefusion_image(
        files: List[UploadFile] = File(...)
    ):
		source_image = None
		target_image = None
		for file in files:
			if file.filename == "source_image":
				source_image = file
			if file.filename == "target_image":
				target_image = file
		if source_image == None:
			raise HTTPException(status_code=404, detail="Source Image not found")
		if target_image == None:
			raise HTTPException(status_code=404, detail="Target Image not found")

        # vis = get_image_colorizer(root_folder=Path(paths_internal.models_path),render_factor=render_factor, artistic=artistic)
        # # 判断input_image是否是url
        # if input_image.startswith("http"):
        #     img = vis._get_image_from_url(input_image)
        # else:
        #     # 把base64转换成图片 PIL.Image
        #     img = Image.open(BytesIO(base64.b64decode(input_image)))
        # outImg = vis.get_transformed_image_from_image(img, render_factor=render_factor)
        # return {"image": api.encode_pil_to_base64(outImg).decode("utf-8")}

try:
    import modules.script_callbacks as script_callbacks

    script_callbacks.on_app_started(facefusion_api)
except:
    pass

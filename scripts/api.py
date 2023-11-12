from fastapi import FastAPI, Body, HTTPException
from fastapi.responses import RedirectResponse
from fastapi import File, UploadFile

from typing import List
import gradio as gr

import facefusion.globals
from facefusion.utilities import is_image
from facefusion.uis.components.output import predict 



def facefusion_api(_: gr.Blocks, app: FastAPI):
    @app.post('/facefusion/image')
    async def facefusion_image(
        source_image: str,
        target_image: str
    ):
        if is_image(source_image):
            facefusion.globals.source_path = source_image
        else:
            facefusion.globals.source_path = None
            raise HTTPException(status_code=404, detail="Source Image not found")
            
        if is_image(target_image):
            facefusion.globals.target_path = target_image
        else:
            facefusion.globals.target_path = None
            raise HTTPException(status_code=404, detail="Target Image not found")

        predict("/siam/output")
        
        if is_image(facefusion.globals.output_path):
            return FileResponse(facefusion.globals.output_path)
        else:
            raise HTTPException(status_code=500, detail="Couldn't process your request")


    
 #    @app.post('/facefusion/image')
 #    async def facefusion_image(
 #        source_image: UploadFile,
 #        target_image: UploadFile
 #    ):
 #        if source_image:
 #            facefusion.globals.source_path = source_image.filename
 #        else:
 #            facefusion.globals.source_path = None
 #            raise HTTPException(status_code=404, detail="Source Image not found")
            
 #        if target_image:
 #            facefusion.globals.target_path = target_image.filename
 #        else:
 #            facefusion.globals.target_path = None
 #            raise HTTPException(status_code=404, detail="Target Image not found")

 #        return start("\siam\output")
 # #        facefusion.globals.output_path = normalize_output_path(facefusion.globals.source_path, facefusion.globals.target_path, output_path)
	# # limit_resources()
	# # conditional_process()

 #        return {
 #            "response": "got source and target",
 #            "source": source_image.filename,
 #            "target": target_image.filename
 #               }
        
		
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

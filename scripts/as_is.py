import modules.images as images
import modules.scripts as scripts
import gradio as gr

class AsIsScript(scripts.Script):
  def title(self):
    return 'As Is'

  def show(self, is_img2img):
    return scripts.AlwaysVisible if is_img2img else False

  def ui(self, is_img2img):
    with gr.Accordion('As Is', open=False):
      with gr.Row():
        enable = gr.Checkbox(
          False,
          label="Enable"
        )
    return [enable]

  def postprocess_image(self, p, pp, enable):
      if not enable:
          return

      if len(p.init_images) == 0:
        raise ValueError('As Is: source image not specified')

      init_image = p.init_images[0]
      width, height = pp.image.size
      pp.image = images.resize_image(p.resize_mode, init_image, width, height)


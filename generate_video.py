from moviepy.editor import TextClip, CompositeVideoClip

def generate():
    txt = TextClip("فيديو جديد من الذكاء الاصطناعي!", fontsize=70, color='white', size=(1280, 720))
    txt = txt.set_duration(10).set_position('center')
    video = CompositeVideoClip([txt])
    video.write_videofile("video_content/output.mp4", fps=24)

if __name__ == "__main__":
    generate()
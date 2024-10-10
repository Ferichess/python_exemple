# ffmpeg
# import os
# import subprocess


# def convert_video_to_mp3(input_file, output_file):
#     # Convert video to mp3
#     # command = f"ffmpeg -i {input_file} -codec:a libmp3lame -qscale:a 0 {output_file}"
#     # subprocess.run(command, shell=True)

#     ffmpeg = [
#         "ffmpeg",
#         "-i",
#         input_file,
#         "-vn",
#         "-acodec",
#         "libmp3lame",
#         "-ab",
#         "192k",
#         "-ar",
#         "44100",
#         "-y",
#         output_file,
#     ]
#     try:
#         subprocess.run(ffmpeg, check=True)
#         print(f"Successfully converted {input_file} to {output_file}")
#     except subprocess.CalledProcessError as e:
#         print(f"Error converting {input_file} to {output_file}: {e}")


# # convert_video_to_mp3("exemple.mov", "music.mp3")

# for i, filename in enumerate(os.listdir(".")):
#     if filename.endswith(".mov"):
#         convert_video_to_mp3(filename, f"music{i}.mp3")


import os
import subprocess


def video_editor(
    input_file,
    # input2_file,
    # input3_file,
    # input4_file,
    # input5_file,
    # input6_file,
    output_file,
):
    # command = f"ffmpeg -i {input_file} -vf scale=-1:1000 -r 15 {output_file}"
    # command = f"ffmpeg -i {input_file} -ss 00:00:04 -t 00:00:01 -crf 5 {output_file}"
    # command = f"ffmpeg -i {input_file} -filter_complex scale=640:-1:flags=lanczos -crf 5 {output_file}"
    # command = (
    #     f"ffmpeg -r 1 -i {input_file} -vcodec libx264 -pix_fmt yuv420p {output_file}"
    # )
    # command = f"ffmpeg -ss 00:00:04 -i {input_file} -frames 1 -vf scale=iw*0.5:ih*0.5 -f image2 {output_file}"
    # command = (
    #     f"ffmpeg -ss 00:00:04 -to 00:00:10 -i {input_file} -codec copy {output_file}"
    # )
    # command = (
    #     f"ffmpeg -i {input_file} -c:a aac -b:a 128k -c:v libx264 -crf 23 {output_file}"
    # )
    # command = f"ffmpeg -i {input_file} -codec copy {output_file}"
    # command = f"ffmpeg -i {input_file} -c:v libvpx-vp9 -crf 30 -b:v 0 -c:a libopus -vbr on -threads 8 {output_file}"
    # command = f'ffmpeg -i "{input_file}" -i "{input2_file}" -i "{input3_file}" -filter_complex "[1] scale=1080:1920 [twibbon];[2] scale=300:100 [gif];[twibbon][gif] overlay=(main_w-overlay_w)/2:(main_h-overlay_h-50) [overlay_with_gif];[0] format=rgba, scale=540:960, pad=1080:1920:(1080-540)/2:(1920-960)/2, drawbox=x=0:y=0 [bg];[bg][overlay_with_gif] overlay=0:0, drawtext=fontfile=/path/to/font.ttf:text="text_my_chanel":fontcolor=white:fontsize=50:x=(w-text_w)/2:y=50" -c:v libx264 -c:a copy {output_file}"'
    # command = f"ffmpeg -i {input_file} -vf scale=1080:1920 -c:v libx264 -c:a copy {output_file}"
    command = f"ffmpeg -i {input_file}  -filter_complex [0:v]setpts=2.0*PTS[v];[0:a]atempo=0.5[a] -map [v] -map [a] {output_file}"

    subprocess.run(command, shell=True)


# video_editor("C:/feri/lern_node.js/python_exemple/CR.mp4", "pic.gif") # kenapa ini berhasil
# video_editor(os.path.join(os.getcwd(), "CR.mp4"), "pic.gif") # sedangkan ini tidak berfungsi
# video_editor(os.path.abspath("CR.mp4"), "pic.gif")
video_editor(
    # os.path.join("C:/feri/result_ffmpeg", "CR.mp4"),
    # os.path.join("C:/feri/result_ffmpeg", "movie.webm"),
    os.path.join("C:/feri/result_ffmpeg", "resize.mp4"),
    # os.path.join("C:/feri/result_ffmpeg", "overlay.png"),
    # os.path.join("C:/feri/result_ffmpeg", "click.gif"),
    os.path.join("C:/feri/result_ffmpeg", "grid3.mp4"),
)

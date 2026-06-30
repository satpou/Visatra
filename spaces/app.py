import gradio as gr
import cv2
import numpy as np
from pathlib import Path
from detector import process_frame, process_image, process_video
from gesture import process_with_gesture

def process_webcam(image, mode, blur_enabled):
    if image is None:
        return None, "No image captured"
    
    frame = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    info = ""
    
    if mode in ["both", "hand"]:
        frame, gesture_text = process_with_gesture(frame, blur_enabled)
        info += f"Gesture: {gesture_text}\n"
    else:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    if mode in ["both", "yolo"]:
        frame, count = process_frame(frame)
        info += f"Objects detected: {count}"
    
    return frame, info

def process_image_upload(image, mode, blur_enabled):
    if image is None:
        return None, "No image provided"
    
    frame = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    info = ""
    
    if mode in ["both", "hand"]:
        frame, gesture_text = process_with_gesture(frame, blur_enabled)
        info += f"Gesture: {gesture_text}\n"
    else:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    if mode in ["both", "yolo"]:
        frame, count = process_frame(frame)
        info += f"Objects detected: {count}"
    
    return frame, info

def process_video_upload(video_path, mode, blur_enabled):
    if video_path is None:
        return None, "No video provided"
    
    try:
        output_path = Path("/tmp") / "output_video.mp4"
        frame_count, total_objs = process_video(video_path, str(output_path))
        info = f"Processed {frame_count} frames\nTotal objects: {total_objs}"
        return str(output_path), info
    except Exception as e:
        return None, f"Error: {str(e)}"

with gr.Blocks(title="Visatra — Vision + Satria", theme=gr.themes.Soft(primary_hue="blue")) as demo:
    gr.Markdown("# 🎯 Visatra — Real-Time Detection")
    gr.Markdown("Vision + Satria: YOLOv8 + MediaPipe Hand Detection")
    
    with gr.Row():
        mode = gr.Radio(
            choices=["Both (YOLO + Gesture)", "YOLO Only", "Hand Gesture Only"],
            value="Both (YOLO + Gesture)",
            label="Detection Mode"
        )
        blur_enabled = gr.Checkbox(label="Enable Blur on Peace Gesture", value=False)
    
    with gr.Tabs():
        with gr.TabItem("📷 Webcam"):
            with gr.Row():
                webcam_input = gr.Image(sources=["webcam"], label="Webcam Input", type="numpy")
                webcam_output = gr.Image(label="Result")
            webcam_info = gr.Textbox(label="Info", interactive=False)
            webcam_btn = gr.Button("📸 Capture & Process")
            
            def process_webcam_click(image):
                mode_map = {
                    "Both (YOLO + Gesture)": "both",
                    "YOLO Only": "yolo",
                    "Hand Gesture Only": "hand"
                }
                result, info = process_webcam(image, mode_map[mode.value], blur_enabled.value)
                return result, info
            
            webcam_btn.click(process_webcam_click, inputs=[webcam_input], outputs=[webcam_output, webcam_info])
        
        with gr.TabItem("🖼️ Image"):
            with gr.Row():
                image_input = gr.Image(label="Upload Image", type="numpy")
                image_output = gr.Image(label="Result")
            image_info = gr.Textbox(label="Info", interactive=False)
            image_btn = gr.Button("🔍 Process Image")
            
            def process_image_click(image):
                mode_map = {
                    "Both (YOLO + Gesture)": "both",
                    "YOLO Only": "yolo",
                    "Hand Gesture Only": "hand"
                }
                result, info = process_image_upload(image, mode_map[mode.value], blur_enabled.value)
                return result, info
            
            image_btn.click(process_image_click, inputs=[image_input], outputs=[image_output, image_info])
        
        with gr.TabItem("🎥 Video"):
            with gr.Row():
                video_input = gr.Video(label="Upload Video")
                video_output = gr.Video(label="Result")
            video_info = gr.Textbox(label="Info", interactive=False)
            video_btn = gr.Button("▶️ Process Video")
            
            def process_video_click(video):
                mode_map = {
                    "Both (YOLO + Gesture)": "both",
                    "YOLO Only": "yolo",
                    "Hand Gesture Only": "hand"
                }
                result, info = process_video_upload(video, mode_map[mode.value], blur_enabled.value)
                return result, info
            
            video_btn.click(process_video_click, inputs=[video_input], outputs=[video_output, video_info])
    
    gr.Markdown("---")
    gr.Markdown("**Visatra** — Vision + Satria | Powered by YOLOv8 & MediaPipe | [GitHub](https://github.com/satpou/Visatra)")

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860, share=True)

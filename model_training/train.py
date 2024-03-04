from ultralytics import YOLO
import comet_ml

comet_ml.init(project_name="chess-ai")
if __name__ == "__main__":
    model = YOLO('yolov8n-cls.pt')
    results = model.train(data="dataset2", epochs=300, imgsz=640, project="chessboardai", save_period=1, batch=8, save_json=True)
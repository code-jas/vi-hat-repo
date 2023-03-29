import argparse


class Detect:
    def __init__(self):
        self.args = self.parse_arguments()

    @staticmethod
    def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument('--weights', nargs='+', type=str,
                            default='weights/v5lite-s.pt', help='model.pt path(s)')
        # Add other arguments here
        parser.add_argument('--read', action='store_true')
        return parser.parse_args()


if __name__ == "__main__":
    detect = Detect()
    print(detect.args)

    # @staticmethod
    # def parse_opt(self):
    #     parser = argparse.ArgumentParser()
    #     parser.add_argument('--weights', nargs='+', type=str, default='weights/v5lite-s.pt', help='model.pt path(s)')
    #     parser.add_argument('--source', type=str, default='sample', help='source')  # file/folder, 0 for webcam
    #     parser.add_argument('--img-size', type=int, default=640, help='inference size (pixels)')
    #     parser.add_argument('--conf-thres', type=float, default=0.45, help='object confidence threshold')
    #     parser.add_argument('--iou-thres', type=float, default=0.5, help='IOU threshold for NMS')
    #     parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
    #     parser.add_argument('--view-img', action='store_true', help='display results')
    #     parser.add_argument('--save-txt', action='store_true', help='save results to *.txt')
    #     parser.add_argument('--save-conf', action='store_true', help='save confidences in --save-txt labels')
    #     parser.add_argument('--nosave', action='store_true', help='do not save images/videos')
    #     parser.add_argument('--classes', nargs='+', type=int, help='filter by class: --class 0, or --class 0 2 3')
    #     parser.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
    #     parser.add_argument('--augment', action='store_true', help='augmented inference')
    #     parser.add_argument('--update', action='store_true', help='update all models')
    #     parser.add_argument('--project', default='runs/detect', help='save results to project/name')
    #     parser.add_argument('--name', default='exp', help='save results to project/name')
    #     parser.add_argument('--exist-ok', action='store_true', help='existing project/name ok, do not increment')
    #     parser.add_argument('--read', action='store_true')
    #     self.opt = parser.parse_args()
    #     print(self.opt)
    #     check_requirements(exclude=('pycocotools', 'thop'))

    #     with torch.no_grad():
    #         if self.opt.update:  # update all models (to fix SourceChangeWarning)
    #             for self.opt.weights in ['yolov5s.pt', 'yolov5m.pt', 'yolov5l.pt', 'yolov5x.pt']:
    #                 self.detect()
    #                 strip_optimizer(self.opt.weights)
    #         else:
    #             self.detect()

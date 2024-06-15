import os
import cv2
from robot.api import logger

class ImageScaler:

    @staticmethod
    def _calculate_number_of_images(min_scale_x, max_scale_x, min_scale_y, max_scale_y, step):
        count = 0
        scale_x = min_scale_x
        while scale_x <= max_scale_x:
            scale_y = min_scale_y
            while scale_y <= max_scale_y:
                if scale_x != scale_y:
                    count += 1
                scale_y += step
            scale_x += step
        print (f'numberof combination is : {count}')
        #return count

    @staticmethod
    def __scale_image_two_factors(path, scale_x: float, scale_y: float):
        """
        Two factors scaling 
        """
        image = cv2.imread(path)
        if image is None:
            raise FileNotFoundError(f"The image at path {path} could not be found.")
        
        scaled_image = cv2.resize(image, None, fx=scale_x, fy=scale_y, interpolation=cv2.INTER_LINEAR)
        
        base_name = os.path.basename(path)
        name, ext = os.path.splitext(base_name)
        output_path = f"scaled_{scale_x:.2f}_{scale_y:.2f}_{name}{ext}"
        cv2.imwrite(output_path, scaled_image)
        logger.info(f"Image saved at {output_path}")


#currenlty not used 
    @staticmethod
    def __scale_image_single_factor(path, scale: float):
        """
        scale image l'image d'une façon consistente 
        """
        image = cv2.imread(path)
        if image is None:
            raise FileNotFoundError(f"The image at path {path} could not be found.")

        scaled_image = cv2.resize(image, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)
        
        base_name = os.path.basename(path)
        name, ext = os.path.splitext(base_name)
        output_path = f"scaled_{scale:.2f}_{name}{ext}"
        cv2.imwrite(output_path, scaled_image)
        logger.info(f"Image saved at {output_path}")


#currently not used - 
    @staticmethod
    def __scale_image_range(path, min_scale: float, max_scale: float, step: float):
        current_scale = min_scale
        while current_scale <= max_scale:
            try:
                ImageScaler.__scale_image_single_factor(path, current_scale)
            except Exception as e:
                logger.error(f"Failed to scale image at scale {current_scale}: {str(e)}")
            current_scale += step

    @staticmethod
    def prepare_data_by_scaling(path, min_scale_x: float, max_scale_x: float, min_scale_y: float, max_scale_y: float, step: float):
        """
        make all possibility of scaling an image
        """
        scale_x = min_scale_x
        while scale_x <= max_scale_x:
            scale_y = min_scale_y
            while scale_y <= max_scale_y:
                try:
                    ImageScaler.__scale_image_two_factors(path, scale_x, scale_y)
                except Exception as e:
                    logger.error(f"Failed to scale image at scale_x {scale_x} and scale_y {scale_y}: {str(e)}")
                scale_y += step
            scale_x += step


curdir = os.getcwd()

path_to_image = f'{curdir}/communauto.png'
min_scale_x = 0.7
max_scale_x = 1.3
min_scale_y = 0.7
max_scale_y = 1.2
step_size = 0.1

ImageScaler._calculate_number_of_images(min_scale_x, max_scale_x, min_scale_y, max_scale_y, step_size)

ImageScaler.prepare_data_by_scaling(path_to_image, min_scale_x, max_scale_x, min_scale_y, max_scale_y, step_size)

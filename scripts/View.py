from PIL import Image, ImageFont
import numpy as np


path_font = "/usr/share/fonts/liberation/LiberationMono-Regular.ttf"
font = ImageFont.truetype(path_font, 24)


def string_for_action(action):
    if action == 0:
        return "START"
    if action == 1:
        return 'up-left'
    elif action == 2:
        return 'up-right'
    elif action == 3:
        return 'down-left'
    elif action == 4:
        return 'down-right'
    elif action == 5:
        return 'center'
    elif action == 6:
        return 'TRIGGER'


def draw_sequences(i, k, step, action, draw, region_image, background, path_testing_folder, iou, reward,
                   gt_mask, region_mask, image_name, save_boolean):
    mask = Image.fromarray(255 * gt_mask)
    mask_img = Image.fromarray(255 * region_mask)
    image_offset = (1000 * step, 70)
    text_offset = (1000 * step, 550)
    masked_image_offset = (1000 * step, 1400)
    mask_offset = (1000 * step, 700)
    action_string = string_for_action(action)

    iou = round(iou, 3)
    footnote = 'action: ' + action_string + ' ' + 'reward: ' + str(reward) + ' Iou:' + str(iou)
    draw.text(text_offset, str(footnote), (0, 0, 0), font=font)

    img_for_paste = Image.fromarray(region_image)
    background.paste(img_for_paste, image_offset)
    background.paste(mask, mask_offset)
    background.paste(mask_img, masked_image_offset)
    file_name = path_testing_folder + '/' + image_name + str(i) + '_object_' + str(k) + '.png'

    if save_boolean == 1:
        background.save(file_name)
    return background

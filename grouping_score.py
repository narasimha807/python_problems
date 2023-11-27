#grouping_Score
def get_color_score_pairs_dict(ball_score_list):
    color_score_pairs_dict = {}
    for item in ball_score_list:
        pair = item.split(":")
        key, value = pair[0], int(pair[1])
        if key in color_score_pairs_dict:
            score = color_score_pairs_dict[key]
            color_score_pairs_dict[key] = score + value

        else:
            color_score_pairs_dict[key] = value

    return color_score_pairs_dict
ball_score_list = input().split(",")
color_score_pairs_dict = get_color_score_pairs_dict(ball_score_list)
color_score_pairs_dict_items = color_score_pairs_dict.items()
color_score_pairs_dict_items = sorted(color_score_pairs_dict_items)
print(color_score_pairs_dict_items)


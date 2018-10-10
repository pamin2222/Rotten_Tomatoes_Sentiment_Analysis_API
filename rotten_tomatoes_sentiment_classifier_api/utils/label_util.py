from constant.classifier_attribute_enum import SentimentAttributeEnum


def clf_pred_num_to_cls_name(clf_pred_num):
    if clf_pred_num == 0:
        return SentimentAttributeEnum.NEGATIVE.value
    elif clf_pred_num == 1:
        return SentimentAttributeEnum.SOMEWHAT_NEGATIVE.value
    elif clf_pred_num == 2:
        return SentimentAttributeEnum.NEUTRAL.value
    elif clf_pred_num == 3:
        return SentimentAttributeEnum.SOMEWHAT_POSITIVE.value
    elif clf_pred_num == 4:
        return SentimentAttributeEnum.POSITIVE.value
    else:
        return SentimentAttributeEnum.NEUTRAL.value

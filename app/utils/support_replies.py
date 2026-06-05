SUPPORT_REPLIES = {

    "Recharge Related Issues":
    """
    Thank you for contacting us.
    Please provide your transaction ID
    and recharge details so we can
    investigate the issue.
    """,

    "Did not receive cashback/discount":
    """
    Thank you for contacting us.
    Please share your order details.
    Cashback processing may take
    up to 7 working days.
    """,

    "User ID Report/Block Issues":
    """
    Thank you for contacting us.

    We regret the inconvenience.

    Please provide additional details about the issue you are facing. Our support team will review your account and investigate.

    Important:
    Accounts blocked due to guideline
    violations remain restricted until
    review is completed.
    """
}

def generate_chat_reply(
    message
):

    text = message.lower()

    if "block" in text:
        return (
            "Please provide additional details about the issue you are facing. Our support team will review your account and investigate."
        )

    if "recharge" in text:
        return (
            "Please share your recharge "
            "transaction ID."
        )

    if "cashback" in text:
        return (
            "Cashback verification usually "
            "takes up to 7 working days."
        )

    return (
        "Thank you. Our support team "
        "is reviewing your issue."
    )
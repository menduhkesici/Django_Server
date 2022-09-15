import matplotlib.pyplot as plt

WORDS_PER_LINE = 4


def message_box(message, time, message_x=None, img=None):
    if img is None:
        plt.gca().text(0.5, 0.5, divide_message(message), fontsize=20, transform=plt.gca().transAxes,
                       horizontalalignment='center', verticalalignment='center')
    else:
        plt.imshow(img, interpolation='nearest')
        plt.title(message, fontsize=20)
        if message_x is not None:
            plt.xlabel(message_x, fontsize=16)

    plt.xticks([])
    plt.yticks([])
    plt.gcf().canvas.set_window_title('System Message')

    if time == 0:
        plt.show()
    else:
        plt.show(block=False)
        plt.pause(time)
        plt.close()


def divide_message(message):
    split = message.split()
    message = ''
    for i in range(len(split) // WORDS_PER_LINE + 1):
        message += ' '.join(split[i*WORDS_PER_LINE:min((i+1)*WORDS_PER_LINE, len(split))]) + '\n'
    return message[:-1]


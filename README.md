# 代码使用说明

这段代码主要功能是使用 PaddleOCR 进行图片文字识别，并根据识别结果生成 Anki 卡片。以下是代码的使用说明：

1. **命令行参数**：
    - `-n` 或 `--filename`：指定要处理的图片文件名，默认值为 `3.jpg`。
    - `-l` 或 `--language`：指定文本的语言，默认值为 `zh`（中文）。
    - `-c` 或 `--count`：指定用于计算比例的数字，默认值为 `1`。

2. **使用步骤**：
    - 在命令行中导航到代码所在的目录。
    - 运行以下命令来执行代码，并根据需要指定参数：
      ```bash
      python script.py -n new_image.jpg -l en -c 2
      ```
      这将处理名为 `new_image.jpg` 的图片，使用英文语言，并将中文列表数量除以 `2` 来计算比例。

3. **输出**：
    - 代码将打印识别出的中英文文本。
    - 如果指定了 `-l` 参数为 `zh`，将打印中文文本；如果指定为 `en`，将打印英文文本；如果未指定 `-l` 参数，将同时打印中英文文本。
    - 如果指定了 `-c` 参数，代码将打印识别比例，格式为 `识别比例: 数量/指定数字, 百分比`。

4. **其他**：
    - 代码还会生成一个 Anki 卡片包（.apkg 文件），文件名与输入的图片文件名相同。
    - 可以通过修改代码中的 `my_model` 和 `my_deck` 来定制 Anki 卡片的模板和牌组信息。

请注意，代码中的 `ocr = PaddleOCR(use_angle_cls=True)` 需要提前安装 PaddleOCR 库，并且可能需要下载模型文件。此外，代码中的图片处理部分可能需要根据实际情况进行调整。

# 其他

## 代码由 cursor 和 MarsCodeAI 共同生成。安装环境到简单功能生成，大约 2 小时左右。特别是 README 生成，几乎秒成。


## 安装过程中MacOS @M1 silicon 遇到CPU卡死情况的解决办法：
 1. https://github.com/PaddlePaddle/PaddleOCR/issues/9761
 2. https://github.com/PaddlePaddle/PaddleOCR/discussions/13060?converting=1#discussioncomment-9762733
 3. https://github.com/PaddlePaddle/PaddleOCR/issues/9761

## 参考链接
 1. [paddlepaddle 官网](https://paddlepaddle.github.io/PaddleOCR/latest/quick_start.html#_2)
 2. [Web 实例](https://aistudio.baidu.com/community/app/91660/webUI)
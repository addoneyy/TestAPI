


def record_result(passed, failed, skipped, file="./results/results.txt"):
    """
        记录测试结果
    """
    with open(file=file, mode="w", encoding="utf-8") as f:
        f.write(f"{len(passed+failed+skipped)}:{len(passed)}:{len(failed)}:{len(skipped)}")
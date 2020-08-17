import psutil
"""Scale large byte sizes"""

def get_size(bytes, suffix="B"):
    factor=1024
    for unit in ["","K","M","G","T","P"]:
        if bytes < factor:
            return f"{bytes:.2f} {unit}{suffix}"
        bytes /= factor

def memory():
    print("="*5,"Memory Information","="*5)
    svmem= psutil.virtual_memory()
    print(f"Total: {get_size(svmem.total)}")
    print(f"Available: {get_size(svmem.available)}")
    print(f"Used: {get_size(svmem.used)}")
    print(f"Percentage: {svmem.percent} %")
    """Swap"""
    print("="*5,"Swap Memory Information","="*5)
    swap= psutil.swap_memory()
    print(f"Total: {get_size(swap.total)}")
    print(f"Free: {get_size(swap.free)}")
    print(f"Used: {get_size(swap.used)}")
    print(f"Percentage: {swap.percent} %")
    print("="*30)

if __name__ == "__main__":
    memory()
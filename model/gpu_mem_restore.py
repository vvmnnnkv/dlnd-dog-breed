import functools
import traceback
import gc
import sys

def get_ref_free_exc_info():
    "Free traceback from references to locals/globals to avoid circular reference leading to gc.collect() unable to reclaim memory"
    type, val, tb = sys.exc_info()
    traceback.clear_frames(tb)
    return (type, val, tb)

def gpu_mem_restore(func):
    "Reclaim GPU RAM if CUDA out of memory happened, or execution was interrupted"
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        oom_exc = False
        try:
            return func(*args, **kwargs)
        except RuntimeError as e:
            if "CUDA out of memory" in str(e):
                oom_exc = True
                type, val, tb = get_ref_free_exc_info() # must!
                raise type(val).with_traceback(tb) from None
            else: raise # re-raises the exact last exception
        except: raise # any other types of errors
        finally:
            if oom_exc:
                # reclaim memory
                gc.collect()
                if torch.cuda.is_available(): torch.cuda.empty_cache()
    return wrapper


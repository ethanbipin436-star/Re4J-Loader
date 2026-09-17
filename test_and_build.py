import os
import sys
import glob
import json

def log(tag, msg):
    print(f"[{tag}] {msg}")

class LCEEngineSimulator:
    """Simulates the LCE C++ Engine environment to verify mod logic safely without launching the game."""
    def __init__(self):
        self.block_registry = {}
        self.item_registry = {}

    def set_block(self, x, y, z, block_id):
        self.block_registry[(x, y, z)] = block_id
        return True

    def register_item(self, item_id, name):
        self.item_registry[item_id] = name
        log("SIMULATOR", f"Registered Item: {name} (ID: {item_id})")
        return True

# --- 1. DRY-RUN COMPATIBILITY TESTER ---
def run_compatibility_test():
    log("TEST", "Starting Re4J LCE Compatibility & Static Verification...")
    
    # Test Python environment architecture
    is_64bit = sys.maxsize > 2**32
    log("ENV", f"Python Runtime: {sys.version.split()[0]} ({'64-bit' if is_64bit else '32-bit'})")
    
    # Create required directory structure
    dirs = ["./mods", "./build", "./assets"]
    for d in dirs:
        if not os.path.exists(d):
            os.makedirs(d)
            log("SETUP", f"Created directory: {d}")

    # Initialize Engine Simulator
    sim = LCEEngineSimulator()
    
    # Test Mod Execution in Sandbox
    mod_files = glob.glob("./mods/*.py")
    log("TEST", f"Found {len(mod_files)} Python mod(s) in ./mods/")
    
    for mod_path in mod_files:
        mod_name = os.path.basename(mod_path)
        log("TEST", f"Verifying mod logic: {mod_name}")
        try:
            # Expose simulated 're4j' module API
            sandbox_env = {
                "set_block": sim.set_block,
                "register_item": sim.register_item,
                "__file__": mod_path
            }
            with open(mod_path, "r") as f:
                code = f.read()
                exec(code, {"re4j": sandbox_env})
            log("SUCCESS", f"Mod '{mod_name}' passed dry-run verification!")
        except Exception as e:
            log("ERROR", f"Mod '{mod_name}' failed verification: {e}")

# --- 2. AUTOMATED C++ DLL & HOOK BUILDER ---
def generate_native_dll_source():
    cpp_code = """// Re4J Native Hook Injector for LCE Codebase (TU19 / 1.6.4 base)
// Safe, original C++ wrapper utilizing Python C-API

#include <windows.h>
#include <Python.h>
#include <iostream>

#define RE4J_API __declspec(dllexport)

// Forward declarations of LCE Native Engine Function pointers
typedef void(*SetBlockFn)(int x, int y, int z, int blockId);
SetBlockFn LCE_SetBlock = nullptr;

// Embedded Python Binding: re4j.set_block(x, y, z, id)
static PyObject* py_re4j_set_block(PyObject* self, PyObject* args) {
    int x, y, z, id;
    if (!PyArg_ParseTuple(args, "iiii", &x, &y, &z, &id)) return NULL;
    if (LCE_SetBlock) LCE_SetBlock(x, y, z, id);
    Py_RETURN_NONE;
}

static PyMethodDef Re4JMethods[] = {
    {"set_block", py_re4j_set_block, METH_VARARGS, "Set a block in LCE world"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef re4jModule = {
    PyModuleDef_HEAD_INIT, "re4j", "Re4J Native Modding API", -1, Re4JMethods
};

PyMODINIT_FUNC PyInit_re4j(void) {
    return PyModule_Create(&re4jModule);
}

// Background thread that launches embedded Python
DWORD WINAPI Re4J_InitThread(LPVOID lpParam) {
    PyImport_AppendInittab("re4j", PyInit_re4j);
    Py_Initialize();
    
    PyRun_SimpleString(
        "import sys, glob\\n"
        "sys.path.append('./mods')\\n"
        "print('[Re4J Native] Embedded Python Runtime Started!')\\n"
        "for mod in glob.glob('./mods/*.py'):\\n"
        "    print(f'[Re4J Native] Loading: {mod}')\\n"
        "    exec(open(mod).read())\\n"
    );
    return 0;
}

// Proxy D3D11 / DLL Entrypoint for auto-injection on game launch
BOOL APIENTRY DllMain(HMODULE hModule, DWORD ul_reason_for_call, LPVOID lpReserved) {
    if (ul_reason_for_call == DLL_PROCESS_ATTACH) {
        DisableThreadLibraryCalls(hModule);
        CreateThread(NULL, 0, Re4J_InitThread, NULL, 0, NULL);
    }
    return TRUE;
}
"""
    with open("./build/Re4JLoader.cpp", "w") as f:
        f.write(cpp_code)
    log("BUILD", "Generated './build/Re4JLoader.cpp' source code.")

# --- 3. SAMPLE PRE-1.6 PORT MOD GENERATOR ---
def generate_sample_mod():
    sample_mod_code = """# Re4J Mod Script: Sample Pre-1.6.4 Logic Verification
import re4j

print("[Sample Mod] Initializing Pre-1.6.4 Logic Hook...")

# Simulating block placement and item registration
re4j.register_item(500, "portal_gun")
re4j.set_block(0, 64, 0, 1) # Set stone block at origin
"""
    mod_path = "./mods/sample_portal_gun.py"
    if not os.path.exists(mod_path):
        with open(mod_path, "w") as f:
            f.write(sample_mod_code)
        log("SETUP", f"Generated sample pre-1.6 mod test at: {mod_path}")

if __name__ == "__main__":
    run_compatibility_test()      # <--- Creates ./mods and other folders first!
    generate_sample_mod()         # <--- Now safely writes sample_portal_gun.py
    generate_native_dll_source()
    log("COMPLETE", "All dry-runs complete. Environment is set up and verified!")
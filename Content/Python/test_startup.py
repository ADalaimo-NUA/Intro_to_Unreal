import unreal

def main():
    try:
        unreal.log("Startup Python: Editor has launched successfully.")
    except Exception as e:
        unreal.log_error(f"Startup script failed: {e}")

if __name__ == "__main__":
    main()
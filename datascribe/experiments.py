def run_experiment_a(rag, target_dir):
    rag.ingest(target_dir)
    print(rag.explain("Explain this ETL pipeline","developer"))

def run_experiment_b(rag, target_dir):
    rag.ingest(target_dir)
    print(rag.explain("Explain complex algorithms","senior_ml"))

def run_experiment_c(rag, target_dir):
    rag.ingest(target_dir)
    print(rag.explain("Explain complete pipeline","business"))

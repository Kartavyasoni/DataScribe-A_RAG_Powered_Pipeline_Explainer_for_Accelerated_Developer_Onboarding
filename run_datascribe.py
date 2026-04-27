import argparse
from pathlib import Path
from datascribe.rag_engine import DataScribeRAG
from datascribe.experiments import run_experiment_a, run_experiment_b, run_experiment_c

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--target_dir", required=True)
    parser.add_argument("--persona", default="developer")
    parser.add_argument("--query", default="Explain the full data pipeline and system architecture.")
    parser.add_argument("--experiment", choices=["A","B","C"], default=None)
    args = parser.parse_args()

    rag = DataScribeRAG()
    target_dir = Path(args.target_dir)

    if args.experiment == "A":
        run_experiment_a(rag, target_dir)
    elif args.experiment == "B":
        run_experiment_b(rag, target_dir)
    elif args.experiment == "C":
        run_experiment_c(rag, target_dir)
    else:
        rag.ingest(target_dir)
        print(rag.explain(args.query, args.persona))

if __name__ == "__main__":
    main()

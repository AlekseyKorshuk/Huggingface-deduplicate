from dataclasses import dataclass, field
from typing import Optional

@dataclass
class PreprocessingArguments:
    """
    Configuration for preprocessing data.
    """

    num_workers: Optional[int] = field(
        default=None,
        metadata={
            "help": "The number of CPU cores to use for parallel preprocessing."
        },
    )
    
    dataset_name: Optional[str] = field(
        default="conceptofmind/pile_wikipedia_en", 
        metadata={"help": "Folder or name of dataset to process."}
    )

    dataset_subset: Optional[str] = field(
        default="", 
        metadata={"help": "Subset of dataset to process."}
    )
    
    output_dir: Optional[str] = field(
        default="pile_wikipedia_en_clean", 
        metadata={"help": "Folder to save processed processed dataset."}
    )
    
    samples_per_file: Optional[int] = field(
        default=100_000, 
        metadata={"help": "Number of files to save per JSON output file."}
    )
    
    text_column: Optional[str] = field(
        default="text", 
        metadata={"help": "Column containing text data to process."}
    )

    alpha_frac: Optional[float] = field(
        default=0.62, 
        metadata={"help": "Maximum fraction of non-alphanumeric characters, otherwise file is filtered."}
    )

    tokenizer_path: Optional[str] = field(
        default="/home/henry/token",
        metadata={"help": "Path to tokenizer directory."}
    )

    jaccard_threshold: Optional[float] = field(
        default=0.8, 
        metadata={"help": "Jaccard threshold for near-duplicate samples."}
    )
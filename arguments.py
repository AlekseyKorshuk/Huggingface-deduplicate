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
        default="conceptofmind/pile_enron_emails", 
        metadata={"help": "Folder or name of dataset to process."}
    )
    
    output_dir: Optional[str] = field(
        default="pile_enron_emails_clean", 
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
        default=0.4, 
        metadata={"help": "Maximum fraction of non-alphanumeric characters, otherwise file is filtered."}
    )

    tokenizer_path: Optional[str] = field(
        default="/home/henry/token",
        metadata={"help": "Path to tokenizer directory."}
    )
    
    # tokenizer: Optional[str] = field(
    #     default="lvwerra/codeparrot",
    #     metadata={"help": "Name or path to the tokenizer."},
    # )

    jaccard_threshold: Optional[float] = field(
        default=0.95, 
        metadata={"help": "Jaccard threshold for near-duplicate samples."}
    )
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
        default="conceptofmind/pile_dm_mathematics", 
        metadata={"help": "Folder or name of dataset to process."}
    )
    
    output_dir: Optional[str] = field(
        default="pile_dm_mathematics_clean", 
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
    
    line_max: Optional[float] = field(
        default=1000, 
        metadata={"help": "Maximum line length in file, otherwise file is filtered."}
    )

    line_mean: Optional[float] = field(
        default=100, 
        metadata={"help": "Maximum mean line length in file, otherwise file is filtered."}
    )

    alpha_frac: Optional[float] = field(
        default=0.25, 
        metadata={"help": "Maximum fraction of non-alphanumeric characters, otherwise file is filtered."}
    )

    min_token_ratio: Optional[float] = field(
        default=1.5, 
        metadata={"help": "Minimum character token ratio for the file, otherwise file is filtered."}
    )
    
    filter_proba: Optional[float] = field(
        default=0.7, 
        metadata={"help": "Probability for filtering config, test and uncommon files."}
    )
    
    # tokenizer: Optional[str] = field(
    #     default="lvwerra/codeparrot",
    #     metadata={"help": "Name or path to the tokenizer."},
    # )

    near_deduplication: Optional[bool] = field(
        default=True, 
        metadata={"help": "If True, near-duplicate samples are removed."}
    )

    jaccard_threshold: Optional[float] = field(
        default=0.85, 
        metadata={"help": "Jaccard threshold for near-duplicate samples."}
    )
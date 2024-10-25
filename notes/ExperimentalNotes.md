# Experimental Notes
What is the end goal of this study?
    0. The enzymes we're studying are expressed in different microbes in the soil. They're important because we can measure the amount of gas they produce from catalyzing chloride and bromide. 
    1. Generate enzymes that are specific to chloride and bromide
        * **Clustering approach:** take enzymes (MHTs) that already exist and explore representatives of different clusters to see if there's anything close to what we want.
        * **PLM approach:** use a foundation model to see if we can learn binding site characteristics and occupancy. Leverage this to engineer halide-specific enzymes.
            - Caveat: the dataset may be imbalanced, containing more chloride than bromide examples. Might be good to keep in mind for the future.
        * **Statistical analysis:** extract domain-specific statistical features (volume, hydropathy, etc.) to see if there are differences between proteins that bind to chloride and bromide.
    2. Improve performance of the enzyme
        * performance: catalytic efficiency
        * catalytic efficiency: speed/volume improvement in reaction
What should we produce for Ilenne?
    1. The clustering approach should yield sequences that are highly different from each other. Ilenne can use these sequences to produce experimental data for us.
    
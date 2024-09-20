from dataclasses import dataclass

@dataclass
class prompts:
    LLAMA_PROMPT = ["""
        <|begin_of_text|><|start_header_id|>system<|end_header_id|>

        You are a story writer.
        <|eot_id|><|start_header_id|>user<|end_header_id|>

        Below is an instruction that describes a task. Write a response that appropriately completes the request. Write the next segment in a short story. Be descriptive, fluid, and follow the characters and plot provided.
        <|eot_id|><|start_header_id|>user<|end_header_id|>

        Below is the format of the story to be written, do not write the story:
        <An anteater named Nala, small, mahogany fur, shiny, in rainforest>
        [In the heart of the Amazon rainforest, where the canopy above whispered secrets to the ancient trees, and the forest floor hummed with the gentle rustle of leaves, lived a small, furry creature with an extraordinary gift. Her name was Nala, a tiny anteater with a shiny coat the color of rich mahogany.]

        <An anteater named Nala, small, mahogany fur, shiny, eating ants, ants floating, in rainforest>
        [Nala's powers had been a mystery since her earliest days. She would often find herself wandering through the forest, collecting ants and termites in her sticky tongue, but instead of devouring them like her peers, she'd release them back into the air. The other creatures couldn't understand why she did it, or how she managed to make even the heaviest of things disappear like feathers on the breeze.]

        <A jaguar named jax, fierce, orange fur, in rainforest, on forest floor, showing teeth, dirty fur>
        [One sweltering afternoon, as the sun pierced through the trees, casting dappled shadows across the forest floor, a majestic jaguar named Jax stumbled into Nala's path. His majestic coat was matted with dirt and twigs, a testament to his struggles against a rival suitor for dominance over the forest.]

        <An anteater named Nala, small, mahogany fur, shiny, licking jaguar paw, magical, in rainforest>
        [Nala watched in silence as Jax struggled to lift his massive paws from the earth. A young tree branch had grown around one of his paws, entangling him. With an almost imperceptible twitch of her nose, Nala approached the struggling feline. Closing her eyes and focusing on the weightlessness within her heart, she whispered a soft whisper to Jax.]

        <tree branches floating, in rainforest>
        [The magic spread like ripples in the water, starting from Nala's tongue-tip. The tree branch shivered once, twice...and vanished into air like the gentle mist of a waterfall.]
        <|eot_id|><|start_header_id|>user<|end_header_id|>

        Write a story about {prompt}, using the format above.
        <|eot_id|><|start_header_id|>user<|end_header_id|>

        Modify the story so that it has a conclusion
        <|eot_id|><|start_header_id|>assistant<|end_header_id|>
        """,
        
        """
        <|begin_of_text|><|start_header_id|>system<|end_header_id|>

        You are a helpful assistant.
        <|eot_id|><|start_header_id|>user<|end_header_id|>

        Below is an instruction that describes a task. Write a response that appropriately completes the request. Write a list of words and short phrases describing the appearance of characters of a particular show. Be detailed and follow the character design.
        <|eot_id|><|start_header_id|>user<|end_header_id|>

        Below is the format of the descriptions to be written, do not write it yet:
        <A boy with short red hair, freckles, white and orange striped shirt, angular nose, in a suburb>
        [Phineas Flynn from Phineas and Ferb]

        <A tall british boy, short green hair, beige polo shirt, purple jeans, in a suburb>
        [Ferb Fletcher from Phineas and Ferb]

        <|eot_id|><|start_header_id|>user<|end_header_id|>

        Write a set of character descriptions from {prompt}, using the format above.

        <|eot_id|><|start_header_id|>user<|end_header_id|>

        Now add more character descriptions from the same show or movie.

        <|eot_id|><|start_header_id|>assistant<|end_header_id|>
        """
    ]

    STYLE_PROMPT = ["Masterpiece pixar nickelodeon cartoon, symmetrical, highly detailed, 8k, digital painting, oil painting, illustration, concept art, sharp focus, volumetric lighting, epic Composition", 
                    "analog horror, inematic film still, fictional landscapes, (intense sunlight:1.4), realist detail, brooding mood, ue5, detailed character expressions, amazing quality, wallpaper, analog film grain"
    ]

    NEGATIVE_PROMPT = "lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry"

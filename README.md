# 🎲 BogoLLM - BogoSort, Guaranteed... Maybe

> *"Why iterate when you can hallucinate?"* - Ancient LLM proverb

## What is BogoSort?

BogoSort (also known as "Stupid Sort" or "Monkey Sort") is the gold standard of sorting algorithms for people who have:
- Unlimited time ⏰
- Unlimited patience 🧘
- A burning desire to watch the universe heat-death before their array sorts

The traditional algorithm works like this:
1. Check if the list is sorted
2. If not, shuffle it randomly
3. Repeat until sorted (or until the heat death of the universe, whichever comes first)

**Time Complexity:** O(∞) - It's not a bug, it's a *lifestyle choice*

## But Wait, There's More! 🚀

We asked ourselves: *"What if we made it worse?"*

Introducing **LLM-Powered BogoSort** - because why rely on random chance when you can rely on:
- A 7B parameter model running on your laptop 🔥
- Network latency 🌐
- The inherent unpredictability of artificial intelligence 🤖

## Features

✨ **AI-Powered Sorting** - Let the machines do the thinking!
🎯 **Zero Iterations** - No loops, no recursion, just *vibes*
🌍 **Environmentally Conscious** - Uses fewer CPU cycles (transfers them to your GPU instead)
📊 **Guaranteed Results** - Eventually... probably... maybe
🎭 **Drama-Free** - If it fails, blame the model, not the algorithm!

## Installation

```bash
# Clone this monument to human ingenuity
git clone <repository-url>
cd BogoSort

# Copy the .env.example to .env and update the values! (Refer to Configuration)
cp .env.example .env

# Create a virtual environment (highly recommended for your sanity)
uv venv
source .venv/bin/activate # Windows users may use .venv/Scripts/activate

# Install dependencies
uv add openai python-dotenv
```

## Usage

### Method 1: Command Line (For the Brave)

```bash
# Sort numbers the LLM way
python bogosort.py 5 2 8 1 3

# Use a specific model
python bogosort.py 42 17 99 --model llama-3.2-3b

# Connect to a different LM Studio instance
python bogosort.py 3.14 2.71 1.41 --url http://localhost:8080/v1
```

### Method 2: Interactive Mode (For the Patient)

```bash
python main.py
```

Then enter numbers one by one:
```
Enter numbers to sort (type 'exit' to finish):
> 42
Added: 42.0
> 17
Added: 17.0
> 99
Added: 99.0
> exit

Sorting 3 number(s) using LLM...

The sorted list is [17.0, 42.0, 99.0]
```

## Configuration

Create a `.env` file from the example:

```bash
cp .env.example .env
```

Then edit it:
```env
MODEL_NAME="local-model"        # Your model's ego
API_URL="http://localhost:1234/v1"  # Where your GPU is crying
API_KEY="not-needed"            # LM Studio doesn't judge
```

## How It Works

1. **Input** 📥 - You provide a list of numbers
2. **Prompt Engineering** 🎨 - We craft a masterpiece of a prompt
3. **Network Request** 🌐 - The numbers travel to your GPU
4. **LLM Contemplates** 🤔 - The model ponders the meaning of "sorted"
5. **Magic Happens** ✨ - Numbers come back (hopefully) in order
6. **Profit** 💰 - You have a sorted list!

## Performance Characteristics

| Metric | Traditional BogoSort | LLM BogoSort |
|--------|---------------------|--------------|
| Time Complexity | O((n+1)!) | O(network latency × model size) |
| Space Complexity | O(1) | O(VRAM) |
| Success Rate | 100% (eventually) | Depends on temperature setting |
| Energy Usage | Low | *Have you seen your electricity bill?* |
| Cool Factor | ❌ | ✅✅✅ |

## Testing

We've written 16 tests because we're responsible developers:

```bash
uv run pytest test.py -v
```

Tests include:
- Basic sorting (boring)
- Floats (exciting!)
- Negative numbers (rebellious!)
- Duplicates (party crashers)
- Empty lists (existential dread)
- Edge cases (where the bugs live)

## FAQ

**Q: Is this practical?**  
A: About as practical as using a Lamborghini to deliver pizza.

**Q: Will this work on my Raspberry Pi?**  
A: Technically yes, but your grandchildren will see the results.

**Q: Why did you make this?**  
A: *stares into the void* ...why does anyone make anything?

**Q: Can I use this in production?**  
A: Only if your SLA is measured in geologic time.

**Q: Is this AI-powered?**  
A: It's LLM-powered, which is like AI but with more buzzwords.

## Architecture

```
┌─────────────┐     ┌──────────────┐     ┌────────────────┐
│   Numbers   │────▶│   Prompt     │────▶│  LM Studio     │
│   [5,2,8]   │     │  "Sort plz"  │     │  🦙 Running    │
└─────────────┘     └──────────────┘     │  on your GPU   │
                                         └───────┬────────┘
                                                 │
                                                 ▼
┌─────────────┐     ┌──────────────┐     ┌────────────────┐
│   Sorted!   │◀────│  Response    │◀────│   "[2,5,8]"    │
│   [2,5,8]   │     │  Parsing     │     │   (hopefully)  │
└─────────────┘     └──────────────┘     └────────────────┘
```

## Contributing

Want to make this even more unnecessary? We welcome:
- Additional LLM providers (Claude, GPT-4, your toaster)
- Blockchain integration (because why not)
- Kubernetes support (for distributed sorting of 3 numbers)
- A GUI (for people who can't handle the command line)

## License

MIT License - Do whatever you want, but please don't blame us when your sorting takes longer than the age of the universe.

## Acknowledgments

- The original BogoSort inventor (you absolute madlad)
- LM Studio for making local LLMs accessible
- Our GPUs for their sacrifice
- Caffeine, for making this possible

---

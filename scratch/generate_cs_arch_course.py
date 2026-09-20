#!/usr/bin/env python3
"""
Generates the Computer Architecture & Operating Systems (cs_arch_101) academic topic
in both English (cs_arch_101_en.yaml) and Hebrew (cs_arch_101_he.yaml).
Follows first-principles pedagogical design, SVG diagrams, 100% 4-option multiple choice,
and comprehensive 'explanation' fields for Learn More context.
"""
import os
import yaml

TARGET_EN = "/Users/orishmuel/Library/CloudStorage/GoogleDrive-ori.shmuel@gmail.com/My Drive/Apps/Shmuel's Trivia App/academic_topics/cs_arch_101_en.yaml"
TARGET_HE = "/Users/orishmuel/Library/CloudStorage/GoogleDrive-ori.shmuel@gmail.com/My Drive/Apps/Shmuel's Trivia App/academic_topics/cs_arch_101_he.yaml"

def create_course_datasets():
    # -------------------------------------------------------------------------
    # ENGLISH COURSE DATASET
    # -------------------------------------------------------------------------
    cs_en = {
        "id": "cs_arch_101_en",
        "type": "academic",
        "icon": "💻",
        "title": "Computer Architecture & Operating Systems (CS Arch 101)",
        "description": "A comprehensive, first-principles guide for software engineers exploring how silicon transistors execute instructions, how caches beat the memory wall, and how operating system kernels manage memory, processes, and concurrency.",
        "lang": "en",
        "audience": "family",
        "categories": [
            # =================================================================
            # MODULE 1: CPU Architecture & The Instruction Pipeline
            # =================================================================
            {
                "id": "cpu_pipeline_execution",
                "title": "1. CPU Architecture & The Instruction Pipeline",
                "description": "From silicon clock pulses to machine code execution: understanding the 5-stage RISC pipeline, branch prediction, and how processors maximize Instructions Per Cycle (IPC).",
                "cards": [
                    {
                        "title": "The Von Neumann Architecture & The Instruction Cycle",
                        "figure": {
                            "title": "Classic 5-Stage CPU Instruction Pipeline",
                            "svg": """<svg viewBox="0 0 520 140" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-height:140px;">
  <rect x="10" y="40" width="90" height="55" rx="8" fill="#3b82f6" fill-opacity="0.15" stroke="#3b82f6" stroke-width="2"/>
  <text x="55" y="65" font-size="12" font-weight="bold" fill="#3b82f6" text-anchor="middle">IF</text>
  <text x="55" y="82" font-size="9" fill="currentColor" opacity="0.8" text-anchor="middle">Instruction Fetch</text>

  <path d="M 100 67 L 115 67" stroke="#3b82f6" stroke-width="2" marker-end="url(#arr)"/>

  <rect x="115" y="40" width="90" height="55" rx="8" fill="#6366f1" fill-opacity="0.15" stroke="#6366f1" stroke-width="2"/>
  <text x="160" y="65" font-size="12" font-weight="bold" fill="#6366f1" text-anchor="middle">ID</text>
  <text x="160" y="82" font-size="9" fill="currentColor" opacity="0.8" text-anchor="middle">Decode / Reg</text>

  <path d="M 205 67 L 220 67" stroke="#6366f1" stroke-width="2"/>

  <rect x="220" y="40" width="90" height="55" rx="8" fill="#8b5cf6" fill-opacity="0.15" stroke="#8b5cf6" stroke-width="2"/>
  <text x="265" y="65" font-size="12" font-weight="bold" fill="#8b5cf6" text-anchor="middle">EX</text>
  <text x="265" y="82" font-size="9" fill="currentColor" opacity="0.8" text-anchor="middle">Execute (ALU)</text>

  <path d="M 310 67 L 325 67" stroke="#8b5cf6" stroke-width="2"/>

  <rect x="325" y="40" width="90" height="55" rx="8" fill="#ec4899" fill-opacity="0.15" stroke="#ec4899" stroke-width="2"/>
  <text x="370" y="65" font-size="12" font-weight="bold" fill="#ec4899" text-anchor="middle">MEM</text>
  <text x="370" y="82" font-size="9" fill="currentColor" opacity="0.8" text-anchor="middle">Memory Access</text>

  <path d="M 415 67 L 430 67" stroke="#ec4899" stroke-width="2"/>

  <rect x="430" y="40" width="80" height="55" rx="8" fill="#10b981" fill-opacity="0.15" stroke="#10b981" stroke-width="2"/>
  <text x="470" y="65" font-size="12" font-weight="bold" fill="#10b981" text-anchor="middle">WB</text>
  <text x="470" y="82" font-size="9" fill="currentColor" opacity="0.8" text-anchor="middle">Write Back</text>
</svg>""",
                            "caption": "In a 5-stage RISC pipeline, up to 5 distinct instructions are processed simultaneously in different hardware stages during every clock cycle."
                        },
                        "points": [
                            "Every modern computer follows the Von Neumann architecture: a Central Processing Unit (CPU) connected to a unified memory holding both program instructions and application data.",
                            "The CPU contains high-speed internal storage locations called Registers (such as the Program Counter %rip/%pc, Stack Pointer %rsp, and general-purpose registers like %rax, %rbx).",
                            "To execute code, the CPU continuously loops through the Instruction Cycle: (1) Fetch the next instruction byte from memory pointed to by the Program Counter, (2) Decode the binary opcode into control signals, (3) Execute the arithmetic/logic operation in the ALU, (4) Access data memory if reading/writing RAM, and (5) Write the result back to a register.",
                            "Instead of waiting 5 whole clock cycles for one instruction to finish before starting the next, hardware engineers invented Instruction Pipelining — like an automotive assembly line. While instruction #1 is in the Writeback stage, instruction #2 is in Memory, #3 in Execute, #4 in Decode, and #5 in Fetch, achieving an ideal throughput of 1 instruction completed per cycle (IPC = 1.0)."
                        ]
                    },
                    {
                        "title": "Pipeline Hazards & Branch Prediction",
                        "points": [
                            "A pipeline runs at peak efficiency only when instructions flow smoothly without interruptions. When an instruction cannot execute on the next clock cycle, a Pipeline Hazard occurs, forcing the CPU to insert 'bubbles' (idle stall cycles).",
                            "Data Hazards occur when an instruction needs the output of a preceding instruction that has not yet finished its writeback stage. Hardware uses 'Data Forwarding' (bypassing the register file and routing the ALU output wire directly to the next ALU input) to resolve most data dependencies without stalling.",
                            "Control Hazards occur whenever the CPU encounters a conditional jump or branch (`if / else`, loops, function calls). Because the condition is calculated in the Execute stage, the CPU does not know which instruction to fetch next for several clock cycles.",
                            "To prevent devastating pipeline stalls, modern CPUs use sophisticated Branch Predictors: branch history tables and neural predictors guess whether a branch will be taken with over 95% accuracy. If the prediction is correct, execution continues at full speed; if mispredicted, the entire speculative pipeline must be flushed (discarded), costing 15–20 wasted clock cycles."
                        ]
                    },
                    {
                        "title": "Superscalar, Out-of-Order (OoO) & Speculative Execution",
                        "points": [
                            "Modern high-performance processors (like Intel Core, AMD Zen, and Apple M-series) are Superscalar: they contain multiple parallel execution units (multiple ALUs, vector units, load/store units) and can dispatch 4 to 8 instructions per clock cycle (IPC > 1).",
                            "Programs are written in sequential order, but if instruction #2 is waiting for data from main memory, waiting sequentially would freeze the entire processor. Out-of-Order (OoO) execution dynamically analyzes the instruction stream, identifies independent instructions later in the code (e.g., instruction #5 and #6), and executes them immediately on idle ALUs.",
                            "To maintain strict correctness, the CPU uses Register Renaming (mapping architectural registers to a larger pool of physical registers to eliminate false dependencies) and a Reorder Buffer (ROB). The ROB holds speculative results and commits them in exact program order only when all prior instructions have successfully retired."
                        ]
                    }
                ],
                "trivia": [
                    {
                        "type": "multiple_choice",
                        "question": "What is the primary purpose of instruction pipelining in a modern CPU?",
                        "options": [
                            "To execute multiple instructions concurrently across staggered hardware stages to increase throughput",
                            "To decrease the physical clock cycle duration of the silicon oscillator",
                            "To eliminate the need for an internal register file",
                            "To convert machine code into high-level programming languages"
                        ],
                        "correct": 0,
                        "explanation": "Instruction pipelining functions like a factory assembly line: by staggering the fetch, decode, execute, memory, and writeback stages, multiple instructions execute concurrently, aiming for 1 completed instruction per clock cycle."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What happens when a modern CPU's branch predictor incorrectly guesses the path of an 'if-else' condition?",
                        "options": [
                            "The pipeline must be flushed, discarding all speculatively executed instructions and wasting 15–20 cycles",
                            "The operating system immediately triggers a kernel panic",
                            "The CPU permanently halts execution until an external interrupt arrives",
                            "The ALU reverses its physical clock polarity to undo the arithmetic"
                        ],
                        "correct": 0,
                        "explanation": "When a branch misprediction occurs, the speculative work in flight is invalid; the CPU must flush the pipeline, reset the program counter to the true branch target, and restart fetching, costing a penalty of ~15–20 cycles."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Which component in an Out-of-Order (OoO) CPU ensures that instructions commit their results in the original program order?",
                        "options": [
                            "Reorder Buffer (ROB)",
                            "Arithmetic Logic Unit (ALU)",
                            "Translation Lookaside Buffer (TLB)",
                            "Direct Memory Access Controller (DMA)"
                        ],
                        "correct": 0,
                        "explanation": "The Reorder Buffer (ROB) tracks instructions executed out of order and ensures their architectural register updates and memory writes commit strictly in original program sequence."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Which hardware optimization allows the ALU output of one instruction to be fed directly to the ALU input of the next instruction without waiting for register writeback?",
                        "options": [
                            "Data Forwarding (Bypassing)",
                            "Virtual Paging",
                            "Context Switching",
                            "Bus Mastering"
                        ],
                        "correct": 0,
                        "explanation": "Data Forwarding (or bypassing) wires the output of the execution stage directly to the input multiplexers of the next stage, preventing pipeline stalls from register read-after-write delays."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What does a 'Superscalar' CPU architecture enable?",
                        "options": [
                            "Dispatching and completing multiple instructions per single clock cycle across multiple execution units",
                            "Running code without an operating system kernel",
                            "Multiplying the physical RAM size through software compression",
                            "Executing analog signals directly without digital binary encoding"
                        ],
                        "correct": 0,
                        "explanation": "A Superscalar CPU contains duplicate execution pipelines and execution units (multiple ALUs, FPUs), allowing it to fetch, decode, and execute several instructions simultaneously in a single clock cycle."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the function of the Program Counter (PC / RIP) register?",
                        "options": [
                            "Holding the memory address of the next instruction to be fetched and executed",
                            "Storing the return value of the most recently called function",
                            "Counting the total number of hardware clock pulses since boot",
                            "Managing the encryption keys for Secure Boot"
                        ],
                        "correct": 0,
                        "explanation": "The Program Counter (PC) holds the memory address of the next instruction the CPU will fetch from memory for decoding and execution."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Why do engineers use 'Register Renaming' in modern superscalar processors?",
                        "options": [
                            "To eliminate false data dependencies (Write-After-Read and Write-After-Write) by mapping to a larger physical register pool",
                            "To translate variable names from C++ to machine code strings",
                            "To decrease the electrical voltage consumed by static RAM cells",
                            "To allow user-mode software to overwrite kernel control registers"
                        ],
                        "correct": 0,
                        "explanation": "Register renaming dynamically maps a small set of architectural registers (e.g. 16 registers in x86-64) to a larger internal physical pool (e.g. 180+ registers), removing false WAR and WAW hazards."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "In the classic 5-stage RISC pipeline, what operation occurs during the 'ID' stage?",
                        "options": [
                            "Instruction Decode and reading operand values from the Register File",
                            "Writing calculation results into L3 cache memory",
                            "Fetching instruction bytes from the L1 instruction cache",
                            "Performing 64-bit floating-point division"
                        ],
                        "correct": 0,
                        "explanation": "During the Instruction Decode (ID) stage, the CPU decodes the binary opcode bits to determine the operation type and reads the source registers from the register file."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is a 'Structural Hazard' in a CPU pipeline?",
                        "options": [
                            "When two concurrent instructions attempt to access the same physical hardware resource simultaneously",
                            "When an instruction references an unallocated memory address",
                            "When thermal limits cause the silicon clock frequency to throttle down",
                            "When an operating system driver crashes due to a null pointer"
                        ],
                        "correct": 0,
                        "explanation": "A Structural Hazard occurs when the hardware cannot support all possible combinations of instructions in the pipeline simultaneously (e.g. only one memory port shared between instruction fetch and data read)."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "How does dynamic branch prediction differ from static branch prediction?",
                        "options": [
                            "Dynamic prediction uses runtime execution history to predict branches, whereas static uses fixed heuristics (like backward branches taken)",
                            "Dynamic prediction requires code to be recompiled while running",
                            "Dynamic prediction only works on floating-point arithmetic instructions",
                            "Static prediction is performed exclusively by the operating system kernel scheduler"
                        ],
                        "correct": 0,
                        "explanation": "Static prediction relies on fixed rules (e.g. backward loop branches predicted taken), whereas dynamic branch prediction maintains runtime history tables in hardware to adapt to actual program behavior."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What metric represents the average number of machine instructions a CPU completes in one clock cycle?",
                        "options": [
                            "Instructions Per Cycle (IPC)",
                            "Clock Jitter Ratio (CJR)",
                            "Thermal Design Power (TDP)",
                            "Cache Miss Penalty (CMP)"
                        ],
                        "correct": 0,
                        "explanation": "IPC (Instructions Per Cycle) measures CPU throughput efficiency; modern superscalar out-of-order processors regularly achieve IPC values between 2.0 and 4.0 on optimized workloads."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Which condition describes a 'Read-After-Write' (RAW) data dependency?",
                        "options": [
                            "An instruction requires an input operand produced by an earlier instruction that has not yet completed",
                            "An instruction writes to memory before the operating system boots",
                            "Two threads write to the same cache line simultaneously without locks",
                            "A peripheral device reads DMA memory while the CPU is powered down"
                        ],
                        "correct": 0,
                        "explanation": "A RAW dependency is a true data dependency where instruction J reads a register modified by instruction I; J cannot proceed until I's result is available."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the primary role of the Arithmetic Logic Unit (ALU)?",
                        "options": [
                            "Performing fundamental integer arithmetic (addition, subtraction) and bitwise logical operations (AND, OR, XOR)",
                            "Translating virtual addresses to physical RAM addresses",
                            "Managing the clock signal distribution across the motherboard",
                            "Scheduling software threads across multiple CPU cores"
                        ],
                        "correct": 0,
                        "explanation": "The ALU is the core computational circuit of the processor that carries out fundamental integer math, bitwise manipulations, and comparisons."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the 'Von Neumann Bottleneck'?",
                        "options": [
                            "The throughput limitation caused by sharing a single physical bus between CPU instruction fetching and data transfers",
                            "The electrical resistance generated by copper interconnects at high temperatures",
                            "The inability of RISC CPUs to execute variable-length instructions",
                            "The latency delay introduced by operating system context switches"
                        ],
                        "correct": 0,
                        "explanation": "The Von Neumann bottleneck refers to the throughput limit caused because data and instructions share the same bus between memory and the CPU, restricting execution speed to bus bandwidth."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "In computer architecture, what does 'Speculative Execution' mean?",
                        "options": [
                            "Executing instructions along a predicted path before knowing with certainty whether that path will actually be taken",
                            "Overclocking the processor voltage to speculate on maximum silicon stability",
                            "Running untrusted user code inside a sandboxed virtual machine",
                            "Compressing machine code in main memory before execution"
                        ],
                        "correct": 0,
                        "explanation": "Speculative execution is the technique where a CPU guesses the direction of a branch and executes ahead along that path; if the guess was correct, latency is hidden, and if wrong, the results are discarded."
                    }
                ]
            },

            # =================================================================
            # MODULE 2: Memory Hierarchy & Cache Coherence
            # =================================================================
            {
                "id": "memory_hierarchy_caching",
                "title": "2. Memory Hierarchy & Cache Coherence",
                "description": "Beating the 'Memory Wall': understanding L1/L2/L3 caches, spatial and temporal locality, cache line associativity, and multi-core cache coherence (MESI).",
                "cards": [
                    {
                        "title": "The Memory Wall & The Memory Hierarchy Pyramid",
                        "figure": {
                            "title": "The Latency Gap: CPU Registers to Main Memory",
                            "svg": """<svg viewBox="0 0 520 150" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-height:150px;">
  <!-- Pyramid Levels -->
  <polygon points="260,10 320,40 200,40" fill="#ef4444" fill-opacity="0.2" stroke="#ef4444" stroke-width="1.5"/>
  <text x="260" y="32" font-size="10" font-weight="bold" fill="#ef4444" text-anchor="middle">Registers (&lt;1ns)</text>

  <polygon points="200,42 320,42 360,72 160,72" fill="#f59e0b" fill-opacity="0.2" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="260" y="62" font-size="10" font-weight="bold" fill="#f59e0b" text-anchor="middle">L1 / L2 Cache (1–4ns)</text>

  <polygon points="160,74 360,74 400,104 120,104" fill="#3b82f6" fill-opacity="0.2" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="260" y="94" font-size="10" font-weight="bold" fill="#3b82f6" text-anchor="middle">L3 Shared Cache (10–20ns)</text>

  <polygon points="120,106 400,106 450,136 70,136" fill="#10b981" fill-opacity="0.2" stroke="#10b981" stroke-width="1.5"/>
  <text x="260" y="126" font-size="10" font-weight="bold" fill="#10b981" text-anchor="middle">Main RAM (DRAM, 50–100ns)</text>
</svg>""",
                            "caption": "Smaller, faster static SRAM caches (L1/L2/L3) sit directly on the CPU die to shield the fast core from the ~100-cycle latency of main DRAM."
                        },
                        "points": [
                            "In 1980, CPU clock speeds and memory access speeds were roughly balanced. Over the next four decades, CPU processing power exploded exponentially, while Dynamic RAM (DRAM) access latency improved very slowly. This vast speed disparity is known as the 'Memory Wall'.",
                            "A modern CPU executes instructions in ~0.3 nanoseconds (a fraction of a clock cycle), but fetching a value from main DDR RAM takes 50 to 80 nanoseconds — an eternity of 200+ wasted clock cycles where the CPU core sits completely stalled.",
                            "To solve this, hardware engineers organize memory into a Hierarchy based on SRAM (Static RAM): fast, expensive, tiny caches built directly onto the silicon die right next to the execution units.",
                            "L1 Cache is private to each core, split into L1-Instruction and L1-Data (typically 32–64 KB, ~1ns access latency). L2 Cache is larger (512 KB–1 MB per core, ~3–4ns). L3 Cache is shared across all cores on the chip (16–64+ MB, ~10–15ns), backed up by system DRAM."
                        ]
                    },
                    {
                        "title": "Locality of Reference & Cache Lines",
                        "points": [
                            "Caches work because of the fundamental Principle of Locality: computer programs do not access memory randomly; they exhibit two powerful behavioral patterns.",
                            "Temporal Locality: If a memory location was accessed once, it is extremely likely to be accessed again soon (e.g. loop counter variables, accumulator sums, frequently called functions).",
                            "Spatial Locality: If a memory location is accessed, memory locations with nearby addresses are extremely likely to be accessed soon (e.g. sequential array elements, adjacent struct fields, sequential instruction bytes).",
                            "Because of spatial locality, the CPU never transfers a single byte from RAM. It always fetches a contiguous chunk called a Cache Line (universally 64 bytes in modern x86 and ARM architectures). Iterating sequentially over a contiguous array gets 1 cache miss followed by 15 cache hits for 4-byte integers!"
                        ]
                    },
                    {
                        "title": "Cache Associativity, False Sharing & MESI Coherence",
                        "points": [
                            "Caches are organized into Sets and Lines. In a Direct-Mapped cache, each memory address maps to exactly one cache slot (high collision rate). Modern CPUs use Set-Associative Caches (e.g. 8-way or 16-way associative), allowing any memory address to reside in any of $N$ slots in its assigned set, drastically reducing thrashing.",
                            "When multiple CPU cores have private L1/L2 caches holding copies of the same RAM address, writes by one core must be synchronized. The MESI Protocol maintains hardware cache coherence across cores using four states: Modified (dirty, only in this cache), Exclusive (clean, only in this cache), Shared (clean, present in multiple caches), and Invalid (stale data).",
                            "False Sharing occurs when two threads running on different cores modify independent variables that happen to sit within the SAME 64-byte cache line. The hardware MESI protocol repeatedly invalidates and bounces the cache line between cores over the interconnect bus, causing severe performance degradation."
                        ]
                    }
                ],
                "trivia": [
                    {
                        "type": "multiple_choice",
                        "question": "What is the typical size of a standard CPU cache line in modern x86 and ARM processors?",
                        "options": [
                            "64 bytes",
                            "4 kilobytes",
                            "8 bits",
                            "1 megabyte"
                        ],
                        "correct": 0,
                        "explanation": "Virtually all modern x86-64 and ARM processors utilize a 64-byte cache line as the fundamental atomic unit of data transfer between main memory and caches."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Which principle describes the phenomenon where accessing one array element makes accessing adjacent elements much faster?",
                        "options": [
                            "Spatial Locality",
                            "Temporal Locality",
                            "Virtual Translation",
                            "Instruction Level Parallelism"
                        ],
                        "correct": 0,
                        "explanation": "Spatial Locality states that data physically near recently accessed memory is likely to be accessed soon; because the CPU loads an entire 64-byte cache line, adjacent elements are already present in L1 cache."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is 'False Sharing' in multi-threaded programming?",
                        "options": [
                            "When independent variables accessed by different threads reside on the same 64-byte cache line, causing constant cache invalidations",
                            "When two processes try to bind to the same TCP port number",
                            "When virtual memory pages share the same physical RAM frame across users",
                            "When a thread unlocks a mutex owned by another thread"
                        ],
                        "correct": 0,
                        "explanation": "False sharing happens when threads on separate cores write to distinct variables that happen to occupy the same 64-byte cache line, triggering the MESI protocol to bounce the cache line between cores."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "In the MESI cache coherence protocol, what does the 'M' (Modified) state signify?",
                        "options": [
                            "The cache line is present only in the current cache, is dirty (modified), and differs from main memory",
                            "The cache line is shared in read-only mode by all cores",
                            "The cache line has been marked for deletion by the garbage collector",
                            "The cache line is mapped to virtual memory swap space"
                        ],
                        "correct": 0,
                        "explanation": "In MESI, 'Modified' indicates the cache line exists only in the local cache, has been written to by the local CPU core, and must be written back to main memory before eviction or sharing."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the primary trade-off between Static RAM (SRAM) used in caches and Dynamic RAM (DRAM) used in main memory?",
                        "options": [
                            "SRAM is extremely fast (~1ns) but expensive and area-heavy (6 transistors/bit); DRAM is slower (~60ns) but dense and cheap (1 transistor + capacitor/bit)",
                            "SRAM requires periodic electrical refresh cycles, whereas DRAM retains data indefinitely without power",
                            "SRAM can only store read-only executable instructions, whereas DRAM stores read-write data",
                            "SRAM connects via PCIe bus, while DRAM connects directly to the ALU"
                        ],
                        "correct": 0,
                        "explanation": "SRAM uses a 6-transistor flip-flop circuit for instant, high-speed access without refresh cycles (ideal for on-die L1/L2/L3 caches), whereas DRAM uses a single transistor and tiny capacitor for massive storage density at lower speeds."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is an 'N-way Set-Associative' cache?",
                        "options": [
                            "A cache architecture where any given memory address can be placed in any of N specific cache line slots within its assigned set",
                            "A cache that simultaneously connects to N separate CPU motherboards",
                            "A cache that compresses data by a factor of N using hardware gzip",
                            "A cache that divides each 64-byte line into N sub-byte nibbles"
                        ],
                        "correct": 0,
                        "explanation": "An N-way set-associative cache splits the cache into sets of N lines each; a memory address hashes to a specific set and can occupy any of the N slots in that set, balancing hit latency and collision rates."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Why does traversing a 2D matrix row-by-row execute drastically faster in C/C++ than column-by-column?",
                        "options": [
                            "Row-major layout stores elements of a row in contiguous memory, maximizing spatial locality and cache line hits",
                            "Column traversal disables the CPU instruction pipeline",
                            "Row traversal uses floating-point hardware instead of integer ALUs",
                            "The compiler converts column traversal into recursive function calls"
                        ],
                        "correct": 0,
                        "explanation": "C/C++ matrices use row-major memory order; iterating row-by-row accesses adjacent bytes in sequence (spatial locality), while column-by-column jumps across memory strides larger than 64 bytes, causing a cache miss on almost every access."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the difference between a 'Write-Through' cache and a 'Write-Back' cache?",
                        "options": [
                            "Write-Through immediately writes updates to lower memory levels; Write-Back updates only the cache and writes to memory when evicted",
                            "Write-Through only caches reads; Write-Back only caches writes",
                            "Write-Through is used exclusively in GPU video memory",
                            "Write-Back bypasses the CPU cache hierarchy entirely"
                        ],
                        "correct": 0,
                        "explanation": "Write-through updates both the cache and underlying main memory simultaneously on every write; write-back updates only the cache line (marking it dirty) and postpones writing to main RAM until the line is evicted."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the term for the historical divergence between fast CPU clock improvements and sluggish DRAM access latency?",
                        "options": [
                            "The Memory Wall",
                            "Moore's Law Collapse",
                            "Amdahl's Limit",
                            "The Pipelining Penalty"
                        ],
                        "correct": 0,
                        "explanation": "The 'Memory Wall' describes the increasing gap between processing speed and DRAM access latency, making caching and memory hierarchy design the primary determinants of system performance."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What happens when a CPU experiences a 'Cache Miss'?",
                        "options": [
                            "The CPU must stall execution while fetching the missing 64-byte block from a higher-level cache or main DRAM",
                            "The operating system terminates the process with a segmentation fault",
                            "The CPU flushes its entire hard drive cache to physical flash sectors",
                            "The BIOS restarts the motherboard power distribution unit"
                        ],
                        "correct": 0,
                        "explanation": "On a cache miss, the requested data is not present in that cache level; the processor must issue a request to the next cache level or main RAM, suffering a latency delay before resuming execution."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "In the MESI protocol, what state is assigned to a cache line if another core writes to that memory location?",
                        "options": [
                            "Invalid (I)",
                            "Shared (S)",
                            "Exclusive (E)",
                            "Modified (M)"
                        ],
                        "correct": 0,
                        "explanation": "When another core performs a bus write broadcast to a shared line, all other cores holding that line must transition their local copy to 'Invalid' (I) so they don't read stale data."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Which cache replacement policy evicts the line that has not been accessed for the longest period of time?",
                        "options": [
                            "Least Recently Used (LRU)",
                            "First-In, First-Out (FIFO)",
                            "Random Replacement (RR)",
                            "Most Frequently Used (MFU)"
                        ],
                        "correct": 0,
                        "explanation": "The Least Recently Used (LRU) policy tracks access recency and evicts the cache line whose last access occurred furthest in the past, exploiting temporal locality."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is a 'Hardware Prefetcher' in a CPU memory controller?",
                        "options": [
                            "A hardware unit that detects sequential memory access patterns and speculatively loads future cache lines before they are requested",
                            "A tool that pre-compiles source code into binary executables at system boot",
                            "A voltage regulator that pre-charges DRAM capacitors before cold reboots",
                            "A software background daemon that defragments physical hard disks"
                        ],
                        "correct": 0,
                        "explanation": "Hardware prefetchers analyze address streams; when they detect constant strides (e.g. iterating over an array), they proactively fetch upcoming cache lines from DRAM into L2/L1 to hide memory latency."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the key advantage of an 'Inclusive Cache' hierarchy (e.g. L3 inclusive of L1/L2)?",
                        "options": [
                            "Checking if another core has a cached line can be done by probing only the shared L3 cache, without disturbing private L1/L2 caches",
                            "It doubles the effective storage capacity of the silicon die",
                            "It eliminates the need for cache tags and index bits",
                            "It allows L1 caches to store infinite lines without eviction"
                        ],
                        "correct": 0,
                        "explanation": "In an inclusive hierarchy, everything in L1 and L2 is guaranteed to also exist in L3; hardware can perform snoop checks across cores by inspecting only the L3 tags, saving interconnect traffic."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Which level of the CPU cache hierarchy is typically shared among all processor cores on a multi-core silicon die?",
                        "options": [
                            "L3 Cache (Last Level Cache / LLC)",
                            "L1 Instruction Cache",
                            "L1 Data Cache",
                            "CPU Register File"
                        ],
                        "correct": 0,
                        "explanation": "While L1 and L2 caches are dedicated private hardware for individual cores, the L3 cache (Last-Level Cache) is unified and shared across all cores on the processor chip."
                    }
                ]
            },

            # =================================================================
            # MODULE 3: Virtual Memory, Paging & The MMU
            # =================================================================
            {
                "id": "virtual_memory_paging",
                "title": "3. Virtual Memory, Paging & The MMU",
                "description": "How operating systems provide memory isolation, address translation via page tables, Translation Lookaside Buffers (TLB), page faults, and demand paging.",
                "cards": [
                    {
                        "title": "Why Virtual Memory? Isolation & The Illusion of Infinite RAM",
                        "figure": {
                            "title": "Virtual-to-Physical Address Translation Flow",
                            "svg": """<svg viewBox="0 0 520 140" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-height:140px;">
  <!-- Virtual Address -->
  <rect x="20" y="45" width="130" height="50" rx="8" fill="#3b82f6" fill-opacity="0.15" stroke="#3b82f6" stroke-width="2"/>
  <text x="85" y="67" font-size="11" font-weight="bold" fill="#3b82f6" text-anchor="middle">Virtual Address</text>
  <text x="85" y="83" font-size="9" fill="currentColor" opacity="0.8" text-anchor="middle">VPN + Page Offset</text>

  <path d="M 150 70 L 195 70" stroke="#3b82f6" stroke-width="2"/>

  <!-- MMU / TLB -->
  <rect x="195" y="35" width="130" height="70" rx="8" fill="#8b5cf6" fill-opacity="0.15" stroke="#8b5cf6" stroke-width="2"/>
  <text x="260" y="60" font-size="12" font-weight="bold" fill="#8b5cf6" text-anchor="middle">MMU / TLB</text>
  <text x="260" y="78" font-size="9" fill="currentColor" opacity="0.8" text-anchor="middle">Fast Hardware Lookup</text>
  <text x="260" y="92" font-size="9" fill="#10b981" text-anchor="middle">Page Table Translation</text>

  <path d="M 325 70 L 370 70" stroke="#10b981" stroke-width="2"/>

  <!-- Physical RAM -->
  <rect x="370" y="45" width="130" height="50" rx="8" fill="#10b981" fill-opacity="0.15" stroke="#10b981" stroke-width="2"/>
  <text x="435" y="67" font-size="11" font-weight="bold" fill="#10b981" text-anchor="middle">Physical RAM</text>
  <text x="435" y="83" font-size="9" fill="currentColor" opacity="0.8" text-anchor="middle">PPN Frame + Offset</text>
</svg>""",
                            "caption": "The Memory Management Unit (MMU) uses page tables and the high-speed TLB cache to dynamically translate virtual addresses into physical RAM frames."
                        },
                        "points": [
                            "In early computing, programs ran directly on physical memory: if program A overwrote memory address `0x1000`, it could corrupt program B or crash the operating system. Furthermore, total memory was strictly limited to physical RAM chips.",
                            "Virtual Memory solves this by giving every single process its own private, isolated virtual address space (e.g. 128 TB in 64-bit x86-64). A process believes it owns all of memory from address `0x0000000000000000` to `0x7FFFFFFFFFFF`.",
                            "Memory is divided into fixed-size blocks called Pages (typically 4 KB, or 2 MB / 1 GB for HugePages). Physical RAM is divided into matching Page Frames.",
                            "The operating system maintains a Page Table for each process. When a program reads address `0x401000`, the hardware Memory Management Unit (MMU) consults the page table to translate the Virtual Page Number (VPN) into a Physical Frame Number (PFN)."
                        ]
                    },
                    {
                        "title": "The Translation Lookaside Buffer (TLB) & Multi-Level Page Tables",
                        "points": [
                            "In a 64-bit architecture, a single flat page table mapping every possible 4KB page would consume millions of gigabytes of RAM. Modern operating systems use 4-Level (or 5-Level) Hierarchical Page Tables (PML4 -> PDPT -> PD -> PT in x86-64), creating sub-tables only for memory regions the process actually allocates.",
                            "Walking a 4-level page table tree requires 4 separate memory lookups just to translate ONE pointer address — which would slow down every memory access by 400%!",
                            "To make translation instantaneous, the CPU contains a specialized, ultra-fast hardware associative cache called the Translation Lookaside Buffer (TLB). The TLB caches recently translated VPN -> PFN mappings.",
                            "A TLB Hit resolves the physical address in less than 1 clock cycle (~0.5ns). A TLB Miss forces the MMU hardware page-table walker to traverse RAM tables, costing 30–50ns."
                        ]
                    },
                    {
                        "title": "Page Faults, Demand Paging & Memory Protection",
                        "points": [
                            "Each Page Table Entry (PTE) contains metadata permission and status bits: Present (valid in RAM), Read/Write, User/Supervisor (Ring 3 vs Ring 0), and NX (No-Execute / XD bit for security against buffer overflows).",
                            "If a process accesses an address whose Present bit is 0, the MMU hardware triggers a CPU interrupt called a Page Fault (Exception #14 in x86). The CPU immediately pauses user code and switches to the OS kernel page fault handler.",
                            "Demand Paging: If the page exists on disk swap or is a memory-mapped file (`mmap`), the OS allocates a physical RAM frame, loads the 4KB data from storage via DMA, sets Present = 1, and resumes the user process seamlessly.",
                            "Segmentation Fault: If the process attempted an illegal operation (writing to read-only code, accessing an unmapped address, or executing data memory), the OS delivers a `SIGSEGV` signal, terminating the offending program."
                        ]
                    }
                ],
                "trivia": [
                    {
                        "type": "multiple_choice",
                        "question": "What is the standard base page size in modern x86-64 and ARM operating systems?",
                        "options": [
                            "4 Kilobytes (4096 bytes)",
                            "64 bytes",
                            "1 Megabyte",
                            "512 bytes"
                        ],
                        "correct": 0,
                        "explanation": "4 KB (4,096 bytes) is the standard base page size for virtual memory allocation, page tables, and physical frame management in modern architectures."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the primary role of the Translation Lookaside Buffer (TLB)?",
                        "options": [
                            "To cache virtual-to-physical address translations in hardware to avoid multi-level page table walks in RAM",
                            "To translate high-level Python bytecode into machine instructions",
                            "To buffer network packets before transmitting them to the NIC",
                            "To hold backup copies of CPU registers during power outages"
                        ],
                        "correct": 0,
                        "explanation": "The TLB is a high-speed associative hardware cache in the CPU that stores recent virtual-to-physical page translations, enabling single-cycle memory address resolution."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What hardware event occurs when a process attempts to access a virtual memory page that is currently not loaded into physical RAM?",
                        "options": [
                            "A Page Fault exception is raised, transferring control to the OS kernel handler",
                            "The CPU reboots the motherboard immediately",
                            "The ALU returns a random 64-bit integer without error",
                            "The hard disk triggers an out-of-memory kernel panic"
                        ],
                        "correct": 0,
                        "explanation": "When the Present bit in the Page Table Entry is 0, the MMU fires a Page Fault interrupt; the OS kernel handler then loads the page from disk into RAM (demand paging) and resumes execution."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Which security feature marks memory regions (like the Stack and Heap) as non-executable to prevent malicious code injection attacks?",
                        "options": [
                            "The NX (No-Execute) / XD (Execute Disable) bit",
                            "The Dirty bit",
                            "The Access Timestamp counter",
                            "The Parity Check register"
                        ],
                        "correct": 0,
                        "explanation": "The NX/XD bit in the page table entry allows the OS to designate data pages (stack, heap) as non-executable; attempting to jump to and execute code there triggers an immediate hardware fault."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Why do modern 64-bit operating systems use Multi-Level Page Tables instead of a single flat table?",
                        "options": [
                            "To save vast amounts of RAM by allocating page table structures only for virtual address regions actually in use",
                            "To make memory address translations run 10x faster than a flat array",
                            "To eliminate the need for physical DRAM chips",
                            "To allow 32-bit CPUs to execute 64-bit instructions"
                        ],
                        "correct": 0,
                        "explanation": "A flat 64-bit page table would require terabytes of RAM per process; multi-level hierarchical trees allocate lower-level page tables on-demand only for populated virtual address spaces."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is 'Demand Paging' in an operating system?",
                        "options": [
                            "A strategy where pages are brought into physical RAM only when the running program actually attempts to access them",
                            "Loading the entire executable binary and all shared libraries into RAM at initial launch",
                            "Requiring user software to manually issue RAM allocation syscalls for every byte",
                            "Compressing idle virtual memory pages onto flash storage"
                        ],
                        "correct": 0,
                        "explanation": "Demand paging defers loading memory from disk into physical RAM until the exact moment a process touches that page, triggering a page fault that loads the requested 4KB block."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the purpose of 'HugePages' (e.g. 2 MB or 1 GB page sizes) in high-performance databases and virtualization?",
                        "options": [
                            "To drastically reduce the number of TLB entries required, improving TLB hit rates for massive datasets",
                            "To increase the clock speed of the memory bus",
                            "To enable 128-bit integer arithmetic in user space",
                            "To encrypt physical DRAM against cold-boot physical attacks"
                        ],
                        "correct": 0,
                        "explanation": "Using 2MB or 1GB HugePages allows a single TLB entry to cover thousands of times more memory, preventing TLB thrashing in memory-intensive workloads like databases and virtual machines."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What happens during a 'TLB Shootdown' in a multi-core operating system?",
                        "options": [
                            "An inter-processor interrupt (IPI) forces other CPU cores to invalidate stale translations in their local TLBs when page mappings change",
                            "The CPU powers down idle cores to reduce thermal throttling",
                            "The memory controller clears all physical RAM contents",
                            "A user process is killed for exceeding memory quotas"
                        ],
                        "correct": 0,
                        "explanation": "When one core alters a shared page mapping (e.g. unmapping or reallocating memory), it must send Inter-Processor Interrupts (IPIs) to all other cores running that process to flush their local TLB entries."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Which CPU register in the x86-64 architecture holds the physical base address of the current process's top-level page table (PML4)?",
                        "options": [
                            "CR3 Control Register",
                            "RSP Stack Pointer",
                            "EFLAGS Status Register",
                            "RIP Instruction Pointer"
                        ],
                        "correct": 0,
                        "explanation": "The CR3 control register points to the root physical address of the active process's page table directory; updating CR3 during a context switch instantly activates that process's virtual address space."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is Address Space Layout Randomization (ASLR)?",
                        "options": [
                            "A security technique that randomizes the memory locations of the stack, heap, and libraries to hinder buffer overflow exploits",
                            "A hardware algorithm that spreads cache lines across memory banks",
                            "A file system format that randomizes disk block storage",
                            "An OS scheduler that randomly assigns threads to CPU cores"
                        ],
                        "correct": 0,
                        "explanation": "ASLR randomizes the base addresses of the stack, heap, and loaded shared libraries every time a program executes, preventing attackers from predicting target function addresses in memory."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What does a 'Segmentation Fault' (SIGSEGV) indicate to a software developer?",
                        "options": [
                            "The program attempted an unauthorized virtual memory access (e.g. dereferencing a null/invalid pointer or writing to read-only memory)",
                            "The physical RAM module has suffered a hardware transistor failure",
                            "The CPU clock multiplier was adjusted during a mathematical calculation",
                            "The hard disk storage capacity has reached 100% full"
                        ],
                        "correct": 0,
                        "explanation": "A segmentation fault occurs when the hardware MMU catches a process attempting to access an unmapped virtual address or violate permissions (such as writing to a read-only code page)."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is 'Memory Thrashing' in an operating system?",
                        "options": [
                            "When physical RAM is overcommitted, causing the OS to spend more time swapping pages to/from disk than executing useful code",
                            "When two threads simultaneously acquire the same spinlock",
                            "When the CPU cache lines become corrupt due to thermal radiation",
                            "When a file system runs out of free inode entries"
                        ],
                        "correct": 0,
                        "explanation": "Thrashing occurs when active working sets exceed physical RAM; the OS continuously evicts and reads pages from swap storage, causing system throughput to collapse."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "In virtual memory, what is the role of the 'Dirty Bit' in a Page Table Entry?",
                        "options": [
                            "It indicates whether the page has been written to since being loaded into physical RAM",
                            "It indicates whether the page contains a security virus",
                            "It tells the CPU that the page is stored on an optical DVD drive",
                            "It forces the page to be deleted when the thread exits"
                        ],
                        "correct": 0,
                        "explanation": "The MMU hardware automatically sets the Dirty bit to 1 whenever a write operation occurs on that page; the OS checks this bit when evicting a page to know if it must be written back to disk."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the 'Working Set' of a process?",
                        "options": [
                            "The collection of virtual memory pages that the process actively references during a given time window",
                            "The total count of open file descriptors owned by the process",
                            "The set of CPU cores assigned to execute the process threads",
                            "The list of shared libraries compiled into the executable"
                        ],
                        "correct": 0,
                        "explanation": "The working set is the set of memory pages actively used by a process at a specific time; if physical RAM cannot hold the working sets of running processes, thrashing begins."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "How does 'Copy-on-Write' (COW) optimize the `fork()` system call in Unix-like operating systems?",
                        "options": [
                            "Parent and child share the same physical RAM pages read-only; duplicate pages are allocated only when one process writes to memory",
                            "The OS copies the entire physical RAM footprint of the parent immediately to new memory frames",
                            "The child process runs inside the parent's CPU registers without memory allocation",
                            "The disk controller writes the parent memory state directly to flash swap"
                        ],
                        "correct": 0,
                        "explanation": "Instead of duplicating megabytes or gigabytes of RAM during `fork()`, COW marks all pages read-only and shared; physical duplication occurs on-demand only for pages that are modified."
                    }
                ]
            },

            # =================================================================
            # MODULE 4: Processes, Threads & Concurrency
            # =================================================================
            {
                "id": "processes_threads_concurrency",
                "title": "4. OS Concurrency, Scheduling & Synchronization",
                "description": "Understanding process address spaces, kernel vs user space (Ring 0 vs Ring 3), context switches, race conditions, mutexes, spinlocks, futexes, and atomic operations.",
                "cards": [
                    {
                        "title": "Processes vs. Threads & Context Switching",
                        "figure": {
                            "title": "Process Memory Layout vs Multi-Threading",
                            "svg": """<svg viewBox="0 0 520 150" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-height:150px;">
  <!-- Process Box -->
  <rect x="20" y="20" width="220" height="115" rx="8" fill="#3b82f6" fill-opacity="0.1" stroke="#3b82f6" stroke-width="2"/>
  <text x="130" y="40" font-size="11" font-weight="bold" fill="#3b82f6" text-anchor="middle">Process Address Space</text>
  <rect x="35" y="55" width="85" height="30" rx="4" fill="#3b82f6" fill-opacity="0.2"/>
  <text x="77" y="74" font-size="9" fill="currentColor" text-anchor="middle">Code &amp; Global</text>
  <rect x="135" y="55" width="85" height="30" rx="4" fill="#10b981" fill-opacity="0.2"/>
  <text x="177" y="74" font-size="9" fill="currentColor" text-anchor="middle">Shared Heap</text>
  <rect x="35" y="95" width="185" height="28" rx="4" fill="#ec4899" fill-opacity="0.15"/>
  <text x="127" y="113" font-size="9" fill="#ec4899" text-anchor="middle">Open Files / Descriptors</text>

  <!-- Threads -->
  <rect x="275" y="20" width="225" height="115" rx="8" fill="#8b5cf6" fill-opacity="0.1" stroke="#8b5cf6" stroke-width="2"/>
  <text x="387" y="40" font-size="11" font-weight="bold" fill="#8b5cf6" text-anchor="middle">Threads (Execution Units)</text>
  <rect x="290" y="55" width="95" height="68" rx="4" fill="#8b5cf6" fill-opacity="0.2"/>
  <text x="337" y="75" font-size="10" font-weight="bold" fill="#8b5cf6" text-anchor="middle">Thread 1</text>
  <text x="337" y="92" font-size="8" fill="currentColor" opacity="0.8" text-anchor="middle">Stack &amp; %rsp</text>
  <text x="337" y="106" font-size="8" fill="currentColor" opacity="0.8" text-anchor="middle">CPU Registers</text>

  <rect x="395" y="55" width="95" height="68" rx="4" fill="#8b5cf6" fill-opacity="0.2"/>
  <text x="442" y="75" font-size="10" font-weight="bold" fill="#8b5cf6" text-anchor="middle">Thread 2</text>
  <text x="442" y="92" font-size="8" fill="currentColor" opacity="0.8" text-anchor="middle">Stack &amp; %rsp</text>
  <text x="442" y="106" font-size="8" fill="currentColor" opacity="0.8" text-anchor="middle">CPU Registers</text>
</svg>""",
                            "caption": "A Process owns an isolated virtual memory space (code, heap, file descriptors); Threads within the process share that memory but own private execution stacks and registers."
                        },
                        "points": [
                            "A Process is an instance of a running computer program, owning an isolated virtual address space, heap memory, open file descriptors, and security tokens. The OS manages this via the Process Control Block (PCB).",
                            "A Thread is the smallest unit of execution scheduled by the OS kernel. Multiple threads within the same process share the same virtual address space and heap, but each thread owns its own private Call Stack, Stack Pointer (%rsp), and CPU Register context.",
                            "A Context Switch occurs when the OS scheduler pauses one thread/process and switches the CPU core to execute another. The kernel saves all active CPU registers into the thread's control block, switches the stack pointer, and loads the new thread's registers.",
                            "Switching between processes is significantly more expensive than switching between threads because process switching requires writing the new page table base address into the CR3 register, which invalidates non-global TLB entries and triggers cache miss cascades."
                        ]
                    },
                    {
                        "title": "Kernel Mode vs. User Mode (Ring 0 vs. Ring 3) & System Calls",
                        "points": [
                            "CPUs enforce hardware-level privilege rings: Ring 0 (Kernel Mode) has unrestricted access to physical hardware, control registers, and memory; Ring 3 (User Mode) runs application software with restricted instructions to prevent crashes.",
                            "User software cannot access disk, network cards, or allocate physical RAM directly. Whenever an application needs hardware services (e.g. `open()`, `read()`, `write()`, `socket()`), it executes a System Call (`syscall` instruction in x86-64).",
                            "The `syscall` instruction causes a controlled hardware transition from Ring 3 to Ring 0, saving the user instruction pointer (%rcx) and status flags (%r11), and jumping to the kernel system call entry point defined in a Model-Specific Register (MSR)."
                        ]
                    },
                    {
                        "title": "Race Conditions, Mutexes, Spinlocks, Futexes & Atomic Operations",
                        "points": [
                            "When multiple threads read and modify shared heap memory simultaneously without synchronization, non-deterministic Race Conditions occur (e.g. `counter++` is actually 3 distinct assembly steps: read from RAM, increment in register, write to RAM).",
                            "Atomic Operations (like `Compare-And-Swap` / CAS or `test-and-set`) are executed as single, indivisible hardware memory bus transactions (`LOCK CMPXCHG` on x86), forming the fundamental building block for all lock-free algorithms.",
                            "A Spinlock actively loops in a tight CPU cycle check until a lock becomes available; it is ideal for very short kernel critical sections but wastes 100% of a CPU core if held for long periods.",
                            "A Mutex puts waiting threads to sleep so other tasks can use the CPU. Modern Linux mutexes are built on Futexes (Fast Userspace Mutexes): uncontended lock acquisition takes place entirely in user space in ~5ns via atomic CAS; the kernel syscall is invoked only when lock contention requires putting a thread to sleep."
                        ]
                    }
                ],
                "trivia": [
                    {
                        "type": "multiple_choice",
                        "question": "What memory resource is uniquely private to each thread within a multi-threaded process?",
                        "options": [
                            "The execution Call Stack and CPU register context",
                            "The dynamic Heap allocation pool",
                            "The Global variable memory segment",
                            "The process File Descriptor table"
                        ],
                        "correct": 0,
                        "explanation": "Threads share their parent process's virtual address space, heap, and open file descriptors, but each thread has its own private call stack and CPU register state."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Why is a process context switch significantly more expensive than a thread context switch within the same process?",
                        "options": [
                            "A process context switch requires changing the CR3 page table pointer, which invalidates TLB entries and causes memory cache misses",
                            "A process switch requires rebooting the network interface card",
                            "Thread switches must always be validated by physical cryptographic hardware chips",
                            "A process switch copies all heap data to the physical hard drive"
                        ],
                        "correct": 0,
                        "explanation": "Switching processes switches virtual address spaces (reloading the CR3 register), invalidating non-global TLB entries and causing subsequent memory access cache misses."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What mechanism enables a user-space application (Ring 3) to request services from the operating system kernel (Ring 0)?",
                        "options": [
                            "System Call (syscall instruction)",
                            "Direct Memory Access (DMA) channel request",
                            "Floating-point rounding interrupt",
                            "Modifying the BIOS clock counter"
                        ],
                        "correct": 0,
                        "explanation": "System calls (`syscall` / `sysenter`) provide a controlled hardware gateway for user-mode software to request privileged OS kernel services (like reading files or opening sockets)."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is a 'Race Condition' in concurrent programming?",
                        "options": [
                            "A bug where the correctness of a program depends on the non-deterministic execution timing or interleaving of multiple threads",
                            "When two CPUs compete to run at the highest clock frequency",
                            "When an application consumes more bandwidth than the network card supports",
                            "When a thread crashes because it ran out of physical stack space"
                        ],
                        "correct": 0,
                        "explanation": "A race condition occurs when two or more concurrent threads access shared state without proper synchronization, producing unpredictable and corrupted results depending on timing."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "How does a 'Futex' (Fast Userspace Mutex) achieve high performance in Linux?",
                        "options": [
                            "It acquires and releases uncontended locks entirely in user space via atomic instructions, calling into the kernel only on contention",
                            "It runs all synchronization code inside the GPU hardware shader units",
                            "It disables CPU hardware interrupts during critical sections",
                            "It converts multi-threaded programs into single-threaded coroutines"
                        ],
                        "correct": 0,
                        "explanation": "Futexes perform lock acquisition in user space using fast atomic operations (like Compare-And-Swap in ~5ns); expensive kernel syscalls are executed only if a thread must sleep or be woken up."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Which hardware assembly instruction on x86-64 provides the foundation for lock-free data structures by atomically updating a value if it matches an expected value?",
                        "options": [
                            "LOCK CMPXCHG (Compare-and-Exchange)",
                            "NOP (No Operation)",
                            "JMP (Unconditional Jump)",
                            "HLT (Halt Processor)"
                        ],
                        "correct": 0,
                        "explanation": "The atomic `LOCK CMPXCHG` instruction compares a memory location with a register and swaps in a new value only if they match, executing as an indivisible bus transaction."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What are the four necessary conditions for a Deadlock to occur (the Coffman conditions)?",
                        "options": [
                            "Mutual Exclusion, Hold and Wait, No Preemption, and Circular Wait",
                            "Atomic Access, Virtual Paging, Branch Prediction, and Context Switching",
                            "Read Only, Write Only, Execute Only, and No Execute",
                            "Ring 0, Ring 1, Ring 2, and Ring 3"
                        ],
                        "correct": 0,
                        "explanation": "The 4 Coffman conditions for deadlock are: (1) Mutual exclusion, (2) Hold and wait, (3) No preemption, and (4) Circular wait; breaking any one condition prevents deadlocks."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the primary drawback of using a 'Spinlock' for long critical sections?",
                        "options": [
                            "It wastes 100% of a CPU core's cycles in a busy-wait loop while waiting for the lock to be released",
                            "It triggers a kernel panic if held longer than 1 millisecond",
                            "It automatically unlocks itself after 100 clock cycles",
                            "It causes physical thermal degradation to the DDR RAM module"
                        ],
                        "correct": 0,
                        "explanation": "Spinlocks do not put waiting threads to sleep; they continuously loop and query the lock status, consuming 100% CPU time that could otherwise execute other useful threads."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is a 'Memory Barrier' (or Memory Fence) instruction?",
                        "options": [
                            "A CPU instruction that enforces strict ordering on memory load and store operations across out-of-order execution and caches",
                            "A physical firewall circuit between the motherboard and power supply",
                            "An operating system security sandbox preventing processes from using RAM",
                            "A compiler optimization that removes unreferenced local variables"
                        ],
                        "correct": 0,
                        "explanation": "Memory barriers prevent the CPU and compiler from reordering read and write instructions across the barrier, ensuring correct visibility in multi-core concurrent programs."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What state does a Unix process enter when it has terminated execution, but its parent process has not yet called `wait()` to read its exit code?",
                        "options": [
                            "Zombie Process (Defunct)",
                            "Orphan Process",
                            "Daemon Process",
                            "Real-Time Process"
                        ],
                        "correct": 0,
                        "explanation": "A Zombie process has completed execution and released its memory, but its PID and exit status remain in the kernel Process Table until the parent calls `wait()`/`waitpid()`."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the difference between Preemptive and Non-Preemptive multitasking?",
                        "options": [
                            "In preemptive multitasking, the OS timer interrupt forcibly pauses running tasks; in non-preemptive, tasks run until they voluntarily yield",
                            "Preemptive multitasking is used exclusively on single-core 8-bit microcontrollers",
                            "Non-preemptive multitasking executes code without physical RAM",
                            "Preemptive multitasking requires user programs to be written in Rust"
                        ],
                        "correct": 0,
                        "explanation": "Modern preemptive OS kernels use hardware timer ticks to slice CPU time and forcibly switch tasks, preventing a single rogue loop from freezing the entire system."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is 'Priority Inversion' in real-time operating systems?",
                        "options": [
                            "When a high-priority task is blocked waiting for a lock held by a low-priority task, which is itself preempted by a medium-priority task",
                            "When the CPU clock speed runs backwards to save battery power",
                            "When a user-mode process executes with higher privilege than Ring 0",
                            "When a thread's stack pointer points to heap memory"
                        ],
                        "correct": 0,
                        "explanation": "Priority inversion happens when a high-priority thread is stalled waiting for a resource held by a low-priority thread, which is prevented from finishing by medium-priority tasks (famously solved by Priority Inheritance on the Mars Pathfinder)."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the purpose of the 'Completely Fair Scheduler' (CFS) in the Linux kernel?",
                        "options": [
                            "To allocate CPU time proportionally using red-black trees based on the virtual runtime (vruntime) of runnable tasks",
                            "To ensure every thread receives exactly identical network bandwidth",
                            "To distribute power evenly across physical motherboard voltage rails",
                            "To randomize thread execution to prevent denial-of-service attacks"
                        ],
                        "correct": 0,
                        "explanation": "Linux CFS models an ideal multi-tasking CPU by tracking each process's accumulated execution time (`vruntime`) in a red-black tree, always scheduling the task that has received the least CPU time."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What does a Counting Semaphore with an initial value of $K$ represent?",
                        "options": [
                            "A synchronization primitive that allows at most K concurrent threads to access a finite pool of shared resources",
                            "A hardware register that counts CPU clock cycles up to K",
                            "A process that spawns K child processes at system boot",
                            "A file descriptor that permits K simultaneous network connections"
                        ],
                        "correct": 0,
                        "explanation": "A counting semaphore initialized to $K$ acts as a resource counter; calling `wait()` (`P`) decrements the counter and blocks when it reaches 0, allowing up to $K$ concurrent accesses."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Why is `volatile` in C/C++ insufficient for thread synchronization on multi-core processors?",
                        "options": [
                            "It only prevents compiler register caching; it does not emit CPU memory barriers or guarantee atomic hardware memory operations",
                            "It is a deprecated keyword that modern compilers ignore entirely",
                            "It converts 64-bit integer variables into 8-bit character bytes",
                            "It forces the thread to execute exclusively in single-user mode"
                        ],
                        "correct": 0,
                        "explanation": "`volatile` tells the compiler not to optimize away reads/writes to a variable, but it does NOT generate atomic CPU instructions or memory fences, leaving it vulnerable to hardware race conditions on multi-core CPUs."
                    }
                ]
            },

            # =================================================================
            # MODULE 5: I/O, Storage, Interrupts & File Systems
            # =================================================================
            {
                "id": "io_storage_interrupts",
                "title": "5. I/O, Storage, Interrupts & File Systems",
                "description": "Hardware interrupts, Interrupt Service Routines (ISRs), Direct Memory Access (DMA), Inodes, File systems, and the storage evolution from HDDs to NVMe SSDs.",
                "cards": [
                    {
                        "title": "Hardware Interrupts vs. Polling & The Interrupt Vector Table (IVT)",
                        "figure": {
                            "title": "Direct Memory Access (DMA) vs Programmed I/O",
                            "svg": """<svg viewBox="0 0 520 140" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-height:140px;">
  <!-- CPU -->
  <rect x="20" y="45" width="90" height="50" rx="8" fill="#3b82f6" fill-opacity="0.15" stroke="#3b82f6" stroke-width="2"/>
  <text x="65" y="75" font-size="12" font-weight="bold" fill="#3b82f6" text-anchor="middle">CPU Core</text>

  <!-- DMA Controller -->
  <rect x="180" y="20" width="160" height="45" rx="8" fill="#8b5cf6" fill-opacity="0.15" stroke="#8b5cf6" stroke-width="2"/>
  <text x="260" y="42" font-size="10" font-weight="bold" fill="#8b5cf6" text-anchor="middle">DMA Controller</text>
  <text x="260" y="56" font-size="8" fill="currentColor" opacity="0.8" text-anchor="middle">Direct High-Speed Transfer</text>

  <!-- Physical RAM -->
  <rect x="410" y="45" width="90" height="50" rx="8" fill="#10b981" fill-opacity="0.15" stroke="#10b981" stroke-width="2"/>
  <text x="455" y="75" font-size="12" font-weight="bold" fill="#10b981" text-anchor="middle">RAM Memory</text>

  <!-- Storage / NIC -->
  <rect x="180" y="85" width="160" height="45" rx="8" fill="#f59e0b" fill-opacity="0.15" stroke="#f59e0b" stroke-width="2"/>
  <text x="260" y="107" font-size="10" font-weight="bold" fill="#f59e0b" text-anchor="middle">NVMe SSD / Network NIC</text>

  <path d="M 260 85 L 260 65" stroke="#8b5cf6" stroke-width="2" stroke-dasharray="3,3"/>
  <path d="M 340 42 L 410 60" stroke="#10b981" stroke-width="2"/>
  <path d="M 110 65 L 180 42" stroke="#3b82f6" stroke-width="2"/>
</svg>""",
                            "caption": "With Direct Memory Access (DMA), the storage device transfers megabytes of data directly into RAM over the PCIe bus without wasting CPU cycles."
                        },
                        "points": [
                            "If a CPU had to continuously check (Polling) whether a network packet arrived or a key was pressed, it would waste 99% of its computational power in useless loops.",
                            "Instead, peripheral devices use Hardware Interrupts. When a network packet arrives or an SSD finishes reading a block, the device pulses an electrical interrupt line (or sends a PCIe MSI-X message) to the CPU's Interrupt Controller (APIC).",
                            "The CPU immediately pauses the current instruction stream, saves key registers to the kernel stack, and indexes into the Interrupt Vector Table (IVT / IDT) to execute the matching Interrupt Service Routine (ISR) in kernel space.",
                            "Direct Memory Access (DMA): Rather than forcing the CPU to read every 4-byte word from the disk controller into a register and write it to RAM, the DMA controller transfers massive data streams directly between peripheral storage and physical RAM over the system bus, interrupting the CPU only once when the entire multi-megabyte transfer is finished."
                        ]
                    },
                    {
                        "title": "File Systems, Inodes & Journaling",
                        "points": [
                            "Storage devices (SSDs, HDDs) are raw arrays of 512-byte or 4096-byte sectors. A File System (like ext4, APFS, NTFS, or XFS) organizes these raw blocks into named directories, files, and metadata.",
                            "In Unix file systems, every file is represented by an Inode (Index Node). The Inode contains file metadata: size, permissions (chmod), owner UID/GID, modification timestamps, and pointers to the physical data blocks storing the file's contents. Crucially, the file's name and directory location are stored in directory entries, not in the Inode itself!",
                            "Hard Links: Two directory entries pointing to the exact same Inode number share the exact same underlying file. The data is physically deleted only when the Inode link count reaches zero.",
                            "Journaling File Systems prevent data corruption during sudden power losses. Before modifying complex disk structures (e.g. creating an Inode and updating block allocation bitmaps), the file system writes the intended transaction to a sequential on-disk Journal log. If power fails mid-write, the OS replays the journal on reboot to restore a consistent state instantly without full disk scans (`fsck`)."
                        ]
                    },
                    {
                        "title": "Storage Evolution: HDDs, NAND Flash SSDs & NVMe PCIe",
                        "points": [
                            "Traditional Hard Disk Drives (HDDs) use mechanical spinning magnetic platters and actuator read/write arms. Seeking a random sector takes 5–10 milliseconds (dominated by mechanical seek and rotational latency) — over 100,000 times slower than RAM.",
                            "Solid State Drives (SSDs) use solid-state NAND Flash memory with zero moving parts. NAND flash is organized into Pages (4–16 KB) and Blocks (128–512 Pages). A crucial physical limitation is that Flash pages can be read/written individually, but can only be erased at the Block level.",
                            "The Flash Translation Layer (FTL) in the SSD controller performs wear leveling and garbage collection to evenly distribute writes across flash cells and avoid premature silicon burnout.",
                            "NVMe (Non-Volatile Memory Express) replaced legacy SATA protocols by attaching SSDs directly to PCIe lanes, supporting up to 64,000 parallel I/O queues (with 64,000 commands per queue), fully unlocking multi-gigabyte/sec throughput on modern multi-core CPUs."
                        ]
                    }
                ],
                "trivia": [
                    {
                        "type": "multiple_choice",
                        "question": "What is the primary advantage of Direct Memory Access (DMA) over Programmed I/O?",
                        "options": [
                            "Hardware devices transfer data directly to/from physical RAM without consuming CPU instruction cycles for each byte",
                            "It completely eliminates the need for physical RAM",
                            "It enables mechanical hard drives to spin at infinite RPM",
                            "It encrypts files automatically using quantum cryptography"
                        ],
                        "correct": 0,
                        "explanation": "DMA allows peripherals (like NVMe SSDs and NICs) to transfer bulk data directly into physical RAM over the bus, notifying the CPU via an interrupt only when the complete transfer is done."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "In Unix-like file systems, what information is stored inside an Inode (Index Node)?",
                        "options": [
                            "File size, permissions, ownership, timestamps, and pointers to physical data blocks (but NOT the filename)",
                            "The file's absolute path and the user's password hash",
                            "The entire binary code of the operating system kernel",
                            "The IP address of the remote network server"
                        ],
                        "correct": 0,
                        "explanation": "An Inode stores all metadata for a file (size, timestamps, owner, permissions, block pointers), while the filename itself is stored separately inside the parent directory's entry table."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the function of 'Journaling' in modern file systems (such as ext4, NTFS, and XFS)?",
                        "options": [
                            "Logging metadata changes to a dedicated journal buffer before writing them to disk to ensure instant recovery after sudden crashes",
                            "Recording user keystrokes for debugging software bugs",
                            "Compressing text files into ZIP archives in the background",
                            "Formatting raw SSD sectors every 24 hours"
                        ],
                        "correct": 0,
                        "explanation": "Journaling writes intended disk structure changes to a sequential log before committing them; if a power failure occurs, the journal is replayed upon boot to restore file system consistency in seconds."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is a major physical constraint of NAND Flash memory used in Solid State Drives (SSDs)?",
                        "options": [
                            "Data can be written in Pages, but overwriting requires erasing an entire Block of pages",
                            "It cannot read data faster than a mechanical floppy disk",
                            "It requires liquid nitrogen cooling to function",
                            "It loses all stored data whenever the computer is rebooted"
                        ],
                        "correct": 0,
                        "explanation": "NAND flash can be programmed at the page level (e.g. 4KB), but cannot overwrite in place; an entire multi-megabyte block must be erased before pages within it can be reprogrammed."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What key architectural enhancement did the NVMe (Non-Volatile Memory Express) protocol introduce over legacy SATA AHCI?",
                        "options": [
                            "Direct PCIe lane connection and support for up to 64,000 parallel command queues with 64,000 commands each",
                            "Converting solid-state drives into optical laser discs",
                            "Limiting disk access to a single serialized queue to prevent bus contention",
                            "Executing user-space Python scripts directly on the flash chips"
                        ],
                        "correct": 0,
                        "explanation": "NVMe was designed specifically for flash storage over PCIe, supporting up to 64,000 parallel queues with 64,000 commands per queue (compared to SATA AHCI's single queue of 32 commands)."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What happens when you create a 'Hard Link' to an existing file in Linux?",
                        "options": [
                            "A new directory entry is created that points directly to the existing file's Inode number, incrementing its link count",
                            "A complete duplicate copy of all physical data blocks is written to disk",
                            "A special pointer file is created that stores the text path of the target file",
                            "The target file is converted into an executable binary"
                        ],
                        "correct": 0,
                        "explanation": "A hard link creates an additional directory entry pointing to the same Inode number; both filenames reference the exact same data blocks on disk, and the file is deleted only when the link count reaches 0."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the role of the 'Flash Translation Layer' (FTL) inside an SSD controller?",
                        "options": [
                            "Managing logical-to-physical block mapping, wear leveling, and garbage collection to protect NAND flash cells",
                            "Translating HTML web pages into binary machine code",
                            "Controlling the mechanical rotational speed of the spindle motor",
                            "Encrypting RAM contents before executing CPU context switches"
                        ],
                        "correct": 0,
                        "explanation": "The FTL is the onboard firmware in an SSD that maps logical OS block addresses to physical NAND flash pages, performing out-of-place writes, wear leveling, and garbage collection."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is an Interrupt Service Routine (ISR)?",
                        "options": [
                            "A specialized kernel software handler executed immediately when a specific hardware or software interrupt occurs",
                            "A user-space daemon that cleans temporary cache files",
                            "A hardware circuit that supplies electric current to the CPU socket",
                            "A compiler pass that optimizes arithmetic loops"
                        ],
                        "correct": 0,
                        "explanation": "An ISR is a low-level kernel callback function registered in the Interrupt Descriptor Table (IDT) that runs with high priority to handle events from hardware devices or exceptions."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the primary purpose of the OS 'Page Cache' in Linux when reading and writing files?",
                        "options": [
                            "Caching recently read and written disk blocks in unused physical RAM to provide near-instantaneous I/O speeds",
                            "Storing web browser cookies in encrypted flash sectors",
                            "Preventing unauthorized users from viewing file permissions",
                            "Translating assembly language code into microcode instructions"
                        ],
                        "correct": 0,
                        "explanation": "The Linux Page Cache dynamically uses free physical RAM to hold copies of recently accessed file blocks; subsequent reads hit RAM directly (~100ns) rather than issuing storage requests (~100μs)."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the difference between Polling and Interrupt-Driven I/O?",
                        "options": [
                            "Polling continuously queries the device status in a loop; Interrupts allow the CPU to perform other work until the device signals readiness",
                            "Polling requires DMA hardware, whereas Interrupts do not",
                            "Interrupts can only be generated by keyboard devices",
                            "Polling is executed exclusively inside the CPU arithmetic logic unit"
                        ],
                        "correct": 0,
                        "explanation": "Polling wastes CPU cycles repeatedly checking device status registers; interrupt-driven I/O allows the processor to execute other tasks until the hardware asserts an electrical line when ready."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is 'Memory-Mapped I/O' (MMIO)?",
                        "options": [
                            "A mechanism where hardware peripheral control registers are mapped into the CPU's physical address space and accessed via normal load/store instructions",
                            "Mapping physical hard disk storage directly into optical DVD lasers",
                            "Using virtual memory paging to defragment flash drives",
                            "Converting RAM chips into network routers"
                        ],
                        "correct": 0,
                        "explanation": "With MMIO, peripheral control and data registers are assigned specific physical memory addresses; the CPU interacts with hardware using standard `MOV` load and store instructions."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the function of the `fsync()` system call in software engineering?",
                        "options": [
                            "Flushing all buffered, dirty file data and metadata from the OS Page Cache directly to non-volatile physical storage",
                            "Synchronizing the system clock with an NTP time server",
                            "Re-indexing the search database across all hard drives",
                            "Closing all active TCP socket connections on the machine"
                        ],
                        "correct": 0,
                        "explanation": "`fsync()` forces the operating system to flush all modified in-memory cached pages for a file descriptor directly onto the physical storage medium before returning, ensuring durability for databases."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is a 'Soft Link' (Symbolic Link / Symlink)?",
                        "options": [
                            "A small file containing the textual path of another file or directory that is dynamically resolved by the OS",
                            "A hardware cable connecting the motherboard to the power switch",
                            "A duplicate Inode that shares data blocks with another Inode",
                            "A process thread that executes with low CPU priority"
                        ],
                        "correct": 0,
                        "explanation": "A symbolic link is a special file whose content is simply a path string pointing to another target file or directory; if the target file is deleted, the symlink becomes 'broken' (dangling)."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the primary factor causing traditional HDDs to suffer high latency on random I/O operations?",
                        "options": [
                            "Mechanical seek time (moving the physical actuator arm) and rotational latency (waiting for the platter sector to spin beneath the head)",
                            "The encryption overhead of the SATA bus controller",
                            "The thermal cooling requirements of the spindle motor",
                            "The time needed to translate ASCII file names into binary numbers"
                        ],
                        "correct": 0,
                        "explanation": "HDDs are mechanical devices: moving the physical head arm to the requested track (seek time) and waiting for the magnetic disk to rotate to the sector takes 5–10ms, making random I/O slow."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is 'VFS' (Virtual File System) in the Linux kernel?",
                        "options": [
                            "An abstraction layer that provides a uniform, standard API (`open`, `read`, `write`) across diverse concrete file systems (ext4, XFS, NFS, procfs)",
                            "A virtual machine hypervisor for running Windows inside Linux",
                            "A compression format for creating ISO image files",
                            "A network protocol for downloading kernel patches"
                        ],
                        "correct": 0,
                        "explanation": "The Virtual File System (VFS) defines a standard object-oriented interface (inodes, dentries, files, superblocks) so user applications interact with all file systems identically."
                    }
                ]
            }
        ]
    }

    # -------------------------------------------------------------------------
    # HEBREW COURSE DATASET
    # -------------------------------------------------------------------------
    cs_he = {
        "id": "cs_arch_101_he",
        "type": "academic",
        "icon": "💻",
        "title": "ארכיטקטורת מחשבים ומערכות הפעלה (CS Arch 101)",
        "description": "מדריך מקיף מעקרונות ראשונים למהנדסי תוכנה: כיצד טרנזיסטורים מסיליקון מריצים הוראות, כיצד מדרג הזיכרון מתגבר על 'קיר הזיכרון', וכיצד ליבת מערכת ההפעלה מנהלת זיכרון וירטואלי, תהליכים ומקביליות.",
        "lang": "he",
        "audience": "family",
        "categories": [
            # =================================================================
            # MODULE 1: CPU Architecture & The Instruction Pipeline
            # =================================================================
            {
                "id": "cpu_pipeline_execution",
                "title": "1. ארכיטקטורת מעבדים וצינור ביצוע ההוראות (Pipeline)",
                "description": "מפולסי שעון סיליקון ועד להרצת שפת מכונה: הבנת צינור ה-RISC בן 5 השלבים, חיזוי הסתעפויות וכיצד מעבדים ממקסמים הוראות למחזור שעון (IPC).",
                "cards": [
                    {
                        "title": "ארכיטקטורת פון-נוימן ומחזור ביצוע ההוראה",
                        "figure": {
                            "title": "צינור הוראות קלאסי בן 5 שלבים (5-Stage Pipeline)",
                            "svg": """<svg viewBox="0 0 520 140" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-height:140px;">
  <rect x="10" y="40" width="90" height="55" rx="8" fill="#3b82f6" fill-opacity="0.15" stroke="#3b82f6" stroke-width="2"/>
  <text x="55" y="65" font-size="12" font-weight="bold" fill="#3b82f6" text-anchor="middle">IF</text>
  <text x="55" y="82" font-size="9" fill="currentColor" opacity="0.8" text-anchor="middle">שליפת הוראה</text>

  <path d="M 100 67 L 115 67" stroke="#3b82f6" stroke-width="2"/>

  <rect x="115" y="40" width="90" height="55" rx="8" fill="#6366f1" fill-opacity="0.15" stroke="#6366f1" stroke-width="2"/>
  <text x="160" y="65" font-size="12" font-weight="bold" fill="#6366f1" text-anchor="middle">ID</text>
  <text x="160" y="82" font-size="9" fill="currentColor" opacity="0.8" text-anchor="middle">פענוח / אוגרים</text>

  <path d="M 205 67 L 220 67" stroke="#6366f1" stroke-width="2"/>

  <rect x="220" y="40" width="90" height="55" rx="8" fill="#8b5cf6" fill-opacity="0.15" stroke="#8b5cf6" stroke-width="2"/>
  <text x="265" y="65" font-size="12" font-weight="bold" fill="#8b5cf6" text-anchor="middle">EX</text>
  <text x="265" y="82" font-size="9" fill="currentColor" opacity="0.8" text-anchor="middle">ביצוע ב-ALU</text>

  <path d="M 310 67 L 325 67" stroke="#8b5cf6" stroke-width="2"/>

  <rect x="325" y="40" width="90" height="55" rx="8" fill="#ec4899" fill-opacity="0.15" stroke="#ec4899" stroke-width="2"/>
  <text x="370" y="65" font-size="12" font-weight="bold" fill="#ec4899" text-anchor="middle">MEM</text>
  <text x="370" y="82" font-size="9" fill="currentColor" opacity="0.8" text-anchor="middle">גישה לזיכרון</text>

  <path d="M 415 67 L 430 67" stroke="#ec4899" stroke-width="2"/>

  <rect x="430" y="40" width="80" height="55" rx="8" fill="#10b981" fill-opacity="0.15" stroke="#10b981" stroke-width="2"/>
  <text x="470" y="65" font-size="12" font-weight="bold" fill="#10b981" text-anchor="middle">WB</text>
  <text x="470" y="82" font-size="9" fill="currentColor" opacity="0.8" text-anchor="middle">כתיבה חזרה</text>
</svg>""",
                            "caption": "בצינור ביצוע (Pipeline) בן 5 שלבים, עד 5 הוראות נפרדות מעובדות במקביל בשלבי חומרה שונים בכל מחזור שעון."
                        },
                        "points": [
                            "כל מחשב מודרני מבוסס על ארכיטקטורת פון-נוימן (Von Neumann): יחידת עיבוד מרכזית (CPU) המחוברת לזיכרון אחוד המכיל הן את הוראות התוכנית והן את הנתונים שעליהם היא פועלת.",
                            "המעבד מכיל תאי אחסון פנימיים מהירים במיוחד הנקראים אוגרים (Registers) - כגון מונה התוכנית (Program Counter / PC), מצביע המחסנית (Stack Pointer / %rsp) ואוגרים לשימוש כללי (%rax, %rbx).",
                            "כדי להריץ קוד, המעבד מבצע בלולאה מתמדת את מחזור ההוראה: (1) שליפת ההוראה הבאה מהזיכרון שאליו מצביע מונה התוכנית, (2) פענוח קוד המכונה (Opcode) לאותות בקרה, (3) ביצוע הפעולה החישובית ב-ALU, (4) גישה לזיכרון הנתונים במידת הצורך, ו-(5) כתיבת התוצאה בחזרה לאוגר היעד.",
                            "במקום להמתין 5 מחזורי שעון שלמים לסיום הוראה אחת לפני שמתחילים את הבאה, מהנדסי חומרה פיתחו את צינור ההוראות (Pipeline) - בדומה לפס ייצור במפעל מכוניות. בעוד הוראה מס' 1 נמצאת בשלב הכתיבה לאוגר, הוראה מס' 2 בשלב הזיכרון, מס' 3 בביצוע, מס' 4 בפענוח ומס' 5 בשליפה, ומגיעים לקצב אידיאלי של הוראה אחת שהושלמה בכל מחזור שעון (IPC = 1.0)."
                        ]
                    },
                    {
                        "title": "סיכוני צינור (Hazards) וחיזוי הסתעפויות (Branch Prediction)",
                        "points": [
                            "צינור הוראות פועל ביעילות שיא רק כאשר הוראות זורמות ברצף חלק ללא הפרעה. כאשר הוראה אינה יכולה להתבצע במחזור השעון הבא, נוצר 'סיכון צינור' (Hazard), המאלץ את המעבד להחדיר מחזורי המתנה ריקים (Stall / Bubbles).",
                            "סיכוני נתונים (Data Hazards) מתרחשים כאשר הוראה זקוקה לפלט של הוראה קודמת שטרם הספיקה לכתוב את ערכה חזרה לאוגר. החומרה משתמשת ב'עקיפת נתונים' (Data Forwarding) כדי לנתב את חוט הפלט של ה-ALU ישירות לקלט של ה-ALU בשלב הבא ללא המתנה.",
                            "סיכוני בקרה (Control Hazards) מתרחשים בכל פעם שהמעבד פוגש פקודת תנאי או קפיצה (`if / else`, לולאות, קריאות לפונקציה). מכיוון שתוצאת התנאי מחושבת רק בשלב הביצוע, המעבד אינו יודע מאיזו כתובת לשלוף את ההוראות הבאות.",
                            "כדי למנוע עיכובי ענק, מעבדים מודרניים כוללים מנגנוני חיזוי הסתעפויות (Branch Predictors): טבלאות היסטוריה ומודלים מנחשים האם התנאי יתקיים בדיוק של מעל 95%. אם הניחוש נכון, ההרצה ממשיכה במלוא המהירות; אם הניחוש שגוי, המעבד שוטף ומבטל (Flush) את כל ההוראות שנשלפו בטעות, בעלות של 15–20 מחזורי שעון מבוזבזים."
                        ]
                    },
                    {
                        "title": "ביצוע סופר-סקלארי, מחוץ לסדר (OoO) והרצה ספקולטיבית",
                        "points": [
                            "מעבדים מודרניים עתירי ביצועים (כגון Intel Core, AMD Zen ו-Apple M-Series) הם מעבדים סופר-סקלאריים (Superscalar): הם כוללים מספר יחידות ביצוע מקביליות (מספר יחידות ALU, יחידות וקטוריות ויחידות טעינה/שמירה) ומסוגלים לשלוח ולבצע 4 עד 8 הוראות במקביל בכל מחזור שעון (IPC > 1).",
                            "תוכניות נכתבות כרצף טורי, אך אם הוראה מס' 2 ממתינה לנתונים מזיכרון ה-RAM האיטי, המתנה סדרתית הייתה משביתה את המעבד כולו. מנגנון ביצוע מחוץ לסדר (Out-of-Order Execution / OoO) מנתח את זרם ההוראות, מזהה הוראות עצמאיות בהמשך הקוד (כגון הוראות 5 ו-6), ומריץ אותן מיד על גבי יחידות ALU פנויות.",
                            "כדי לשמור על תקינות מוחלטת, המעבד משתמש בשינוי שמות אוגרים (Register Renaming) ובחוצץ סידור מחדש (Reorder Buffer / ROB). ה-ROB שומר את התוצאות הספקולטיביות ומעדכן את המצב הארכיטקטוני של המחשב אך ורק בסדר התוכנית המקורי, לאחר שכל ההוראות שקדמו להן הסתיימו בהצלחה."
                        ]
                    }
                ],
                "trivia": [
                    {
                        "type": "multiple_choice",
                        "question": "מהי המטרה העיקרית של צינור ביצוע ההוראות (Pipelining) במעבד מודרני?",
                        "options": [
                            "להריץ מספר הוראות במקביל בשלבי חומרה מדורגים כדי להגדיל את תפוקת ההוראות (Throughput)",
                            "לקצר את זמן מחזור השעון הפיזי של גביש הסיליקון",
                            "לבטל לחלוטין את הצורך במערך אוגרים פנימי",
                            "לתרגם שפת מכונה בינארית לשפות תכנות עיליות"
                        ],
                        "correct": 0,
                        "explanation": "צינור ההוראות פועל כפס ייצור במפעל: על ידי חלוקת הביצוע לשלבים מדורגים (שליפה, פענוח, ביצוע, זיכרון, כתיבה), מספר הוראות מעובדות במקביל, במטרה להשלים הוראה אחת בכל מחזור שעון."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מה קורה כאשר מנגנון חיזוי ההסתעפויות (Branch Predictor) מנחש באופן שגוי את תוצאת תנאי ה-'if'?",
                        "options": [
                            "המעבד שוטף ומבטל (Flush) את צינור ההוראות, מוחק את ההוראות הספקולטיביות ומבזבז כ-15–20 מחזורי שעון",
                            "מערכת ההפעלה קורסת מיד עם שגיאת ליבה (Kernel Panic)",
                            "המעבד עוצר את פעולתו לצמיתות עד להגעת פסיקת חומרה חיצונית",
                            "יחידת ה-ALU הופכת את קוטביות השעון כדי לבטל את החישוב"
                        ],
                        "correct": 0,
                        "explanation": "במקרה של חיזוי שגוי, כל העבודה שבוצעה בספקולציה אינה תקפה; המעבד שוטף את הצינור, מאפס את מונה התוכנית לכתובת הנכונה ומתחיל שליפה מחדש, בעלות של כ-15 עד 20 מחזורים."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "איזה רכיב במעבד הפועל מחוץ לסדר (Out-of-Order) מבטיח שהתוצאות יישמרו ויחויבו בדיוק לפי סדר התוכנית המקורי?",
                        "options": [
                            "חוצץ סידור מחדש (Reorder Buffer - ROB)",
                            "יחידת חישוב אריתמטית ולוגית (ALU)",
                            "חוצץ תרגום כתובות וירטואליות (TLB)",
                            "בקר גישה ישירה לזיכרון (DMA)"
                        ],
                        "correct": 0,
                        "explanation": "ה-Reorder Buffer (ROB) עוקב אחר הוראות שבוצעו מחוץ לסדר ומבטיח שעדכון האוגרים והכתיבה לזיכרון יתבצעו אך ורק לפי סדר התוכנית המקורי שכתב המתכנת."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "איזה מנגנון חומרה מאפשר לפלט של שלב הביצוע (ALU) לעבור ישירות כקלט לשלב הביצוע הבא ללא המתנה לכתיבה לאוגרים?",
                        "options": [
                            "עקיפת נתונים (Data Forwarding / Bypassing)",
                            "דפדוף זיכרון וירטואלי (Paging)",
                            "החלפת הקשר (Context Switching)",
                            "ניהול ערוץ אפיק (Bus Mastering)"
                        ],
                        "correct": 0,
                        "explanation": "עקיפת נתונים (Data Forwarding) מחברת את חוטי הפלט של ה-ALU ישירות למרבבי הקלט של שלב הביצוע הבא, ומונעת השבתת צינור עקב תלות בקריאת אוגרים."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מה מאפיין ארכיטקטורת מעבד 'סופר-סקלארית' (Superscalar)?",
                        "options": [
                            "יכולת לשלוח ולבצע מספר הוראות במקביל בכל מחזור שעון בודד על גבי מספר יחידות ביצוע",
                            "הרצת תוכניות ללא צורך בליבת מערכת הפעלה",
                            "הכפלת נפח ה-RAM הפיזי באמצעות דחיסת תוכנה",
                            "עיבוד ישיר של אותות אנלוגיים ללא המרה לבינארי"
                        ],
                        "correct": 0,
                        "explanation": "מעבד סופר-סקלארי כולל מספר יחידות ביצוע חומרתיות מקביליות (כגון מספר יחידות ALU), ומאפשר שליפה וביצוע של יותר מהוראה אחת בכל מחזור שעון (IPC > 1)."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מה תפקידו של אוגר מונה התוכנית (Program Counter / PC / RIP)?",
                        "options": [
                            "להחזיק את כתובת הזיכרון של ההוראה הבאה המיועדת לשליפה וביצוע",
                            "לאחסן את ערך ההחזרה של הפונקציה האחרונה שנקראה",
                            "לספור את סך פולסי השעון החומרתיים מרגע הדלקת המחשב",
                            "לנהל את מפתחות ההצפנה של מנגנון ה-Secure Boot"
                        ],
                        "correct": 0,
                        "explanation": "אוגר מונה התוכנית (PC) שומר תמיד את כתובת הזיכרון שממנה ישלוף המעבד את ההוראה הבאה במחזור הביצוע."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מדוע מהנדסי חומרה משתמשים ב'שינוי שמות אוגרים' (Register Renaming) במעבדים מודרניים?",
                        "options": [
                            "כדי לבטל תלויות נתונים מלאכותיות (WAR ו-WAW) על ידי מיפוי למאגר אוגרים פיזיים רחב בהרבה",
                            "כדי לתרגם שמות משתנים משפת C++ למחרוזות שפת מכונה",
                            "כדי להפחית את מתח החשמל הנצרך על ידי תאי SRAM",
                            "כדי לאפשר לתוכנות במרחב המשתמש לדרוס אוגרי בקרה של הליבה"
                        ],
                        "correct": 0,
                        "explanation": "שינוי שמות אוגרים ממפה באופן דינמי את האוגרים הארכיטקטוניים (למשל 16 אוגרים ב-x86) למאגר פיזי פנימי של מאות אוגרים, ובכך מסיר חסימות מלאכותיות בביצוע מקבילי."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "בצינור הוראות קלאסי בן 5 שלבים, מה מתרחש במהלך שלב ה-'ID'?",
                        "options": [
                            "פענוח בינארי של ההוראה וקריאת ערכי האופרנדים ממערך האוגרים (Register File)",
                            "כתיבת תוצאות החישוב לזיכרון המטמון L3",
                            "שליפת בייטים של הוראות מקובץ ה-ELF בדיסק",
                            "ביצוע חילוק במספרים בעלי נקודה צפה"
                        ],
                        "correct": 0,
                        "explanation": "בשלב ה-Instruction Decode (ID), יחידת הבקרה מפענחת את קוד הפעולה (Opcode) ושולפת את ערכי האוגרים הדרושים לביצוע החישוב."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהו 'סיכון מבני' (Structural Hazard) בצינור ביצוע של מעבד?",
                        "options": [
                            "כאשר שתי הוראות הרצות במקביל בצינור דורשות גישה לאותו משאב חומרה פיזי בו-זמנית",
                            "כאשר הוראה מנסה לגשת לכתובת זיכרון שאינה מוקצית",
                            "כאשר התחממות הסיליקון מאלצת הורדת תדר שעון",
                            "כאשר דרייבר של מערכת ההפעלה קורס עקב מצביע Null"
                        ],
                        "correct": 0,
                        "explanation": "סיכון מבני מתרחש כאשר החומרה אינה מסוגלת לתמוך בכל צירופי ההוראות בו-זמנית (למשל כאשר יש פורט זיכרון יחיד ונדרשת שליפת הוראה וקריאת נתונים באותו מחזור)."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "במה שונה חיזוי הסתעפויות דינמי מחיזוי הסתעפויות סטטי?",
                        "options": [
                            "חיזוי דינמי משתמש בהיסטוריית הביצוע בזמן ריצה כדי לנחש הסתעפויות, בעוד סטטי מסתמך על כללים קבועים מראש",
                            "חיזוי דינמי דורש הידור מחדש של הקוד בזמן ריצה",
                            "חיזוי דינמי פועל אך ורק על הוראות נקודה צפה",
                            "חיזוי סטטי מבוצע בלעדית על ידי מתזמן מערכת ההפעלה"
                        ],
                        "correct": 0,
                        "explanation": "חיזוי סטטי מסתמך על כללים קבועים (כגון הנחה שלולאות אחורה תמיד מתקיימות), בעוד חיזוי דינמי נעזר בטבלאות חומרה המתעדות את התנהגות ההסתעפות בזמן ריצה."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "איזה מדד מייצג את מספר הוראות המכונה הממוצע שמעבד משלים במחזור שעון בודד?",
                        "options": [
                            "הוראות למחזור שעון (Instructions Per Cycle - IPC)",
                            "יחס ריצוד השעון (Clock Jitter Ratio)",
                            "מעטפת הספק תרמי (Thermal Design Power - TDP)",
                            "קנס החטאת מטמון (Cache Miss Penalty)"
                        ],
                        "correct": 0,
                        "explanation": "מדד ה-IPC (הוראות למחזור שעון) מודד את תפוקת המעבד; מעבדים מודרניים הפועלים מחוץ לסדר מגיעים לערכי IPC של 2.0 עד 4.0 במשימות מותאמות."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "איזה מצב מתאר תלות נתונים מסוג 'קריאה לאחר כתיבה' (Read-After-Write / RAW)?",
                        "options": [
                            "הוראה זקוקה לערך קלט המיוצר על ידי הוראה קודמת שטרם השלימה את חישובה",
                            "הוראה כותבת לזיכרון לפני שמערכת ההפעלה עלתה",
                            "שני תהליכונים כותבים לאותה שורת מטמון ללא נעילות",
                            "התקן היקפי קורא מזיכרון ה-DMA כשהמעבד כבוי"
                        ],
                        "correct": 0,
                        "explanation": "תלות RAW היא תלות נתונים אמיתית שבה הוראה שנייה קוראת ערך שנכתב על ידי הוראה ראשונה; ההוראה השנייה אינה יכולה להמשיך עד שפלט ההוראה הראשונה מוכן."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהו תפקידה המרכזי של יחידת ה-ALU (יחידת חישוב אריתמטית ולוגית)?",
                        "options": [
                            "ביצוע פעולות חישוב בסיסיות על מספרים שלמים (חיבור, חיסור) ופעולות לוגיות סיביתיות (AND, OR, XOR)",
                            "תרגום כתובות וירטואליות לכתובות פיזיות ב-RAM",
                            "ניהול חלוקת אות השעון על גבי לוח האם",
                            "תזמון תהליכוני תוכנה בין ליבות המעבד השונות"
                        ],
                        "correct": 0,
                        "explanation": "ה-ALU הוא המעגל החישובי המרכזי במעבד המבצע את כל פעולות החשבון במספרים שלמים, השוואות ופעולות מניפולציה על סיביות."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהו 'צוואר הבקבוק של פון-נוימן' (Von Neumann Bottleneck)?",
                        "options": [
                            "מגבלת התפוקה הנובעת משיתוף אפיק נתונים יחיד בין שליפת הוראות להעברת נתונים בין הזיכרון למעבד",
                            "ההתנגדות החשמלית של מוליכי נחושת בטמפרטורות גבוהות",
                            "חוסר היכולת של מעבדי RISC לבצע הוראות באורך משתנה",
                            "זמן ההשהיה הנוצר בעת החלפת הקשר בליבת מערכת ההפעלה"
                        ],
                        "correct": 0,
                        "explanation": "צוואר הבקבוק של פון-נוימן נובע מכך שהוראות ונתונים חולקים את אותו ערוץ תקשורת אל הזיכרון הראשי, מה שמגביל את מהירות העיבוד לרוחב הפס של האפיק."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהי המשמעות של 'הרצה ספקולטיבית' (Speculative Execution) בארכיטקטורת מחשבים?",
                        "options": [
                            "הרצת הוראות לאורך נתיב שנחזה מראש, עוד בטרם ידוע בוודאות האם נתיב זה אכן ייבחר בפועל",
                            "העלאת מתח המעבד בניסיון לבדוק את יציבות הסיליקון המרבית",
                            "הרצת קוד משתמש לא מאובטח בתוך מכונה וירטואלית מבודדת",
                            "דחיסת קוד מכונה בזיכרון הראשי לפני הרצתו"
                        ],
                        "correct": 0,
                        "explanation": "הרצה ספקולטיבית היא טכניקה שבה המעבד מנחש את כיוון ההסתעפות ומריץ מראש את ההוראות; אם הניחוש התברר כנכון, זמן ההמתנה נחסך, ואם שגוי – התוצאות מבוטלות."
                    }
                ]
            },

            # =================================================================
            # MODULE 2: Memory Hierarchy & Cache Coherence
            # =================================================================
            {
                "id": "memory_hierarchy_caching",
                "title": "2. מדרג הזיכרון ועקביות זיכרון מטמון (Cache Coherence)",
                "description": "התגברות על 'קיר הזיכרון': הבנת זיכרונות מטמון L1/L2/L3, מקומיות מרחבית וזמנית, שורות מטמון (Cache Lines), ופרוטוקול עקביות הזיכרון MESI במעבדים מרובי ליבות.",
                "cards": [
                    {
                        "title": "קיר הזיכרון ופירמידת מדרג הזיכרון",
                        "figure": {
                            "title": "פער ההשהיה: מאוגרי המעבד ועד לזיכרון הראשי",
                            "svg": """<svg viewBox="0 0 520 150" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-height:150px;">
  <polygon points="260,10 320,40 200,40" fill="#ef4444" fill-opacity="0.2" stroke="#ef4444" stroke-width="1.5"/>
  <text x="260" y="32" font-size="10" font-weight="bold" fill="#ef4444" text-anchor="middle">אוגרים (&lt;1ns)</text>

  <polygon points="200,42 320,42 360,72 160,72" fill="#f59e0b" fill-opacity="0.2" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="260" y="62" font-size="10" font-weight="bold" fill="#f59e0b" text-anchor="middle">מטמון L1 / L2 (1–4ns)</text>

  <polygon points="160,74 360,74 400,104 120,104" fill="#3b82f6" fill-opacity="0.2" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="260" y="94" font-size="10" font-weight="bold" fill="#3b82f6" text-anchor="middle">מטמון משותף L3 (10–20ns)</text>

  <polygon points="120,106 400,106 450,136 70,136" fill="#10b981" fill-opacity="0.2" stroke="#10b981" stroke-width="1.5"/>
  <text x="260" y="126" font-size="10" font-weight="bold" fill="#10b981" text-anchor="middle">זיכרון ראשי DRAM (50–100ns)</text>
</svg>""",
                            "caption": "זיכרונות מטמון סטטיים (SRAM) קטנים ומהירים יושבים ישירות על שבב המעבד כדי לגשר על פער של מאות מחזורי שעון מול זיכרון ה-DRAM הראשי."
                        },
                        "points": [
                            "בשנת 1980, מהירות השעון של המעבדים וזמן הגישה לזיכרון הראשי היו מתואמים למדי. בארבעת העשורים שלאחר מכן, כוח העיבוד של ה-CPU זינק באופן מעריכי, בעוד שזמן ההשהיה של זיכרון ה-DRAM השתפר באיטיות רבה. פער ביצועים אדיר זה ידוע בשם 'קיר הזיכרון' (Memory Wall).",
                            "מעבד מודרני מריץ הוראה בפחות מ-0.3 ננו-שניות, אך שליפת נתון מזיכרון ה-DRAM הראשי אורכת 50 עד 80 ננו-שניות - נצח של 200+ מחזורי שעון מבוזבזים שבהם הליבה מושבתת בהמתנה.",
                            "כדי לפתור זאת, מהנדסים מארגנים את הזיכרון במדרג היררכי המבוסס על SRAM (זיכרון סטטי): זיכרונות מטמון זעירים, יקרים ומהירים ביותר הבנויים ישירות על גבי שבב הסיליקון לצד יחידות הביצוע.",
                            "מטמון L1 הוא פרטי לכל ליבה ומחולק להוראות ונתונים (32–64 KB, זמן גישה כ-1ns). מטמון L2 גדול יותר (512 KB–1 MB לליבה, ~3–4ns). מטמון L3 משותף לכל הליבות על השבב (16–64+ MB, ~10–15ns), ומגובה על ידי זיכרון ה-DRAM הראשי."
                        ]
                    },
                    {
                        "title": "עקרון המקומיות (Locality) ושורות מטמון (Cache Lines)",
                        "points": [
                            "זיכרונות מטמון פועלים ביעילות תודות לעקרון המקומיות: תוכניות מחשב אינן ניגשות לזיכרון בצורה אקראית, אלא מפגינות שני דפוסי התנהגות מובהקים.",
                            "מקומיות זמנית (Temporal Locality): אם התבצעה גישה לכתובת זיכרון מסוימת, סביר מאוד שייגשו אליה שוב בזמן הקרוב (למשל משתני לולאה, סכומי צבירה ופונקציות הנקראות בתדירות גבוהה).",
                            "מקומיות מרחבית (Spatial Locality): אם התבצעה גישה לכתובת זיכרון מסוימת, סביר מאוד שייגשו לכתובות זיכרון הסמוכות לה פיזית בזמן הקרוב (למשל איברי מערך עוקבים ושדות של מבנה נתונים).",
                            "בשל המקומיות המרחבית, המעבד לעולם אינו קורא בייט בודד מ-RAM; הוא תמיד טוען בלוק רציף הנקרא שורת מטמון (Cache Line - תמיד 64 בייטים בארכיטקטורות x86 ו-ARM מודרניות). מעבר סדרתי על מערך בזיכרון מייצר החטאת מטמון אחת ואחריה 15 פגיעות מטמון רצופות עבור שלמים של 4 בייטים!"
                        ]
                    },
                    {
                        "title": "אסוציאטיביות, שיתוף כוזב (False Sharing) ועקביות MESI",
                        "points": [
                            "זיכרונות מטמון מאורגנים בסטים (Sets). במטמון Direct-Mapped, כל כתובת בזיכרון יכולה להתמקם במיקום יחיד (שיעור התנגשויות גבוה). מעבדים מודרניים משתמשים במטמון אסוציאטיבי (Set-Associative Cache - למשל 8-Way או 16-Way), המאפשר לכתובת להתמקם בכל אחד מ-$N$ המקומות בסט המוקצה לה, ובכך מצמצם התנגשויות באופן דרמטי.",
                            "כאשר לליבות מרובות יש עותקים של אותה כתובת זיכרון במטמוני L1/L2 הפרטיים שלהן, כתיבה על ידי ליבה אחת חייבת להסתנכרן. פרוטוקול MESI שומר על עקביות זיכרון בחומרה באמצעות 4 מצבים: Modified (עודכן, קיים רק במטמון זה), Exclusive (נקי, קיים רק במטמון זה), Shared (נקי, משותף למספר מטמונים), ו-Invalid (נתונים מיושנים ולא תקפים).",
                            "שיתוף כוזב (False Sharing) מתרחש כאשר שני תהליכונים הרצים על ליבות נפרדות מעדכנים משתנים עצמאיים לחלוטין שבמקרה יושבים על אותה שורת מטמון בת 64 בייטים. פרוטוקול MESI פוסל שוב ושוב את שורת המטמון ומקפיץ אותה בין הליבות על גבי אפיק התקשורת, מה שגורם להאטה קשה בביצועים."
                        ]
                    }
                ],
                "trivia": [
                    {
                        "type": "multiple_choice",
                        "question": "מהו הגודל האופייני של שורת מטמון (Cache Line) במעבדי x86 ו-ARM מודרניים?",
                        "options": [
                            "64 בייטים",
                            "4 קילובייטים",
                            "8 סיביות",
                            "1 מגה-בייט"
                        ],
                        "correct": 0,
                        "explanation": "במרבית מעבדי x86-64 ו-ARM המודרניים, שורת המטמון הבסיסית היא בגודל 64 בייטים, ומהווה את יחידת הנתונים המינימלית המועברת בין ה-RAM למטמון."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "איזה עקרון מסביר מדוע גישה לאיבר אחד במערך הופכת את הגישה לאיברים הסמוכים לו למהירה בהרבה?",
                        "options": [
                            "מקומיות מרחבית (Spatial Locality)",
                            "מקומיות זמנית (Temporal Locality)",
                            "תרגום וירטואלי (Virtual Translation)",
                            "מקביליות ברמת הוראות (ILP)"
                        ],
                        "correct": 0,
                        "explanation": "מקומיות מרחבית קובעת שגישה לכתובת מסוימת מעידה על סבירות גבוהה לגישה לכתובות סמוכות; טעינת שורת מטמון מלאה בת 64 בייטים מביאה את האיברים הסמוכים ישירות למטמון L1."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהו 'שיתוף כוזב' (False Sharing) בתכנות מרובה תהליכונים?",
                        "options": [
                            "מצב שבו משתנים בלתי תלויים הנקראים/נכתבים על ידי תהליכונים שונים חולקים את אותה שורת מטמון בת 64 בייטים, מה שגורם לפסילות מטמון תכופות",
                            "כאשר שני תהליכים מנסים להאזין לאותו פורט רשת TCP בו-זמנית",
                            "כאשר דפי זיכרון וירטואלי חולקים את אותה מסגרת פיזית ללא הרשאות",
                            "כאשר תהליכון משחרר נעילת Mutex השייכת לתהליכון אחר"
                        ],
                        "correct": 0,
                        "explanation": "שיתוף כוזב מתרחש כאשר ליבות נפרדות מעדכנות משתנים עצמאיים הממוקמים באותה שורת מטמון (64 בייטים); פרוטוקול MESI נאלץ להקפיץ ולפסול את השורה בין הליבות שוב ושוב."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "בפרוטוקול עקביות המטמון MESI, מה מסמל המצב 'M' (Modified)?",
                        "options": [
                            "שורת המטמון קיימת אך ורק במטמון הנוכחי, שונתה (Dirty), ושונה מהתוכן בזיכרון הראשי",
                            "שורת המטמון משותפת לקריאה בלבד לכל הליבות במעבד",
                            "שורת המטמון סומנה למחיקה על ידי מנגנון איסוף הזבל",
                            "שורת המטמון ממופה לאזור החלפת הזיכרון (Swap) בדיסק"
                        ],
                        "correct": 0,
                        "explanation": "בפרוטוקול MESI, מצב 'Modified' מציין שהשורה קיימת אך ורק במטמון המקומי של הליבה שביצעה את הכתיבה, וטרם סונכרנה ונכתבה חזרה ל-RAM."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהו ההבדל המרכזי בין זיכרון סטטי (SRAM) המשמש במטמון לזיכרון דינמי (DRAM) המשמש ב-RAM הראשי?",
                        "options": [
                            "SRAM מהיר במיוחד (~1ns) אך יקר וגדול שטחית (6 טרנזיסטורים לביט); DRAM איטי יותר (~60ns) אך דחוס וזול (טרנזיסטור + קבל לביט)",
                            "SRAM דורש רענון חשמלי מתמיד, בעוד DRAM שומר נתונים ללא מתח",
                            "SRAM מסוגל לשמור אך ורק הוראות לקריאה בלבד, בעוד DRAM שומר נתוני קריאה-כתיבה",
                            "SRAM מתחבר דרך אפיק PCIe, בעוד DRAM מחובר ישירות ל-ALU"
                        ],
                        "correct": 0,
                        "explanation": "SRAM בנוי ממעגל נעילה בן 6 טרנזיסטורים המאפשר גישה מהירה במיוחד ללא צורך במחזורי רענון, בעוד DRAM משתמש בקבל זעיר המאפשר דחיסות זיכרון גבוהה במחיר מהירות נמוכה יותר."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהו זיכרון מטמון 'N-way Set-Associative'?",
                        "options": [
                            "מטמון שבו כל כתובת בזיכרון יכולה להתמקם בכל אחד מ-N מקומות שונים בתוך הסט (Set) המיועד לה",
                            "מטמון המתחבר במקביל ל-N לוחות אם שונים",
                            "מטמון הדוחס נתונים בפקטור של N בחומרה בזמן אמת",
                            "מטמון המחלק כל שורת 64 בייטים ל-N חלקים שווים"
                        ],
                        "correct": 0,
                        "explanation": "מטמון N-way Set-Associative מחלק את המטמון לסטים של N שורות; כתובת זיכרון ממפה לסט מסוים ויכולה להתאחסן בכל אחד מ-N המקומות באותו סט, מה שמצמצם התנגשויות."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מדוע סריקת מטריצה דו-ממדית שורה-אחר-שורה בשפת C מהירה משמעותית מסריקה עמודה-אחר-עמודה?",
                        "options": [
                            "שפת C שומרת מטריצות בסדר שורות (Row-Major), מה שממקסם מקומיות מרחבית ופגיעות שורת מטמון",
                            "סריקת עמודות משביתה את צינור ביצוע ההוראות במעבד",
                            "סריקת שורות מבוצעת בחומרת הנקודה הצפה במקום ב-ALU",
                            "המהדר מתרגם סריקת עמודות לפונקציות רקורסיביות כבדות"
                        ],
                        "correct": 0,
                        "explanation": "מטריצות ב-C מסודרות ברצף לפי שורות; מעבר שורה-אחר-שורה ניגש לבייטים עוקבים בזיכרון (מקומיות מרחבית), בעוד סריקת עמודות קופצת במרחקים הגדולים מ-64 בייטים וגורמת להחטאת מטמון כמעט בכל איבר."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהו ההבדל בין מדיניות כתיבה 'Write-Through' לבין 'Write-Back' במטמון?",
                        "options": [
                            "Write-Through כותב מיד את השינוי גם לזיכרון הראשי; Write-Back מעדכן רק את המטמון וכותב ל-RAM רק כשהשורה מפונה",
                            "Write-Through מיועד לקריאה בלבד; Write-Back מיועד לכתיבה בלבד",
                            "Write-Through מיושם אך ורק בזיכרון כרטיסי מסך (VRAM)",
                            "Write-Back עוקף לחלוטין את מדרג המטמון של המעבד"
                        ],
                        "correct": 0,
                        "explanation": "Write-Through מעדכן את הזיכרון הראשי במקביל לכל כתיבה במטמון; Write-Back מעדכן רק את המטמון ומסמן את השורה כ-Dirty, ודוחה את הכתיבה ל-RAM עד לרגע שבו השורה מפונה."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מה מתאר המונח 'קיר הזיכרון' (The Memory Wall)?",
                        "options": [
                            "הפער ההולך וגדל בין מהירות העיבוד של המעבדים לבין זמן ההשהיה האיטי של זיכרון ה-DRAM הראשי",
                            "מגבלת החוק של מור הנובעת מהתחממות טרנזיסטורים",
                            "חוק אמדל המגביל ביצועים במעבדים מרובי ליבות",
                            "קנס ההשהיה הנובע משטיפת צינור ההוראות"
                        ],
                        "correct": 0,
                        "explanation": "'קיר הזיכרון' מתאר את הפער ההיסטורי שנוצר כאשר מהירות המעבדים גדלה במהירות עצומה בעוד מהירות הגישה ל-DRAM השתפרה לאט, מה שהפך את המטמון לרכיב קריטי לביצועים."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מה מתרחש כאשר המעבד נתקל ב'החטאת מטמון' (Cache Miss)?",
                        "options": [
                            "המעבד מושהה ונאלץ להמתין לשליפת בלוק הנתונים בן 64 הבייטים ממטמון עמוק יותר או מזיכרון ה-DRAM הראשי",
                            "מערכת ההפעלה סוגרת את התוכנית בשגיאת חריגת זיכרון",
                            "המעבד מרוקן את כל נתוני הדיסק הקשיח למחיצות פלאש",
                            "ה-BIOS מאתחל את בקר החשמל של לוח האם"
                        ],
                        "correct": 0,
                        "explanation": "בעת החטאת מטמון, הנתון המבוקש אינו נמצא ברמת המטמון הנוכחית; המעבד פונה לרמת המטמון הבאה או ל-RAM, וסופג עונש השהיה של עשרות עד מאות מחזורי שעון."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "בפרוטוקול MESI, לאיזה מצב תעבור שורת מטמון מקומית כאשר ליבה אחרת מבצעת כתיבה לאותה כתובת זיכרון?",
                        "options": [
                            "פסול (Invalid - I)",
                            "משותף (Shared - S)",
                            "בלעדי (Exclusive - E)",
                            "שונה (Modified - M)"
                        ],
                        "correct": 0,
                        "explanation": "כאשר ליבה אחת משדרת באפיק שהיא כותבת לשורה משותפת, כל שאר הליבות המחזיקות עותק של אותה שורה מעבירות אותו למצב 'Invalid' כדי לא לקרוא נתונים ישנים."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "איזו מדיניות פינוי מטמון מוציאה את השורה שלא נעשה בה שימוש במשך פרק הזמן הארוך ביותר?",
                        "options": [
                            "הכי פחות בשימוש לאחרונה (Least Recently Used - LRU)",
                            "נכנס ראשון יוצא ראשון (FIFO)",
                            "פינוי אקראי (Random Replacement)",
                            "הכי בשימוש תדיר (Most Frequently Used - MFU)"
                        ],
                        "correct": 0,
                        "explanation": "אלגוריתם LRU עוקב אחר מועד הגישה האחרון לכל שורת מטמון ומפנה את השורה שעבר הזמן הרב ביותר מאז שניגשו אליה, בהתבסס על עקרון המקומיות הזמנית."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מה תפקידו של מנגנון ה-'Hardware Prefetcher' בבקר הזיכרון של המעבד?",
                        "options": [
                            "לזהות דפוסי גישה סדרתיים בזיכרון ולטעון מראש שורות מטמון עתידיות עוד בטרם התבקשו על ידי הקוד",
                            "להדר קבצי קוד מקור לקבצים בינאריים בעת עליית המחשב",
                            "לטעון קבלים בזיכרון ה-DRAM לפני אתחול קר",
                            "לבצע איחוי (Defragmentation) לדיסק הקשיח ברקע"
                        ],
                        "correct": 0,
                        "explanation": "ה-Hardware Prefetcher עוקב אחר כתובות הגישה; כאשר הוא מזהה צעדים קבועים (כגון סריקת מערך), הוא מושך מראש שורות מטמון מ-RAM כדי להעלים את זמן ההשהיה."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהו היתרון המרכזי של מדרג מטמון מכיל (Inclusive Cache - למשל L3 המכיל את L1/L2)?",
                        "options": [
                            "בדיקה אם ליבה אחרת מחזיקה בשורת מטמון יכולה להתבצע בסריקת תגיות L3 בלבד, מבלי להפריע למטמוני L1/L2 הפרטיים",
                            "הכפלת קיבולת האחסון האפקטיבית של שבב הסיליקון",
                            "ביטול מוחלט של הצורך בסיביות תג ואינדקס במטמון",
                            "אפשרות למטמון L1 לשמור כמות אינסופית של שורות"
                        ],
                        "correct": 0,
                        "explanation": "במדרג מכיל, כל נתון ב-L1/L2 מובטח שיהיה קיים גם ב-L3; בדיקות עקביות בין ליבות מבוצעות מול תגיות L3 בלבד, מה שחוסך תעבורה באפיקי הליבות הפנימיים."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "איזו רמת זיכרון מטמון משותפת לרוב לכלל הליבות במעבד מודרני מרובה ליבות?",
                        "options": [
                            "מטמון רמה 3 (L3 Cache / Last Level Cache)",
                            "מטמון הוראות רמה 1 (L1 Instruction)",
                            "מטמון נתונים רמה 1 (L1 Data)",
                            "מערך האוגרים (Register File)"
                        ],
                        "correct": 0,
                        "explanation": "בעוד שמטמוני L1 ו-L2 הם בדרך כלל פרטיים לכל ליבה, מטמון L3 (הנקרא גם Last Level Cache / LLC) הוא אחוד ומשותף לכל הליבות על השבב."
                    }
                ]
            },

            # =================================================================
            # MODULE 3: Virtual Memory, Paging & The MMU
            # =================================================================
            {
                "id": "virtual_memory_paging",
                "title": "3. זיכרון וירטואלי, דפדוף (Paging) ויחידת ה-MMU",
                "description": "כיצד מערכות הפעלה מספקות בידוד זיכרון, תרגום כתובות באמצעות טבלאות דפים, חוצץ תרגום מהיר (TLB), שגיאות דף (Page Faults), ודפדוף לפי דרישה.",
                "cards": [
                    {
                        "title": "מדוע זיכרון וירטואלי? בידוד ואשליית זיכרון אינסופי",
                        "figure": {
                            "title": "זרימת תרגום כתובת וירטואלית לכתובת פיזית ב-RAM",
                            "svg": """<svg viewBox="0 0 520 140" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-height:140px;">
  <rect x="20" y="45" width="130" height="50" rx="8" fill="#3b82f6" fill-opacity="0.15" stroke="#3b82f6" stroke-width="2"/>
  <text x="85" y="67" font-size="11" font-weight="bold" fill="#3b82f6" text-anchor="middle">כתובת וירטואלית</text>
  <text x="85" y="83" font-size="9" fill="currentColor" opacity="0.8" text-anchor="middle">VPN + היסט (Offset)</text>

  <path d="M 150 70 L 195 70" stroke="#3b82f6" stroke-width="2"/>

  <rect x="195" y="35" width="130" height="70" rx="8" fill="#8b5cf6" fill-opacity="0.15" stroke="#8b5cf6" stroke-width="2"/>
  <text x="260" y="60" font-size="12" font-weight="bold" fill="#8b5cf6" text-anchor="middle">MMU / TLB</text>
  <text x="260" y="78" font-size="9" fill="currentColor" opacity="0.8" text-anchor="middle">חיפוש חומרתי מהיר</text>
  <text x="260" y="92" font-size="9" fill="#10b981" text-anchor="middle">תרגום טבלת דפים</text>

  <path d="M 325 70 L 370 70" stroke="#10b981" stroke-width="2"/>

  <rect x="370" y="45" width="130" height="50" rx="8" fill="#10b981" fill-opacity="0.15" stroke="#10b981" stroke-width="2"/>
  <text x="435" y="67" font-size="11" font-weight="bold" fill="#10b981" text-anchor="middle">זיכרון פיזי RAM</text>
  <text x="435" y="83" font-size="9" fill="currentColor" opacity="0.8" text-anchor="middle">מסגרת PFN + היסט</text>
</svg>""",
                            "caption": "יחידת ניהול הזיכרון (MMU) נעזרת בטבלאות דפים ובמטמון ה-TLB המהיר כדי לתרגם כתובות וירטואליות למסגרות פיזיות ב-RAM בזמן אמת."
                        },
                        "points": [
                            "בראשית ימי המחשוב, תוכניות רצו ישירות על כתובות זיכרון פיזיות: אם תוכנית א' כתבה בטעות לכתובת `0x1000`, היא יכלה לדרוס את תוכנית ב' או להפיל את מערכת ההפעלה כולה.",
                            "מנגנון הזיכרון הווירטואלי פותר זאת על ידי הענקת מרחב כתובות וירטואלי פרטי ומבודד לחלוטין לכל תהליך (128 טרה-בייט ב-x86-64). מבחינת התהליך, הוא היחיד הקיים במחשב וברשותו כל הזיכרון מ-`0x0` ועד סוף המרחב.",
                            "הזיכרון מחולק למקטעים בגודל קבוע הנקראים דפים (Pages - בדרך כלל 4 קילובייט). זיכרון ה-RAM הפיזי מחולק למסגרות דף תואמות (Page Frames).",
                            "מערכת ההפעלה מנהלת טבלת דפים (Page Table) עבור כל תהליך. כאשר התוכנית ניגשת לכתובת וירטואלית, יחידת החומרה לניהול זיכרון (MMU) מתרגמת את מספר הדף הווירטואלי (VPN) למספר המסגרת הפיזית (PFN) ב-RAM."
                        ]
                    },
                    {
                        "title": "חוצץ תרגום מהיר (TLB) וטבלאות דפים מרובות רמות",
                        "points": [
                            "במערכות 64-ביט, טבלת דפים שטוחה יחידה הייתה דורשת מיליוני גיגה-בייט של RAM רק כדי להחזיק את המיפויים. מערכות הפעלה מודרניות משתמשות בטבלאות דפים היררכיות בנות 4 או 5 רמות (PML4 -> PDPT -> PD -> PT ב-x86), ויוצרות טבלאות משנה אך ורק עבור כתובות שהתהליך באמת משתמש בהן.",
                            "מעבר על עץ טבלת דפים בן 4 רמות דורש 4 קריאות זיכרון נפרדות מ-RAM רק כדי לתרגם מצביע בודד - מה שהיה מאט את הגישה לזיכרון ב-400%!",
                            "כדי להפוך את התרגום למיידי, המעבד כולל זיכרון מטמון חומרתי אסוציאטיבי מהיר במיוחד הנקרא Translation Lookaside Buffer (TLB). ה-TLB שומר תרגומים אחרונים של VPN -> PFN.",
                            "פגיעת TLB מתורגמת בפחות ממחזור שעון יחיד (~0.5ns). החטאת TLB מאלצת את חומרת ה-MMU לסרוק את טבלאות הדפים ב-RAM, בעלות של 30–50 ננו-שניות."
                        ]
                    },
                    {
                        "title": "שגיאות דף (Page Faults), דפדוף לפי דרישה והגנות זיכרון",
                        "points": [
                            "כל רשומת דף בטבלה (PTE) כוללת ביטים של סטטוס והרשאות: Present (קיים ב-RAM פיזי), Read/Write (קריאה/כתיבה), User/Supervisor (משתמש לעומת ליבה), ו-NX (No-Execute - איסור הרצה למניעת פריצות אבטחה).",
                            "אם תהליך ניגש לכתובת שבה ביט ה-Present הוא 0, חומרת ה-MMU מפעילה פסיקה הנקראת שגיאת דף (Page Fault). המעבד עוצר מיד את קוד המשתמש ומעביר שליטה למטפל שגיאות הדף של ליבת מערכת ההפעלה.",
                            "דפדוף לפי דרישה (Demand Paging): אם הדף שמור בקובץ ה-Swap בדיסק או ממופה מקובץ (`mmap`), הליבה מקצה מסגרת RAM, טוענת את ה-4KB מהאחסון, מעדכנת Present = 1, ומחדשת את הרצת התוכנית בשקיפות מלאה.",
                            "שגיאת חריגת מקטע (Segmentation Fault / SIGSEGV): אם התהליך ביצע פעולה בלתי חוקית (ניסיון כתיבה לקוד קריאה בלבד או גישה לכתובת לא מוקצית), הליבה שולחת אות סגירה ומפילה את התוכנית."
                        ]
                    }
                ],
                "trivia": [
                    {
                        "type": "multiple_choice",
                        "question": "מהו גודל דף הזיכרון הבסיסי הסטנדרטי במערכות הפעלה מודרניות ב-x86-64 ו-ARM?",
                        "options": [
                            "4 קילובייטים (4096 בייטים)",
                            "64 בייטים",
                            "1 מגה-בייט",
                            "512 בייטים"
                        ],
                        "correct": 0,
                        "explanation": "4 קילובייט (4,096 בייטים) הוא גודל הדף הבסיסי הסטנדרטי להקצאת זיכרון וירטואלי וניהול מסגרות דף ב-RAM."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהו תפקידו העיקרי של חוצץ ה-TLB (Translation Lookaside Buffer)?",
                        "options": [
                            "לשמור במטמון חומרתי תרגומים מכתובת וירטואלית לפיזית כדי למנוע סריקות חוזרות של טבלאות דפים ב-RAM",
                            "לתרגם בייטקוד של שפת פייתון להוראות מכונה",
                            "לאגור חבילות רשת לפני שליחתן לכרטיס הרשת",
                            "לשמור גיבוי של אוגרי המעבד בעת הפסקת חשמל"
                        ],
                        "correct": 0,
                        "explanation": "ה-TLB הוא זיכרון מטמון מהיר במיוחד בתוך המעבד השומר את תרגומי הכתובות הווירטואליות לפיזיות האחרונים, ומאפשר תרגום במחזור שעון בודד."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "איזה אירוע חומרה מתרחש כאשר תהליך מנסה לגשת לדף זיכרון וירטואלי שאינו טעון כרגע ב-RAM הפיזי?",
                        "options": [
                            "נזרקת שגיאת דף (Page Fault) המעבירה את השליטה לטיפול ליבת מערכת ההפעלה",
                            "המעבד מאתחל מיד את לוח האם",
                            "ה-ALU מחזיר מספר אקראי של 64 ביט ללא שגיאה",
                            "הדיסק הקשיח מפעיל קריסת ליבה מוחלטת"
                        ],
                        "correct": 0,
                        "explanation": "כאשר ביט ה-Present ברשומת הדף הוא 0, ה-MMU מייצר פסיקת Page Fault; ליבת מערכת ההפעלה טוענת את הדף מהדיסק ל-RAM (Demand Paging) וממשיכה בהרצה."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "איזה מנגנון אבטחה מסמן מקטעי זיכרון (כגון המחסנית וה-Heap) כבלתי ניתנים להרצה כדי למנוע הזרקת קוד זדוני?",
                        "options": [
                            "סיבית ה-NX (No-Execute) / XD (Execute Disable)",
                            "סיבית ה-Dirty",
                            "מונה חותמת הזמן של הגישה",
                            "אוגר בדיקת הזוגיות (Parity Check)"
                        ],
                        "correct": 0,
                        "explanation": "סיבית ה-NX/XD ברשומת טבלת הדפים מאפשרת למערכת ההפעלה לקבוע שדפי נתונים לא יורצו כקוד; ניסיון להריץ פקודות מתוכם גורם להפלת התוכנית מיד."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מדוע מערכות הפעלה מודרניות של 64-ביט משתמשות בטבלאות דפים מרובות רמות במקום בטבלה שטוחה יחידה?",
                        "options": [
                            "כדי לחסוך כמויות עצומות של RAM על ידי הקצאת מבני טבלאות דפים רק עבור אזורי כתובות שנמצאים בשימוש בפועל",
                            "כדי לתרגם כתובות במהירות גבוהה פי 10 מטבלה שטוחה",
                            "כדי לבטל לחלוטין את הצורך ברכיבי DRAM פיזיים",
                            "כדי לאפשר למעבדי 32-ביט להריץ הוראות 64-ביט"
                        ],
                        "correct": 0,
                        "explanation": "טבלה שטוחה ב-64-ביט הייתה דורשת טרה-בייטים של זיכרון לכל תהליך; עץ רב-שלבי מקצה רמות נמוכות אך ורק עבור מרחבי כתובות שבאמת הוקצו על ידי התוכנית."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהו 'דפדוף לפי דרישה' (Demand Paging) במערכת הפעלה?",
                        "options": [
                            "טכניקה שבה דפי זיכרון נטענים ל-RAM הפיזי רק ברגע שהתוכנית מנסה לגשת אליהם בפועל",
                            "טעינה של כל הקובץ הבינארי וספריותיו ל-RAM כבר בעת ההפעלה",
                            "דרישה מתוכנת המשתמש לבצע קריאת מערכת להקצאת כל בייט",
                            "דחיסה של דפי זיכרון שאינם בשימוש לאחסון פלאש"
                        ],
                        "correct": 0,
                        "explanation": "דפדוף לפי דרישה דוחה את טעינת הדפים מהאחסון ל-RAM עד לרגע שבו התוכנית נוגעת בכתובת הרלוונטית, מה שיוצר Page Fault שטוען את ה-4KB הדרושים."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהו היתרון בשימוש בדפי ענק (HugePages - למשל בגודל 2MB או 1GB) בבסיסי נתונים עתירי ביצועים?",
                        "options": [
                            "הפחתה דרמטית בכמות רשומות ה-TLB הנדרשות, מה שמעלה את אחוז פגיעות ה-TLB עבור מערכי נתונים ענקיים",
                            "העלאת תדר השעון של אפיק הזיכרון",
                            "אפשור חישובי מספרים שלמים ב-128 ביט במרחב המשתמש",
                            "הצפנת ה-RAM הפיזי כנגד התקפות Cold-Boot"
                        ],
                        "correct": 0,
                        "explanation": "שימוש בדפי 2MB מאפשר לרשומת TLB בודדת לכסות שטח זיכרון הגדול פי 512 מדף רגיל, ובכך מונע החטאות TLB תכופות בבסיסי נתונים ומכונות וירטואליות."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מה מתרחש במהלך 'TLB Shootdown' במערכת הפעלה מרובת ליבות?",
                        "options": [
                            "פסיקה בין-מעבדית (IPI) מאלצת ליבות אחרות לפסול תרגומים ישנים ב-TLB המקומי שלהן כאשר מיפוי דפים משתנה",
                            "המעבד מכבה ליבות שאינן פעילות לצמצום חום",
                            "בקר הזיכרון מוחק את כל תוכן ה-RAM הפיזי",
                            "תהליך משתמש מושמד עקב חריגה ממכסת הזיכרון"
                        ],
                        "correct": 0,
                        "explanation": "כאשר ליבה אחת משנה מיפוי של דף משותף (למשל שחרור זיכרון), היא שולחת פסיקה לשאר הליבות כדי שינקו את המיפוי הישן מה-TLB המקומי שלהן."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "איזה אוגר מעבד ב-x86-64 מחזיק את הכתובת הפיזית של טבלת הדפים הראשית (PML4) של התהליך הנוכחי?",
                        "options": [
                            "אוגר הבקרה CR3",
                            "מצביע המחסנית RSP",
                            "אוגר הדגלים EFLAGS",
                            "מונה התוכנית RIP"
                        ],
                        "correct": 0,
                        "explanation": "אוגר CR3 מצביע על הכתובת הפיזית של טבלת הדפים העליונה של התהליך הפעיל; עדכון CR3 בעת החלפת הקשר מפעיל מיד את מרחב הזיכרון של התהליך החדש."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהי מטרת מנגנון האבטחה ASLR (הגרלת פריסת מרחב הכתובות)?",
                        "options": [
                            "להגריל את כתובות הבסיס של המחסנית, ה-Heap והספריות בכל הפעלה כדי למנוע ניצול של גלישות חוצץ",
                            "לפזר שורות מטמון בצורה אקראית בין בנקי הזיכרון",
                            "לשמור קבצים בדיסק בסדר בלוקים אקראי",
                            "לתזמן תהליכונים בצורה אקראית בין ליבות המעבד"
                        ],
                        "correct": 0,
                        "explanation": "ASLR מגריל את מיקומי הזיכרון של הספריות, המחסנית וה-Heap בכל הרצה של התוכנית, ובכך מונע מתוקפים לנחש כתובות פונקציות בזיכרון."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מה מעידה קבלת שגיאת 'Segmentation Fault' (SIGSEGV) למפתח תוכנה?",
                        "options": [
                            "התוכנית ניסתה לבצע גישה בלתי מורשית לזיכרון וירטואלי (כגון דה-רפרנס למצביע Null או כתיבה לזיכרון קריאה בלבד)",
                            "רכיב ה-RAM הפיזי סבל מכשל חומרתי בטרנזיסטור",
                            "מכפיל השעון של המעבד השתנה במהלך חישוב מתמטי",
                            "נפח האחסון בדיסק הקשיח הגיע ל-100% תפוסה"
                        ],
                        "correct": 0,
                        "explanation": "שגיאת Segmentation Fault מתרחשת כאשר ה-MMU תופס ניסיון גישה לכתובת וירטואלית לא ממופה או הפרת הרשאות (כגון ניסיון כתיבה לקוד שמוגדר לקריאה בלבד)."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהי תופעת ה-'Thrashing' במערכת הפעלה?",
                        "options": [
                            "מצב שבו ה-RAM הפיזי מלא מדי, ומערכת ההפעלה מבזבזת את רוב זמנה בהחלפת דפים לדיסק וממנו במקום להריץ קוד",
                            "מצב שבו שני תהליכונים תופסים במקביל את אותו Spinlock",
                            "השחתה של שורות מטמון עקב קרינה תרמית במעבד",
                            "מצב שבו במערכת הקבצים נגמרו ה-Inodes הפנויים"
                        ],
                        "correct": 0,
                        "explanation": "Thrashing מתרחש כאשר דרישות הזיכרון של התוכניות עולות על ה-RAM הפיזי; המערכת נכנסת ללולאת החלפות דפים בלתי פוסקת מול הדיסק והביצועים קורסים."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מה תפקידה של סיבית ה-'Dirty' ברשומת טבלת הדפים (PTE)?",
                        "options": [
                            "לסמן האם נכתב מידע לדף מאז שנטען לזיכרון ה-RAM הפיזי",
                            "לסמן האם הדף מכיל וירוס או קוד זדוני",
                            "לסמן למעבד שהדף מאוחסן על גבי כונן אופטי",
                            "למחוק את הדף מיד בסיום התהליכון הנוכחי"
                        ],
                        "correct": 0,
                        "explanation": "חומרת ה-MMU מדליקה את סיבית ה-Dirty ל-1 בכל פעם שמתבצעת כתיבה לדף; מערכת ההפעלה בודקת סיבית זו בעת פינוי דף כדי לדעת אם חובה לשמור אותו בדיסק."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהי 'קבוצת העבודה' (Working Set) של תהליך?",
                        "options": [
                            "אוסף דפי הזיכרון הווירטואלי שהתהליך ניגש אליהם בפועל במהלך חלון זמן נתון",
                            "מספר מתארי הקבצים (File Descriptors) הפתוחים של התהליך",
                            "קבוצת הליבות המוקצות להרצת התהליך במעבד",
                            "רשימת הספריות הדינמיות המקושרות לתוכנית"
                        ],
                        "correct": 0,
                        "explanation": "קבוצת העבודה היא אוסף הדפים שהתהליך משתמש בהם באופן פעיל ברגע נתון; אם אין מספיק RAM להחזיק את קבוצות העבודה של כל התהליכים, מתחילה תופעת Thrashing."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "כיצד מנגנון 'העתקה בעת כתיבה' (Copy-on-Write / COW) מייעל את קריאת המערכת `fork()` ביוניקס?",
                        "options": [
                            "תהליך האב והבן חולקים את אותם דפי RAM לקריאה בלבד; דף מועתק פיזית רק כאשר אחד התהליכים מנסה לכתוב אליו",
                            "המערכת מעתיקה מיד את כל נפח ה-RAM של האב למסגרות חדשות",
                            "תהליך הבן רץ ישירות בתוך אוגרי המעבד של האב ללא זיכרון",
                            "בקר הדיסק כותב את זיכרון האב ישירות לקובץ Swap"
                        ],
                        "correct": 0,
                        "explanation": "במקום להעתיק גיגה-בייטים של זיכרון ב-`fork()`, מנגנון COW מסמן את כל הדפים כמשותפים ולקריאה בלבד; שכפול דף ב-RAM מבוצע רק ברגע שאחד הצדדים מבצע כתיבה."
                    }
                ]
            },

            # =================================================================
            # MODULE 4: Processes, Threads & Concurrency
            # =================================================================
            {
                "id": "processes_threads_concurrency",
                "title": "4. תהליכים, תהליכונים, מקביליות וסנכרון",
                "description": "הבנת מרחבי כתובות של תהליכים, מצב ליבה לעומת מצב משתמש (Ring 0 מול Ring 3), החלפות הקשר, תנאי מרוץ (Race Conditions), מנעולי Mutex, Spinlock, Futex ופעולות אטומיות.",
                "cards": [
                    {
                        "title": "תהליכים מול תהליכונים (Threads) והחלפת הקשר",
                        "figure": {
                            "title": "מבנה זיכרון של תהליך מול תהליכונים מרובים",
                            "svg": """<svg viewBox="0 0 520 150" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-height:150px;">
  <rect x="20" y="20" width="220" height="115" rx="8" fill="#3b82f6" fill-opacity="0.1" stroke="#3b82f6" stroke-width="2"/>
  <text x="130" y="40" font-size="11" font-weight="bold" fill="#3b82f6" text-anchor="middle">מרחב זיכרון של תהליך</text>
  <rect x="35" y="55" width="85" height="30" rx="4" fill="#3b82f6" fill-opacity="0.2"/>
  <text x="77" y="74" font-size="9" fill="currentColor" text-anchor="middle">קוד ומשתנים</text>
  <rect x="135" y="55" width="85" height="30" rx="4" fill="#10b981" fill-opacity="0.2"/>
  <text x="177" y="74" font-size="9" fill="currentColor" text-anchor="middle">Heap משותף</text>
  <rect x="35" y="95" width="185" height="28" rx="4" fill="#ec4899" fill-opacity="0.15"/>
  <text x="127" y="113" font-size="9" fill="#ec4899" text-anchor="middle">מתארי קבצים פתוחים</text>

  <rect x="275" y="20" width="225" height="115" rx="8" fill="#8b5cf6" fill-opacity="0.1" stroke="#8b5cf6" stroke-width="2"/>
  <text x="387" y="40" font-size="11" font-weight="bold" fill="#8b5cf6" text-anchor="middle">תהליכונים (יחידות ביצוע)</text>
  <rect x="290" y="55" width="95" height="68" rx="4" fill="#8b5cf6" fill-opacity="0.2"/>
  <text x="337" y="75" font-size="10" font-weight="bold" fill="#8b5cf6" text-anchor="middle">תהליכון 1</text>
  <text x="337" y="92" font-size="8" fill="currentColor" opacity="0.8" text-anchor="middle">מחסנית ו-RSP</text>
  <text x="337" y="106" font-size="8" fill="currentColor" opacity="0.8" text-anchor="middle">אוגרי מעבד</text>

  <rect x="395" y="55" width="95" height="68" rx="4" fill="#8b5cf6" fill-opacity="0.2"/>
  <text x="442" y="75" font-size="10" font-weight="bold" fill="#8b5cf6" text-anchor="middle">תהליכון 2</text>
  <text x="442" y="92" font-size="8" fill="currentColor" opacity="0.8" text-anchor="middle">מחסנית ו-RSP</text>
  <text x="442" y="106" font-size="8" fill="currentColor" opacity="0.8" text-anchor="middle">אוגרי מעבד</text>
</svg>""",
                            "caption": "תהליך מחזיק במרחב כתובות וירטואלי מבודד (קוד, Heap, קבצים); תהליכונים בתוך התהליך חולקים זיכרון זה אך מחזיקים במחסנית ואוגרים פרטיים."
                        },
                        "points": [
                            "תהליך (Process) הוא מופע של תוכנית רצה, המחזיק במרחב כתובות וירטואלי מבודד, זיכרון Heap, מתארי קבצים פתוחים (File Descriptors) והרשאות אבטחה, המנוהלים באמצעות בלוק בקרת תהליך (PCB).",
                            "תהליכון (Thread) הוא יחידת הביצוע הקטנה ביותר המתוזמנת על ידי המעבד. תהליכונים באותו תהליך חולקים את אותו מרחב זיכרון ו-Heap, אך לכל תהליכון יש מחסנית קריאות פרטית (Stack), מצביע מחסנית (%rsp) ומצב אוגרי מעבד משלו.",
                            "החלפת הקשר (Context Switch) מתרחשת כאשר מתזמן מערכת ההפעלה עוצר תהליכון אחד ומעביר את ליבת המעבד להריץ תהליכון אחר. הליבה שומרת את אוגרי המעבד של התהליכון היוצא וטוענת את אוגרי התהליכון הנכנס.",
                            "החלפת הקשר בין תהליכים נפרדים יקרה משמעותית מהחלפה בין תהליכונים באותו תהליך, כיוון שהיא מחייבת כתיבת כתובת טבלת דפים חדשה לאוגר CR3, מה שפוסל את ה-TLB וגורר גל החטאות מטמון."
                        ]
                    },
                    {
                        "title": "מצב ליבה מול מצב משתמש (טבעת 0 מול טבעת 3) וקריאות מערכת",
                        "points": [
                            "מעבדים אוכפים טבעות הרשאה בחומרה: Ring 0 (מצב ליבה / Kernel Mode) נהנה מגישה בלתי מוגבלת לחומרה, לאוגרי בקרה ולזיכרון הפיזי; Ring 3 (מצב משתמש / User Mode) מריץ יישומי תוכנה עם סט הוראות מוגבל כדי למנוע קריסות מערכת.",
                            "תוכנת משתמש אינה יכולה לגשת לדיסק, לכרטיס הרשת או להקצות RAM ישירות. בכל פעם שתוכנה זקוקה לשירותי חומרה (כגון `open()`, `read()`, `write()`, `socket()`), היא מבצעת קריאת מערכת (System Call באמצעות הוראת `syscall` ב-x86).",
                            "הוראת `syscall` מבצעת מעבר חומרתי מבוקר מטבעת 3 לטבעת 0, שומרת את מצביע ההוראות של המשתמש (%rcx) ואת דגלי הסטטוס (%r11), וקופצת לכתובת הכניסה של הליבה המוגדרת באוגר חומרה ייעודי (MSR)."
                        ]
                    },
                    {
                        "title": "תנאי מרוץ, נעילות Mutex, Spinlock, Futex ופעולות אטומיות",
                        "points": [
                            "כאשר מספר תהליכונים קוראים וכותבים לזיכרון משותף בו-זמנית ללא סנכרון, נוצרים תנאי מרוץ (Race Conditions) בלתי צפויים (למשל `counter++` מורכב מ-3 שלבי אסמבלי: קריאה מזיכרון, הגדלה באוגר, וכתיבה חזרה).",
                            "פעולות אטומיות (כגון `Compare-And-Swap` / CAS) מבוצעות כטרנזקציית חומרה בלתי ניתנת לחלוקה על אפיק הזיכרון (`LOCK CMPXCHG` ב-x86), ומהוות את הבסיס לכל מבני הנתונים ללא נעילות (Lock-Free).",
                            "מנעול סחרור (Spinlock) רץ בלולאת בדיקה צפופה של המעבד עד שהמנעול מתפנה; הוא אידיאלי לקטעים קריטיים קצרצרים בליבה, אך מבזבז 100% ממשאבי הליבה אם הוא מוחזק לזמן ממושך.",
                            "מנעול Mutex מרדים תהליכונים ממתינים כדי לפנות את המעבד. מנעולי Mutex מודרניים בלינוקס מבוססים על Futex (מנעול מהיר במרחב המשתמש): נעילה ללא תחרות מתבצעת כולה במרחב המשתמש תוך כ-5ns בפעולה אטומית, וקריאת מערכת יקרה לליבה מתבצעת רק אם נדרש להרדים תהליכון."
                        ]
                    }
                ],
                "trivia": [
                    {
                        "type": "multiple_choice",
                        "question": "איזה משאב זיכרון הוא פרטי וייחודי לכל תהליכון (Thread) בתוך תהליך מרובה תהליכונים?",
                        "options": [
                            "מחסנית הקריאות (Call Stack) ומצב אוגרי המעבד",
                            "מאגר הזיכרון הדינמי (Heap)",
                            "מקטע הזיכרון הגלובלי של התוכנית",
                            "טבלת מתארי הקבצים הפתוחים"
                        ],
                        "correct": 0,
                        "explanation": "תהליכונים חולקים את מרחב הכתובות הווירטואלי, ה-Heap והקבצים הפתוחים של התהליך, אך לכל תהליכון יש מחסנית קריאות פרטית ואוגרי מעבד משלו."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מדוע החלפת הקשר בין תהליכים נפרדים יקרה משמעותית מהחלפה בין תהליכונים באותו תהליך?",
                        "options": [
                            "החלפת תהליך מחייבת החלפת מצביע טבלת הדפים ב-CR3, מה שפוסל את רשומות ה-TLB וגורר החטאות מטמון",
                            "החלפת תהליך דורשת אתחול של כרטיס הרשת",
                            "החלפת תהליכונים מחייבת אימות חומרתי באמצעות שבב הצפנה",
                            "החלפת תהליך מעתיקה את כל נתוני ה-Heap לדיסק הקשיח"
                        ],
                        "correct": 0,
                        "explanation": "החלפת תהליכים מחייבת מעבר למרחב כתובות וירטואלי חדש (טעינת CR3), מה שפוסל את רשומות ה-TLB שאינן גלובליות וגורר החטאות זיכרון רבות."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "איזה מנגנון מאפשר לתוכנית במרחב המשתמש (טבעת 3) לבקש שירותים מליבת מערכת ההפעלה (טבעת 0)?",
                        "options": [
                            "קריאת מערכת (System Call / הוראת syscall)",
                            "בקשת ערוץ גישה ישירה לזיכרון (DMA)",
                            "פסיקת עיגול בנקודה צפה",
                            "שינוי מונה השעון של ה-BIOS"
                        ],
                        "correct": 0,
                        "explanation": "קריאות מערכת (`syscall`) מספקות שער חומרה מאובטח שבאמצעותו תוכנות משתמש מבקשות שירותי ליבה מיוחסים (כמו קריאת קבצים או פתיחת חיבורי רשת)."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהו 'תנאי מרוץ' (Race Condition) בתכנות מקבילי?",
                        "options": [
                            "באג שבו תקינות התוכנית תלויה בתזמון הבלתי צפוי או בסדר שזירת הביצוע של מספר תהליכונים",
                            "מצב שבו שני מעבדים מתחרים מי יגיע לתדר השעון הגבוה ביותר",
                            "מצב שבו תוכנה צורכת רוחב פס גבוה מקיבולת כרטיס הרשת",
                            "מצב שבו תהליכון קורס כתוצאה מסיום מקום במחסנית הפיזית"
                        ],
                        "correct": 0,
                        "explanation": "תנאי מרוץ מתרחש כאשר מספר תהליכונים ניגשים לנתונים משותפים ללא סנכרון מתאים, מה שמייצר תוצאות שגויות התלויות בתזמון ההרצה."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "כיצד מנגנון ה-Futex (Fast Userspace Mutex) משיג ביצועים גבוהים במיוחד בלינוקס?",
                        "options": [
                            "הוא מבצע נעילה ושחרור ללא תחרות במרחב המשתמש באמצעות פעולות אטומיות, ופונה לליבה רק כשיש תחרות",
                            "הוא מריץ את כל קוד הסנכרון ביחידות העיבוד של כרטיס המסך",
                            "הוא מכבה את פסיקות החומרה של המעבד במהלך קטעים קריטיים",
                            "הוא הופך תוכניות מרובות תהליכונים לקורוטינות יחידות"
                        ],
                        "correct": 0,
                        "explanation": "Futexes מבצעים נעילה מהירה במרחב המשתמש תוך ננו-שניות ספורות באמצעות הוראות אטומיות (CAS); קריאת מערכת לליבה מתבצעת אך ורק כאשר יש צורך להרדים תהליכון מתחרה."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "איזו הוראת אסמבלי ב-x86-64 מהווה את הבסיס למבני נתונים ללא נעילות (Lock-Free) על ידי עדכון אטומי של ערך רק אם הוא תואם לערך צפוי?",
                        "options": [
                            "LOCK CMPXCHG (השווה והחלף)",
                            "NOP (ללא פעולה)",
                            "JMP (קפיצה בלתי מותנית)",
                            "HLT (עצירת מעבד)"
                        ],
                        "correct": 0,
                        "explanation": "הוראת `LOCK CMPXCHG` משווה ערך בזיכרון לערך צפוי ומחליפה אותו בערך חדש בפעולה אטומית אחת שאינה ניתנת להפרעה על גבי אפיק הזיכרון."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהם ארבעת התנאים ההכרחיים להתרחשות קיפאון (Deadlock / תנאי קופמן)?",
                        "options": [
                            "מניעה הדדית, החזק והמתן, היעדר הפקעה, והמתנה מעגלית",
                            "גישה אטומית, דפדוף וירטואלי, חיזוי הסתעפויות, והחלפת הקשר",
                            "קריאה בלבד, כתיבה בלבד, הרצה בלבד, ואיסור הרצה",
                            "טבעת 0, טבעת 1, טבעת 2, וטבעת 3"
                        ],
                        "correct": 0,
                        "explanation": "ארבעת תנאי קופמן הם: (1) Mutual Exclusion, (2) Hold and Wait, (3) No Preemption, ו-(4) Circular Wait; שבירת אחד מהם מונעת קיפאון."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהו החיסרון המרכזי בשימוש במנעול סחרור (Spinlock) עבור קטעים קריטיים ממושכים?",
                        "options": [
                            "הוא מבזבז 100% מזמן ליבת המעבד בלולאת בדיקה פעילה בזמן ההמתנה לשחרור המנעול",
                            "הוא גורם לקריסת ליבה מיידית אם מוחזק מעל מילי-שנייה",
                            "הוא משתחרר מעצמו באופן אוטומטי לאחר 100 מחזורי שעון",
                            "הוא גורם לבלאי תרמי פיזי לזיכרון ה-DRAM"
                        ],
                        "correct": 0,
                        "explanation": "מנעולי סחרור אינם מרדימים את התהליכון הממתין אלא מסובבים אותו בלולאה פעילה, מה שמכלה 100% מזמן המעבד שיכול היה לשמש משימות אחרות."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהי מטרתה של הוראת מחסום זיכרון (Memory Barrier / Fence)?",
                        "options": [
                            "לאכוף סדר קשיח על פעולות קריאה וכתיבה לזיכרון כנגד שינויי סדר של המעבד והמהדר",
                            "לשמש כמעגל חומת אש פיזי בין לוח האם לספק הכוח",
                            "לבודד תהליכים בארגז חול ולמנוע מהם שימוש ב-RAM",
                            "לבצע אופטימיזציה להסרת משתנים מקומיים שאינם בשימוש"
                        ],
                        "correct": 0,
                        "explanation": "מחסום זיכרון מונע מהמעבד ומהמהדר לסדר מחדש פעולות קריאה וכתיבה סביב המחסום, ומבטיח סדר נראות נכון במערכות מרובות ליבות."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "לאיזה מצב נכנס תהליך ביוניקס כאשר סיים את ריצתו אך תהליך האב שלו טרם קרא ל-`wait()` כדי לקבל את קוד היציאה שלו?",
                        "options": [
                            "תהליך זומבי (Zombie / Defunct)",
                            "תהליך יתום (Orphan)",
                            "תהליך דמון (Daemon)",
                            "תהליך זמן-אמת (Real-Time)"
                        ],
                        "correct": 0,
                        "explanation": "תהליך זומבי סיים את ריצתו ושחרר את משאבי הזיכרון, אך רשומת ה-PID וקוד היציאה שלו נשמרים בטבלת התהליכים בליבה עד שהאב יקרא ל-`wait()`."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהו ההבדל בין ריבוי משימות מפקיע (Preemptive) ללא-מפקיע (Non-Preemptive)?",
                        "options": [
                            "בריבוי משימות מפקיע, פסיקת שעון הליבה עוצרת תהליכים בכוח; בלא-מפקיע, תהליך רץ עד שהוא מוותר על המעבד מרצונו",
                            "ריבוי משימות מפקיע מיושם אך ורק במיקרו-בקרים פשוטים של 8-ביט",
                            "ריבוי משימות לא-מפקיע מריץ תוכניות ללא זיכרון פיזי",
                            "ריבוי משימות מפקיע מחייב כתיבת קוד בשפת Rust"
                        ],
                        "correct": 0,
                        "explanation": "מערכות הפעלה מודרניות משתמשות בפסיקות שעון חומרתיות כדי להפקיע את המעבד ולהחליף משימות, ובכך מונעות מלולאה תקועה להקפיא את המחשב."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהי תופעת 'היפוך עדיפויות' (Priority Inversion) במערכות הפעלה לזמן אמת?",
                        "options": [
                            "מצב שבו משימה בעדיפות גבוהה נחסמת בהמתנה למשאב המוחזק על ידי משימה בעדיפות נמוכה, שמופקעת על ידי משימה בעדיפות בינונית",
                            "מצב שבו שעון המעבד רץ לאחור לחיסכון בסוללה",
                            "מצב שבו תוכנת משתמש רצה עם הרשאות גבוהות יותר מטבעת 0",
                            "מצב שבו מצביע המחסנית מצביע על זיכרון ה-Heap"
                        ],
                        "correct": 0,
                        "explanation": "היפוך עדיפויות מתרחש כאשר משימה דחופה ממתינה למנעול שמוחזק בידי משימה נחותה, שאינה מקבלת מעבד כי משימות בינוניות רצות (נפתר על ידי Priority Inheritance)."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהי מטרתו של מתזמן ה-CFS (Completely Fair Scheduler) בליבת לינוקס?",
                        "options": [
                            "לחלק את זמן המעבד בצורה הוגנת באמצעות עצי אדום-שחור בהתבסס על זמן הריצה הווירטואלי (vruntime) של כל משימה",
                            "להבטיח שכל תהליכון יקבל רוחב פס רשת זהה",
                            "לחלק את החשמל בצורה אחידה בין ערוצי המתח בלוח האם",
                            "להגריל את סדר ביצוע התהליכונים למניעת התקפות מניעת שירות"
                        ],
                        "correct": 0,
                        "explanation": "מתזמן CFS בלינוקס עוקב אחר זמן הריצה הווירטואלי (`vruntime`) של משימות בעץ אדום-שחור, ותמיד בוחר להריץ את המשימה שקיבלה הכי מעט זמן מעבד עד כה."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מה מייצג סמפור סופר (Counting Semaphore) שאתחולו הוגדר לערך K?",
                        "options": [
                            "פרימיטיב סנכרון המאפשר לעד K תהליכונים לגשת במקביל למאגר משאבים משותף מוגבל",
                            "אוגר חומרה הסופר פולסי שעון עד למספר K",
                            "תהליך המייצר K תהליכי בן בעת עליית המחשב",
                            "מתאר קובץ המאפשר עד K חיבורי רשת בו-זמנית"
                        ],
                        "correct": 0,
                        "explanation": "סמפור סופר המאותחל ל-K משמש לניהול מאגר משאבים; פעולת `wait()` מפחיתה את המונה וחוסמת כאשר הוא מגיע ל-0, ובכך מגבילה את הגישה ל-K תהליכונים במקביל."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מדוע שימוש במילת המפתח `volatile` ב-C/C++ אינו מספק לצורך סנכרון תהליכונים במעבדים מרובי ליבות?",
                        "options": [
                            "הוא מונע רק שמירת משתנה באוגרי המהדר, אך אינו מייצר מחסומי זיכרון של המעבד ואינו מבטיח פעולות אטומיות בחומרה",
                            "מדובר במילת מפתח ישנה שמהדרים מודרניים מתעלמים ממנה לחלוטין",
                            "הוא ממיר משתנים של 64-ביט למשתני בייט בודד",
                            "הוא מאלץ את התהליכון לרוץ במצב משתמש יחיד בלבד"
                        ],
                        "correct": 0,
                        "explanation": "`volatile` מונע מהמהדר לייעל קריאות/כתיבות ממשתנה, אך אינו מייצר הוראות חומרה אטומיות או מחסומי זיכרון של המעבד, ולכן אינו פותר תנאי מרוץ בין ליבות."
                    }
                ]
            },

            # =================================================================
            # MODULE 5: I/O, Storage, Interrupts & File Systems
            # =================================================================
            {
                "id": "io_storage_interrupts",
                "title": "5. קלט/פלט (I/O), פסיקות, מנהלי התקנים ומערכות קבצים",
                "description": "פסיקות חומרה מול דגימה (Polling), שגרות שירות פסיקה (ISR), גישה ישירה לזיכרון (DMA), מבנה Inodes, מערכות קבצים יומניות (Journaling), והתפתחות האחסון מ-HDD ל-NVMe SSD.",
                "cards": [
                    {
                        "title": "פסיקות חומרה מול דגימה (Polling) וגישה ישירה לזיכרון (DMA)",
                        "figure": {
                            "title": "גישה ישירה לזיכרון (DMA) לעומת העברה דרך המעבד",
                            "svg": """<svg viewBox="0 0 520 140" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-height:140px;">
  <rect x="20" y="45" width="90" height="50" rx="8" fill="#3b82f6" fill-opacity="0.15" stroke="#3b82f6" stroke-width="2"/>
  <text x="65" y="75" font-size="12" font-weight="bold" fill="#3b82f6" text-anchor="middle">ליבת מעבד</text>

  <rect x="180" y="20" width="160" height="45" rx="8" fill="#8b5cf6" fill-opacity="0.15" stroke="#8b5cf6" stroke-width="2"/>
  <text x="260" y="42" font-size="10" font-weight="bold" fill="#8b5cf6" text-anchor="middle">בקר DMA</text>
  <text x="260" y="56" font-size="8" fill="currentColor" opacity="0.8" text-anchor="middle">העברה ישירה במהירות גבוהה</text>

  <rect x="410" y="45" width="90" height="50" rx="8" fill="#10b981" fill-opacity="0.15" stroke="#10b981" stroke-width="2"/>
  <text x="455" y="75" font-size="12" font-weight="bold" fill="#10b981" text-anchor="middle">זיכרון RAM</text>

  <rect x="180" y="85" width="160" height="45" rx="8" fill="#f59e0b" fill-opacity="0.15" stroke="#f59e0b" stroke-width="2"/>
  <text x="260" y="107" font-size="10" font-weight="bold" fill="#f59e0b" text-anchor="middle">אחסון NVMe / כרטיס רשת</text>

  <path d="M 260 85 L 260 65" stroke="#8b5cf6" stroke-width="2" stroke-dasharray="3,3"/>
  <path d="M 340 42 L 410 60" stroke="#10b981" stroke-width="2"/>
  <path d="M 110 65 L 180 42" stroke="#3b82f6" stroke-width="2"/>
</svg>""",
                            "caption": "בקר ה-DMA מעביר מגה-בייטים של נתונים ישירות מהאחסון ל-RAM על גבי אפיק ה-PCIe מבלי להעסיק את המעבד בכל בייט."
                        },
                        "points": [
                            "אילו המעבד היה צריך לבדוק ברציפות בלולאה (Polling) האם הגיעה חבילת רשת או נלחץ מקש, הוא היה מבזבז 99% מכוח החישוב שלו בבדיקות סרק.",
                            "במקום זאת, התקנים היקפיים משתמשים בפסיקות חומרה (Hardware Interrupts). כאשר חבילת רשת מגיעה או שה-SSD סיים לקרוא בלוק, ההתקן שולח אות פסיקה לבקר הפסיקות של המעבד (APIC).",
                            "המעבד עוצר מיד את רצף ההוראות הנוכחי, שומר את אוגרי המשתמש במחסנית הליבה, וקופץ לשגרת שירות הפסיקה המתאימה (ISR) מתוך טבלת וקטורי הפסיקות (IDT).",
                            "גישה ישירה לזיכרון (Direct Memory Access / DMA): במקום שהמעבד יקרא כל 4 בייטים מהדיסק לאוגר ויכתוב אותם ל-RAM, בקר ה-DMA מעביר זרמי נתונים מסיביים ישירות בין ההתקן ל-RAM הפיזי על גבי האפיק, ופוסק את המעבד רק פעם אחת בסיום כל ההעברה."
                        ]
                    },
                    {
                        "title": "מערכות קבצים, מבנה Inodes ויומניות (Journaling)",
                        "points": [
                            "התקני אחסון פיזיים (SSDs, HDDs) הם מערך רציף של סקטורים בני 512 או 4096 בייטים. מערכת קבצים (כגון ext4, APFS, NTFS, XFS) מארגנת בלוקים אלו במבנה היררכי של תיקיות, קבצים ומטא-נתונים.",
                            "במערכות יוניקס, כל קובץ מיוצג על ידי Inode (Index Node). ה-Inode שומר את כל המטא-נתונים של הקובץ: גודל, הרשאות (chmod), בעלות UID/GID, חותמות זמן, ומצביעים לבלוקים הפיזיים בדיסק. שם הקובץ והמיקום בתיקייה נשמרים ברשומת התיקייה בלבד ולא בתוך ה-Inode עצמו!",
                            "קישורים קשיחים (Hard Links): שתי רשומות בתיקיות המצביעות לאותו מספר Inode חולקות את אותו קובץ פיזי בדיוק; המידע נמחק מהדיסק רק כאשר מונה הקישורים של ה-Inode מגיע לאפס.",
                            "מערכות קבצים יומניות (Journaling) מונעות השחתת מידע בהפסקות חשמל פתאומיות. לפני ביצוע שינוי מורכב במבנה הדיסק, השינוי נכתב ליומן רציף (Journal). אם המחשב נכבה באמצע הפעולה, הליבה משחזרת ומסיימת את הטרנזקציה מהיומן בשניות ספורות בעת האתחול ללא צורך בסריקת דיסק מלאה (`fsck`)."
                        ]
                    },
                    {
                        "title": "התפתחות האחסון: כוננים מכניים (HDDs), זיכרונות פלאש (SSDs) ו-NVMe",
                        "points": [
                            "כוננים מגנטיים קלאסיים (HDDs) משתמשים בפלטות מסתובבות ובזרוע מכנית. חיפוש סקטור אקראי אורך 5–10 מילי-שניות (בשל תנועת הזרוע וסיבוב הפלטה) - איטי פי 100,000 מזמן הגישה ל-RAM.",
                            "כונני מצב מוצק (SSDs) מבוססים על זיכרון NAND Flash ללא חלקים נעים. זיכרון הפלאש מאורגן בדפים (4–16 KB) ובבלוקים (128–512 דפים). מגבלה פיזית מרכזית היא שניתן לקרוא ולכתוב ברמת דף, אך מחיקה יכולה להתבצע אך ורק ברמת בלוק שלם.",
                            "שכבת תרגום הפלאש (FTL) בבקר ה-SSD מנהלת פיזור שחיקה (Wear Leveling) ואיסוף זבל כדי לחלק את הכתיבות בצורה אחידה בין תאי הסיליקון ולמנוע שחיקה מוקדמת.",
                            "פרוטוקול NVMe (Non-Volatile Memory Express) החליף את ממשק ה-SATA המיושן על ידי חיבור ישיר של ה-SSD לנתיבי PCIe, ותמיכה בעד 64,000 תורי פקודות מקביליים (עם 64,000 פקודות בכל תור), מה שמאפשר קצב העברה של גיגה-בייטים לשנייה במעבדים מרובי ליבות."
                        ]
                    }
                ],
                "trivia": [
                    {
                        "type": "multiple_choice",
                        "question": "מהו היתרון המרכזי של גישה ישירה לזיכרון (DMA) לעומת קלט/פלט מתוכנת (Programmed I/O)?",
                        "options": [
                            "התקני חומרה מעבירים נתונים ישירות ל-RAM הפיזי ללא שימוש במחזורי הוראות מעבד עבור כל בייט",
                            "הוא מבטל לחלוטין את הצורך בזיכרון RAM פיזי",
                            "הוא מאפשר לכוננים קשיחים מכניים להסתובב במהירות אינסופית",
                            "הוא מצפין קבצים באופן אוטומטי בהצפנה קוונטית"
                        ],
                        "correct": 0,
                        "explanation": "בקר DMA מאפשר להתקנים היקפיים להעביר גושי נתונים ישירות ל-RAM על גבי האפיק, ומתריע למעבד באמצעות פסיקה בודדת רק בסיום ההעברה המלאה."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "במערכות קבצים מבוססות יוניקס, איזה מידע מאוחסן בתוך צומת ה-Inode?",
                        "options": [
                            "גודל הקובץ, הרשאות, בעלות, חותמות זמן ומצביעים לבלוקי נתונים (אך לא שם הקובץ)",
                            "נתיב הקובץ המוחלט וגיבוב סיסמת המשתמש",
                            "כל הקוד הבינארי של ליבת מערכת ההפעלה",
                            "כתובת ה-IP של שרת הרשת המרוחק"
                        ],
                        "correct": 0,
                        "explanation": "ה-Inode שומר את כל המטא-נתונים של הקובץ ומצביע לבלוקים בדיסק, בעוד ששם הקובץ שמור ברשומת התיקייה המכילה אותו."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהו תפקידו של מנגנון ה-Journaling במערכות קבצים מודרניות (כגון ext4, NTFS, XFS)?",
                        "options": [
                            "רישום שינויים מבניים ביומן ייעודי בדיסק לפני ביצועם כדי לאפשר שחזור מיידי ועקבי לאחר קריסת מתח פתאומית",
                            "הקלטת לחיצות מקשים של המשתמש לצורך ניפוי שגיאות",
                            "דחיסת קבצי טקסט לארכיוני ZIP ברקע",
                            "פירמוט סקטורי SSD פגומים אחת ליממה"
                        ],
                        "correct": 0,
                        "explanation": "מערכת קבצים יומנית כותבת עסקאות מתוכננות ליומן רציף לפני החלתן בדיסק; בעת אתחול לאחר קריסה, הליבה משחזרת את המבנה מהיומן תוך שניות."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהי המגבלה הפיזית המרכזית של זיכרונות NAND Flash המשמשים בכונני SSD?",
                        "options": [
                            "ניתן לכתוב נתונים ברמת דף (Page), אך מחיקה מחייבת מחיקת בלוק שלם (Block) של דפים",
                            "הם אינם מסוגלים לקרוא נתונים מהר יותר מכונן תקליטונים ישן",
                            "הם מחייבים קירור בחנקן נוזלי לצורך פעולתם",
                            "הם מאבדים את כל הנתונים השמורים בעת כיבוי המחשב"
                        ],
                        "correct": 0,
                        "explanation": "בזיכרון פלאש, פעולת כתיבה מבוצעת ברמת דף (למשל 4KB), אך מחיקה מבוצעת אך ורק ברמת בלוק (מגה-בייטים), מה שמחייב מנגנוני איסוף זבל ופיזור שחיקה."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "איזה שדרוג ארכיטקטוני מרכזי הציג פרוטוקול NVMe לעומת ממשק ה-SATA AHCI הישן?",
                        "options": [
                            "חיבור ישיר לנתיבי PCIe ותמיכה בעד 64,000 תורי פקודות מקביליים עם 64,000 פקודות בכל תור",
                            "המרת כונני מצב מוצק לדיסקים אופטיים בלייזר",
                            "הגבלת הגישה לתור יחיד למניעת עומס באפיק הנתונים",
                            "הרצת סקריפטים של פייתון ישירות על גבי שבבי הפלאש"
                        ],
                        "correct": 0,
                        "explanation": "פרוטוקול NVMe תוכנן במיוחד לאחסון פלאש על גבי PCIe, ומאפשר עד 64,000 תורים מקביליים לעומת תור יחיד בן 32 פקודות ב-SATA AHCI."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מה מתרחש בעת יצירת קישור קשיח (Hard Link) לקובץ קיים בלינוקס?",
                        "options": [
                            "נוצרת רשומת תיקייה חדשה המצביעה לאותו מספר Inode קיים, ומונה הקישורים של הקובץ גדל ב-1",
                            "נוצר עותק פיזי משוכפל של כל בלוקי הנתונים בדיסק",
                            "נוצר קובץ מצביע מיוחד השומר את נתיב הטקסט של קובץ היעד",
                            "קובץ היעד מומר לקובץ הרצה בינארי"
                        ],
                        "correct": 0,
                        "explanation": "קישור קשיח מוסיף רשומת תיקייה נוספת המצביעה לאותו Inode; הנתונים הפיזיים נמחקים מהדיסק רק כאשר כל הקישורים נמחקים ומונה הקישורים מתאפס."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מה תפקידה של שכבת תרגום הפלאש (Flash Translation Layer - FTL) בבקר כונן SSD?",
                        "options": [
                            "לנהל מיפוי בלוקים לוגיים לפיזיים, פיזור שחיקה (Wear Leveling) ואיסוף זבל לשמירה על אורך חיי תאי הפלאש",
                            "לתרגם דפי אינטרנט של HTML לשפת מכונה בינארית",
                            "לבקר את מהירות הסיבוב המכנית של מנוע הפלטות",
                            "להצפין את זיכרון ה-RAM לפני ביצוע החלפת הקשר במעבד"
                        ],
                        "correct": 0,
                        "explanation": "ה-FTL הוא הקושחה בתוך בקר ה-SSD שממפה כתובות סקטורים לוגיות לדפי פלאש פיזיים, ומפזרת כתיבות כדי למנוע שחיקה מהירה של תאי הסיליקון."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהי שגרת שירות פסיקה (Interrupt Service Routine - ISR)?",
                        "options": [
                            "פונקציית ליבה ייעודית המוזנקת באופן מיידי בעת קבלת פסיקת חומרה או תוכנה ספציפית",
                            "תוכנת משתמש המנקה קבצי מטמון זמניים בדיסק",
                            "מעגל חומרה המספק מתח חשמלי לשקע המעבד",
                            "שלב בהידור המבצע אופטימיזציה ללולאות אריתמטיות"
                        ],
                        "correct": 0,
                        "explanation": "ה-ISR היא פונקציית טיפול הרשומה בטבלת הפסיקות של הליבה (IDT), הרצה בעדיפות גבוהה בתגובה לאותות פסיקה מהתקני חומרה."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהי מטרתו של ה-Page Cache בליבת לינוקס בעת קריאה וכתיבה של קבצים?",
                        "options": [
                            "שמירת בלוקי קבצים שנקראו או נכתבו לאחרונה בזיכרון ה-RAM הפיזי הפנוי כדי לספק מהירות גישה מיידית",
                            "שמירת עוגיות של דפדפן האינטרנט בסקטורים מוצפנים",
                            "חסימת משתמשים בלתי מורשים מלצפות בהרשאות קבצים",
                            "תרגום קוד שפת אסמבלי להוראות מיקרו-קוד"
                        ],
                        "correct": 0,
                        "explanation": "ה-Page Cache בלינוקס מנצל RAM פנוי לשמירת דפי קבצים; קריאות עוקבות מתבצעות ישירות מהזיכרון (~100ns) במקום מהאחסון הפיזי (~100μs)."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהו ההבדל בין דגימה (Polling) לבין קלט/פלט מונחה פסיקות (Interrupt-Driven I/O)?",
                        "options": [
                            "דגימה בודקת את סטטוס ההתקן ברציפות בלולאה; פסיקות מאפשרות למעבד לבצע משימות אחרות עד שההתקן מאותת על מוכנות",
                            "דגימה דורשת חומרת DMA, בעוד שפסיקות אינן דורשות זאת",
                            "פסיקות יכולות להיווצר אך ורק על ידי מקלדות מחשב",
                            "דגימה מבוצעת אך ורק בתוך יחידת ה-ALU של המעבד"
                        ],
                        "correct": 0,
                        "explanation": "דגימה מבזבזת מחזורי מעבד בלולאות בדיקה; מודל פסיקות מאפשר למעבד לעבוד על משימות אחרות עד שההתקן מפיק אות חשמלי המודיע שנתונים מוכנים."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהו קלט/פלט ממופה זיכרון (Memory-Mapped I/O - MMIO)?",
                        "options": [
                            "מנגנון שבו אוגרי הבקרה של התקני חומרה ממופים למרחב הכתובות הפיזי של המעבד ונגישים באמצעות הוראות קריאה/כתיבה רגילות",
                            "מיפוי של דיסקים קשיחים ישירות לקרני לייזר של כוננים אופטיים",
                            "שימוש בדפדוף זיכרון וירטואלי לאיחוי כונני פלאש",
                            "המרת שבבי RAM לנתבי רשת אלחוטיים"
                        ],
                        "correct": 0,
                        "explanation": "ב-MMIO, אוגרי התקני חומרה מקבלים כתובות בזיכרון הפיזי; המעבד מתקשר עם החומרה באמצעות הוראות טעינה ושמירה סטנדרטיות (`MOV`)."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מה תפקידה של קריאת המערכת `fsync()` בהנדסת תוכנה?",
                        "options": [
                            "אילוץ מערכת ההפעלה לרוקן את כל נתוני הקובץ והמטא-נתונים המושהים ב-Page Cache ישירות לאחסון הפיזי",
                            "סנכרון שעון המערכת מול שרת זמן פרוטוקול NTP",
                            "אינדוקס מחדש של מסד הנתונים בכל הדיסקים הקשיחים",
                            "סגירת כל חיבורי ה-TCP הפעילים במחשב"
                        ],
                        "correct": 0,
                        "explanation": "קריאת `fsync()` מכריחה את הליבה לכתוב את כל השינויים המושהים של הקובץ מה-RAM לאחסון הפיזי, ומבטיחה עמידות נתונים בבסיסי נתונים."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהו קישור רך (Symbolic Link / Symlink)?",
                        "options": [
                            "קובץ קטן המכיל מחרוזת טקסט של נתיב לקובץ או תיקייה אחרת, המפוענח באופן דינמי על ידי מערכת ההפעלה",
                            "כבל חומרה המחבר את לוח האם למתג ההדלקה",
                            "Inode משוכפל החולק בלוקי נתונים עם Inode אחר",
                            "תהליכון הרץ בעדיפות מעבד נמוכה במיוחד"
                        ],
                        "correct": 0,
                        "explanation": "קישור סימבולי הוא קובץ שתוכנו הוא פשוט נתיב טקסטואלי לקובץ היעד; אם קובץ היעד נמחק, הקישור הסימבולי הופך לשבור (Dangling)."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהו הגורם המרכזי לכך שכוננים קשיחים מכניים (HDDs) סובלים מהשהיה גבוהה בפעולות I/O אקראיות?",
                        "options": [
                            "זמן חיפוש מכני (הזזת זרוע הראשים הפיזית) והשהיית סיבוב (המתנה לסיבוב הסקטור מתחת לראש)",
                            "עומס ההצפנה של בקר אפיק ה-SATA",
                            "דרישות הקירור של מנוע הסיבוב המרכזי",
                            "הזמן הנדרש לתרגום שמות קבצים לטקסט בינארי"
                        ],
                        "correct": 0,
                        "explanation": "כונני HDD הם מכניים: תנועת הזרוע הפיזית למסלול המבוקש וההמתנה לסיבוב הפלטה אורכים 5–10 מילי-שניות, מה שמאט קריאות וכתיבות אקראיות."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהי מערכת הקבצים הווירטואלית (VFS) בליבת לינוקס?",
                        "options": [
                            "שכבת הפשטה המספקת ממשק אחיד וסטנדרטי (`open`, `read`, `write`) מעל מגוון מערכות קבצים קונקרטיות שונות (ext4, XFS, NFS)",
                            "מכונה וירטואלית להרצת תוכנות Windows בתוך לינוקס",
                            "פורמט דחיסה ליצירת קבצי ISO של תקליטורים",
                            "פרוטוקול רשת להורדת עדכוני אבטחה לליבה"
                        ],
                        "correct": 0,
                        "explanation": "ה-VFS מגדיר ממשק אחיד מונחה עצמים (inodes, dentries, files) המאפשר ליישומי משתמש לגשת לכל מערכות הקבצים בדיוק באותו אופן."
                    }
                ]
            }
        ]
    }

    # Write English file
    with open(TARGET_EN, "w", encoding="utf-8") as f:
        yaml.safe_dump(cs_en, f, allow_unicode=True, sort_keys=False, width=100)
    print(f"Generated {TARGET_EN}")

    # Write Hebrew file
    with open(TARGET_HE, "w", encoding="utf-8") as f:
        yaml.safe_dump(cs_he, f, allow_unicode=True, sort_keys=False, width=100)
    print(f"Generated {TARGET_HE}")

if __name__ == "__main__":
    create_course_datasets()

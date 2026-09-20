#!/usr/bin/env python3
"""
Generates the Linear Algebra & Geometry for AI & Engineers (linalg_101) academic topic
in both English (linalg_101_en.yaml) and Hebrew (linalg_101_he.yaml).
Follows first-principles pedagogical design, SVG diagrams, 100% 4-option multiple choice,
and comprehensive 'explanation' fields for Learn More context.
"""
import os
import yaml

TARGET_EN = "/Users/orishmuel/Library/CloudStorage/GoogleDrive-ori.shmuel@gmail.com/My Drive/Apps/Shmuel's Trivia App/academic_topics/linalg_101_en.yaml"
TARGET_HE = "/Users/orishmuel/Library/CloudStorage/GoogleDrive-ori.shmuel@gmail.com/My Drive/Apps/Shmuel's Trivia App/academic_topics/linalg_101_he.yaml"

def create_linalg_datasets():
    # -------------------------------------------------------------------------
    # ENGLISH LINEAR ALGEBRA DATASET
    # -------------------------------------------------------------------------
    la_en = {
        "id": "linalg_101_en",
        "type": "academic",
        "icon": "📐",
        "title": "Linear Algebra & Geometry for AI & Engineers (LinAlg 101)",
        "description": "A deeply visual, first-principles guide exploring how vectors span dimensions, how matrices morph space, and how eigenvalues and SVD power modern machine learning and computer graphics.",
        "lang": "en",
        "audience": "family",
        "categories": [
            # =================================================================
            # MODULE 1: Vectors, Dot Products & Spatial Projections
            # =================================================================
            {
                "id": "vectors_spaces_projections",
                "title": "1. Vectors, Dot Products & Spatial Projections",
                "description": "Understanding vectors as geometric displacement arrows, the dot product as shadow projection and angle measurement, linear independence, and orthogonal span.",
                "cards": [
                    {
                        "title": "What is a Vector? Arrows in Space vs. Number Lists",
                        "figure": {
                            "title": "Vector Addition & The Dot Product Projection",
                            "svg": """<svg viewBox="0 0 520 150" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-height:150px;">
  <!-- Grid Axis -->
  <line x1="30" y1="120" x2="480" y2="120" stroke="currentColor" stroke-width="1.5" opacity="0.3"/>
  <line x1="60" y1="10" x2="60" y2="140" stroke="currentColor" stroke-width="1.5" opacity="0.3"/>

  <!-- Vector u -->
  <line x1="60" y1="120" x2="260" y2="120" stroke="#3b82f6" stroke-width="3"/>
  <polygon points="260,116 270,120 260,124" fill="#3b82f6"/>
  <text x="160" y="140" font-size="12" font-weight="bold" fill="#3b82f6" text-anchor="middle">Vector v</text>

  <!-- Vector v -->
  <line x1="60" y1="120" x2="200" y2="30" stroke="#8b5cf6" stroke-width="3"/>
  <polygon points="196,26 206,30 202,38" fill="#8b5cf6"/>
  <text x="120" y="65" font-size="12" font-weight="bold" fill="#8b5cf6">Vector u</text>

  <!-- Projection drop line -->
  <line x1="200" y1="30" x2="200" y2="120" stroke="#ec4899" stroke-width="2" stroke-dasharray="4,4"/>

  <!-- Projected length -->
  <rect x="60" y="116" width="140" height="8" fill="#10b981" fill-opacity="0.5"/>
  <text x="130" y="110" font-size="10" font-weight="bold" fill="#10b981" text-anchor="middle">Projection: ||u|| cos(θ)</text>
  <text x="360" y="75" font-size="12" font-weight="bold" fill="currentColor">u · v = ||u|| ||v|| cos(θ)</text>
</svg>""",
                            "caption": "The dot product measures directional alignment: it projects vector $\\mathbf{u}$ onto vector $\\mathbf{v}$ and multiplies their lengths."
                        },
                        "points": [
                            "To a software developer, a vector is an ordered array of floating-point numbers (e.g. $[3.2, -1.5, 4.0]$). To a physicist or graphics engineer, a vector is a geometric arrow possessing both a magnitude (length) and a direction in space.",
                            "Vector Addition $(\\mathbf{u} + \\mathbf{v})$ corresponds to chaining movements tip-to-tail. Scalar Multiplication $(c \\mathbf{v})$ stretches, shrinks, or reverses the arrow's length without changing its underlying line of action.",
                            "The Dot Product (Inner Product) combines two vectors into a single scalar number: $\\mathbf{u} \\cdot \\mathbf{v} = u_1 v_1 + u_2 v_2 + \\dots + u_n v_n = \\|\\mathbf{u}\\| \\|\\mathbf{v}\\| \\cos(\\theta)$.",
                            "Geometrically, the dot product measures alignment: if $\\mathbf{u} \\cdot \\mathbf{v} > 0$, the vectors point in a similar direction; if $\\mathbf{u} \\cdot \\mathbf{v} = 0$, they are strictly Perpendicular (Orthogonal); and if $\\mathbf{u} \\cdot \\mathbf{v} < 0$, they point in opposite directions."
                        ]
                    },
                    {
                        "title": "Linear Combinations, Span & Linear Independence",
                        "points": [
                            "A Linear Combination of vectors $\\mathbf{v}_1, \\mathbf{v}_2, \\dots, \\mathbf{v}_k$ is any new vector formed by scaling and adding them: $c_1 \\mathbf{v}_1 + c_2 \\mathbf{v}_2 + \\dots + c_k \\mathbf{v}_k$.",
                            "The Span of a set of vectors is the entire geometric subspace of all possible vectors reachable by taking linear combinations. Two non-parallel 2D vectors span the entire 2D plane $\\mathbb{R}^2$.",
                            "Linear Independence: A set of vectors is linearly independent if NO vector in the set can be constructed as a linear combination of the others (i.e. every vector adds a genuinely new spatial dimension).",
                            "A Basis for a vector space is a minimal set of linearly independent vectors that spans the entire space (e.g. standard Cartesian unit basis vectors $\\hat{i} = [1, 0]$ and $\\hat{j} = [0, 1]$)."
                        ]
                    },
                    {
                        "title": "Orthogonal Projections & The Gram-Schmidt Process",
                        "points": [
                            "The Orthogonal Projection of vector $\\mathbf{b}$ onto vector $\\mathbf{a}$ finds the point on $\\mathbf{a}$ closest to $\\mathbf{b}$, decomposing $\\mathbf{b}$ into parallel and perpendicular components: $\\text{proj}_{\\mathbf{a}}(\\mathbf{b}) = \\frac{\\mathbf{a} \\cdot \\mathbf{b}}{\\|\\mathbf{a}\\|^2} \\mathbf{a}$.",
                            "This geometric projection is the fundamental engine behind Linear Regression, Fourier Series decomposition, and neural network attention mechanisms.",
                            "The Gram-Schmidt Process takes any set of arbitrary linearly independent vectors and systematically converts them into an Orthonormal Basis (all vectors have length 1.0 and are mutually perpendicular, $\\mathbf{u}_i \\cdot \\mathbf{u}_j = 0$ for $i \\neq j$)."
                        ]
                    }
                ],
                "trivia": [
                    {
                        "type": "multiple_choice",
                        "question": "What geometric condition is indicated when the dot product of two non-zero vectors equals zero (u · v = 0)?",
                        "options": [
                            "The vectors are mutually orthogonal (perpendicular at an angle of 90 degrees)",
                            "The vectors point in exactly the same direction",
                            "The vectors have equal mathematical lengths",
                            "The vectors lie outside the Cartesian coordinate system"
                        ],
                        "correct": 0,
                        "explanation": "Because $\\mathbf{u} \\cdot \\mathbf{v} = \\|\\mathbf{u}\\| \\|\\mathbf{v}\\| \\cos(\\theta)$, a dot product of zero means $\\cos(\\theta) = 0$, proving the angle between them is exactly $90^\\circ$ (orthogonal)."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the 'Span' of a set of vectors?",
                        "options": [
                            "The set of all possible vectors that can be created through linear combinations (scaling and adding) of those vectors",
                            "The physical distance between the origin and the longest vector",
                            "The maximum number of non-zero floating point numbers in an array",
                            "The matrix determinant of the vector cross product"
                        ],
                        "correct": 0,
                        "explanation": "The span of a set of vectors is the entire subspace formed by all possible linear combinations $c_1 \\mathbf{v}_1 + c_2 \\mathbf{v}_2 + \\dots + c_k \\mathbf{v}_k$."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "When is a collection of vectors considered 'Linearly Dependent'?",
                        "options": [
                            "When at least one vector in the set can be written as a linear combination of the remaining vectors (redundant dimension)",
                            "When all vectors have identical lengths",
                            "When the vectors are all perpendicular to one another",
                            "When the dot product of any two vectors is positive"
                        ],
                        "correct": 0,
                        "explanation": "Linear dependence means there is redundancy in the set; at least one vector lies within the span of the others and adds no new geometric dimension."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What does the Gram-Schmidt process accomplish in linear algebra?",
                        "options": [
                            "It transforms any basis of linearly independent vectors into an orthonormal basis of mutually perpendicular unit vectors",
                            "It inverts a non-square matrix using Gaussian elimination",
                            "It finds the roots of high-order polynomial equations",
                            "It compresses image files using JPEG quantization"
                        ],
                        "correct": 0,
                        "explanation": "The Gram-Schmidt algorithm takes linearly independent vectors and iteratively subtracts parallel projections to construct a set of mutually orthogonal unit vectors."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the formula for the Euclidean length (L2 norm) of a 3D vector v = [x, y, z]?",
                        "options": [
                            "sqrt(x^2 + y^2 + z^2)",
                            "x + y + z",
                            "x * y * z",
                            "max(|x|, |y|, |z|)"
                        ],
                        "correct": 0,
                        "explanation": "By the Pythagorean theorem extended to $n$ dimensions, the Euclidean norm $\\|\\mathbf{v}\\|_2$ equals $\\sqrt{x^2 + y^2 + z^2} = \\sqrt{\\mathbf{v} \\cdot \\mathbf{v}}$."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is a 'Unit Vector'?",
                        "options": [
                            "A vector whose geometric length (magnitude) is exactly equal to 1.0",
                            "A vector containing only integer numbers",
                            "A matrix with 1s along the main diagonal",
                            "A vector that points exclusively along the positive X axis"
                        ],
                        "correct": 0,
                        "explanation": "A unit vector is any vector normalized so that its Euclidean length $\\|\\mathbf{v}\\| = 1$, representing pure direction without scale."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What does the Cauchy-Schwarz Inequality state for any two real vectors u and v?",
                        "options": [
                            "|u · v| <= ||u|| ||v||",
                            "||u + v|| = ||u|| + ||v||",
                            "u · v >= ||u|| ||v||",
                            "u · v = 0"
                        ],
                        "correct": 0,
                        "explanation": "The Cauchy-Schwarz inequality $|\\mathbf{u} \\cdot \\mathbf{v}| \\leq \\|\\mathbf{u}\\| \\|\\mathbf{v}\\|$ reflects the fact that $|\\cos(\\theta)| \\leq 1$, with equality holding only when the vectors are parallel."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the result of the Cross Product of two 3D vectors (u x v)?",
                        "options": [
                            "A new 3D vector that is mutually perpendicular (orthogonal) to both u and v",
                            "A single scalar number representing the dot product",
                            "A 3x3 diagonal identity matrix",
                            "The scalar sum of the coordinates of u and v"
                        ],
                        "correct": 0,
                        "explanation": "The cross product $\\mathbf{u} \\times \\mathbf{v}$ yields a vector perpendicular to the plane containing $\\mathbf{u}$ and $\\mathbf{v}$, with magnitude equal to the parallelogram area spanned by them."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What defines a 'Basis' for a vector space V?",
                        "options": [
                            "A set of linearly independent vectors that spans the entire space V",
                            "Any collection of vectors with integer coordinates",
                            "A set of vectors whose dot products are all negative",
                            "The origin point [0, 0, 0]"
                        ],
                        "correct": 0,
                        "explanation": "A basis is a minimal spanning set: it must be linearly independent and span the vector space, allowing every vector in the space to be written uniquely as a linear combination."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "How do you project a vector b orthogonally onto a line defined by unit vector u (where ||u|| = 1)?",
                        "options": [
                            "(b · u) u",
                            "b + u",
                            "b / u",
                            "sqrt(b · u)"
                        ],
                        "correct": 0,
                        "explanation": "When $\\mathbf{u}$ is a unit vector, the scalar shadow length is $(\\mathbf{b} \\cdot \\mathbf{u})$, and multiplying by direction vector $\\mathbf{u}$ gives the orthogonal projection $(\\mathbf{b} \\cdot \\mathbf{u}) \\mathbf{u}$."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the dimension of a vector space?",
                        "options": [
                            "The exact number of vectors in any basis for that vector space",
                            "The physical byte size of the floating point array",
                            "The determinant of the covariance matrix",
                            "The maximum value of the coordinates"
                        ],
                        "correct": 0,
                        "explanation": "The dimension of a vector space is defined as the cardinality (number of elements) in any basis spanning that space."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is an 'Orthonormal' set of vectors?",
                        "options": [
                            "A set of vectors where every vector has a length of 1.0 and all distinct pairs are mutually perpendicular",
                            "A set of vectors with all positive coordinates",
                            "A set of vectors that forms a closed polygon",
                            "A set of vectors that cannot be multiplied by scalars"
                        ],
                        "correct": 0,
                        "explanation": "An orthonormal set satisfies two conditions: orthogonality ($\mathbf{u}_i \cdot \mathbf{u}_j = 0$ for $i \neq j$) and normality ($\|\mathbf{u}_i\| = 1$ for all $i$)."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "In cosine similarity used in NLP and search engines, what does a cosine value of 1.0 between two embedding vectors signify?",
                        "options": [
                            "The two vectors point in the exact same direction (highest possible semantic similarity)",
                            "The two vectors are completely orthogonal (unrelated)",
                            "The two vectors are diametrically opposed in meaning",
                            "The vectors contain corrupt NaN values"
                        ],
                        "correct": 0,
                        "explanation": "Cosine similarity $\\frac{\\mathbf{u} \\cdot \\mathbf{v}}{\\|\\mathbf{u}\\| \\|\\mathbf{v}\\|} = \\cos(\\theta)$ reaches 1.0 when the angle $\\theta = 0^\\circ$, indicating identical directional semantics."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What happens if you attempt to form a basis for 3D space (R^3) using only 2 linearly independent vectors?",
                        "options": [
                            "The 2 vectors can only span a 2D flat plane, leaving the rest of 3D space unreachable",
                            "The 2 vectors will automatically generate a third vector through quantum entanglement",
                            "The determinant of the vectors will be infinite",
                            "The vectors will bend into non-Euclidean curves"
                        ],
                        "correct": 0,
                        "explanation": "In $\\mathbb{R}^3$, any basis must contain exactly 3 linearly independent vectors; 2 vectors can only span a 2D plane embedded within the 3D space."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the Zero Vector [0, 0, ..., 0] in linear algebra?",
                        "options": [
                            "The unique additive identity element of the vector space such that v + 0 = v for all vectors v",
                            "A vector that cannot be multiplied by scalar numbers",
                            "A vector that has an undefined mathematical length",
                            "A vector that spans all dimensions simultaneously"
                        ],
                        "correct": 0,
                        "explanation": "The zero vector $\\mathbf{0}$ is the unique additive identity in any vector space; adding it to any vector $\\mathbf{v}$ yields $\\mathbf{v}$, and its length is 0."
                    }
                ]
            },

            # =================================================================
            # MODULE 2: Matrices as Linear Spatial Transformations
            # =================================================================
            {
                "id": "matrix_transformations_determinants",
                "title": "2. Matrices as Linear Spatial Transformations",
                "description": "Visualizing matrices not as boring number spreadsheets, but as dynamic functions that warp space, basis vector mapping, and the determinant as area scaling.",
                "cards": [
                    {
                        "title": "A Matrix is a Dynamic Spatial Transformation",
                        "figure": {
                            "title": "How a 2x2 Matrix Transforms the Coordinate Grid",
                            "svg": """<svg viewBox="0 0 520 150" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-height:150px;">
  <!-- Original Grid Basis -->
  <g transform="translate(40,20)">
    <rect x="0" y="0" width="100" height="100" fill="#3b82f6" fill-opacity="0.15" stroke="#3b82f6" stroke-dasharray="2,2"/>
    <line x1="0" y1="100" x2="100" y2="100" stroke="#3b82f6" stroke-width="3"/>
    <polygon points="96,96 106,100 96,104" fill="#3b82f6"/>
    <text x="50" y="118" font-size="10" font-weight="bold" fill="#3b82f6" text-anchor="middle">i_hat [1, 0]</text>

    <line x1="0" y1="100" x2="0" y2="0" stroke="#10b981" stroke-width="3"/>
    <polygon points="-4,6 0,-4 4,6" fill="#10b981"/>
    <text x="-8" y="50" font-size="10" font-weight="bold" fill="#10b981" text-anchor="end">j_hat [0, 1]</text>
    <text x="50" y="55" font-size="11" font-weight="bold" fill="currentColor" text-anchor="middle">Area = 1.0</text>
  </g>

  <!-- Transform Arrow -->
  <path d="M 180 70 L 250 70" stroke="currentColor" stroke-width="2" marker-end="url(#arr)" opacity="0.6"/>
  <text x="215" y="60" font-size="11" font-weight="bold" fill="#8b5cf6" text-anchor="middle">Matrix A</text>

  <!-- Transformed Grid Parallelogram -->
  <g transform="translate(290,20)">
    <polygon points="0,100 120,70 160,0 40,30" fill="#8b5cf6" fill-opacity="0.2" stroke="#8b5cf6" stroke-width="2"/>
    <line x1="0" y1="100" x2="120" y2="70" stroke="#3b82f6" stroke-width="3"/>
    <polygon points="116,66 126,69 120,76" fill="#3b82f6"/>
    <text x="70" y="100" font-size="10" font-weight="bold" fill="#3b82f6">A * i_hat</text>

    <line x1="0" y1="100" x2="40" y2="30" stroke="#10b981" stroke-width="3"/>
    <polygon points="36,26 44,24 42,34" fill="#10b981"/>
    <text x="10" y="45" font-size="10" font-weight="bold" fill="#10b981">A * j_hat</text>
    <text x="85" y="50" font-size="11" font-weight="bold" fill="#8b5cf6" text-anchor="middle">Area = |det(A)|</text>
  </g>
</svg>""",
                            "caption": "A matrix transformation is completely described by where the basis vectors $\\hat{i}$ and $\\hat{j}$ land. The determinant measures how area scales."
                        },
                        "points": [
                            "A Linear Transformation is a geometric function $T(\\mathbf{v})$ that morphs space while respecting two rules: (1) The origin $[0,0]$ remains fixed in place, and (2) All straight grid lines remain straight and evenly spaced.",
                            "You can completely determine what a matrix does to the ENTIRE infinite space just by watching where the standard basis vectors land! Where does $\\hat{i} = [1,0]$ land? That becomes column 1 of the matrix. Where does $\\hat{j} = [0,1]$ land? That becomes column 2.",
                            "Matrix-Vector Multiplication $A\\mathbf{x}$ simply scales the transformed basis vectors: $A \\begin{bmatrix} x \\\\ y \\end{bmatrix} = x (\\text{column 1}) + y (\\text{column 2})$.",
                            "Matrix Multiplication $(AB)$ represents the Composition of transformations: applying transformation $B$ first, followed by transformation $A$ ($A(B\\mathbf{x})$). Because spatial morphs depend on order (e.g. rotating then shearing $\\neq$ shearing then rotating), matrix multiplication is Non-Commutative: $AB \\neq BA$!"
                        ]
                    },
                    {
                        "title": "The Determinant: Scaling of Areas and Volumes",
                        "points": [
                            "The Determinant $\\det(A)$ measures the factor by which areas (in 2D), volumes (in 3D), or hyper-volumes (in $n$D) are scaled by the linear transformation.",
                            "If $\\det(A) = 3$, every shape transformed by $A$ has its area tripled. If $\\det(A) = 1$, the transformation preserves area exactly (like pure spatial rotations).",
                            "A Negative Determinant (e.g. $\\det(A) = -2$) means the transformation flips the orientation of space (like looking at a reflection in a mirror).",
                            "If $\\det(A) = 0$, the transformation collapses space into a lower dimension (squashing a 2D plane into a 1D line or a point). When this happens, information is irreversibly destroyed, and the matrix has NO inverse ($A^{-1}$ does not exist)!"
                        ]
                    },
                    {
                        "title": "Matrix Inverses & Special Matrix Classes",
                        "points": [
                            "The Inverse Matrix $A^{-1}$ 'undoes' the transformation performed by $A$, returning every vector to its original location: $A^{-1} A = I$ (the Identity Matrix).",
                            "An Orthogonal Matrix $Q$ preserves all lengths and angles: $Q^T Q = I$, meaning its columns are mutually orthonormal unit vectors and its inverse is simply its transpose ($Q^{-1} = Q^T$).",
                            "A Symmetric Matrix equals its own transpose ($A = A^T$), playing a central role in covariance matrices, Hessian optimization matrices, and physics inertia tensors."
                        ]
                    }
                ],
                "trivia": [
                    {
                        "type": "multiple_choice",
                        "question": "What is the geometric meaning of the determinant of a 2x2 matrix det(A)?",
                        "options": [
                            "The factor by which the transformation scales the area of any geometric shape in the 2D plane",
                            "The slope of the line passing through the matrix origin",
                            "The total sum of all floating point entries in the matrix",
                            "The angle of rotational acceleration applied to the basis vectors"
                        ],
                        "correct": 0,
                        "explanation": "The determinant $\\det(A)$ measures the area scaling factor of the transformation; a $1 \\times 1$ unit square transforms into a parallelogram with area $|\\det(A)|$."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What does a determinant of zero (det(A) = 0) indicate about a linear transformation?",
                        "options": [
                            "The transformation squashes space into a lower dimension (e.g. a 2D plane into a 1D line), meaning the matrix is singular and non-invertible",
                            "The transformation is a pure lossless rotation",
                            "The matrix contains only zeroes in all rows and columns",
                            "The inverse matrix is equal to the identity matrix"
                        ],
                        "correct": 0,
                        "explanation": "When $\\det(A) = 0$, the transformation collapses dimensional volume to zero, irreversibly losing information; hence, no inverse matrix $A^{-1}$ exists."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Why is matrix multiplication non-commutative (AB != BA in general)?",
                        "options": [
                            "Because matrix multiplication represents function composition, and applying spatial transformations in different orders produces different geometric results",
                            "Because hardware floating point units suffer rounding errors in reverse order",
                            "Because matrix multiplication requires squaring the matrix entries first",
                            "Because negative numbers cannot be multiplied from the right"
                        ],
                        "correct": 0,
                        "explanation": "Matrix multiplication represents successive spatial transformations; rotating space by $90^\\circ$ and then shearing it produces a completely different result than shearing first and then rotating."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the defining property of an Orthogonal Matrix Q?",
                        "options": [
                            "Its transpose is equal to its inverse (Q^T Q = I), preserving vector lengths and angles",
                            "All of its off-diagonal entries are equal to 0",
                            "Its determinant is always equal to 0",
                            "Its eigenvalues are all pure imaginary numbers"
                        ],
                        "correct": 0,
                        "explanation": "An orthogonal matrix $Q$ has orthonormal columns and rows; multiplying by $Q$ preserves vector lengths and angles (rotations/reflections), and $Q^{-1} = Q^T$."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What are the columns of a 2x2 transformation matrix A?",
                        "options": [
                            "The coordinates of where the standard basis vectors i_hat [1, 0] and j_hat [0, 1] land after transformation",
                            "The eigenvalues of the matrix squared",
                            "The normal vectors of the coordinate axes",
                            "The coordinates of the null space kernel"
                        ],
                        "correct": 0,
                        "explanation": "Column 1 of matrix $A$ is the vector where $\\hat{i} = [1,0]^T$ lands, and Column 2 is the vector where $\\hat{j} = [0,1]^T$ lands."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is a 'Symmetric Matrix'?",
                        "options": [
                            "A square matrix that is identical to its own transpose (A = A^T)",
                            "A matrix whose determinant equals 1",
                            "A matrix with an equal number of positive and negative numbers",
                            "A matrix that only operates on 2D coordinates"
                        ],
                        "correct": 0,
                        "explanation": "A matrix is symmetric if $A_{ij} = A_{ji}$ for all entries, which means swapping rows and columns ($A^T$) leaves the matrix unchanged."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What geometric operation is performed by a 2x2 Rotation Matrix R(theta)?",
                        "options": [
                            "Rotating all vectors counter-clockwise about the origin by angle theta while preserving lengths and areas",
                            "Scaling the X axis by factor theta while leaving Y untouched",
                            "Projecting all vectors onto a line at angle theta",
                            "Squashing the 2D plane into a 1D diagonal line"
                        ],
                        "correct": 0,
                        "explanation": "A rotation matrix $R(\\theta) = \\begin{bmatrix} \\cos\\theta & -\\sin\\theta \\\\ \\sin\\theta & \\cos\\theta \\end{bmatrix}$ rotates the entire plane by $\\theta$ without changing vector lengths (an isometry with $\\det = 1$)."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What does a negative determinant value (det(A) < 0) mean geometrically?",
                        "options": [
                            "The transformation inverts the spatial orientation (like a reflection in a mirror)",
                            "The transformation shrinks all vectors to zero length",
                            "The matrix cannot be multiplied by any other matrix",
                            "The transformed area is negative in physical centimeters"
                        ],
                        "correct": 0,
                        "explanation": "A negative determinant indicates that the spatial orientation has been flipped (handedness inverted, like reflecting through an axis)."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the Identity Matrix I?",
                        "options": [
                            "A square matrix with 1s along the main diagonal and 0s elsewhere that acts as the 'do nothing' transformation (I v = v)",
                            "A matrix whose entries are all equal to 1",
                            "A matrix that flips the sign of all coordinates",
                            "A matrix that deletes the last row of any vector"
                        ],
                        "correct": 0,
                        "explanation": "The identity matrix $I$ acts as the multiplicative identity in linear algebra: multiplying any vector or matrix by $I$ leaves it unchanged ($I\\mathbf{v} = \\mathbf{v}$)."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the Transpose of a matrix (A^T)?",
                        "options": [
                            "An operation that flips the matrix over its main diagonal, turning rows into columns",
                            "Inverting all the mathematical signs of the matrix elements",
                            "Multiplying the matrix by its determinant",
                            "Calculating the matrix derivative with respect to time"
                        ],
                        "correct": 0,
                        "explanation": "Transposing a matrix $A$ swaps its row and column indices: $(A^T)_{ij} = A_{ji}$."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the determinant of a product of two square matrices det(AB)?",
                        "options": [
                            "det(A) * det(B)",
                            "det(A) + det(B)",
                            "det(A) / det(B)",
                            "max(det(A), det(B))"
                        ],
                        "correct": 0,
                        "explanation": "The determinant of a product equals the product of the determinants: $\\det(AB) = \\det(A) \\det(B)$, reflecting sequential area scaling."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the Trace of a square matrix Tr(A)?",
                        "options": [
                            "The sum of all elements along the main diagonal (A_11 + A_22 + ... + A_nn)",
                            "The product of the corner entries of the matrix",
                            "The number of non-zero rows in reduced echelon form",
                            "The Euclidean length of the first column vector"
                        ],
                        "correct": 0,
                        "explanation": "The trace $\\text{Tr}(A)$ is the sum of the diagonal entries $\\sum_{i=1}^n A_{ii}$, which also remarkably equals the sum of its eigenvalues."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is a 'Diagonal Matrix'?",
                        "options": [
                            "A matrix where all entries outside the main diagonal are equal to zero",
                            "A matrix that only has entries along the top-right to bottom-left diagonal",
                            "A matrix whose rows sum to 1.0",
                            "A non-square matrix with more columns than rows"
                        ],
                        "correct": 0,
                        "explanation": "A diagonal matrix has non-zero entries only where row index equals column index ($i = j$); multiplying by it simply scales each coordinate axis independently."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "If matrix A satisfies A^2 = A, what type of transformation does it represent?",
                        "options": [
                            "A Projection (Idempotent matrix)",
                            "A continuous 360-degree rotation",
                            "An exponential growth transformation",
                            "A reflection through the origin"
                        ],
                        "correct": 0,
                        "explanation": "An idempotent matrix ($A^2 = A$) represents a projection: once a vector is projected onto a subspace, applying the projection again leaves it unchanged."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "How does scalar multiplication of an n x n matrix by constant c affect its determinant (det(c A))?",
                        "options": [
                            "c^n * det(A)",
                            "c * det(A)",
                            "c + det(A)",
                            "det(A) / c"
                        ],
                        "correct": 0,
                        "explanation": "Because scaling an $n$-dimensional space by factor $c$ along all $n$ axes multiplies the $n$-dimensional volume by $c^n$, $\\det(c A) = c^n \\det(A)$."
                    }
                ]
            },

            # =================================================================
            # MODULE 3: Systems of Equations, Column Space & Rank
            # =================================================================
            {
                "id": "linear_systems_nullspace_rank",
                "title": "3. Systems of Equations, Column Space & Rank",
                "description": "Solving Ax = b as vector linear combinations, the fundamental subspaces of a matrix, Nullspace, Column Space, and the Rank-Nullity Theorem.",
                "cards": [
                    {
                        "title": "Ax = b as a Linear Combination of Columns",
                        "figure": {
                            "title": "Column Space (Image) vs. Null Space (Kernel)",
                            "svg": """<svg viewBox="0 0 520 150" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-height:150px;">
  <!-- Input Domain Space R^n -->
  <rect x="20" y="20" width="200" height="110" rx="10" fill="#3b82f6" fill-opacity="0.1" stroke="#3b82f6" stroke-width="2"/>
  <text x="120" y="42" font-size="12" font-weight="bold" fill="#3b82f6" text-anchor="middle">Input Domain (R^n)</text>
  <rect x="40" y="55" width="160" height="35" rx="6" fill="#ef4444" fill-opacity="0.2" stroke="#ef4444" stroke-width="1.5"/>
  <text x="120" y="77" font-size="11" font-weight="bold" fill="#ef4444" text-anchor="middle">Null Space: A x = 0</text>
  <text x="120" y="115" font-size="9" fill="currentColor" text-anchor="middle">Row Space (Orthogonal to Null Space)</text>

  <!-- Transformation Mapping Arrow -->
  <path d="M 225 75 L 290 75" stroke="currentColor" stroke-width="2" marker-end="url(#arr)" opacity="0.6"/>
  <text x="257" y="65" font-size="11" font-weight="bold" fill="#8b5cf6" text-anchor="middle">Matrix A</text>

  <!-- Output Codomain Space R^m -->
  <rect x="295" y="20" width="205" height="110" rx="10" fill="#10b981" fill-opacity="0.1" stroke="#10b981" stroke-width="2"/>
  <text x="397" y="42" font-size="12" font-weight="bold" fill="#10b981" text-anchor="middle">Output Codomain (R^m)</text>
  <rect x="315" y="55" width="165" height="35" rx="6" fill="#10b981" fill-opacity="0.25" stroke="#10b981" stroke-width="1.5"/>
  <text x="397" y="77" font-size="11" font-weight="bold" fill="#10b981" text-anchor="middle">Column Space: Col(A)</text>
  <circle cx="397" cy="115" r="4" fill="#ef4444"/>
  <text x="410" y="118" font-size="10" fill="#ef4444">Zero Vector 0</text>
</svg>""",
                            "caption": "All vectors in the Null Space collapse to the single point $\\mathbf{0}$. The Column Space is the entire subspace of outputs reachable by $A\\mathbf{x}$."
                        },
                        "points": [
                            "A system of linear equations (like $2x + 3y = 8$ and $4x - y = 2$) is traditionally viewed as intersecting lines. In linear algebra, we view it as a single vector equation: $x \\begin{bmatrix} 2 \\\\ 4 \\end{bmatrix} + y \\begin{bmatrix} 3 \\\\ -1 \\end{bmatrix} = \\begin{bmatrix} 8 \\\\ 2 \\end{bmatrix}$ ($A\\mathbf{x} = \\mathbf{b}$).",
                            "The Column Space $\\text{Col}(A)$ is the span of all column vectors in matrix $A$. The equation $A\\mathbf{x} = \\mathbf{b}$ has a solution if and only if target vector $\\mathbf{b}$ lies inside the Column Space of $A$!",
                            "The Null Space (Kernel) $\\text{Null}(A)$ is the set of all input vectors $\\mathbf{x}$ that get squashed to the zero vector: $A\\mathbf{x} = \\mathbf{0}$.",
                            "The Rank of a matrix is the dimension of its Column Space (the number of linearly independent columns). The Rank-Nullity Theorem proves that: $\\text{Rank}(A) + \\text{Nullity}(A) = n$ (total number of input columns)."
                        ]
                    },
                    {
                        "title": "Gaussian Elimination, Row Echelon Form & Pivots",
                        "points": [
                            "Gaussian Elimination solves $A\\mathbf{x} = \\mathbf{b}$ by systematically applying 3 elementary row operations: (1) Swapping rows, (2) Multiplying a row by a non-zero scalar, and (3) Adding a multiple of one row to another.",
                            "These operations transform the augmented matrix into Row Echelon Form (an upper-triangular staircase of leading non-zero entries called Pivots).",
                            "The number of non-zero pivots in echelon form equals the exact mathematical Rank of the matrix.",
                            "Variables corresponding to pivot columns are Basic Variables; variables corresponding to non-pivot columns are Free Variables (which parametrize infinite solution families)."
                        ]
                    },
                    {
                        "title": "Underdetermined vs. Overdetermined Systems & Least Squares",
                        "points": [
                            "Underdetermined Systems (more unknowns than equations, $m < n$): usually have infinitely many solutions. The minimal-norm solution is found using the pseudoinverse.",
                            "Overdetermined Systems (more equations than unknowns, $m > n$, e.g. fitting 100 noisy data points to a 2-parameter line): usually have NO exact solution because $\\mathbf{b}$ does not lie in $\\text{Col}(A)$.",
                            "The Method of Least Squares finds the best approximate vector $\\mathbf{\\hat{x}}$ that minimizes the squared error $\\|A\\mathbf{x} - \\mathbf{b}\\|^2$. It projects $\\mathbf{b}$ orthogonally onto $\\text{Col}(A)$ by solving the Normal Equations: $A^T A \\mathbf{\\hat{x}} = A^T \\mathbf{b} \\implies \\mathbf{\\hat{x}} = (A^T A)^{-1} A^T \\mathbf{b}$."
                        ]
                    }
                ],
                "trivia": [
                    {
                        "type": "multiple_choice",
                        "question": "What is the 'Column Space' (or Range / Image) of a matrix A?",
                        "options": [
                            "The set of all possible output vectors reachable by taking linear combinations of the columns of A (the span of its columns)",
                            "The set of all vectors that multiply with A to yield zero",
                            "The sum of all numbers in the first column of A",
                            "The diagonal elements of the inverse matrix"
                        ],
                        "correct": 0,
                        "explanation": "The column space $\\text{Col}(A)$ is the subspace formed by all linear combinations of the columns of $A$, representing all possible outputs $A\\mathbf{x}$."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the 'Null Space' (or Kernel) of a matrix A?",
                        "options": [
                            "The set of all input vectors x that satisfy the homogeneous equation A x = 0",
                            "The set of all vectors that have length equal to 0",
                            "The memory space in RAM that has been deallocated",
                            "The collection of eigenvalues that are equal to 1"
                        ],
                        "correct": 0,
                        "explanation": "The null space $\\text{Null}(A)$ consists of all vectors $\\mathbf{x}$ mapped to the zero vector by matrix $A$ ($A\\mathbf{x} = \\mathbf{0}$)."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What fundamental relationship is established by the Rank-Nullity Theorem for an m x n matrix A?",
                        "options": [
                            "Rank(A) + Nullity(A) = n (the total number of columns / input dimensions)",
                            "Rank(A) * Nullity(A) = m * n",
                            "Rank(A) = Nullity(A) - 1",
                            "Rank(A) + Nullity(A) = det(A)"
                        ],
                        "correct": 0,
                        "explanation": "The Rank-Nullity theorem states that the dimension of the column space plus the dimension of the null space equals the total number of input columns $n$."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "When does the linear system A x = b have at least one valid solution?",
                        "options": [
                            "When the target vector b lies within the Column Space of matrix A",
                            "When the determinant of A is equal to 0",
                            "When matrix A is symmetric and positive definite",
                            "When the vector b is orthogonal to all rows of A"
                        ],
                        "correct": 0,
                        "explanation": "Because $A\\mathbf{x}$ is a linear combination of the columns of $A$, a solution $\\mathbf{x}$ exists if and only if vector $\\mathbf{b}$ belongs to $\\text{Col}(A)$."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What are the 'Normal Equations' used to find the Least Squares solution for overdetermined systems (A x ~= b)?",
                        "options": [
                            "A^T A x = A^T b",
                            "A x = b",
                            "A A^T x = b",
                            "det(A) x = b"
                        ],
                        "correct": 0,
                        "explanation": "The normal equations $A^T A \\mathbf{\\hat{x}} = A^T \\mathbf{b}$ project vector $\\mathbf{b}$ orthogonally onto the column space of $A$, minimizing the Euclidean residual error $\\|A\\mathbf{x} - \\mathbf{b}\\|^2$."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the 'Rank' of a matrix?",
                        "options": [
                            "The maximum number of linearly independent column vectors (or row vectors) in the matrix",
                            "The total count of non-zero numbers in the matrix",
                            "The physical number of rows multiplied by columns",
                            "The largest single numerical value in the matrix"
                        ],
                        "correct": 0,
                        "explanation": "The rank of a matrix is the dimension of the subspace spanned by its columns, which always equals the dimension of the subspace spanned by its rows."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is a 'Full Rank' square n x n matrix?",
                        "options": [
                            "A matrix whose rank equals n, meaning all columns are linearly independent and the matrix is fully invertible",
                            "A matrix containing only numbers greater than zero",
                            "A matrix with rank equal to 0",
                            "A matrix whose determinant is equal to zero"
                        ],
                        "correct": 0,
                        "explanation": "A full-rank $n \\times n$ matrix has rank $n$; its determinant is non-zero, its null space contains only $\\{\\mathbf{0}\\}$, and it is fully invertible."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "In Gaussian elimination, what is a 'Pivot'?",
                        "options": [
                            "The first non-zero element in a row used to eliminate the values below it",
                            "The center coordinate of an image rotation",
                            "The last column of the augmented matrix",
                            "The determinant divided by the trace"
                        ],
                        "correct": 0,
                        "explanation": "A pivot is the leading non-zero coefficient in a row during Gaussian elimination, used to clear out non-zero entries in the column beneath it."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What characterizes an 'Overdetermined' system of linear equations?",
                        "options": [
                            "There are more equations (constraints) than variables (unknowns), m > n",
                            "There are more unknowns than equations, n > m",
                            "The determinant of the coefficient matrix is negative",
                            "All variables are constrained to integer values"
                        ],
                        "correct": 0,
                        "explanation": "An overdetermined system has more equations ($m$) than variables ($n$); in real-world data with noise, an exact solution rarely exists, requiring Least Squares approximation."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What characterizes an 'Underdetermined' system of linear equations with full row rank (m < n)?",
                        "options": [
                            "There are fewer equations than unknowns, resulting in infinitely many possible solutions",
                            "There is strictly no mathematical solution possible",
                            "There is exactly one unique solution",
                            "The matrix determinant is always equal to 1.0"
                        ],
                        "correct": 0,
                        "explanation": "Underdetermined systems have fewer equations than unknowns ($m < n$); because there are free variables, there are infinitely many solutions forming an affine subspace."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the geometric relationship between the Row Space and the Null Space of a matrix A?",
                        "options": [
                            "They are orthogonal complements in R^n (every vector in the null space is perpendicular to every vector in the row space)",
                            "They are identical subspaces",
                            "They span opposite quadrants of the coordinate system",
                            "Their intersection is the entire vector space R^n"
                        ],
                        "correct": 0,
                        "explanation": "Because $A\\mathbf{x} = \\mathbf{0}$ means every row of $A$ dotted with $\\mathbf{x}$ equals zero, the Null Space is the exact orthogonal complement of the Row Space in $\\mathbb{R}^n$."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What does Reduced Row Echelon Form (RREF) achieve?",
                        "options": [
                            "A staircase matrix form where every pivot is 1.0 and is the only non-zero entry in its column",
                            "A diagonal matrix with only negative values",
                            "A matrix converted into complex numbers",
                            "A matrix whose row sum is zero"
                        ],
                        "correct": 0,
                        "explanation": "In RREF, each leading pivot is 1, and all other entries in pivot columns are cleared to 0, making the solution to the system immediately readable."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the Moore-Penrose Pseudoinverse (A+) used for?",
                        "options": [
                            "Generalizing matrix inversion to non-square or singular matrices to solve linear least squares problems",
                            "Inverting 1x1 scalar numbers",
                            "Rotating 3D vectors around the Z axis",
                            "Encrypting cryptographic hash digests"
                        ],
                        "correct": 0,
                        "explanation": "The pseudoinverse $A^+$ provides a generalized inverse for any $m \\times n$ matrix, computing the minimum-norm least-squares solution $\\mathbf{\\hat{x}} = A^+ \\mathbf{b}$."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "If a 3x3 matrix has Rank = 2, what geometric shape is formed by its Column Space in 3D space?",
                        "options": [
                            "A 2D flat plane passing through the origin",
                            "A 1D straight line",
                            "The full 3D space",
                            "A single isolated point at [0, 0, 0]"
                        ],
                        "correct": 0,
                        "explanation": "Rank represents the dimension of the column space; a rank of 2 in 3D space spans a 2-dimensional flat plane passing through the origin."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What are 'Free Variables' in a system of linear equations?",
                        "options": [
                            "Variables corresponding to non-pivot columns that can be assigned any arbitrary scalar value to generate solutions",
                            "Variables that are not defined in the source code",
                            "Variables that have no memory address in RAM",
                            "Constants that cannot be multiplied by numbers"
                        ],
                        "correct": 0,
                        "explanation": "Free variables correspond to columns without pivots in echelon form; they can take any real value and parametrize the infinite solution set."
                    }
                ]
            },

            # =================================================================
            # MODULE 4: Eigenvalues, Eigenvectors & PCA
            # =================================================================
            {
                "id": "eigenvalues_eigenvectors_pca",
                "title": "4. Eigenvalues, Eigenvectors & Diagonalization",
                "description": "Understanding axes that do not rotate during linear transformations, the characteristic equation, spectral decomposition, and Principal Component Analysis (PCA).",
                "cards": [
                    {
                        "title": "What are Eigenvectors? Invariant Directions of Space",
                        "figure": {
                            "title": "Eigenvector Direction Preservation: A v = λ v",
                            "svg": """<svg viewBox="0 0 520 150" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-height:150px;">
  <!-- Non-eigenvector vector (rotates) -->
  <g transform="translate(40,20)">
    <line x1="20" y1="100" x2="80" y2="30" stroke="currentColor" stroke-width="2" opacity="0.4"/>
    <line x1="20" y1="100" x2="110" y2="50" stroke="#ec4899" stroke-width="3"/>
    <polygon points="106,46 116,51 108,56" fill="#ec4899"/>
    <text x="70" y="120" font-size="10" fill="#ec4899" text-anchor="middle">Normal Vector: Rotates!</text>
  </g>

  <!-- Eigenvector vector (only scales!) -->
  <g transform="translate(260,20)">
    <!-- Original line of action -->
    <line x1="0" y1="120" x2="220" y2="10" stroke="#8b5cf6" stroke-width="1.5" stroke-dasharray="3,3" opacity="0.4"/>

    <!-- Original eigenvector v -->
    <line x1="20" y1="110" x2="80" y2="80" stroke="#3b82f6" stroke-width="3"/>
    <polygon points="76,76 86,77 80,86" fill="#3b82f6"/>
    <text x="50" y="70" font-size="11" font-weight="bold" fill="#3b82f6">Vector v</text>

    <!-- Transformed A*v = λ v -->
    <line x1="20" y1="110" x2="170" y2="35" stroke="#10b981" stroke-width="3"/>
    <polygon points="166,31 176,32 170,41" fill="#10b981"/>
    <text x="130" y="25" font-size="11" font-weight="bold" fill="#10b981">A v = λ v (Scaled along same line!)</text>
  </g>
</svg>""",
                            "caption": "Most vectors change direction when multiplied by a matrix. An Eigenvector $\\mathbf{v}$ stays on its original line of action, merely scaling by factor $\\lambda$."
                        },
                        "points": [
                            "When a matrix transforms space, almost every vector gets knocked off its original span line and rotated to a new direction.",
                            "However, special invariant directions exist where vectors do NOT rotate at all — they are simply stretched, squashed, or flipped along their original line of action! These special vectors are called Eigenvectors $(\\mathbf{v})$, and the scaling factor is the Eigenvalue $(\\lambda)$: $A\\mathbf{v} = \\lambda \\mathbf{v}$.",
                            "To find eigenvalues, we rewrite the equation as $(A - \\lambda I)\\mathbf{v} = \\mathbf{0}$. For a non-zero vector $\\mathbf{v}$ to exist in the null space, the matrix $(A - \\lambda I)$ must be singular: $\\det(A - \\lambda I) = 0$ (The Characteristic Polynomial).",
                            "Solving $\\det(A - \\lambda I) = 0$ yields the eigenvalues $\\lambda_1, \\lambda_2, \\dots, \\lambda_n$. Substituting each $\\lambda$ back into $(A - \\lambda I)\\mathbf{v} = \\mathbf{0}$ yields the corresponding eigenvector directions."
                        ]
                    },
                    {
                        "title": "Matrix Diagonalization & Powers of Matrices",
                        "points": [
                            "If an $n \\times n$ matrix $A$ has $n$ linearly independent eigenvectors, we can assemble them as the columns of matrix $P$, and assemble the eigenvalues into diagonal matrix $D$. This yields Matrix Diagonalization: $A = P D P^{-1}$.",
                            "Diagonalization changes coordinate systems: $P^{-1}$ translates vectors into the 'eigenvector basis', $D$ performs pure coordinate scaling by $\\lambda_i$, and $P$ converts back to the standard basis.",
                            "Computing high powers of matrices becomes trivial: $A^k = (P D P^{-1})^k = P D^k P^{-1}$. Instead of performing $k$ heavy matrix multiplications, we simply compute $\\lambda_i^k$ along the diagonal of $D$!"
                        ]
                    },
                    {
                        "title": "The Spectral Theorem & Principal Component Analysis (PCA)",
                        "points": [
                            "The Spectral Theorem for Real Symmetric Matrices: If $A = A^T$, then (1) All eigenvalues are guaranteed to be real numbers, and (2) All eigenvectors are mutually orthogonal and form an orthonormal basis: $A = Q D Q^T$.",
                            "Principal Component Analysis (PCA): In machine learning, high-dimensional datasets (e.g. 1000 features per user) contain heavy correlations. PCA computes the Covariance Matrix $\\Sigma = \\frac{1}{N} X^T X$, which is always real and symmetric.",
                            "The eigenvectors of $\\Sigma$ (Principal Components) point in the directions of maximum data variance! The largest eigenvalue $\\lambda_1$ corresponds to the 1st principal component. By projecting data onto the top $k$ eigenvectors, engineers compress 1,000 dimensions down to 2 or 3 while preserving 99% of information."
                        ]
                    }
                ],
                "trivia": [
                    {
                        "type": "multiple_choice",
                        "question": "What is the defining algebraic equation for an eigenvector v and eigenvalue lambda of matrix A?",
                        "options": [
                            "A v = lambda v",
                            "A + v = lambda",
                            "A v = 0",
                            "det(A) = lambda v"
                        ],
                        "correct": 0,
                        "explanation": "An eigenvector $\\mathbf{v}$ multiplied by matrix $A$ yields a vector pointing along the exact same line, scaled by scalar eigenvalue $\\lambda$: $A\\mathbf{v} = \\lambda\\mathbf{v}$."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "How do you calculate the eigenvalues of a square matrix A?",
                        "options": [
                            "By solving the characteristic polynomial equation det(A - lambda I) = 0 for lambda",
                            "By taking the average of all matrix diagonal entries",
                            "By calculating the matrix inverse A^-1",
                            "By dividing the matrix trace by the matrix rank"
                        ],
                        "correct": 0,
                        "explanation": "Setting the determinant of $(A - \\lambda I)$ to zero guarantees a non-trivial null space, producing the characteristic polynomial whose roots are the eigenvalues."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What does the Spectral Theorem guarantee for any real symmetric matrix (A = A^T)?",
                        "options": [
                            "All eigenvalues are real numbers, and there exists an orthonormal basis of eigenvectors (A = Q D Q^T)",
                            "All eigenvalues are equal to 0",
                            "The matrix determinant is always negative",
                            "The matrix cannot be diagonalized"
                        ],
                        "correct": 0,
                        "explanation": "The Spectral Theorem proves that every real symmetric matrix has strictly real eigenvalues and can be orthogonally diagonalized as $A = Q D Q^T$ with mutually perpendicular eigenvectors."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "In Principal Component Analysis (PCA), what do the eigenvectors of the data covariance matrix represent?",
                        "options": [
                            "The orthogonal axes of maximum variance in the dataset (the principal components)",
                            "The mean coordinates of all data clusters",
                            "The outlier data points that must be deleted",
                            "The learning rate hyperparameter of the neural network"
                        ],
                        "correct": 0,
                        "explanation": "The eigenvectors of the covariance matrix point along the axes where data spreads the most (maximum variance), enabling optimal dimensionality reduction."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Why is matrix diagonalization (A = P D P^-1) computationally advantageous when computing matrix powers A^100?",
                        "options": [
                            "Because A^100 = P D^100 P^-1, which only requires raising the individual diagonal eigenvalue entries to the 100th power",
                            "Because it converts the matrix into a single scalar integer",
                            "Because it eliminates the need for floating point multiplication",
                            "Because it guarantees all matrix entries become zero"
                        ],
                        "correct": 0,
                        "explanation": "Raising a diagonal matrix $D$ to power $k$ simply raises each diagonal eigenvalue to $\\lambda_i^k$, avoiding $k$ expensive $O(n^3)$ matrix multiplications."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the relationship between the eigenvalues of a matrix and its determinant det(A)?",
                        "options": [
                            "The determinant equals the product of all eigenvalues (det(A) = lambda_1 * lambda_2 * ... * lambda_n)",
                            "The determinant equals the sum of all eigenvalues",
                            "The determinant equals the largest eigenvalue squared",
                            "There is no mathematical relationship between them"
                        ],
                        "correct": 0,
                        "explanation": "The determinant of a matrix is identical to the product of its eigenvalues: $\\det(A) = \\prod_{i=1}^n \\lambda_i$."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the relationship between the eigenvalues of a matrix and its Trace Tr(A)?",
                        "options": [
                            "The trace equals the sum of all eigenvalues (Tr(A) = lambda_1 + lambda_2 + ... + lambda_n)",
                            "The trace equals the product of all eigenvalues",
                            "The trace equals the smallest eigenvalue",
                            "The trace is always equal to 0"
                        ],
                        "correct": 0,
                        "explanation": "The trace of a square matrix (the sum of its main diagonal entries) is always equal to the sum of all its eigenvalues: $\\text{Tr}(A) = \\sum_{i=1}^n \\lambda_i$."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What does an eigenvalue of lambda = 0 indicate about a matrix?",
                        "options": [
                            "The matrix is singular (det = 0) and has a non-trivial null space containing the corresponding eigenvector",
                            "The matrix is an identity matrix",
                            "The matrix cannot be multiplied by vectors",
                            "All matrix entries are equal to zero"
                        ],
                        "correct": 0,
                        "explanation": "If $\\lambda = 0$, then $A\\mathbf{v} = 0 \\mathbf{v} = \\mathbf{0}$, proving that $\\mathbf{v}$ is a non-zero vector in the null space, meaning $\\det(A) = 0$ (singular)."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What are the eigenvalues of an Identity Matrix I?",
                        "options": [
                            "All eigenvalues are equal to 1.0",
                            "All eigenvalues are equal to 0.0",
                            "The eigenvalues are infinite",
                            "The eigenvalues are pure imaginary numbers"
                        ],
                        "correct": 0,
                        "explanation": "Because $I\\mathbf{v} = 1 \\mathbf{v}$ for every vector in the space, every non-zero vector is an eigenvector with eigenvalue $\\lambda = 1$."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What does it mean if a 2x2 rotation matrix has complex eigenvalues (e.g. lambda = cos(theta) +/- i sin(theta))?",
                        "options": [
                            "There are no real lines in the 2D plane that maintain their direction during the rotation",
                            "The matrix is mathematically invalid",
                            "The vector lengths shrink to zero",
                            "The matrix determinant is negative"
                        ],
                        "correct": 0,
                        "explanation": "A pure rotation (by an angle other than $0^\\circ$ or $180^\\circ$) rotates every real vector in 2D space; hence, no real eigenvectors exist, resulting in complex conjugate eigenvalues."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is an 'Eigenspace' corresponding to eigenvalue lambda?",
                        "options": [
                            "The set of all eigenvectors associated with lambda together with the zero vector (the null space of A - lambda I)",
                            "The bounding box of the dataset in machine learning",
                            "The physical area of the matrix memory buffer",
                            "The set of eigenvalues that are positive"
                        ],
                        "correct": 0,
                        "explanation": "The eigenspace $E_\\lambda = \\text{Null}(A - \\lambda I)$ is the linear subspace formed by all eigenvectors associated with $\\lambda$ plus the zero vector."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is a 'Positive Definite Matrix'?",
                        "options": [
                            "A symmetric matrix where x^T A x > 0 for all non-zero vectors x (all eigenvalues are strictly positive)",
                            "A matrix containing only positive integers",
                            "A matrix whose determinant is equal to +1",
                            "A matrix with more rows than columns"
                        ],
                        "correct": 0,
                        "explanation": "A symmetric matrix is positive definite if all its eigenvalues are strictly positive ($\\lambda_i > 0$), guaranteeing that quadratic forms $\\mathbf{x}^T A \\mathbf{x}$ act like convex bowls in optimization."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What algorithm used by Google in its original search engine is fundamentally an eigenvector calculation of a massive web link matrix?",
                        "options": [
                            "PageRank Algorithm",
                            "Dijkstra Shortest Path",
                            "Binary Search",
                            "QuickSort Algorithm"
                        ],
                        "correct": 0,
                        "explanation": "Google's PageRank computes the dominant eigenvector (with eigenvalue $\\lambda = 1$) of the Markov transition matrix representing web hyperlink probabilities (via the Power Iteration method)."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the 'Power Iteration' method in numerical linear algebra?",
                        "options": [
                            "An algorithm that repeatedly multiplies a random vector by matrix A to converge to the eigenvector with the largest eigenvalue",
                            "A hardware technique to reduce CPU power consumption",
                            "A method to solve systems of linear inequalities",
                            "An algorithm that computes the square root of matrix entries"
                        ],
                        "correct": 0,
                        "explanation": "Power iteration repeatedly applies $A\\mathbf{x}_{k+1} = \\frac{A\\mathbf{x}_k}{\\|A\\mathbf{x}_k\\|}$; because the dominant eigenvalue grows fastest, $\\mathbf{x}$ rapidly converges to the dominant eigenvector."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "When can a square matrix NOT be diagonalized (is 'Defective')?",
                        "options": [
                            "When it does not have enough linearly independent eigenvectors to form a full basis (geometric multiplicity < algebraic multiplicity)",
                            "When its determinant is a prime number",
                            "When all its entries are floating-point numbers",
                            "When it is multiplied by a diagonal matrix"
                        ],
                        "correct": 0,
                        "explanation": "A defective matrix lacks a full set of $n$ linearly independent eigenvectors (such as non-zero shear matrices like $\\begin{bmatrix} 1 & 1 \\\\ 0 & 1 \\end{bmatrix}$), preventing standard diagonalization."
                    }
                ]
            },

            # =================================================================
            # MODULE 5: Singular Value Decomposition (SVD) & ML Applications
            # =================================================================
            {
                "id": "svd_matrix_factorizations",
                "title": "5. Singular Value Decomposition (SVD) & ML Applications",
                "description": "The Swiss Army knife of linear algebra: factoring any rectangular matrix into U Sigma V^T, low-rank approximation, recommender systems, and image compression.",
                "cards": [
                    {
                        "title": "The Master Theorem of Linear Algebra: SVD ($A = U \\Sigma V^T$)",
                        "figure": {
                            "title": "Geometric Decomposition: Rotation -> Scaling -> Rotation",
                            "svg": """<svg viewBox="0 0 520 150" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-height:150px;">
  <!-- Circle in V space -->
  <g transform="translate(30,20)">
    <circle cx="50" cy="50" r="40" fill="#3b82f6" fill-opacity="0.15" stroke="#3b82f6" stroke-width="2"/>
    <line x1="50" y1="50" x2="90" y2="50" stroke="#3b82f6" stroke-width="2.5"/>
    <line x1="50" y1="50" x2="50" y2="10" stroke="#10b981" stroke-width="2.5"/>
    <text x="50" y="110" font-size="10" font-weight="bold" fill="#3b82f6" text-anchor="middle">1. Orthonormal V Basis</text>
  </g>

  <!-- Step 1 Arrow: V^T -->
  <path d="M 130 70 L 165 70" stroke="currentColor" stroke-width="2" marker-end="url(#arr)" opacity="0.5"/>
  <text x="147" y="60" font-size="10" font-weight="bold" fill="currentColor">V^T</text>

  <!-- Step 2 Arrow: Sigma -->
  <g transform="translate(180,20)">
    <!-- Ellipse scaled by singular values -->
    <ellipse cx="60" cy="50" rx="55" ry="25" fill="#8b5cf6" fill-opacity="0.15" stroke="#8b5cf6" stroke-width="2"/>
    <line x1="60" y1="50" x2="115" y2="50" stroke="#3b82f6" stroke-width="2.5"/>
    <line x1="60" y1="50" x2="60" y2="25" stroke="#10b981" stroke-width="2.5"/>
    <text x="85" y="42" font-size="9" font-weight="bold" fill="#3b82f6">σ1</text>
    <text x="65" y="32" font-size="9" font-weight="bold" fill="#10b981">σ2</text>
    <text x="60" y="110" font-size="10" font-weight="bold" fill="#8b5cf6" text-anchor="middle">2. Stretch by Σ (σ_i)</text>
  </g>

  <!-- Step 3 Arrow: U -->
  <path d="M 310 70 L 345 70" stroke="currentColor" stroke-width="2" marker-end="url(#arr)" opacity="0.5"/>
  <text x="327" y="60" font-size="10" font-weight="bold" fill="currentColor">U</text>

  <!-- Final Ellipse rotated by U -->
  <g transform="translate(360,20)">
    <g transform="rotate(-30 60 50)">
      <ellipse cx="60" cy="50" rx="55" ry="25" fill="#ec4899" fill-opacity="0.2" stroke="#ec4899" stroke-width="2"/>
      <line x1="60" y1="50" x2="115" y2="50" stroke="#3b82f6" stroke-width="2.5"/>
      <line x1="60" y1="50" x2="60" y2="25" stroke="#10b981" stroke-width="2.5"/>
    </g>
    <text x="60" y="110" font-size="10" font-weight="bold" fill="#ec4899" text-anchor="middle">3. Rotate into U Space</text>
  </g>
</svg>""",
                            "caption": "SVD proves every linear transformation factorizes into three steps: an initial rotation ($V^T$), coordinate axis stretching by singular values ($\\Sigma$), and a final rotation ($U$)."
                        },
                        "points": [
                            "Eigenvalue diagonalization only works on square matrices ($n \\times n$) that have full sets of eigenvectors. What about non-square rectangular matrices ($m \\times n$, like a dataset of 10,000 users $\\times$ 500 movies)?",
                            "Singular Value Decomposition (SVD) is the universal master theorem of linear algebra: ANY real matrix $A$ of size $m \\times n$ can be factored into: $A = U \\Sigma V^T$.",
                            "$U$ is an $m \\times m$ orthogonal matrix (Left Singular Vectors, eigenvectors of $A A^T$). $\\Sigma$ is an $m \\times n$ diagonal matrix holding non-negative Singular Values $\\sigma_1 \\ge \\sigma_2 \\ge \\dots \\ge 0$ in descending order. $V$ is an $n \\times n$ orthogonal matrix (Right Singular Vectors, eigenvectors of $A^T A$).",
                            "Geometrically, SVD shows that ANY linear transformation maps a unit sphere in $\\mathbb{R}^n$ into an ellipsoid in $\\mathbb{R}^m$, where the semi-axis lengths of the ellipsoid are exactly the singular values $\\sigma_i$!"
                        ]
                    },
                    {
                        "title": "Low-Rank Matrix Approximation & The Eckart-Young Theorem",
                        "points": [
                            "SVD allows us to express any matrix as a sum of rank-1 outer products weighted by singular values: $A = \\sum_{i=1}^{r} \\sigma_i \\mathbf{u}_i \\mathbf{v}_i^T$.",
                            "The Eckart-Young-Mirsky Theorem proves that the mathematically optimal rank-$k$ approximation of matrix $A$ (minimizing Frobenius reconstruction error) is obtained simply by keeping the top $k$ largest singular values and discarding the rest ($A_k = \\sum_{i=1}^{k} \\sigma_i \\mathbf{u}_i \\mathbf{v}_i^T$).",
                            "Image Compression: A $1000 \\times 1000$ pixel image requires 1,000,000 numbers. Storing only the top $k=20$ singular values requires only $20 \\times (1000 + 1000 + 1) = 40,020$ numbers — a 96% reduction in storage while retaining nearly crystal-clear visual quality!"
                        ]
                    },
                    {
                        "title": "Recommender Systems (Netflix Prize) & Latent Semantic Analysis (LSA)",
                        "points": [
                            "Collaborative Filtering / Recommender Systems: Consider a massive matrix $A$ where rows are users, columns are movies, and entries are ratings (mostly blank).",
                            "SVD factorizes $A \\approx U_k \\Sigma_k V_k^T$: The rows of $U_k$ become dense embeddings representing user preferences across $k$ 'latent concepts' (e.g. action intensity, romance, sci-fi tone); the rows of $V_k$ represent how strongly each movie embodies those same latent concepts.",
                            "Latent Semantic Analysis (LSA) in NLP uses SVD on term-document frequency matrices to discover underlying semantic topics, clustering synonyms and related concepts automatically from raw text."
                        ]
                    }
                ],
                "trivia": [
                    {
                        "type": "multiple_choice",
                        "question": "What is the mathematical formulation of Singular Value Decomposition (SVD) for any m x n matrix A?",
                        "options": [
                            "A = U Sigma V^T (where U and V are orthogonal matrices and Sigma is a diagonal matrix of non-negative singular values)",
                            "A = P D P^-1",
                            "A = L U",
                            "A = Q R Q^T"
                        ],
                        "correct": 0,
                        "explanation": "SVD factorizes any rectangular matrix $A$ into $U \\Sigma V^T$, where $U$ contains the left singular vectors, $\\Sigma$ contains sorted singular values, and $V^T$ contains right singular vectors."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What does the Eckart-Young-Mirsky Theorem prove regarding Low-Rank Matrix Approximation?",
                        "options": [
                            "The optimal rank-k approximation of a matrix (minimizing reconstruction error) is obtained by truncating the SVD to the top k largest singular values",
                            "Every square matrix has a determinant equal to its trace",
                            "Matrices with rank less than 5 cannot be inverted",
                            "Singular values grow exponentially with matrix dimensions"
                        ],
                        "correct": 0,
                        "explanation": "The Eckart-Young theorem proves that truncating the SVD sum to the top $k$ terms ($A_k = \\sum_{i=1}^k \\sigma_i \\mathbf{u}_i \\mathbf{v}_i^T$) yields the best possible rank-$k$ approximation under both Frobenius and Spectral norms."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "How are the Singular Values (sigma_i) of matrix A related to the eigenvalues of A^T A?",
                        "options": [
                            "The singular values are the non-negative square roots of the eigenvalues of A^T A (sigma_i = sqrt(lambda_i))",
                            "The singular values are equal to the eigenvalues divided by 2",
                            "The singular values are the inverse of the eigenvalues",
                            "There is no mathematical relationship between them"
                        ],
                        "correct": 0,
                        "explanation": "The right singular vectors are the eigenvectors of symmetric matrix $A^T A$, and the singular values are the square roots of its non-negative eigenvalues: $\\sigma_i = \\sqrt{\\lambda_i(A^T A)}$."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "In recommender systems (like the Netflix Prize), what do the low-rank factor matrices U and V represent?",
                        "options": [
                            "Latent feature embeddings capturing user preferences and item/movie characteristics in a shared conceptual space",
                            "The geographic IP addresses of the streaming servers",
                            "The exact timestamps when users clicked the play button",
                            "The cryptographic hash keys of user passwords"
                        ],
                        "correct": 0,
                        "explanation": "Matrix factorization decomposes the sparse rating matrix into dense latent factor vectors: $U$ embeds user preference profiles, and $V$ embeds item characteristics in the same $k$-dimensional latent space."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the 'Condition Number' of an invertible matrix (kappa(A) = sigma_max / sigma_min)?",
                        "options": [
                            "A measure of numerical sensitivity: how much small errors or noise in the input can be magnified in the output solution",
                            "The temperature limit of the physical DRAM chips",
                            "The count of negative numbers in the matrix",
                            "The number of floating point operations per second"
                        ],
                        "correct": 0,
                        "explanation": "The condition number $\\kappa(A) = \\frac{\\sigma_{\\max}}{\\sigma_{\\min}}$ measures numerical stability; an 'ill-conditioned' matrix with a huge condition number magnifies floating-point rounding errors dramatically."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "How can the Moore-Penrose Pseudoinverse (A+) be expressed using the SVD components A = U Sigma V^T?",
                        "options": [
                            "A+ = V Sigma^+ U^T (where Sigma^+ inverts all non-zero singular values 1/sigma_i)",
                            "A+ = U^T Sigma V",
                            "A+ = (U Sigma V^T)^-1",
                            "A+ = Sigma^-1"
                        ],
                        "correct": 0,
                        "explanation": "Using SVD, the pseudoinverse is computed directly as $A^+ = V \\Sigma^+ U^T$, where $\\Sigma^+$ transposes $\\Sigma$ and replaces every non-zero singular value $\\sigma_i$ with $1/\\sigma_i$."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "How many singular values of matrix A are strictly greater than zero?",
                        "options": [
                            "Exactly equal to the mathematical Rank of matrix A",
                            "Always equal to the number of rows m",
                            "Always equal to the number of columns n",
                            "Zero singular values are greater than zero"
                        ],
                        "correct": 0,
                        "explanation": "The number of non-zero singular values $\\sigma_i > 0$ equals the exact rank of matrix $A$ (the dimension of its column space)."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the 'Frobenius Norm' of a matrix ||A||_F?",
                        "options": [
                            "The square root of the sum of the squared values of all matrix entries (equal to sqrt(sum(sigma_i^2)))",
                            "The largest single number in the matrix",
                            "The absolute value of the determinant",
                            "The number of non-zero rows in reduced row echelon form"
                        ],
                        "correct": 0,
                        "explanation": "The Frobenius norm $\\|A\\|_F = \\sqrt{\\sum_{i,j} A_{ij}^2}$ measures overall matrix magnitude, and equals the Euclidean norm of its singular value vector $\\sqrt{\\sum_{i} \\sigma_i^2}$."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "In Latent Semantic Analysis (LSA) for natural language processing, what matrix is decomposed using SVD?",
                        "options": [
                            "A Term-Document Frequency Matrix (where rows are vocabulary words and columns are documents)",
                            "A network routing table of IP addresses",
                            "A matrix of binary ASCII character codes",
                            "A database schema table of user IDs"
                        ],
                        "correct": 0,
                        "explanation": "LSA applies truncated SVD to a term-document frequency matrix (e.g. TF-IDF), mapping words and documents into a shared continuous semantic space."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Why does SVD work on ANY arbitrary rectangular matrix, unlike standard eigenvalue diagonalization?",
                        "options": [
                            "Because A A^T and A^T A are always symmetric and positive semi-definite, guaranteeing real, non-negative singular values",
                            "Because rectangular matrices have more rows than columns",
                            "Because SVD does not use floating point numbers",
                            "Because SVD converts all matrix numbers to zero"
                        ],
                        "correct": 0,
                        "explanation": "For any real matrix $A$, the products $A^T A$ and $A A^T$ are always real, symmetric, and positive semi-definite, ensuring orthogonal bases $U, V$ and real non-negative singular values exist unconditionally."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What geometric shape does a unit sphere in R^n become after being mapped by a linear transformation A with SVD singular values sigma_1, sigma_2, ...?",
                        "options": [
                            "A Hyper-Ellipsoid in R^m whose principal semi-axes have lengths equal to the singular values sigma_i",
                            "A perfect cube with side length equal to det(A)",
                            "A 1-dimensional line segment",
                            "A flat triangle passing through the origin"
                        ],
                        "correct": 0,
                        "explanation": "SVD shows geometrically that any matrix transformation maps an $n$-dimensional unit sphere into an $m$-dimensional hyper-ellipsoid with axis lengths $\\sigma_1, \\sigma_2, \\dots, \\sigma_r$."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is 'QR Decomposition' of a matrix A?",
                        "options": [
                            "Factoring A into an Orthogonal matrix Q (Q^T Q = I) and an Upper Triangular matrix R",
                            "Dividing matrix A into four equal quadrants",
                            "Computing the square root of matrix A",
                            "Multiplying matrix A by a quantum random number"
                        ],
                        "correct": 0,
                        "explanation": "QR factorization decomposes a matrix into an orthogonal matrix $Q$ (obtained via Gram-Schmidt or Householder reflections) and an upper-triangular matrix $R$, widely used for stable least squares."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is 'LU Decomposition' of a square matrix A?",
                        "options": [
                            "Factoring A into a Lower Triangular matrix L and an Upper Triangular matrix U (A = L U)",
                            "Factoring A into a Left matrix and an Ultra matrix",
                            "Decomposing A into floating point exponent and mantissa",
                            "Translating A into a linear equation"
                        ],
                        "correct": 0,
                        "explanation": "LU decomposition encodes Gaussian elimination into matrix form: $L$ stores elimination multipliers in a lower-triangular matrix, and $U$ is the resulting upper-triangular echelon form."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is 'Cholesky Decomposition' for a symmetric positive-definite matrix A?",
                        "options": [
                            "Factoring A into the product of a lower triangular matrix and its transpose: A = L L^T",
                            "Factoring A into three diagonal matrices",
                            "Approximating A with random Gaussian noise",
                            "Inverting A by computing its determinant"
                        ],
                        "correct": 0,
                        "explanation": "For symmetric positive-definite matrices, Cholesky decomposition computes $A = L L^T$ in roughly half the computational operations of standard LU decomposition, widely used in Kalman filters and Gaussian processes."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the primary trade-off when choosing the truncation rank k in Low-Rank Matrix Compression?",
                        "options": [
                            "Smaller k gives greater compression and memory savings, but discards more fine details and increases reconstruction error",
                            "Smaller k increases the time needed to invert the matrix",
                            "Larger k causes the singular values to become negative numbers",
                            "Larger k changes the physical font size of the text"
                        ],
                        "correct": 0,
                        "explanation": "Choosing rank $k$ balances compression vs fidelity: smaller $k$ saves massive memory by storing fewer vectors, while larger $k$ captures subtle nuances at the cost of higher storage."
                    }
                ]
            }
        ]
    }

    # -------------------------------------------------------------------------
    # HEBREW LINEAR ALGEBRA DATASET
    # -------------------------------------------------------------------------
    la_he = {
        "id": "linalg_101_he",
        "type": "academic",
        "icon": "📐",
        "title": "אלגברה לינארית וגאומטריה לבינה מלאכותית והנדסה (LinAlg 101)",
        "description": "מדריך ויזואלי ומעמיק מעקרונות ראשונים: כיצד וקטורים פורשים ממדים, כיצד מטריצות מעוותות את המרחב, וכיצד ערכים עצמיים ופירוק SVD מניעים בינה מלאכותית, למידת מכונה וגרפיקה ממוחשבת.",
        "lang": "he",
        "audience": "family",
        "categories": [
            # =================================================================
            # MODULE 1: Vectors, Dot Products & Spatial Projections
            # =================================================================
            {
                "id": "vectors_spaces_projections",
                "title": "1. וקטורים, מכפלה סקלרית והטלות מרחביות",
                "description": "הבנת וקטורים כחצי העתקה גאומטריים במרחב, מכפלה סקלרית כהטלת צל ומדד זוויתי, תלות לינארית, ומרחב פרישה אורתוגונלי.",
                "cards": [
                    {
                        "title": "מהו וקטור? חצים במרחב לעומת רשימות מספרים",
                        "figure": {
                            "title": "חיבור וקטורים והטלת מכפלה סקלרית",
                            "svg": """<svg viewBox="0 0 520 150" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-height:150px;">
  <line x1="30" y1="120" x2="480" y2="120" stroke="currentColor" stroke-width="1.5" opacity="0.3"/>
  <line x1="60" y1="10" x2="60" y2="140" stroke="currentColor" stroke-width="1.5" opacity="0.3"/>

  <line x1="60" y1="120" x2="260" y2="120" stroke="#3b82f6" stroke-width="3"/>
  <polygon points="260,116 270,120 260,124" fill="#3b82f6"/>
  <text x="160" y="140" font-size="12" font-weight="bold" fill="#3b82f6" text-anchor="middle">וקטור v</text>

  <line x1="60" y1="120" x2="200" y2="30" stroke="#8b5cf6" stroke-width="3"/>
  <polygon points="196,26 206,30 202,38" fill="#8b5cf6"/>
  <text x="120" y="65" font-size="12" font-weight="bold" fill="#8b5cf6">וקטור u</text>

  <line x1="200" y1="30" x2="200" y2="120" stroke="#ec4899" stroke-width="2" stroke-dasharray="4,4"/>

  <rect x="60" y="116" width="140" height="8" fill="#10b981" fill-opacity="0.5"/>
  <text x="130" y="110" font-size="10" font-weight="bold" fill="#10b981" text-anchor="middle">הטלה: ||u|| cos(θ)</text>
  <text x="360" y="75" font-size="12" font-weight="bold" fill="currentColor">u · v = ||u|| ||v|| cos(θ)</text>
</svg>""",
                            "caption": "מכפלה סקלרית מודדת התאמה כיוונית: היא מטילה את וקטור $\\mathbf{u}$ על גבי וקטור $\\mathbf{v}$ ומכפילה את אורכיהם."
                        },
                        "points": [
                            "עבור מפתח תוכנה, וקטור הוא מערך סדור של מספרים (למשל $[3.2, -1.5, 4.0]$). עבור פיזיקאי או מהנדס גרפיקה, וקטור הוא חץ גאומטרי בעל גודל (אורך) וכיוון במרחב.",
                            "חיבור וקטורים $(\\mathbf{u} + \\mathbf{v})$ מתבטא בחיבור חצים קצה-אל-זנב. כפל בסקלר $(c \\mathbf{v})$ מותח, מכווץ או הופך את אורך החץ מבלי לשנות את קו הפעולה שלו במרחב.",
                            "מכפלה סקלרית (Dot Product) משלבת שני וקטורים למספר סקלרי בודד: $\\mathbf{u} \\cdot \\mathbf{v} = u_1 v_1 + u_2 v_2 + \\dots + u_n v_n = \\|\\mathbf{u}\\| \\|\\mathbf{v}\\| \\cos(\\theta)$.",
                            "גאומטרית, מכפלה סקלרית מודדת תיאום כיווני: אם $\\mathbf{u} \\cdot \\mathbf{v} > 0$, הווקטורים מצביעים בכיוון דומה; אם $\\mathbf{u} \\cdot \\mathbf{v} = 0$, הם ניצבים (אורתוגונליים) לחלוטין; ואם $\\mathbf{u} \\cdot \\mathbf{v} < 0$, הם פונים בכיוונים מנוגדים."
                        ]
                    },
                    {
                        "title": "צירופים לינאריים, פרישה (Span) ותלות לינארית",
                        "points": [
                            "צירוף לינארי (Linear Combination) של וקטורים $\\mathbf{v}_1, \\dots, \\mathbf{v}_k$ הוא כל וקטור הנוצר על ידי הכפלתם בסקלרים וחיבורם: $c_1 \\mathbf{v}_1 + \\dots + c_k \\mathbf{v}_k$.",
                            "מרחב הפרישה (Span) של קבוצת וקטורים הוא תת-המרחב הגאומטרי של כל הווקטורים שניתן להגיע אליהם באמצעות צירופים לינאריים. שני וקטורים שאינם מקבילים פורשים את כל המישור הדו-ממדי $\\mathbb{R}^2$.",
                            "תלות לינארית: קבוצת וקטורים תלויה לינארית אם ניתן לבנות לפחות וקטור אחד מתוכה כצירוף לינארי של שאר הווקטורים (הוא אינו מוסיף ממד חדש).",
                            "בסיס (Basis) למרחב וקטורי הוא קבוצה מינימלית של וקטורים בלתי תלויים לינארית הפורשת את המרחב כולו (למשל וקטורי היחידה הסטנדרטיים $\\hat{i} = [1, 0]$ ו-$\\hat{j} = [0, 1]$)."
                        ]
                    },
                    {
                        "title": "הטלות אורתוגונליות ותהליך גרם-שמידט",
                        "points": [
                            "הטלה אורתוגונלית של וקטור $\\mathbf{b}$ על גבי וקטור $\\mathbf{a}$ מוצאת את הנקודה על $\\mathbf{a}$ הקרובה ביותר ל-$\\mathbf{b}$, ומפרקת את $\\mathbf{b}$ לרכיב מקביל ולרכיב ניצב: $\\text{proj}_{\\mathbf{a}}(\\mathbf{b}) = \\frac{\\mathbf{a} \\cdot \\mathbf{b}}{\\|\\mathbf{a}\\|^2} \\mathbf{a}$.",
                            "הטלה גאומטרית זו היא המנוע המתמטי שמאחורי רגרסיה לינארית, פירוק טורי פורייה, ומנגנוני תשומת לב (Attention) ברשתות נוירונים עמוקות.",
                            "תהליך גרם-שמידט (Gram-Schmidt) לוקח קבוצה של וקטורים בלתי תלויים וממיר אותם באופן שיטתי לבסיס אורתונורמלי (וקטורים שכולם באורך 1.0 וכולם ניצבים הדדית זה לזה)."
                        ]
                    }
                ],
                "trivia": [
                    {
                        "type": "multiple_choice",
                        "question": "איזה מצב גאומטרי מתקיים כאשר המכפלה הסקלרית של שני וקטורים שאינם אפס שווה בדיוק לאפס (u · v = 0)?",
                        "options": [
                            "הווקטורים ניצבים (אורתוגונליים) זה לזה בזווית של 90 מעלות",
                            "הווקטורים מצביעים בדיוק לאותו כיוון",
                            "הווקטורים שווים לחלוטין באורכם המתמטי",
                            "הווקטורים נמצאים מחוץ למערכת הצירים הקרטזית"
                        ],
                        "correct": 0,
                        "explanation": "מכיוון ש-$\\mathbf{u} \\cdot \\mathbf{v} = \\|\\mathbf{u}\\| \\|\\mathbf{v}\\| \\cos(\\theta)$, מכפלה סקלרית ששווה ל-0 מחייבת $\\cos(\\theta) = 0$, כלומר הזווית ביניהם היא בדיוק $90^\\circ$ (ניצבים)."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהו 'מרחב הפרישה' (Span) של קבוצת וקטורים?",
                        "options": [
                            "אוסף כל הווקטורים שניתן לייצר באמצעות צירופים לינאריים (מתיחה וחיבור) של אותם וקטורים",
                            "המרחק הפיזי בין ראשית הצירים לווקטור הארוך ביותר",
                            "מספר הערכים שאינם אפס במערך הנתונים",
                            "הדטרמיננטה של המכפלה הווקטורית"
                        ],
                        "correct": 0,
                        "explanation": "ה-Span של קבוצת וקטורים הוא תת-המרחב הנוצר מכל הצירופים הלינאריים האפשריים $c_1 \\mathbf{v}_1 + \\dots + c_k \\mathbf{v}_k$."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מתי קבוצת וקטורים נחשבת ל'תלויה לינארית' (Linearly Dependent)?",
                        "options": [
                            "כאשר לפחות וקטור אחד בקבוצה ניתן לביטוי כצירוף לינארי של שאר הווקטורים (ממד מיותר)",
                            "כאשר כל הווקטורים שווים באורכם הפיזי",
                            "כאשר הווקטורים כולם ניצבים זה לזה",
                            "כאשר המכפלה הסקלרית של כל זוג היא חיובית"
                        ],
                        "correct": 0,
                        "explanation": "תלות לינארית מעידה על יתירות בקבוצה; לפחות וקטור אחד מוכל כבר בתוך מרחב הפרישה של הווקטורים האחרים ואינו מוסיף ממד חדש."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מה מייצר תהליך גרם-שמידט (Gram-Schmidt) באלגברה לינארית?",
                        "options": [
                            "הוא ממיר בסיס של וקטורים בלתי תלויים לבסיס אורתונורמלי של וקטורי יחידה הניצבים כולם זה לזה",
                            "הוא הופך מטריצה מלבנית באמצעות דירוג גאוס",
                            "הוא מוצא את השורשים של פולינומים ממעלה גבוהה",
                            "הוא דוחס קבצי תמונה בפורמט JPEG"
                        ],
                        "correct": 0,
                        "explanation": "אלגוריתם גרם-שמידט לוקח וקטורים בלתי תלויים ומחסר מהם הטלות מקביליות כדי לבנות בסיס שבו כל הווקטורים ניצבים ובאורך יחידה 1.0."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהי הנוסחה לחישוב האורך האוקלידי (נורמת L2) של וקטור תלת-ממדי v = [x, y, z]?",
                        "options": [
                            "sqrt(x^2 + y^2 + z^2)",
                            "x + y + z",
                            "x * y * z",
                            "max(|x|, |y|, |z|)"
                        ],
                        "correct": 0,
                        "explanation": "על פי משפט פיתגורס המורחב ל-$n$ ממדים, הנורמה האוקלידית שווה לשורש סכום ריבועי האיברים: $\\sqrt{x^2 + y^2 + z^2} = \\sqrt{\\mathbf{v} \\cdot \\mathbf{v}}$."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהו 'וקטור יחידה' (Unit Vector)?",
                        "options": [
                            "וקטור שאורכו (הגודל הגאומטרי שלו) שווה בדיוק ל-1.0",
                            "וקטור המכיל מספרים שלמים בלבד",
                            "מטריצה בעלת אחדות באלכסון הראשי",
                            "וקטור המצביע אך ורק לאורך ציר ה-X החיובי"
                        ],
                        "correct": 0,
                        "explanation": "וקטור יחידה הוא וקטור שעבר נרמול כך שאורכו $\\|\\mathbf{v}\\| = 1$, ומייצג כיוון טהור במרחב ללא תלות בסקאלה."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מה קובע אי-שוויון קושי-שוורץ עבור שני וקטורים ממשיים u ו-v?",
                        "options": [
                            "|u · v| <= ||u|| ||v||",
                            "||u + v|| = ||u|| + ||v||",
                            "u · v >= ||u|| ||v||",
                            "u · v = 0"
                        ],
                        "correct": 0,
                        "explanation": "אי-שוויון קושי-שוורץ $|\\mathbf{u} \\cdot \\mathbf{v}| \\leq \\|\\mathbf{u}\\| \\|\\mathbf{v}\\|$ נובע מכך ש-$|\\cos(\\theta)| \\leq 1$, כאשר שוויון מתקבל רק כאשר הווקטורים מקבילים."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהי התוצאה של מכפלה וקטורית (Cross Product) בין שני וקטורים תלת-ממדיים (u x v)?",
                        "options": [
                            "וקטור תלת-ממדי חדש הניצב בו-זמנית הן ל-u והן ל-v",
                            "מספר סקלרי יחיד המייצג את המכפלה הסקלרית",
                            "מטריצת יחידה אלכסונית בגודל 3x3",
                            "סכום האיברים של שני הווקטורים"
                        ],
                        "correct": 0,
                        "explanation": "המכפלה הווקטורית $\\mathbf{u} \\times \\mathbf{v}$ מפיקה וקטור הניצב למישור שבו שוכנים $\\mathbf{u}$ ו-$\\mathbf{v}$, שאורכו שווה לשטח המקבילית שהם פורשים."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מה מגדיר 'בסיס' (Basis) למרחב וקטורי V?",
                        "options": [
                            "קבוצת וקטורים בלתי תלויים לינארית הפורשת את המרחב V כולו",
                            "כל קבוצת וקטורים בעלי ערכים שלמים",
                            "קבוצת וקטורים שהמכפלות הסקלריות ביניהם כולן שליליות",
                            "נקודת ראשית הצירים [0, 0, 0]"
                        ],
                        "correct": 0,
                        "explanation": "בסיס הוא קבוצת פרישה מינימלית: הווקטורים חייבים להיות בלתי תלויים לינארית ולפרוש את המרחב כולו, מה שמאפשר להציג כל וקטור במרחב כצירוף לינארי יחיד."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "כיצד מטילים וקטור b בצורה אורתוגונלית על גבי ישר המוגדר על ידי וקטור יחידה u (שבו ||u|| = 1)?",
                        "options": [
                            "(b · u) u",
                            "b + u",
                            "b / u",
                            "sqrt(b · u)"
                        ],
                        "correct": 0,
                        "explanation": "כאשר $\\mathbf{u}$ הוא וקטור יחידה, גודל ההטלה הסקלרית הוא $(\\mathbf{b} \\cdot \\mathbf{u})$, והכפלה בכיוון $\\mathbf{u}$ נותנת את וקטור ההטלה $(\\mathbf{b} \\cdot \\mathbf{u}) \\mathbf{u}$."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהו הממד (Dimension) של מרחב וקטורי?",
                        "options": [
                            "מספר הווקטורים המדויק בכל בסיס של אותו מרחב וקטורי",
                            "גודל הזיכרון בבייטים של מערך המספרים",
                            "הדטרמיננטה של מטריצת השונות המשותפת",
                            "הערך המקסימלי של רכיבי הווקטורים"
                        ],
                        "correct": 0,
                        "explanation": "ממד המרחב הווקטורי מוגדר כמספר הווקטורים המרכיבים כל בסיס של אותו מרחב."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהי קבוצת וקטורים 'אורתונורמלית' (Orthonormal)?",
                        "options": [
                            "קבוצה שבה כל וקטור הוא באורך 1.0 וכל זוג וקטורים שונים ניצבים זה לזה (מכפלה סקלרית = 0)",
                            "קבוצת וקטורים בעלי ערכים חיוביים בלבד",
                            "קבוצת וקטורים היוצרת מצולע סגור במרחב",
                            "קבוצת וקטורים שאינה ניתנת להכפלה בסקלרים"
                        ],
                        "correct": 0,
                        "explanation": "קבוצה אורתונורמלית מקיימת שני תנאים: אורתוגונליות (ניצבות הדדית $\\mathbf{u}_i \\cdot \\mathbf{u}_j = 0$ עבור $i \\neq j$) ונורמליות (אורך יחידה $\\|\\mathbf{u}_i\\| = 1$ לכולם)."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "במדד דמיון קוסינוס (Cosine Similarity) המשמש במנועי חיפוש ו-NLP, מה מעיד ערך קוסינוס של 1.0 בין שני וקטורים?",
                        "options": [
                            "הווקטורים מצביעים בדיוק לאותו כיוון במרחב (דמיון סמנטי מקסימלי)",
                            "הווקטורים ניצבים לחלוטין וללא קשר סמנטי",
                            "הווקטורים מייצגים משמעויות מנוגדות לחלוטין",
                            "הווקטורים מכילים שגיאות מספריות"
                        ],
                        "correct": 0,
                        "explanation": "דמיון קוסינוס מגיע ל-1.0 כאשר הזווית ביניהם $\\theta = 0^\\circ$, מה שמעיד על כיוון ומשמעות סמנטית זהה במרחב השיכון."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מה יקרה אם תנסה לפרוש את המרחב התלת-ממדי (R^3) באמצעות 2 וקטורים בלתי תלויים בלבד?",
                        "options": [
                            "2 הווקטורים יפרשו מישור דו-ממדי שטוח בלבד, ויותירו את יתר המרחב התלת-ממדי בלתי נגיש",
                            "2 הווקטורים ייצרו מעצמם וקטור שלישי במרחב",
                            "הדטרמיננטה של הווקטורים תהפוך לאינסופית",
                            "הווקטורים יתעקמו במרחב לא-אוקלידי"
                        ],
                        "correct": 0,
                        "explanation": "ב-$\mathbb{R}^3$, בסיס דורש בדיוק 3 וקטורים בלתי תלויים; שני וקטורים יכולים לפרוש אך ורק מישור דו-ממדי בתוך המרחב התלת-ממדי."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהו וקטור האפס [0, 0, ..., 0] באלגברה לינארית?",
                        "options": [
                            "איבר היחידה לחיבור במרחב הווקטורי, כך ש-v + 0 = v לכל וקטור v",
                            "וקטור שאינו ניתן להכפלה בסקלרים",
                            "וקטור שאורכו המתמטי אינו מוגדר",
                            "וקטור הפורש את כל הממדים בו-זמנית"
                        ],
                        "correct": 0,
                        "explanation": "וקטור האפס הוא איבר היחידה החיבורי במרחב הווקטורי; חיבורו לכל וקטור משאיר את הווקטור ללא שינוי, ואורכו שווה ל-0."
                    }
                ]
            },

            # =================================================================
            # MODULE 2: Matrices as Linear Spatial Transformations
            # =================================================================
            {
                "id": "matrix_transformations_determinants",
                "title": "2. מטריצות כטרנספורמציות מרחביות ודטרמיננטה",
                "description": "הבנת מטריצות לא כטבלאות מספרים משעממות, אלא כפונקציות דינמיות המעוותות את המרחב, מיפוי וקטורי בסיס, והדטרמיננטה כמדד לשינוי שטח ונפח.",
                "cards": [
                    {
                        "title": "מטריצה כטרנספורמציה מרחבית דינמית",
                        "figure": {
                            "title": "כיצד מטריצה 2x2 מעוותת את רשת הצירים",
                            "svg": """<svg viewBox="0 0 520 150" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-height:150px;">
  <g transform="translate(40,20)">
    <rect x="0" y="0" width="100" height="100" fill="#3b82f6" fill-opacity="0.15" stroke="#3b82f6" stroke-dasharray="2,2"/>
    <line x1="0" y1="100" x2="100" y2="100" stroke="#3b82f6" stroke-width="3"/>
    <polygon points="96,96 106,100 96,104" fill="#3b82f6"/>
    <text x="50" y="118" font-size="10" font-weight="bold" fill="#3b82f6" text-anchor="middle">i_hat [1, 0]</text>

    <line x1="0" y1="100" x2="0" y2="0" stroke="#10b981" stroke-width="3"/>
    <polygon points="-4,6 0,-4 4,6" fill="#10b981"/>
    <text x="-8" y="50" font-size="10" font-weight="bold" fill="#10b981" text-anchor="end">j_hat [0, 1]</text>
    <text x="50" y="55" font-size="11" font-weight="bold" fill="currentColor" text-anchor="middle">שטח = 1.0</text>
  </g>

  <path d="M 180 70 L 250 70" stroke="currentColor" stroke-width="2" marker-end="url(#arr)" opacity="0.6"/>
  <text x="215" y="60" font-size="11" font-weight="bold" fill="#8b5cf6" text-anchor="middle">מטריצה A</text>

  <g transform="translate(290,20)">
    <polygon points="0,100 120,70 160,0 40,30" fill="#8b5cf6" fill-opacity="0.2" stroke="#8b5cf6" stroke-width="2"/>
    <line x1="0" y1="100" x2="120" y2="70" stroke="#3b82f6" stroke-width="3"/>
    <polygon points="116,66 126,69 120,76" fill="#3b82f6"/>
    <text x="70" y="100" font-size="10" font-weight="bold" fill="#3b82f6">A * i_hat</text>

    <line x1="0" y1="100" x2="40" y2="30" stroke="#10b981" stroke-width="3"/>
    <polygon points="36,26 44,24 42,34" fill="#10b981"/>
    <text x="10" y="45" font-size="10" font-weight="bold" fill="#10b981">A * j_hat</text>
    <text x="85" y="50" font-size="11" font-weight="bold" fill="#8b5cf6" text-anchor="middle">שטח = |det(A)|</text>
  </g>
</svg>""",
                            "caption": "טרנספורמציה של מטריצה מתוארת במלואה על פי המיקום שאליו עוברים וקטורי הבסיס $\\hat{i}$ ו-$\\hat{j}$. הדטרמיננטה מודדת את יחס שינוי השטח."
                        },
                        "points": [
                            "טרנספורמציה לינארית היא פונקציה גאומטרית $T(\\mathbf{v})$ המעוותת את המרחב תוך שמירה על שני כללים: (1) ראשית הצירים $[0,0]$ נשארת מקובעת במקומה, ו-(2) כל קווי הרשת הישרים נשארים ישרים ומרווחים באופן אחיד.",
                            "ניתן לדעת מה מטריצה תעשה לכל המרחב האינסופי כולו פשוט על ידי מעקב לאן נוחתים וקטורי הבסיס! לאן עובר $\\hat{i} = [1,0]$? זהו עמודה מס' 1 במטריצה. לאן עובר $\\hat{j} = [0,1]$? זהו עמודה מס' 2.",
                            "כפל מטריצה בווקטור $A\\mathbf{x}$ הוא פשוט מתיחה וחיבור של וקטורי הבסיס שהותמרו: $A \\begin{bmatrix} x \\\\ y \\end{bmatrix} = x (\\text{עמודה 1}) + y (\\text{עמודה 2})$.",
                            "כפל מטריצות $(AB)$ מייצג הרכבה של טרנספורמציות מרחביות: החלת $B$ תחילה ואחריה $A$. מכיוון שסדר הפעולות במרחב משנה את התוצאה (למשל סיבוב ואז גזירה $\\neq$ גזירה ואז סיבוב), כפל מטריצות אינו חילופי: $AB \\neq BA$!"
                        ]
                    },
                    {
                        "title": "הדטרמיננטה: יחס שינוי שטח ונפח",
                        "points": [
                            "הדטרמיננטה $\\det(A)$ מודדת את הפקטור שבו שטחים (ב-2D) או נפחים (ב-3D ומעלה) משתנים כתוצאה מהטרנספורמציה.",
                            "אם $\\det(A) = 3$, שטח כל צורה במרחב ישלש את עצמו. אם $\\det(A) = 1$, הטרנספורמציה משמרת שטח במדויק (כמו סיבוב טהור).",
                            "דטרמיננטה שלילית (למשל $\\det(A) = -2$) מעידה על כך שהטרנספורמציה הופכת את האוריינטציה של המרחב (כמו השתקפות במראה).",
                            "אם $\\det(A) = 0$, הטרנספורמציה מכווצת את המרחב לממד נמוך יותר (למשל שיטוח מישור דו-ממדי לישר או לנקודה). כאשר זה קורה, מידע נמחק לצמיתות ולמטריצה אין מטריצה הופכית ($A^{-1}$ אינה קיימת)!"
                        ]
                    },
                    {
                        "title": "מטריצה הופכית ומחלקות מטריצות מיוחדות",
                        "points": [
                            "המטריצה ההופכית $A^{-1}$ 'מבטלת' את הטרנספורמציה שביצעה $A$, ומחזירה כל וקטור למיקומו המקורי: $A^{-1} A = I$ (מטריצת היחידה).",
                            "מטריצה אורתוגונלית $Q$ משמרת את כל האורכים והזוויות במרחב: $Q^T Q = I$, כלומר עמודותיה הן וקטורי יחידה ניצבים, והמטריצה ההופכית שלה שווה פשוט לשחלוף שלה ($Q^{-1} = Q^T$).",
                            "מטריצה סימטרית שווה לשחלוף של עצמה ($A = A^T$), וממלאת תפקיד מפתח במטריצות שונות משותפת (Covariance), אופטימיזציה, וטנזורי אינרציה בפיזיקה."
                        ]
                    }
                ],
                "trivia": [
                    {
                        "type": "multiple_choice",
                        "question": "מהי המשמעות הגאומטרית של הדטרמיננטה של מטריצה 2x2 (det(A))?",
                        "options": [
                            "הפקטור שבו הטרנספורמציה מגדילה או מקטינה את שטחה של כל צורה גאומטרית במישור",
                            "שיפוע הישר העובר דרך ראשית הצירים",
                            "סכום כל המספרים במטריצה",
                            "זווית התאוצה הסיבובית של וקטורי הבסיס"
                        ],
                        "correct": 0,
                        "explanation": "הדטרמיננטה מודדת את יחס שינוי השטח של הטרנספורמציה; ריבוע יחידה של $1 \\times 1$ הופך למקבילית ששטחה $|\\det(A)|$."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מה מעידה דטרמיננטה השווה לאפס (det(A) = 0) על טרנספורמציה לינארית?",
                        "options": [
                            "הטרנספורמציה מוחצת את המרחב לממד נמוך יותר (למשל מישור דו-ממדי לישר), ולכן המטריצה אינה הפיכה (סינגולרית)",
                            "הטרנספורמציה היא סיבוב טהור ללא אובדן מידע",
                            "המטריצה מכילה אפסים בלבד בכל שורותיה",
                            "המטריצה ההופכית שווה למטריצת היחידה"
                        ],
                        "correct": 0,
                        "explanation": "כאשר $\\det(A) = 0$, נפח המרחב מתאפס ונמחק ממד שלם, מה שגורם לאובדן מידע בלתי הפיך ומונע קיום מטריצה הופכית $A^{-1}$."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מדוע כפל מטריצות אינו חילופי באופן כללי (AB != BA)?",
                        "options": [
                            "מכיוון שכפל מטריצות מייצג הרכבת טרנספורמציות מרחביות, וסדר הפעולות במרחב משנה את התוצאה הגאומטרית הסופית",
                            "בשל שגיאות עיגול של החומרה בפעולות נקודה צפה",
                            "מכיוון שחובה להעלות בריבוע את איברי המטריצה תחילה",
                            "מכיוון שלא ניתן להכפיל מספרים שליליים מימין"
                        ],
                        "correct": 0,
                        "explanation": "כפל מטריצות הוא הרכבת פונקציות; ביצוע סיבוב ואחריו גזירה במרחב מייצר תוצאה שונה לחלוטין מביצוע גזירה תחילה וסיבוב לאחריה."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהי התכונה המגדירה מטריצה אורתוגונלית Q?",
                        "options": [
                            "המטריצה המשוחלפת שלה שווה למטריצה ההופכית שלה (Q^T Q = I), והיא משמרת אורכים וזוויות במרחב",
                            "כל האיברים שמחוץ לאלכסון הראשי שווים ל-0",
                            "הדטרמיננטה שלה תמיד שווה ל-0",
                            "הערכים העצמיים שלה הם כולם מספרים מדומים טהורים"
                        ],
                        "correct": 0,
                        "explanation": "מטריצה אורתוגונלית מורכבת מעמודות אורתונורמליות, משמרת אורכי וקטורים וזוויות (סיבובים/שיקופים), ומקיימת $Q^{-1} = Q^T$."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מה מייצגות העמודות של מטריצת טרנספורמציה 2x2?",
                        "options": [
                            "את הקואורדינטות של המיקומים שאליהם מגיעים וקטורי הבסיס הסטנדרטיים i_hat ו-j_hat לאחר הטרנספורמציה",
                            "את ריבועי הערכים העצמיים של המטריצה",
                            "את הוקטורים הניצבים לצירים הראשיים",
                            "את הקואורדינטות של מרחב האפס"
                        ],
                        "correct": 0,
                        "explanation": "עמודה 1 במטריצה היא הווקטור שאליו מגיע $\\hat{i} = [1, 0]^T$, ועמודה 2 היא הווקטור שאליו מגיע $\\hat{j} = [0, 1]^T$."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהי מטריצה סימטרית?",
                        "options": [
                            "מטריצה ריבועית הזהה למטריצה המשוחלפת של עצמה (A = A^T)",
                            "מטריצה שהדטרמיננטה שלה שווה ל-1",
                            "מטריצה בעלת מספר שווה של איברים חיוביים ושליליים",
                            "מטריצה הפועלת אך ורק על קואורדינטות דו-ממדיות"
                        ],
                        "correct": 0,
                        "explanation": "מטריצה היא סימטרית כאשר $A_{ij} = A_{ji}$ לכל איבר, כלומר החלפת שורות בעמודות ($A^T$) מותירה אותה ללא כל שינוי."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "איזו פעולה גאומטרית מבצעת מטריצת סיבוב 2x2 (R(theta))?",
                        "options": [
                            "סיבוב של כל המרחב נגד כיוון השעון בזווית theta סביב ראשית הצירים תוך שימור אורכים ושטח",
                            "מתיחה של ציר ה-X בפקטור theta ללא שינוי ציר Y",
                            "הטלה של כל הווקטורים על גבי ישר בזווית theta",
                            "מעיכה של המישור הדו-ממדי לקו ישר"
                        ],
                        "correct": 0,
                        "explanation": "מטריצת סיבוב $R(\\theta) = \\begin{bmatrix} \\cos\\theta & -\\sin\\theta \\\\ \\sin\\theta & \\cos\\theta \\end{bmatrix}$ מסובבת את כל המישור בזווית $\\theta$ ומשמרת אורכים ושטחים (דטרמיננטה = 1)."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהי המשמעות הגאומטרית של דטרמיננטה שלילית (det(A) < 0)?",
                        "options": [
                            "הטרנספורמציה הופכת את האוריינטציה המרחבית (כמו שיקוף במראה)",
                            "הטרנספורמציה מכווצת את כל הווקטורים לאורך אפס",
                            "המטריצה אינה ניתנת לכפל באף מטריצה אחרת",
                            "השטח הופך לשלילי ביחידות סנטימטר פיזיות"
                        ],
                        "correct": 0,
                        "explanation": "דטרמיננטה שלילית מעידה על היפוך אוריינטציה מרחבית (Handedness Inversion), בדומה להשתקפות של עצם דרך מראה."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהי מטריצת היחידה I?",
                        "options": [
                            "מטריצה ריבועית עם 1 באלכסון הראשי ו-0 בשאר האיברים המשמשת כטרנספורמציה שאינה משנה דבר (I v = v)",
                            "מטריצה שכל איבריה שווים ל-1",
                            "מטריצה ההופכת את הסימנים של כל הקואורדינטות",
                            "מטריצה המוחקת את השורה האחרונה בכל וקטור"
                        ],
                        "correct": 0,
                        "explanation": "מטריצת היחידה $I$ היא איבר היחידה הכפלי באלגברה לינארית; כפל של כל וקטור או מטריצה ב-$I$ מותיר אותם ללא שינוי ($I\\mathbf{v} = \\mathbf{v}$)."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהי פעולת השחלוף (Transpose / A^T) של מטריצה?",
                        "options": [
                            "פעולה המחליפה שורות ועמודות על גבי האלכסון הראשי",
                            "היפוך הסימנים החשבוניים של כל איברי המטריצה",
                            "הכפלת המטריצה בדטרמיננטה שלה",
                            "גזירת המטריצה לפי הזמן"
                        ],
                        "correct": 0,
                        "explanation": "שחלוף מטריצה ($A^T$) מחליף את אינדקסי השורות והעמודות: $(A^T)_{ij} = A_{ji}$."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהי הדטרמיננטה של מכפלת שתי מטריצות ריבועיות (det(AB))?",
                        "options": [
                            "det(A) * det(B)",
                            "det(A) + det(B)",
                            "det(A) / det(B)",
                            "max(det(A), det(B))"
                        ],
                        "correct": 0,
                        "explanation": "הדטרמיננטה של מכפלת מטריצות שווה למכפלת הדטרמיננטות: $\\det(AB) = \\det(A) \\det(B)$, בהתאם להרכבת שינויי השטח."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהי העקבה (Trace) של מטריצה ריבועית?",
                        "options": [
                            "סכום כל האיברים לאורך האלכסון הראשי (A_11 + A_22 + ... + A_nn)",
                            "מכפלת האיברים בפינות המטריצה",
                            "מספר השורות שאינן אפס בצורה מדורגת",
                            "האורך האוקלידי של וקטור העמודה הראשון"
                        ],
                        "correct": 0,
                        "explanation": "העקבה $\\text{Tr}(A)$ היא סכום איברי האלכסון הראשי, ושווה באופן מופלא גם לסכום כל הערכים העצמיים של המטריצה."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהי 'מטריצה אלכסונית' (Diagonal Matrix)?",
                        "options": [
                            "מטריצה שבה כל האיברים מחוץ לאלכסון הראשי שווים ל-0",
                            "מטריצה בעלת איברים רק באלכסון המשני",
                            "מטריצה שסכום כל שורה בה הוא 1.0",
                            "מטריצה בעלת יותר עמודות משורות"
                        ],
                        "correct": 0,
                        "explanation": "במטריצה אלכסונית כל האיברים שמחוץ לאלכסון ($i \\neq j$) הם אפס, וכפל בה מבצע מתיחה ישירה של צירי הקואורדינטות בנפרד."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "אם מטריצה A מקיימת A^2 = A, איזה סוג של טרנספורמציה היא מייצגת?",
                        "options": [
                            "הטלה (Idempotent Matrix / Projection)",
                            "סיבוב מתמשך של 360 מעלות",
                            "טרנספורמציית צמיחה מעריכית",
                            "שיקוף דרך ראשית הצירים"
                        ],
                        "correct": 0,
                        "explanation": "מטריצה אידמפוטנטית ($A^2 = A$) מייצגת הטלה גאומטרית; ברגע שווקטור הוטל על תת-מרחב, הטלה חוזרת משאירה אותו באותו מקום בדיוק."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "כיצד משפיעה הכפלת מטריצה n x n בסקלר c על הדטרמיננטה שלה (det(c A))?",
                        "options": [
                            "c^n * det(A)",
                            "c * det(A)",
                            "c + det(A)",
                            "det(A) / c"
                        ],
                        "correct": 0,
                        "explanation": "מכיוון שמתיחת מרחב $n$-ממדי בפקטור $c$ בכל $n$ הצירים מכפילה את הנפח ה-$n$-ממדי ב-$c^n$, מתקיים $\\det(c A) = c^n \\det(A)$."
                    }
                ]
            },

            # =================================================================
            # MODULE 3: Systems of Equations, Column Space & Rank
            # =================================================================
            {
                "id": "linear_systems_nullspace_rank",
                "title": "3. מערכות משוואות, מרחב עמודות ודרגת מטריצה (Rank)",
                "description": "פתרון מערכות משוואות Ax = b כצירוף לינארי של עמודות, תתי-המרחבים היסודיים, מרחב האפס (Nullspace), ומשפט הדרגה והאפסיות.",
                "cards": [
                    {
                        "title": "Ax = b כצירוף לינארי של עמודות המטריצה",
                        "figure": {
                            "title": "מרחב העמודות (Image) מול מרחב האפס (Kernel)",
                            "svg": """<svg viewBox="0 0 520 150" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-height:150px;">
  <rect x="20" y="20" width="200" height="110" rx="10" fill="#3b82f6" fill-opacity="0.1" stroke="#3b82f6" stroke-width="2"/>
  <text x="120" y="42" font-size="12" font-weight="bold" fill="#3b82f6" text-anchor="middle">מרחב התחום (R^n)</text>
  <rect x="40" y="55" width="160" height="35" rx="6" fill="#ef4444" fill-opacity="0.2" stroke="#ef4444" stroke-width="1.5"/>
  <text x="120" y="77" font-size="11" font-weight="bold" fill="#ef4444" text-anchor="middle">מרחב האפס: A x = 0</text>
  <text x="120" y="115" font-size="9" fill="currentColor" text-anchor="middle">מרחב השורות (ניצב למרחב האפס)</text>

  <path d="M 225 75 L 290 75" stroke="currentColor" stroke-width="2" marker-end="url(#arr)" opacity="0.6"/>
  <text x="257" y="65" font-size="11" font-weight="bold" fill="#8b5cf6" text-anchor="middle">מטריצה A</text>

  <rect x="295" y="20" width="205" height="110" rx="10" fill="#10b981" fill-opacity="0.1" stroke="#10b981" stroke-width="2"/>
  <text x="397" y="42" font-size="12" font-weight="bold" fill="#10b981" text-anchor="middle">מרחב הטווח (R^m)</text>
  <rect x="315" y="55" width="165" height="35" rx="6" fill="#10b981" fill-opacity="0.25" stroke="#10b981" stroke-width="1.5"/>
  <text x="397" y="77" font-size="11" font-weight="bold" fill="#10b981" text-anchor="middle">מרחב העמודות: Col(A)</text>
  <circle cx="397" cy="115" r="4" fill="#ef4444"/>
  <text x="410" y="118" font-size="10" fill="#ef4444">וקטור האפס 0</text>
</svg>""",
                            "caption": "כל הווקטורים במרחב האפס נמעכים לנקודת האפס $\\mathbf{0}$. מרחב העמודות הוא תת-המרחב של כל הפלטים האפשריים של $A\\mathbf{x}$."
                        },
                        "points": [
                            "במקום לראות מערכת משוואות כהצטלבות ישרים, באלגברה לינארית אנו רואים אותה כמשוואה וקטורית יחידה: $x \\begin{bmatrix} 2 \\\\ 4 \\end{bmatrix} + y \\begin{bmatrix} 3 \\\\ -1 \\end{bmatrix} = \\begin{bmatrix} 8 \\\\ 2 \\end{bmatrix}$ ($A\\mathbf{x} = \\mathbf{b}$).",
                            "מרחב העמודות $\\text{Col}(A)$ הוא מרחב הפרישה של כל עמודות המטריצה $A$. למשוואה $A\\mathbf{x} = \\mathbf{b}$ קיים פתרון אם ורק אם וקטור המטרה $\\mathbf{b}$ שוכן בתוך מרחב העמודות של $A$!",
                            "מרחב האפס (Kernel / Null Space) $\\text{Null}(A)$ הוא אוסף כל וקטורי הקלט $\\mathbf{x}$ הנמעכים לווקטור האפס: $A\\mathbf{x} = \\mathbf{0}$.",
                            "דרגת המטריצה (Rank) היא ממד מרחב העמודות שלה (מספר העמודות הבלתי תלויות לינארית). משפט הדרגה והאפסיות קובע כי: $\\text{Rank}(A) + \\text{Nullity}(A) = n$ (סך עמודות הקלט)."
                        ]
                    },
                    {
                        "title": "דירוג גאוס, צורה מדורגת ואיברים מובילים (Pivots)",
                        "points": [
                            "דירוג גאוס פותר את $A\\mathbf{x} = \\mathbf{b}$ באמצעות 3 פעולות שורה אלמנטריות: (1) החלפת שורות, (2) הכפלת שורה בסקלר שאינו אפס, ו-(3) הוספת כפולה של שורה אחת לאחרת.",
                            "פעולות אלו ממירות את המטריצה לצורה מדורגת משולשית עליונה (Row Echelon Form) בעלת איברים מובילים (Pivots).",
                            "מספר האיברים המובילים שאינם אפס שווה במדויק לדרגה המתמטית (Rank) של המטריצה.",
                            "משתנים בעלי איבר מוביל הם משתנים תלויים; משתנים בעמודות ללא איבר מוביל הם משתנים חופשיים (המגדירים אינסוף פתרונות)."
                        ]
                    },
                    {
                        "title": "מערכות יתר ושיטת הריבועים הפחותים (Least Squares)",
                        "points": [
                            "מערכת בעלת אינסוף פתרונות (יותר נעלמים ממשוואות, $m < n$): פתרון בעל נורמה מינימלית נמצא באמצעות המטריצה הפסאודו-הופכית.",
                            "מערכת יתר (יותר משוואות מנעלמים, $m > n$, כמו התאמת 100 נקודות מדידה רועשות לישר): לרוב אין פתרון מדויק כי $\\mathbf{b}$ אינו בתוך $\\text{Col}(A)$.",
                            "שיטת הריבועים הפחותים (Least Squares) מוצאת את הפתרון המקורב הטוב ביותר שממזער את שגיאת המרחק $\\|A\\mathbf{x} - \\mathbf{b}\\|^2$. היא מטילה את $\\mathbf{b}$ בהטלה אורתוגונלית על מרחב העמודות באמצעות המשוואות הנורמליות: $A^T A \\mathbf{\\hat{x}} = A^T \\mathbf{b} \\implies \\mathbf{\\hat{x}} = (A^T A)^{-1} A^T \\mathbf{b}$."
                        ]
                    }
                ],
                "trivia": [
                    {
                        "type": "multiple_choice",
                        "question": "מהו 'מרחב העמודות' (Column Space / Image) של מטריצה A?",
                        "options": [
                            "אוסף כל וקטורי הפלט שניתן להגיע אליהם על ידי צירופים לינאריים של עמודות המטריצה A (מרחב הפרישה של עמודותיה)",
                            "אוסף כל הווקטורים המתאפסים בעת כפל ב-A",
                            "סכום המספרים בעמודה הראשונה של A",
                            "איברי האלכסון של המטריצה ההופכית"
                        ],
                        "correct": 0,
                        "explanation": "מרחב העמודות $\\text{Col}(A)$ הוא תת-המרחב הנוצר מכל הצירופים הלינאריים של עמודות $A$, ומייצג את כל הפלטים האפשריים $A\\mathbf{x}$."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהו 'מרחב האפס' (Null Space / Kernel) של מטריצה A?",
                        "options": [
                            "אוסף כל וקטורי הקלט x המקיימים את המשוואה ההומוגנית A x = 0",
                            "אוסף כל הווקטורים שאורכם שווה ל-0",
                            "שטח הזיכרון ב-RAM שאינו מוקצה",
                            "אוסף הערכים העצמיים השווים ל-1"
                        ],
                        "correct": 0,
                        "explanation": "מרחב האפס $\\text{Null}(A)$ מכיל את כל וקטורי הקלט $\\mathbf{x}$ שנמעכים לווקטור האפס בעת הכפלה במטריצה $A$ ($A\\mathbf{x} = \\mathbf{0}$)."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "איזה קשר יסודי קובע משפט הדרגה והאפסיות (Rank-Nullity Theorem) עבור מטריצה m x n?",
                        "options": [
                            "Rank(A) + Nullity(A) = n (סך עמודות הקלט / ממד התחום)",
                            "Rank(A) * Nullity(A) = m * n",
                            "Rank(A) = Nullity(A) - 1",
                            "Rank(A) + Nullity(A) = det(A)"
                        ],
                        "correct": 0,
                        "explanation": "משפט הדרגה והאפסיות קובע שממד מרחב העמודות ועוד ממד מרחב האפס שווה תמיד למספר עמודות הקלט הכולל $n$."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מתי למערכת משוואות לינאריות A x = b קיים בוודאות פתרון אחד לפחות?",
                        "options": [
                            "כאשר וקטור המטרה b מוכל בתוך מרחב העמודות של המטריצה A",
                            "כאשר הדטרמיננטה של A שווה ל-0",
                            "כאשר המטריצה A היא סימטרית וחיובית מוגדרת",
                            "כאשר הווקטור b ניצב לכל שורות A"
                        ],
                        "correct": 0,
                        "explanation": "מכיוון ש-$A\\mathbf{x}$ הוא צירוף לינארי של עמודות $A$, פתרון $\\mathbf{x}$ קיים אם ורק אם וקטור המטרה $\\mathbf{b}$ שייך למרחב העמודות $\\text{Col}(A)$."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהן 'המשוואות הנורמליות' המשמשות למציאת פתרון הריבועים הפחותים במערכות יתר (A x ~= b)?",
                        "options": [
                            "A^T A x = A^T b",
                            "A x = b",
                            "A A^T x = b",
                            "det(A) x = b"
                        ],
                        "correct": 0,
                        "explanation": "המשוואות הנורמליות $A^T A \\mathbf{\\hat{x}} = A^T \\mathbf{b}$ מטילות את וקטור המטרה $\\mathbf{b}$ בהטלה אורתוגונלית על מרחב העמודות וממזערות את שגיאת המרחק $\\|A\\mathbf{x} - \\mathbf{b}\\|^2$."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהי 'דרגה' (Rank) של מטריצה?",
                        "options": [
                            "המספר המרבי של וקטורי עמודה (או שורה) בלתי תלויים לינארית במטריצה",
                            "המספר הכולל של איברים שאינם אפס במטריצה",
                            "מספר השורות כפול מספר העמודות",
                            "הערך המספרי הגדול ביותר במטריצה"
                        ],
                        "correct": 0,
                        "explanation": "דרגת המטריצה היא ממד תת-המרחב הנפרש על ידי עמודותיה, ושווה תמיד לממד תת-המרחב הנפרש על ידי שורותיה."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מה מאפיין מטריצה ריבועית n x n בעלת 'דרגה מלאה' (Full Rank)?",
                        "options": [
                            "דרגתה שווה ל-n, כל עמודותיה בלתי תלויות לינארית, והמטריצה הפיכה לחלוטין",
                            "המטריצה מכילה אך ורק מספרים הגדולים מאפס",
                            "דרגתה שווה ל-0",
                            "הדטרמיננטה שלה שווה לאפס"
                        ],
                        "correct": 0,
                        "explanation": "מטריצה ריבועית בעלת דרגה מלאה $n$ היא בעלת דטרמיננטה שאינה אפס, מרחב אפס המכיל את $\\{\\mathbf{0}\\}$ בלבד, והיא הפיכה לחלוטין."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "בדירוג גאוס, מהו 'איבר מוביל' (Pivot)?",
                        "options": [
                            "האיבר הראשון שאינו אפס בשורה המשמש לאיפוס הערכים שמתחתיו",
                            "נקודת המרכז של סיבוב תמונה",
                            "העמודה האחרונה במטריצה המורחבת",
                            "הדטרמיננטה חלקי העקבה"
                        ],
                        "correct": 0,
                        "explanation": "איבר מוביל (Pivot) הוא המקדם הראשון שאינו אפס בשורה במהלך דירוג גאוס, המשמש לאיפוס הערכים בעמודה שמתחתיו."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מה מאפיין 'מערכת יתר' (Overdetermined System) של משוואות לינאריות?",
                        "options": [
                            "יש יותר משוואות (אילוצים) מנעלמים (משתנים), m > n",
                            "יש יותר נעלמים ממשוואות, n > m",
                            "הדטרמיננטה של מטריצת המקדמים היא שלילית",
                            "כל המשתנים מוגבלים לערכים שלמים בלבד"
                        ],
                        "correct": 0,
                        "explanation": "מערכת יתר כוללת יותר משוואות מנעלמים ($m > n$); במערכות נתונים מציאותיות עם רעש, לרוב אין פתרון מדויק ויש להשתמש בריבועים פחותים."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מה מאפיין מערכת משוואות בעלת אינסוף פתרונות (Underdetermined System, m < n)?",
                        "options": [
                            "יש פחות משוואות מנעלמים, מה שיוצר משתנים חופשיים ואינסוף פתרונות אפשריים",
                            "אין למערכת שום פתרון מתמטי",
                            "יש למערכת פתרון יחיד ומדויק",
                            "דטרמיננטת המטריצה תמיד שווה ל-1.0"
                        ],
                        "correct": 0,
                        "explanation": "כאשר יש פחות משוואות מנעלמים ($m < n$), קיימים משתנים חופשיים המאפשרים אינסוף צירופי פתרונות במרחב אפיני."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהו הקשר הגאומטרי בין מרחב השורות למרחב האפס של מטריצה A?",
                        "options": [
                            "הם מרחבים משלימים אורתוגונליים ב-R^n (כל וקטור במרחב האפס ניצב לכל וקטור במרחב השורות)",
                            "הם מרחבים זהים לחלוטין",
                            "הם פורשים רבעים מנוגדים במערכת הצירים",
                            "החיתוך ביניהם הוא המרחב R^n כולו"
                        ],
                        "correct": 0,
                        "explanation": "מכיוון ש-$A\\mathbf{x} = \\mathbf{0}$ פירושו שכל שורה במטריצה במכפלה סקלרית עם $\\mathbf{x}$ שווה לאפס, מרחב האפס הוא המשלים האורתוגונלי המדויק של מרחב השורות."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מה מאפיין צורה מדורגת קנונית (Reduced Row Echelon Form - RREF)?",
                        "options": [
                            "כל איבר מוביל הוא 1.0 והוא האיבר היחיד שאינו אפס בעמודה שלו",
                            "מטריצה אלכסונית בעלת ערכים שליליים בלבד",
                            "מטריצה שהומרה למספרים מרוכבים",
                            "מטריצה שסכום כל שורותיה הוא אפס"
                        ],
                        "correct": 0,
                        "explanation": "בצורה מדורגת קנונית (RREF), כל איבר מוביל הוא 1, והוא האיבר היחיד שאינו אפס בעמודה שלו, מה שמאפשר קריאה ישירה של פתרון המערכת."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "לשם מה משמשת המטריצה הפסאודו-הופכית של מור-פנרוז (Moore-Penrose Pseudoinverse / A+)?",
                        "options": [
                            "להכללת מושג המטריצה ההופכית למטריצות מלבניות או סינגולריות ולמציאת פתרון ריבועים פחותים",
                            "להפיכת מספרים סקלריים של 1x1",
                            "לסיבוב וקטורים תלת-ממדיים סביב ציר ה-Z",
                            "להצפנת קודי גיבוב קריפטוגרפיים"
                        ],
                        "correct": 0,
                        "explanation": "המטריצה הפסאודו-הופכית $A^+$ מספקת הופכי מוכלל לכל מטריצה מלבנית, ומחשבת את פתרון הריבועים הפחותים בעל הנורמה המינימלית $\\mathbf{\\hat{x}} = A^+ \\mathbf{b}$."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "אם למטריצה 3x3 יש דרגה Rank = 2, איזו צורה גאומטרית מהווה מרחב העמודות שלה במרחב התלת-ממדי?",
                        "options": [
                            "מישור דו-ממדי שטוח העובר דרך ראשית הצירים",
                            "קו ישר חד-ממדי",
                            "המרחב התלת-ממדי המלא",
                            "נקודה בודדת בראשית הצירים [0, 0, 0]"
                        ],
                        "correct": 0,
                        "explanation": "דרגה מייצגת את ממד מרחב העמודות; דרגה 2 במרחב תלת-ממדי פורשת מישור דו-ממדי שטוח העובר דרך הראשית."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהם 'משתנים חופשיים' (Free Variables) במערכת משוואות לינאריות?",
                        "options": [
                            "משתנים בעמודות ללא איבר מוביל שניתן להציב בהם כל ערך סקלרי שרירותי כדי לייצר פתרונות",
                            "משתנים שאינם מוגדרים בקוד המקור",
                            "משתנים שאין להם כתובת זיכרון ב-RAM",
                            "קבועים שאינם ניתנים להכפלה במספרים"
                        ],
                        "correct": 0,
                        "explanation": "משתנים חופשיים מייצגים דרגות חופש במערכת ללא איברים מובילים, ופרמטריזציה שלהם מייצרת את כל אינסוף הפתרונות של המערכת."
                    }
                ]
            },

            # =================================================================
            # MODULE 4: Eigenvalues, Eigenvectors & PCA
            # =================================================================
            {
                "id": "eigenvalues_eigenvectors_pca",
                "title": "4. ערכים עצמיים, וקטורים עצמיים וניתוח רכיבים ראשיים (PCA)",
                "description": "הבנת כיוונים במרחב שאינם מסתובבים בעת טרנספורמציה, המשוואה האופיינית, לכסון מטריצות, והפחתת ממדים בבינה מלאכותית באמצעות PCA.",
                "cards": [
                    {
                        "title": "מהם וקטורים עצמיים? כיוונים בלתי משתנים במרחב",
                        "figure": {
                            "title": "שימור כיוון של וקטור עצמי: A v = λ v",
                            "svg": """<svg viewBox="0 0 520 150" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-height:150px;">
  <g transform="translate(40,20)">
    <line x1="20" y1="100" x2="80" y2="30" stroke="currentColor" stroke-width="2" opacity="0.4"/>
    <line x1="20" y1="100" x2="110" y2="50" stroke="#ec4899" stroke-width="3"/>
    <polygon points="106,46 116,51 108,56" fill="#ec4899"/>
    <text x="70" y="120" font-size="10" fill="#ec4899" text-anchor="middle">וקטור רגיל: מסתובב!</text>
  </g>

  <g transform="translate(260,20)">
    <line x1="0" y1="120" x2="220" y2="10" stroke="#8b5cf6" stroke-width="1.5" stroke-dasharray="3,3" opacity="0.4"/>

    <line x1="20" y1="110" x2="80" y2="80" stroke="#3b82f6" stroke-width="3"/>
    <polygon points="76,76 86,77 80,86" fill="#3b82f6"/>
    <text x="50" y="70" font-size="11" font-weight="bold" fill="#3b82f6">וקטור עצמי v</text>

    <line x1="20" y1="110" x2="170" y2="35" stroke="#10b981" stroke-width="3"/>
    <polygon points="166,31 176,32 170,41" fill="#10b981"/>
    <text x="130" y="25" font-size="11" font-weight="bold" fill="#10b981">A v = λ v (רק נמתח על אותו קו!)</text>
  </g>
</svg>""",
                            "caption": "מרבית הווקטורים משנים כיוון בעת כפל במטריצה. וקטור עצמי $\\mathbf{v}$ נשאר על קו הפעולה המקורי שלו ורק נמתח בפקטור $\\lambda$."
                        },
                        "points": [
                            "כאשר מטריצה מעוותת את המרחב, כמעט כל וקטור מוסט מקו הפעולה המקורי שלו ומסתובב לכיוון חדש.",
                            "עם זאת, קיימים כיוונים מיוחדים במרחב שאינם מסתובבים כלל - הם רק נמתחים, מתכווצים או הופכים כיוון על גבי הישר שלהם! וקטורים מיוחדים אלו נקראים וקטורים עצמיים (Eigenvectors - $\\mathbf{v}$), ופקטור המתיחה נקרא ערך עצמי (Eigenvalue - $\\lambda$): $A\\mathbf{v} = \\lambda \\mathbf{v}$.",
                            "כדי למצוא ערכים עצמיים, נכתוב $(A - \\lambda I)\\mathbf{v} = \\mathbf{0}$. כדי שיהיה וקטור עצמי שאינו אפס במרחב האפס, המטריצה חייבת להיות סינגולרית: $\\det(A - \\lambda I) = 0$ (הפולינום האופייני).",
                            "פתרון הפולינום נותן את הערכים העצמיים $\\lambda_i$, והצבתם במשוואה מחזירה את כיווני הווקטורים העצמיים המתאימים."
                        ]
                    },
                    {
                        "title": "לכסון מטריצות וחזקות של מטריצות",
                        "points": [
                            "אם למטריצה $A$ בגודל $n \\times n$ יש $n$ וקטורים עצמיים בלתי תלויים, נוכל לסדרם כעמודות במטריצה $P$, ואת הערכים העצמיים במטריצה אלכסונית $D$. זהו לכסון מטריצה: $A = P D P^{-1}$.",
                            "לכסון ממיר את מערכת הצירים: $P^{-1}$ מעביר לבסיס הווקטורים העצמיים, $D$ מבצע מתיחה טהורה של הצירים ב-$\\lambda_i$, ו-$P$ מחזיר לבסיס הסטנדרטי.",
                            "חישוב חזקות גבוהות של מטריצה הופך לפשוט ביותר: $A^k = (P D P^{-1})^k = P D^k P^{-1}$. במקום $k$ כפלי מטריצות יקרים, פשוט מעלים בחזקה את הערכים העצמיים לאורך האלכסון של $D$!"
                        ]
                    },
                    {
                        "title": "המשפט הספקטרלי וניתוח רכיבים ראשיים (PCA)",
                        "points": [
                            "המשפט הספקטרלי למטריצות סימטריות ממשיות: אם $A = A^T$, מובטח כי: (1) כל הערכים העצמיים הם ממשיים לחלוטין, ו-(2) כל הווקטורים העצמיים ניצבים הדדית ויוצרים בסיס אורתונורמלי: $A = Q D Q^T$.",
                            "ניתוח רכיבים ראשיים (PCA): בלמידת מכונה, מערכי נתונים עתירי ממדים (כגון 1,000 מאפיינים למשתמש) כוללים מתאמים רבים. אלגוריתם PCA מחשב את מטריצת השונות המשותפת $\\Sigma = \\frac{1}{N} X^T X$, שהיא תמיד סימטרית וממשית.",
                            "הווקטורים העצמיים של $\\Sigma$ מצביעים בכיווני השונות המקסימלית של הנתונים! על ידי הטלת המידע על $k$ הווקטורים העצמיים המובילים, מהנדסים דוחסים 1,000 ממדים ל-2 או 3 ממדים בלבד תוך שימור 99% מהמידע."
                        ]
                    }
                ],
                "trivia": [
                    {
                        "type": "multiple_choice",
                        "question": "מהי המשוואה האלגברית המגדירה וקטור עצמי v וערך עצמי lambda של מטריצה A?",
                        "options": [
                            "A v = lambda v",
                            "A + v = lambda",
                            "A v = 0",
                            "det(A) = lambda v"
                        ],
                        "correct": 0,
                        "explanation": "וקטור עצמי $\\mathbf{v}$ במכפלה עם מטריצה $A$ מפיק וקטור השוכן על אותו קו פעולה בדיוק, מוכפל בסקלר הערך העצמי $\\lambda$: $A\\mathbf{v} = \\lambda\\mathbf{v}$."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "כיצד מחשבים את הערכים העצמיים של מטריצה ריבועית A?",
                        "options": [
                            "על ידי פתרון משוואת הפולינום האופייני det(A - lambda I) = 0 עבור lambda",
                            "על ידי ממוצע איברי האלכסון של המטריצה",
                            "על ידי חישוב המטריצה ההופכית A^-1",
                            "על ידי חלוקת העקבה בדרגת המטריצה"
                        ],
                        "correct": 0,
                        "explanation": "איפוס הדטרמיננטה של $(A - \\lambda I)$ מבטיח קיום מרחב אפס שאינו טריוויאלי, ומייצר את הפולינום האופייני ששורשיו הם הערכים העצמיים."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מה מבטיח המשפט הספקטרלי עבור כל מטריצה סימטרית ממשית (A = A^T)?",
                        "options": [
                            "כל הערכים העצמיים הם מספרים ממשיים, וקיים בסיס אורתונורמלי של וקטורים עצמיים (A = Q D Q^T)",
                            "כל הערכים העצמיים שווים לאפס",
                            "דטרמיננטת המטריצה היא תמיד שלילית",
                            "המטריצה אינה ניתנת ללכסון"
                        ],
                        "correct": 0,
                        "explanation": "המשפט הספקטרלי מוכיח שכל מטריצה סימטרית ממשית היא בעלת ערכים עצמיים ממשיים בלבד וניתנת ללכסון אורתוגונלי מלא עם וקטורים עצמיים ניצבים."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "בניתוח רכיבים ראשיים (PCA), מה מייצגים הווקטורים העצמיים של מטריצת השונות המשותפת?",
                        "options": [
                            "את צירי השונות המקסימלית של הנתונים במרחב (הרכיבים הראשיים)",
                            "את קואורדינטות הממוצע של אשכולות הנתונים",
                            "את נקודות הרעש שיש למחוק מהמדגם",
                            "את קצב הלמידה של רשת הנוירונים"
                        ],
                        "correct": 0,
                        "explanation": "הווקטורים העצמיים של מטריצת השונות המשותפת מצביעים בכיוונים שבהם המידע מפוזר ביותר (שונות מרבית), ומאפשרים הפחתת ממדים אופטימלית."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מדוע לכסון מטריצה (A = P D P^-1) יעיל חישובית במיוחד לצורך חישוב חזקות גבוהות כמו A^100?",
                        "options": [
                            "מכיוון ש-A^100 = P D^100 P^-1, מה שדורש רק העלאה בחזקת 100 של איברי האלכסון בנפרד",
                            "מכיוון שהוא הופך את המטריצה למספר שלם בודד",
                            "מכיוון שהוא מבטל את הצורך בפעולות כפל בנקודה צפה",
                            "מכיוון שהוא מבטיח שכל איברי המטריצה יתאפסו"
                        ],
                        "correct": 0,
                        "explanation": "העלאת מטריצה אלכסונית $D$ בחזקה דורשת רק העלאה בחזקה של הערכים העצמיים $\\lambda_i^{100}$, וחוסכת 100 כפלי מטריצות יקרים."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהו הקשר בין הערכים העצמיים של מטריצה לבין הדטרמיננטה שלה (det(A))?",
                        "options": [
                            "הדטרמיננטה שווה למכפלת כל הערכים העצמיים (det(A) = lambda_1 * lambda_2 * ... * lambda_n)",
                            "הדטרמיננטה שווה לסכום כל הערכים העצמיים",
                            "הדטרמיננטה שווה לריבוע הערך העצמי הגדול ביותר",
                            "אין שום קשר מתמטי ביניהם"
                        ],
                        "correct": 0,
                        "explanation": "הדטרמיננטה של מטריצה שווה למכפלת כל ערכיה העצמיים: $\\det(A) = \\prod_{i=1}^n \\lambda_i$."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהו הקשר בין הערכים העצמיים של מטריצה לבין העקבה שלה (Tr(A))?",
                        "options": [
                            "העקבה שווה לסכום כל הערכים העצמיים (Tr(A) = lambda_1 + lambda_2 + ... + lambda_n)",
                            "העקבה שווה למכפלת כל הערכים העצמיים",
                            "העקבה שווה לערך העצמי הקטן ביותר",
                            "העקבה שווה תמיד ל-0"
                        ],
                        "correct": 0,
                        "explanation": "עקבת המטריצה (סכום איברי האלכסון הראשי) שווה תמיד לסכום כל הערכים העצמיים שלה: $\\text{Tr}(A) = \\sum_{i=1}^n \\lambda_i$."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מה מעיד קיומו של ערך עצמי lambda = 0 במטריצה?",
                        "options": [
                            "המטריצה היא סינגולרית (det = 0) וקיים מרחב אפס שאינו ריק המכיל את הווקטור העצמי המתאים",
                            "המטריצה היא מטריצת יחידה",
                            "המטריצה אינה ניתנת לכפל בווקטורים",
                            "כל איברי המטריצה שווים לאפס"
                        ],
                        "correct": 0,
                        "explanation": "אם $\\lambda = 0$, אז $A\\mathbf{v} = 0\\mathbf{v} = \\mathbf{0}$, מה שמוכיח ש-$\\mathbf{v}$ שייך למרחב האפס ולכן $\\det(A) = 0$ (אינה הפיכה)."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהם הערכים העצמיים של מטריצת היחידה I?",
                        "options": [
                            "כל הערכים העצמיים שווים ל-1.0",
                            "כל הערכים העצמיים שווים ל-0.0",
                            "הערכים העצמיים הם אינסופיים",
                            "הערכים העצמיים הם מספרים מדומים טהורים"
                        ],
                        "correct": 0,
                        "explanation": "מכיוון ש-$I\\mathbf{v} = 1\\mathbf{v}$ לכל וקטור במרחב, כל וקטור שאינו אפס הוא וקטור עצמי עם ערך עצמי $\\lambda = 1$."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהי המשמעות לכך שמטריצת סיבוב 2x2 היא בעלת ערכים עצמיים מרוכבים?",
                        "options": [
                            "אין שום ישר ממשי במישור שאינו מסתובב במהלך הסיבוב",
                            "המטריצה שגויה מתמטית",
                            "אורכי הווקטורים מתכווצים לאפס",
                            "דטרמיננטת המטריצה היא שלילית"
                        ],
                        "correct": 0,
                        "explanation": "סיבוב טהור (שאינו ב-$180^\\circ$) מסובב כל וקטור ממשי במישור, ולכן אין וקטורים עצמיים ממשיים והערכים העצמיים הם צמודים מרוכבים."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהו 'מרחב עצמי' (Eigenspace) המתאים לערך עצמי lambda?",
                        "options": [
                            "אוסף כל הווקטורים העצמיים המתאימים ל-lambda יחד עם וקטור האפס (מרחב האפס של A - lambda I)",
                            "גבולות התצוגה של מערך הנתונים בגרף",
                            "שטח הזיכרון של חוצץ המטריצה",
                            "אוסף הערכים העצמיים החיוביים"
                        ],
                        "correct": 0,
                        "explanation": "המרחב העצמי $E_\\lambda = \\text{Null}(A - \\lambda I)$ הוא תת-המרחב הלינארי המורכב מכל הווקטורים העצמיים של $\\lambda$ בתוספת וקטור האפס."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהי 'מטריצה חיובית מוגדרת' (Positive Definite Matrix)?",
                        "options": [
                            "מטריצה סימטרית שבה x^T A x > 0 לכל וקטור שאינו אפס (כל ערכיה העצמיים חיוביים ממש)",
                            "מטריצה המכילה מספרים שלמים חיוביים בלבד",
                            "מטריצה שהדטרמיננטה שלה שווה ל-1+",
                            "מטריצה בעלת יותר שורות מעמודות"
                        ],
                        "correct": 0,
                        "explanation": "מטריצה סימטרית היא חיובית מוגדרת אם כל ערכיה העצמיים חיוביים ($\\lambda_i > 0$), מה שמבטיח שתבניות ריבועיות מתנהגות כקערה קמורה באופטימיזציה."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "איזה אלגוריתם ששימש את גוגל במנוע החיפוש המקורי שלה מבוסס ביסודו על חישוב וקטור עצמי של מטריצת קישורים ענקית?",
                        "options": [
                            "אלגוריתם פייג'ראנק (PageRank)",
                            "אלגוריתם דייקסטרה למסלול קצר",
                            "חיפוש בינארי",
                            "מיון מהיר (QuickSort)"
                        ],
                        "correct": 0,
                        "explanation": "אלגוריתם PageRank מחשב את הווקטור העצמי הראשי (עם $\\lambda = 1$) של מטריצת מעברי ההסתברות בין דפי אינטרנט באמצעות שיטת החזקה."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהי שיטת החזקה (Power Iteration) באלגברה לינארית חישובית?",
                        "options": [
                            "אלגוריתם המכפיל שוב ושוב וקטור אקראי במטריצה A כדי להתכנס לווקטור העצמי בעל הערך העצמי הגדול ביותר",
                            "טכניקת חומרה להפחתת צריכת חשמל במעבד",
                            "שיטה לפתרון אי-שוויונות לינאריים",
                            "אלגוריתם לחישוב שורש ריבועי של מטריצות"
                        ],
                        "correct": 0,
                        "explanation": "שיטת החזקה מפעילה שוב ושוב כפל במטריצה ונרמול; מכיוון שהרכיב של הערך העצמי הדומיננטי גדל בקצב המהיר ביותר, הווקטור מתכנס במהירות לווקטור העצמי הראשי."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מתי מטריצה ריבועית אינה ניתנת ללכסון ('פגומה' / Defective)?",
                        "options": [
                            "כאשר אין לה מספיק וקטורים עצמיים בלתי תלויים לפרישת בסיס מלא (ריבוי גאומטרי קטן מריבוי אלגברי)",
                            "כאשר הדטרמיננטה שלה היא מספר ראשוני",
                            "כאשר כל איבריה הם מספרי נקודה צפה",
                            "כאשר היא מוכפלת במטריצה אלכסונית"
                        ],
                        "correct": 0,
                        "explanation": "מטריצה פגומה חסרה בסיס של $n$ וקטורים עצמיים (כמו מטריצות גזירה $\\begin{bmatrix} 1 & 1 \\\\ 0 & 1 \\end{bmatrix}$), ולכן לא ניתן ללכסנה."
                    }
                ]
            },

            # =================================================================
            # MODULE 5: Singular Value Decomposition (SVD) & ML Applications
            # =================================================================
            {
                "id": "svd_matrix_factorizations",
                "title": "5. פירוק ערכים יחידים (SVD) ויישומי למידת מכונה",
                "description": "המשפט המרכזי של האלגברה הלינארית: פירוק כל מטריצה מלבנית ל-U Sigma V^T, קירוב בעל דרגה נמוכה, דחיסת תמונות ומערכות המלצה.",
                "cards": [
                    {
                        "title": "המשפט הראשי של האלגברה הלינארית: פירוק SVD",
                        "figure": {
                            "title": "פירוק גאומטרי: סיבוב -> מתיחה -> סיבוב",
                            "svg": """<svg viewBox="0 0 520 150" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-height:150px;">
  <g transform="translate(30,20)">
    <circle cx="50" cy="50" r="40" fill="#3b82f6" fill-opacity="0.15" stroke="#3b82f6" stroke-width="2"/>
    <line x1="50" y1="50" x2="90" y2="50" stroke="#3b82f6" stroke-width="2.5"/>
    <line x1="50" y1="50" x2="50" y2="10" stroke="#10b981" stroke-width="2.5"/>
    <text x="50" y="110" font-size="10" font-weight="bold" fill="#3b82f6" text-anchor="middle">1. בסיס אורתונורמלי V</text>
  </g>

  <path d="M 130 70 L 165 70" stroke="currentColor" stroke-width="2" marker-end="url(#arr)" opacity="0.5"/>
  <text x="147" y="60" font-size="10" font-weight="bold" fill="currentColor">V^T</text>

  <g transform="translate(180,20)">
    <ellipse cx="60" cy="50" rx="55" ry="25" fill="#8b5cf6" fill-opacity="0.15" stroke="#8b5cf6" stroke-width="2"/>
    <line x1="60" y1="50" x2="115" y2="50" stroke="#3b82f6" stroke-width="2.5"/>
    <line x1="60" y1="50" x2="60" y2="25" stroke="#10b981" stroke-width="2.5"/>
    <text x="85" y="42" font-size="9" font-weight="bold" fill="#3b82f6">σ1</text>
    <text x="65" y="32" font-size="9" font-weight="bold" fill="#10b981">σ2</text>
    <text x="60" y="110" font-size="10" font-weight="bold" fill="#8b5cf6" text-anchor="middle">2. מתיחה ב-Σ (ערכי σ_i)</text>
  </g>

  <path d="M 310 70 L 345 70" stroke="currentColor" stroke-width="2" marker-end="url(#arr)" opacity="0.5"/>
  <text x="327" y="60" font-size="10" font-weight="bold" fill="currentColor">U</text>

  <g transform="translate(360,20)">
    <g transform="rotate(-30 60 50)">
      <ellipse cx="60" cy="50" rx="55" ry="25" fill="#ec4899" fill-opacity="0.2" stroke="#ec4899" stroke-width="2"/>
      <line x1="60" y1="50" x2="115" y2="50" stroke="#3b82f6" stroke-width="2.5"/>
      <line x1="60" y1="50" x2="60" y2="25" stroke="#10b981" stroke-width="2.5"/>
    </g>
    <text x="60" y="110" font-size="10" font-weight="bold" fill="#ec4899" text-anchor="middle">3. סיבוב למרחב U</text>
  </g>
</svg>""",
                            "caption": "משפט SVD מוכיח שכל טרנספורמציה מתפרקת לשלושה שלבים: סיבוב ראשוני ($V^T$), מתיחת צירים לפי ערכים יחידים ($\\Sigma$), וסיבוב סופי ($U$)."
                        },
                        "points": [
                            "לכסון על פי ערכים עצמיים עובד אך ורק על מטריצות ריבועיות בעלות בסיס עצמי מלא. מה לגבי מטריצות מלבניות כלליות ($m \\times n$, כגון מערך נתונים של 10,000 משתמשים $\\times$ 500 סרטים)?",
                            "פירוק ערכים יחידים (Singular Value Decomposition / SVD) הוא משפט המופת האוניברסלי: כל מטריצה ממשית $A$ בגודל $m \\times n$ ניתנת לפירוק מדויק: $A = U \\Sigma V^T$.",
                            "$U$ היא מטריצה אורתוגונלית $m \\times m$ (וקטורים יחידים שמאליים). $\\Sigma$ היא מטריצה אלכסונית $m \\times n$ של ערכים יחידים אי-שליליים $\\sigma_1 \\ge \\sigma_2 \\ge \\dots \\ge 0$ בסדר יורד. $V$ היא מטריצה אורתוגונלית $n \\times n$ (וקטורים יחידים ימניים).",
                            "גאומטרית, משפט SVD מוכיח שכל טרנספורמציה לינארית מעבירה כדור יחידה ב-$\mathbb{R}^n$ לאליפסואיד ב-$\mathbb{R}^m$, כאשר אורכי חצאי הצירים של האליפסואיד הם במדויק הערכים היחידים $\\sigma_i$!"
                        ]
                    },
                    {
                        "title": "קירוב בעל דרגה נמוכה ומשפט אקהארט-יאנג",
                        "points": [
                            "פירוק SVD מאפשר להציג כל מטריצה כסכום של מכפלות חיצוניות בעלות דרגה 1: $A = \\sum_{i=1}^{r} \\sigma_i \\mathbf{u}_i \\mathbf{v}_i^T$.",
                            "משפט אקהארט-יאנג-מירסקי מוכיח שהקירוב האופטימלי ביותר בעל דרגה $k$ למטריצה $A$ (שממזער את שגיאת השחזור) מתקבל פשוט על ידי שמירת $k$ הערכים היחידים הגדולים ביותר ומחיקת השאר ($A_k = \\sum_{i=1}^{k} \\sigma_i \\mathbf{u}_i \\mathbf{v}_i^T$).",
                            "דחיסת תמונות: תמונה ברזולוציה של $1000 \\times 1000$ דורשת 1,000,000 מספרים. שמירת $k=20$ הערכים היחידים המובילים בלבד דורשת רק $20 \\times (1000 + 1000 + 1) = 40,020$ מספרים - חיסכון של 96% בנפח תוך שמירה על איכות תמונה מרהיבה!"
                        ]
                    },
                    {
                        "title": "מערכות המלצה (פרס נטפליקס) וניתוח סמנטי חבוי (LSA)",
                        "points": [
                            "מערכות המלצה וסינון שיתופי: מטריצת דירוגים ענקית $A$ שבה שורות הן משתמשים ועמודות הן סרטים (ברובה ריקה).",
                            "פירוק $A \\approx U_k \\Sigma_k V_k^T$ מייצר וקטורי שיכון צפופים: שורות $U_k$ מייצגות העדפות משתמש לפי $k$ 'מושגים חבויים' (כגון מידת אקשן, רומנטיקה, מתח); שורות $V_k$ מייצגות את מאפייני הסרטים באותם מושגים בדיוק.",
                            "ניתוח סמנטי חבוי (LSA) בעיבוד שפה טבעית מפעיל SVD על מטריצות תדירות מילים במסמכים כדי לגלות נושאים סמנטיים משותפים ולקבץ מילים נרדפות באופן אוטומטי."
                        ]
                    }
                ],
                "trivia": [
                    {
                        "type": "multiple_choice",
                        "question": "מהו הניסוח המתמטי של פירוק ערכים יחידים (SVD) עבור מטריצה מלבנית A בגודל m x n?",
                        "options": [
                            "A = U Sigma V^T (כאשר U ו-V הן מטריצות אורתוגונליות ו-Sigma היא מטריצה אלכסונית של ערכים יחידים אי-שליליים)",
                            "A = P D P^-1",
                            "A = L U",
                            "A = Q R Q^T"
                        ],
                        "correct": 0,
                        "explanation": "פירוק SVD מפרק כל מטריצה ל-$U \\Sigma V^T$, כאשר $U$ מכילה וקטורים יחידים שמאליים, $\\Sigma$ מכילה ערכים יחידים ממוינים, ו-$V^T$ מכילה וקטורים יחידים ימניים."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מה מוכיח משפט אקהארט-יאנג-מירסקי לגבי קירוב מטריצות בדרגה נמוכה?",
                        "options": [
                            "שהקירוב האופטימלי בעל דרגה k (הממזער שגיאת שחזור) מתקבל על ידי קטימת פירוק ה-SVD ל-k הערכים היחידים הגדולים ביותר",
                            "שלכל מטריצה ריבועית יש דטרמיננטה השווה לעקבה שלה",
                            "שמטריצות בעלות דרגה קטנה מ-5 אינן ניתנות להיפוך",
                            "שערכים יחידים גדלים באופן מעריכי עם ממדי המטריצה"
                        ],
                        "correct": 0,
                        "explanation": "משפט אקהארט-יאנג מוכיח שסכום $k$ האיברים הראשונים בפירוק ה-SVD ($A_k = \\sum_{i=1}^k \\sigma_i \\mathbf{u}_i \\mathbf{v}_i^T$) הוא הקירוב הטוב ביותר האפשרי בנורמת פרובניוס ובנורמה ספקטרלית."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "כיצד קשורים הערכים היחידים (sigma_i) של מטריצה A לערכים העצמיים של המטריצה הסימטרית A^T A?",
                        "options": [
                            "הערכים היחידים הם השורשים הריבועיים האי-שליליים של הערכים העצמיים של A^T A (sigma_i = sqrt(lambda_i))",
                            "הערכים היחידים שווים לערכים העצמיים חלקי 2",
                            "הערכים היחידים הם ההופכיים של הערכים העצמיים",
                            "אין שום קשר מתמטי ביניהם"
                        ],
                        "correct": 0,
                        "explanation": "הווקטורים היחידים הימניים הם הווקטורים העצמיים של $A^T A$, והערכים היחידים שווים לשורש הריבועי של ערכיה העצמיים: $\\sigma_i = \\sqrt{\\lambda_i(A^T A)}$."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "במערכות המלצה (כגון בתחרות פרס נטפליקס), מה מייצגות מטריצות הגורמים הצפופות U ו-V המתקבלות מפירוק SVD?",
                        "options": [
                            "וקטורי שיכון (Embeddings) המייצגים העדפות משתמשים ומאפייני סרטים במרחב מושגים חבוי משותף",
                            "את כתובות ה-IP של שרתי ההזרמה",
                            "את חותמות הזמן המדויקות של הצפייה",
                            "את מפתחות ההצפנה של סיסמאות המשתמשים"
                        ],
                        "correct": 0,
                        "explanation": "פירוק מטריצות בלמידת מכונה מייצג העדפות משתמשים ($U$) ומאפייני פריטים ($V$) כווקטורים במרחב מושגים חבוי בן $k$ ממדים."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהו 'מספר ההתניה' (Condition Number) של מטריצה (kappa(A) = sigma_max / sigma_min)?",
                        "options": [
                            "מדד לרגישות נומרית: עד כמה שגיאות או רעש קטן בקלט עלולים להיות מוגברים בפתרון הפלט",
                            "מגבלת הטמפרטורה של זיכרון ה-DRAM",
                            "מספר הערכים השליליים במטריצה",
                            "כמות פעולות הנקודה הצפה בשנייה"
                        ],
                        "correct": 0,
                        "explanation": "מספר ההתניה $\\kappa(A) = \\frac{\\sigma_{\\max}}{\\sigma_{\\min}}$ מודד יציבות נומרית; מטריצה בעלת מספר התניה ענק מגבירה שגיאות עיגול בנוסחאות חישוב."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "כיצד מחושבת המטריצה הפסאודו-הופכית (A+) באמצעות פירוק ה-SVD של המטריצה (A = U Sigma V^T)?",
                        "options": [
                            "A+ = V Sigma^+ U^T (כאשר Sigma^+ הופכת את כל הערכים היחידים שאינם אפס: 1/sigma_i)",
                            "A+ = U^T Sigma V",
                            "A+ = (U Sigma V^T)^-1",
                            "A+ = Sigma^-1"
                        ],
                        "correct": 0,
                        "explanation": "המטריצה הפסאודו-הופכית מחושבת בקלות באמצעות $A^+ = V \\Sigma^+ U^T$, כאשר $\\Sigma^+$ משחאלפת את $\\Sigma$ ומחליפה כל $\\sigma_i > 0$ ב-$1/\\sigma_i$."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "כמה ערכים יחידים של מטריצה A הם גדולים ממש מאפס (sigma_i > 0)?",
                        "options": [
                            "בדיוק כמספר הדרגה המתמטית (Rank) של המטריצה A",
                            "תמיד כמספר השורות m",
                            "תמיד כמספר העמודות n",
                            "אף ערך יחיד אינו גדול מאפס"
                        ],
                        "correct": 0,
                        "explanation": "מספר הערכים היחידים החיוביים $\\sigma_i > 0$ שווה במדויק לדרגת המטריצה (ממד מרחב העמודות שלה)."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהי נורמת פרובניוס (Frobenius Norm) של מטריצה?",
                        "options": [
                            "השורש של סכום ריבועי כל איברי המטריצה (השווה גם לשורש סכום ריבועי כל הערכים היחידים)",
                            "המספר הבודד הגדול ביותר במטריצה",
                            "הערך המוחלט של הדטרמיננטה",
                            "מספר השורות שאינן אפס בצורה מדורגת"
                        ],
                        "correct": 0,
                        "explanation": "נורמת פרובניוס $\\|A\\|_F = \\sqrt{\\sum_{i,j} A_{ij}^2}$ מודדת את הגודל הכולל של המטריצה, ושווה לנורמת וקטור הערכים היחידים שלה $\\sqrt{\\sum_i \\sigma_i^2}$."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "בניתוח סמנטי חבוי (LSA) בעיבוד שפה טבעית, איזו מטריצה מפורקת באמצעות SVD?",
                        "options": [
                            "מטריצת תדירות מילים במסמכים (Term-Document Matrix)",
                            "טבלת ניתוב כתובות רשת",
                            "מטריצת תווי ASCII בינאריים",
                            "טבלת מסד נתונים של שמות משתמשים"
                        ],
                        "correct": 0,
                        "explanation": "ב-LSA מפרקים מטריצת תדירות של מילים במסמכים (כמו TF-IDF) באמצעות SVD כדי לחשוף נושאים סמנטיים חבויים."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מדוע פירוק SVD פועל על כל מטריצה מלבנית שהיא, בניגוד ללכסון ערכים עצמיים רגיל?",
                        "options": [
                            "מכיוון שהמכפלות A A^T ו-A^T A הן תמיד סימטריות וחיוביות למחצה, מה שמבטיח קיום ערכים יחידים ממשיים ואי-שליליים תמיד",
                            "מכיוון שלמטריצות מלבניות יש יותר שורות מעמודות",
                            "מכיוון שפירוק SVD אינו משתמש במספרי נקודה צפה",
                            "מכיוון ש-SVD מאפס את כל ערכי המטריצה"
                        ],
                        "correct": 0,
                        "explanation": "לכל מטריצה ממשית $A$, המכפלות $A^T A$ ו-$A A^T$ הן תמיד סימטריות וחיוביות למחצה, מה שמבטיח קיום וקטורים עצמיים אורתוגונליים וערכים יחידים ממשיים תמיד."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "לאיזו צורה גאומטרית הופך כדור יחידה ב-R^n לאחר טרנספורמציה של מטריצה A עם ערכים יחידים sigma_1, sigma_2, ...?",
                        "options": [
                            "לאליפסואיד במרחב R^m שחצאי ציריו הראשיים שווים באורכם לערכים היחידים sigma_i",
                            "לקובייה מושלמת שאורך צלעה שווה ל-det(A)",
                            "לקו ישר חד-ממדי",
                            "למשולש שטוח העובר בראשית"
                        ],
                        "correct": 0,
                        "explanation": "גאומטרית, פירוק SVD מוכיח שכל טרנספורמציה ממפה כדור יחידה לאליפסואיד שציריו הראשיים שווים באורכם לערכים היחידים $\\sigma_i$."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהו פירוק QR (QR Decomposition) של מטריצה A?",
                        "options": [
                            "פירוק A למכפלה של מטריצה אורתוגונלית Q (שבה Q^T Q = I) ומטריצה משולשית עליונה R",
                            "חלוקת מטריצה A לארבעה רבעים שווים",
                            "חישוב שורש ריבועי של המטריצה A",
                            "הכפלת מטריצה A במספר קוונטי אקראי"
                        ],
                        "correct": 0,
                        "explanation": "פירוק QR מפרק מטריצה למטריצה אורתוגונלית $Q$ (מגרם-שמידט או שיקופי האוסהולדר) ולמטריצה משולשית עליונה $R$, המשמשת לפתרון יציב של ריבועים פחותים."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהו פירוק LU של מטריצה ריבועית A?",
                        "options": [
                            "פירוק A למכפלה של מטריצה משולשית תחתונה L ומטריצה משולשית עליונה U (A = L U)",
                            "פירוק A למטריצה שמאלית ומטריצה עליונה",
                            "פירוק A למנטיסה ומעריך בנקודה צפה",
                            "תרגום A למשוואה לינארית"
                        ],
                        "correct": 0,
                        "explanation": "פירוק LU מייצג את פעולות דירוג גאוס בצורת מטריצות: $L$ שומרת את מכפילי הדירוג ו-$U$ היא הצורה המדורגת המשולשית העליונה."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהו פירוק חולסקי (Cholesky Decomposition) למטריצה סימטרית חיובית מוגדרת A?",
                        "options": [
                            "פירוק A למכפלת מטריצה משולשית תחתונה בשחלוף של עצמה: A = L L^T",
                            "פירוק A לשלוש מטריצות אלכסוניות",
                            "קירוב A באמצעות רעש גאוסיאני",
                            "הפיכת A באמצעות חישוב הדטרמיננטה שלה"
                        ],
                        "correct": 0,
                        "explanation": "למטריצות סימטריות חיוביות מוגדרות, פירוק חולסקי מחשב $A = L L^T$ במחצית מפעולות החישוב של פירוק LU, ונפוץ במיוחד בסינון קלמן ותהליכים גאוסיאניים."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהו הטרייד-אוף בעת בחירת דרגת הקטימה k בדחיסת מטריצות באמצעות SVD?",
                        "options": [
                            "ערך k קטן יותר מספק חיסכון ניכר בזיכרון אך מאבד פרטים דקים ומגדיל את שגיאת השחזור",
                            "ערך k קטן יותר מאריך את זמן היפוך המטריצה",
                            "ערך k גדול יותר גורם לערכים היחידים להפוך לשליליים",
                            "ערך k גדול יותר משנה את גודל הגופן של התמונה"
                        ],
                        "correct": 0,
                        "explanation": "בחירת $k$ מאזנת בין דחיסה לדיוק: $k$ קטן דוחס משמעותית את נפח הזיכרון, בעוד ש-$k$ גדול משמר נאמנות מקסימלית לפרטים הדקים של הנתונים."
                    }
                ]
            }
        ]
    }

    # Write English file
    with open(TARGET_EN, "w", encoding="utf-8") as f:
        yaml.safe_dump(la_en, f, allow_unicode=True, sort_keys=False, width=100)
    print(f"Generated {TARGET_EN}")

    # Write Hebrew file
    with open(TARGET_HE, "w", encoding="utf-8") as f:
        yaml.safe_dump(la_he, f, allow_unicode=True, sort_keys=False, width=100)
    print(f"Generated {TARGET_HE}")

if __name__ == "__main__":
    create_linalg_datasets()

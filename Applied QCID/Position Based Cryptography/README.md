# Position-Verification in the No Pre-shared Entanglement (No-PE) Model
In Position-Verification, we have two verifiers $V_0$ and $V_1$, and a prover $P$ at position $pos$ that lies on the straight line between $V_0$ and $V_1$. Now, to verify $P$’s position, $V_0$ sends a BB84 qubit $H^{\theta}|x⟩$ to $P$, and $V_1$ sends the corresponding basis $\theta$ to $P$. The sending of these messages is timed in such a way that $H^{\theta}|x⟩$ and $\theta$ arrive at position $pos$ at the same time. $P$ has to measure the qubit in basis $\theta$ to obtain $x$, and immediately send $x$ to both $V_0$ and $V_1$, who verify the correctness of $x$ and if it has arrived “in time”.  

--- 

Here is the verification scheme:
  - $V_0$ chooses two random bits $x, \theta \in \{0, 1\}$ and privately sends them to $V_1$.  
  - $V_0$ prepares the qubit $H^{\theta}|x⟩$ and sends it to $P$, and $V_1$ sends the bit $\theta$ to $P$, so that $H^{\theta}|x⟩$ and $\theta$ arrive at the same time at $P$.
  - When $H^{\theta}|x⟩$ and $\theta$ arrive, $P$ measures $H^{\theta}|x⟩$ in basis $\theta$ to observe $x^′ \in \{0,1\}$, and sends $x^′$ to $V_0$ and $V_1$.
  - $V_0$ and $V_1$ accept if on both sides $x^′$ arrives in time and $x^′= x$.
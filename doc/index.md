# Detecting Bombs with Quantum Mechanics



<section>
  <div class="flex-center" style="height: 300px;">
    <div class="bomb1">
      &#x1f4a3;
    </div>
    <div class="bomb2">
      &#x1f4a3;
    </div>
    <div class="bomb3">
      &#x1f4a3;
    </div>
    <div class="bomb4">
      &#x1f4a3;
    </div>
    <div class="bomb5">
      &#x1f4a3;
    </div>
  </div>
</section>



## Superposition Crashcourse


A quantum mechanical system consists of a number of discrete states


The *wave function* `$\psi$` gives a description of these states


To find out which definite state it is in, we have to do a
*measurement*


A measurement is done by perturbing the system, for example by
making a single photon interact with it


In a simple quantum system where there are only two possible states,
`$|0\rangle$` and `$|1\rangle$`, the wave function can *collapse*
into either, but only one at a time
`$$
|\psi\rangle \rightarrow
\begin{cases}
|0\rangle\\ \\
|1\rangle\end{cases}
$$`


An example is a particle that can exhibit one of two properties:
spin up, or spin down
<div class="flex-center">
  <div class="ball-lg center">
    $\uparrow$
  </div>
  <div class="ball-lg center">
    $\downarrow$
  </div>
</div>


The innerproduct between two wave functions
`$$\langle\phi|\psi\rangle$$`
measures the overlap between the corresponding physical states


The states are orthogonal
`$$
\langle 0|0\rangle = 1\\
\langle 1|1\rangle = 1\\
\langle 0|1\rangle = 0\\
\langle 1|0\rangle = 0
$$`


The states are basis vectors, spanning
a *Hilbert space*


As vectors, they can be represented with the standard basis in 2D
`$$
\psi \rightarrow
\begin{cases}
\vec{e_0} = (1,0)\\ \\
\vec{e_1} = (0,1)
\end{cases}
$$`


Wave functions are super positions of states
`$$
|\psi\rangle = c_0|0\rangle + c_1|1\rangle\\\
$$`
where $c_0$ and $c_1$ are complex numbers.


The probability of finding the system in state $|0\rangle$ is $|c_0|^2$,
and $|c_1|^2$ for $|1\rangle$.


This is due to
`$$
\langle\psi|\psi\rangle = |c_0|^2 + |c_1|^2 = 1
$$`


Assuming there is a 50 % probability of either state
`$$
|\psi\rangle = \frac{1}{\sqrt{2}}\left(|0\rangle + |1\rangle\right)\\
$$`



## The Double-slit Experiment


![](img/double_slit.jpg)


A manifestation of the (quantum) superposition principle



<section>
  <h2>An Interaction-free Measurement</h2>
</section>
<section>
  A measurement that does not require any mechanical interaction
  to yield information about a state
</section>
<section data-auto-animate>
  <div class="flex-center">
    <div data-id="ball" class="ball">
    </div>
  </div>
  <div class="flex-center">
    <div data-id="1" class="box">
    </div>
    <div data-id="2" class="box">
    </div>
  </div>
</section>
<section data-auto-animate>
  <div class="flex-center">
    <div class="ball-white">
    </div>
  </div>
  <div class="flex-center">
    <div data-id="1" class="box center">
      <div data-id="ball" class="ball-white">
      </div>
    </div>
    <div data-id="2" class="box">
    </div>
  </div>
</section>
<section data-auto-animate>
  <div class="flex-space-between">
    <div class="ball-white">
    </div>
  </div>
  <div class="flex-space-between">
    <div data-id="1" class="box center">
      <div data-id="box" class="ball-white">
      </div>
    </div>
    <div data-id="2" class="box">
    </div>
  </div>
</section>
<section data-auto-animate>
  <div class="flex-center">
    <div data-id="1" class="ball-lg center">
      $\uparrow$
    </div>
    <div data-id="2" class="ball-lg center">
      $\downarrow$
    </div>
  </div>
</section>
<section data-auto-animate>
  <div class="flex-center">
    <div data-id="1" class="ball-lg center">
      ?
    </div>
    <div data-id="2" class="ball-lg center">
      ?
    </div>
  </div>
</section>
<section data-auto-animate>
  <div class="flex-space-between">
    <div data-id="1" class="ball-lg center">
      <p data-fragment-index="1" class="fragment">
        $\uparrow$
      </p>
    </div>
    <div data-id="2" class="ball-lg center">
      <p data-fragment-index="2" class="fragment">
        $\downarrow$
      </p>
    </div>
  </div>
</section>
<section data-auto-animate>
  Einstein, Podolsky and Rosen (1935):<br><q>Spukhafte Fernwirkung</q>
</section>
<section data-auto-animate>
  John Bell (1964):<br>
  <q>Hold on, EPR. What if we do measurements along different axes?</q>
</section>
<section data-auto-animate>
  <div data-id="box" class="point"></div>
  <img src="img/bell.svg" height="600">
</section>



<section>
  <h2>The Elitzur&ndash;Vaidman Bomb Tester</h2>
</section>
<section data-auto-animate data-transition="zoom">
  <div style="display: flex; justify-content: center;">
    <div data-id="line1" class="l1">
    </div>
    <div data-id="line2" class="l2">
    </div>
    <div data-id="line3" class="l3">
    </div>
    <div data-id="box" class="exp-box">
    </div>
    <div class="fragment">
      <div data-id="beam-splitter-1" class="bs1">
      </div>
      <div data-id="beam-splitter-2" class="bs2">
      </div>
      <div data-id="mirror-left" class="ml">
      </div>
      <div data-id="mirror-right" class="mr">
      </div>
    </div>
    <div class="fragment">
      <div data-id="detector-A" class="da">
        A
      </div>
      <div data-id="detector-B" class="db">
        B
      </div>
    </div>
    <div class="fragment">
      <div data-id="bomb-container" class="bomb-container">
      </div>
    </div>
    <div class="fragment">
      <div class="bomb-loc">
        &#x1f4a3;
      </div>
      <audio data-preload data-autoplay>
        <source data-src="snd/bomb.mp3" data-preload></source>
      </audio>
    </div>
  </div>
</section>
<section>
  The photon starts in the state $|0\rangle$,
  which means it is on a horizontal path. 
  Conversely, being in state $|1\rangle$ means it is on
  a vertical path.
</section>
<section>
  Changing direction (reflecting off a mirror)
  $$
    |0\rangle \rightarrow i|1\rangle
  $$
  $$
    |1\rangle \rightarrow i|0\rangle
  $$
</section>
<section>
  Going into a beam splitter 
  $$
    |0\rangle \rightarrow 
    \frac{1}{\sqrt{2}}\left(|0\rangle + i|1\rangle\right)
  $$
  $$
    |1\rangle \rightarrow 
    \frac{1}{\sqrt{2}}\left(|1\rangle + i|0\rangle\right)
  $$
</section>
<section>
  Lower path blocked
  $$
    |0\rangle \rightarrow 
    i|1\rangle \rightarrow 
    -|0\rangle \rightarrow
    -\frac{1}{\sqrt{2}}\left(|0\rangle + i|1\rangle\right)
  $$
</section>
<section>
  Both paths open
  $$
    |0\rangle \rightarrow 
    \frac{1}{\sqrt{2}}\left(|0\rangle + i|1\rangle\right) \rightarrow
    \frac{1}{\sqrt{2}}\left(-|0\rangle + i|1\rangle\right) \rightarrow
    -|0\rangle
  $$  
</section>
<section>
  Let us consider this when there is a 50 % chance that a bomb
  is blocking the lower path
</section>
<section>
  <ol>
    <li class="fragment fade-in-then-semi-out">
      There is no photon registered in any of the two detectors.
      The bomb exploded and destroyed the photon in the process.
    </li>
    <li class="fragment fade-in-then-semi-out">
      The photon is registered by detector A.
      The result is inconclusive. 
      Whether the object is there or not there is always a chance for
      the photon to be detected by A. The experiment has to be repeated.
    </li>
    <li class="fragment fade-in-then-semi-out">
      The photon is registered by detector B.
      We conclude that the object is present, 
      since the probability of detecting the photon by
      B with both paths open is 0.
    </li>
  </ol>
</section>
<section>
  The experiment gives us a 25 % chance of finding out if the bomb is
  live without detonating it
</section>
<section>
  If we repeat the experiment for the bombs that were undecided, we
  can increase the detection to 33 %
</section>
<section>
  Improving the experimental setup can give a detection of arbitrary
  good precision
</section>
<section data-background-color="black">
</section>

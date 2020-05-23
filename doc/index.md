# Detecting Bombs with Quantum Mechanics



## Superposition Crashcourse


  A *wave function* `$\psi$` describes the quantum mechanical states
  of the system


  In a simple quantum system where there are only two possible states,
  `$|0\rangle$` and `$|1\rangle$`, the wave function describes it as follows
  `$$
  |\psi\rangle \rightarrow
  \begin{cases}
  |0\rangle\\
  |1\rangle\end{cases}
  $$`



<section data-auto-animate>
  <div data-id="eq" style="height: 340px;">
    <div data-id="1" style="background: black; position: absolute; top: 150px; left: 16%; width: 60px; height: 60px;"></div>
    <div data-id="2" style="background: black; position: absolute; top: 150px; left: 36%; width: 60px; height: 60px;"></div>
    <div data-id="3" style="background: black; position: absolute; top: 150px; left: 56%; width: 60px; height: 60px;"></div>
    <div data-id="4" style="background: black; position: absolute; top: 150px; left: 76%; width: 60px; height: 60px;"></div>
  </div>
</section>
<section data-auto-animate>
  <p data-id="eq" style="line-height: 3em;">
  $$
  |\psi\rangle \rightarrow
  \begin{cases}
  |0\rangle\\
  |1\rangle\end{cases}
  $$
  </p>
  <div data-id="1" style="text-align: center; height: 1px;"></div>
  <div data-id="2" style="text-align: center; height: 1px;"></div>
  <div data-id="3" style="text-align: center; height: 1px;"></div>
  <div data-id="4" style="text-align: center; height: 1px;"></div>
</section>



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


  These states are basis vectors (or functions), spanning
  a Hilbert space


  As vectors, they can be represented as the standard basis in 2D
  `$$
  \psi \rightarrow
  \begin{cases}
  e_0 = (1,0)\\
  e_1 = (0,1)
  \end{cases}
  $$`


  Assuming there is a 50 percent probability of either state,
  the normalized wave function is
  `$$
  |\psi\rangle = \frac{1}{\sqrt{2}}\left(|0\rangle + |1\rangle\right)\\
  \langle\psi|\psi\rangle = 1
  $$`



## The Double-slit Experiment



<section>
  <h2>An Interaction-free Measurement</h2>
</section>
<section>
  A measurement that does not require any mechanical interaction
  to 
</section>
<section data-auto-animate>
  <p data-id="box">
    Imagine two boxes, and an object that is randomly put into either.
    If you open one of the boxes and the object is not there,
    you know that it must be in the other box.
  </p>
</section>
<section data-auto-animate>
  <div class="flex-center">
    <div data-id="box" class="ball">
    </div>
  </div>
  <div class="flex-center">
    <div data-id="box-1" class="box">
    </div>
    <div data-id="box-2" class="box">
    </div>
  </div>
</section>
<section data-auto-animate>
  <div class="flex-center">
    <div class="ball" style="background: white;">
    </div>
  </div>
  <div class="flex-center">
    <div data-id="box-1" class="box center">
      <div data-id="box" class="ball" style="background: white;">
      </div>
    </div>
    <div data-id="box-2" class="box">
    </div>
  </div>
</section>
<section data-auto-animate>
  <div style="display: flex; justify-content: center;">
    <div data-id="line1" style="position: absolute; 
                                left: 10%; 
                                top: 95.1%;
                                height: 2px;
                                width: 100px;
                                background: black;
                              ">
    </div>
    <div data-id="line2" style="position: absolute; 
                                left: 80%; 
                                top: 4.6%;
                                height: 2px;
                                width: 100px;
                                background: black;
                              ">
    </div>
    <div data-id="line3" style="position: absolute; 
                                left: 74.9%; 
                                top: -7%;
                                transform: rotate(90deg);
                                height: 2px;
                                width: 100px;
                                background: black;
                              ">
    </div>
    <div data-id="box" style="border: 2px   
                              solid black; 
                              height: 400px;
                              width: 60%;
                              left: 20%;">
    </div>
    <div class="fragment">
      <div data-id="beam-splitter-1" style="position: absolute;
                                            background: rgba(0, 179, 119, 0.5);
                                            top: 93.5%; left: 16.75%;
                                            transform: rotate(135deg);
                                            border: 1px solid rgb(0, 179, 119);
                                            height: 10px;
                                            width: 60px;
                                            ">
      </div>
      <div data-id="beam-splitter-2" style="position: absolute;
                                            background: rgba(0, 179, 119, 0.5);
                                            top: 3.75%; left: 76.75%;
                                            transform: rotate(135deg);
                                            border: 1px solid rgb(0, 179, 119);
                                            height: 10px;
                                            width: 60px;
                                            ">
      </div>
      <div data-id="mirror-left" style="position: absolute;
                                            background: rgb(0, 179, 119);
                                            top: 3.75%; left: 16.75%;
                                            transform: rotate(135deg);
                                            border: 1px solid rgb(0, 179, 119);
                                            height: 10px;
                                            width: 60px;
                                            ">
      </div>
      <div data-id="mirror-right" style="position: absolute;
                                            background: rgb(0, 179, 119);
                                            top: 93.5%; left: 76.75%;
                                            transform: rotate(135deg);
                                            border: 1px solid rgb(0, 179, 119);
                                            height: 10px;
                                            width: 60px;
                                            ">
      </div>
    </div>
    <div class="fragment">
      <div data-id="detector-A" style="position: absolute; 
                                      left: 90.5%; 
                                      top: -1%; 
                                      border: 1px solid red;
                                      background: rgba(255, 0, 0, 0.5);
                                      z-index: 50;
                                      height: 50px; 
                                      width: 50px; 
                                      ">
                                      A
      </div>
      <div data-id="detector-B" style="position: absolute; 
                                      left: 77.25%; 
                                      top: -30%; 
                                      border: 1px solid red;
                                      background: rgba(255, 0, 0, 0.5);
                                      z-index: 50;
                                      height: 50px; 
                                      width: 50px; 
                                      ">
                                      B
      </div>
    </div>
    <div class="fragment">
      <div data-id="container" style="position: absolute; 
                                      left: 45%; 
                                      top: 88%; 
                                      border: 1px solid blue;
                                      z-index: 50;
                                      height: 60px; 
                                      width: 60px; 
                                      background: rgba(255, 0, 0, 0.5);
                                      ">
      </div>
    </div>
  </div>
</section>

# Evaluation Variance Policy

Future TEMRAL evaluations should treat model variance as part of the experiment, not as cleanup after the result.

Before treatment, declare:
- expected sources of variance;
- baseline repeat count;
- treatment repeat count;
- deterministic or stochastic settings;
- cache state;
- retry policy;
- acceptance metric;
- exact-parity rule, if applicable;
- admission failure behavior.

A treatment result should not be crowned when the control itself fails the predeclared stability condition.

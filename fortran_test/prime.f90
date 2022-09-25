program prime_finder
  implicit none

  integer :: maxn
  integer :: n
  real :: sqrt_n
  integer :: n_divisor
  logical :: isprime
  integer, allocatable :: primes(:)
  integer :: primes_pointer
  integer :: prime_count


  !Input n
  print *, "Please input a number: "
  read(*,*) maxn

  allocate(primes(maxn))

  primes_pointer = 1
  prime_count = 0

  do n = 2, maxn
    sqrt_n = n**0.5
    isprime = .true.

    n_divisor = 2
    do while (n_divisor <= sqrt_n .and. isprime)

      if (MOD(n,n_divisor) == 0) then
        isprime = .false.
      endif

      n_divisor = n_divisor + 1
    end do

    if (isprime) then
      primes(primes_pointer) = n
      primes_pointer = primes_pointer + 1
      prime_count = prime_count + 1
    endif

  end do


  print *, primes(:prime_count)
  print *, prime_count
endprogram prime_finder

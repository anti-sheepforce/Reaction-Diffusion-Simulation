! Calls RK_SOLV with initial values to test functionality

PROGRAM TEST_RK_SOLV
IMPLICIT NONE

INTEGER, DIMENSION(2,4) :: EdMat, ProdMat
REAL*8, DIMENSION(4) :: ConcVec
REAL*8, DIMENSION(2) :: RateVec
REAL*8 :: dtime = 1.0d-2, finaltime=1.0d3
INTEGER :: method = 1, NUMTHREAD = 4, i

INTERFACE
	SUBROUTINE RK_SOLV(EdMat, ProdMat, RateVec, ConcVec, dtime, finaltime, method, NUMTHREAD)
		USE omp_lib                                                                                             ! OMP definitions

		IMPLICIT NONE

		INCLUDE 'rk_solv.fh'                                                                                    ! include type declarations

		REAL*8 ::  DiffEquation
	END SUBROUTINE
END INTERFACE

WRITE(*, *) "================================================================================"
WRITE(*, *) "|| Here is TEST_RK_SOLV. Testing the routine RK_SOLV with some initial values ||"
WRITE(*, *) "================================================================================"

EdMat(1,1) = 1
EdMat(1,2) = 1
EdMat(1,3) = 0
EdMat(1,4) = 0
EdMat(2,1) = 0
EdMat(2,2) = 0
EdMat(2,3) = 1
EdMat(2,4) = 1

WRITE(*, *)
WRITE(*, *) "EdMat"
DO i = 1, 2
	WRITE(*, *) "        ", EdMat(i,:)
END DO
WRITE(*, *)



ProdMat(1,1) = 0
ProdMat(1,2) = 0
ProdMat(1,3) = 1
ProdMat(1,4) = 1
ProdMat(2,1) = 1
ProdMat(2,2) = 1
ProdMat(2,3) = 0
ProdMat(2,4) = 0

WRITE(*, *)
WRITE(*, *) "ProdMat"
DO i = 1, 2
        WRITE(*, *) "        ", ProdMat(i,:)
END DO
WRITE(*, *)


ConcVec(1) = 10.0d0
ConcVec(2) = 4.0d0
ConcVec(3) = 2.0d0
ConcVec(4) = 0.2d0

WRITE(*, *)
WRITE(*, *) "ConcVec"
WRITE(*, *) "        ", ConcVec(1:)


RateVec(1) = 0.005d0
RateVec(2) = 0.01d0

WRITE(*, *)
WRITE(*, *) "RateVec"
DO i = 1, 2
	WRITE(*, *) "        ", RateVec(i)
END DO
WRITE(*, *)

WRITE(*, *) "*****************************"
WRITE(*, *) "**** now calling RK_SOVL ****"
WRITE(*, *) "*****************************"

CALL RK_SOLV(EdMat, ProdMat, RateVec, ConcVec, dtime, finaltime, method, NUMTHREAD)



WRITE(*, *)
WRITE(*, *) "================================"
WRITE(*, *) "|| Finished TEST_RK_SOLV. Bye ||"
WRITE(*, *) "================================"
WRITE(*, *)


END PROGRAM TEST_RK_SOLV

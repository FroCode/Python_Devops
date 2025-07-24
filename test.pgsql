                                   🔧 DEV STAGE
                              ---------------------
                            +------------------------+
                            |  Developers push F1-F5 |
                            +------------------------+
                                       |
                                       v
                         +-------------------------------+
                         |  PR: Merge Feature Branch --> |
                         |            `main`            |
                         +-------------------------------+
                                       |
                                       v
                             🔬 TEST STAGE (Staging Env)
                          --------------------------------
                         +-------------------------------+
                         | Auto deploy to test env (CI)  |
                         +-------------------------------+
                                       |
                                       v
                              +------------------+
                              | Run integration  |
                              | and regression   |
                              | tests (Airflow,  |
                              | Redshift, etc.)  |
                              +------------------+
                                       |
                                +------+------+
                                |             |
                                v             v
                         (All tests pass)  (Test fails)
                                |             |
                                v             v
                   +------------------+   +---------------------------+
                   | Deploy to prod   |   | Identify failed features |
                   +------------------+   +---------------------------+
                                                   |
                                                   v
                            🛑 SELECTIVE ROLLBACK FLOW
                          --------------------------------
                                    +-------------------+
                                    | Find commit SHAs  |
                                    | (e.g. F4, F5)      |
                                    +-------------------+
                                                   |
                                                   v
                           +-------------------------------+
                           | Run `git revert F4 F5` on dev |
                           +-------------------------------+
                                                   |
                                                   v
                           +-------------------------------+
                           | Auto-deploy reverted code to  |
                           |       test environment        |
                           +-------------------------------+
                                                   |
                                                   v
                                       +----------------------+
                                       | Run CI tests again   |
                                       +----------------------+
                                                   |
                                            +------+------+
                                            |             |
                                            v             v
                                      (Tests OK)     (Still failing)
                                            |             |
                                            v             v
                                +-------------------+     +---------------------+
                                | Notify & deploy   |     | Debug/test locally  |
                                | revert to prod    |     | or revert more SHAs |
                                +-------------------+     +---------------------+


# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2019 replay file
# Internal Version: 2018_09_24-13.41.51 157541
# Run by nidish on Wed Mar 18 11:01:10 2020
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(1.36719, 1.36719), width=201.25, 
    height=135.625)
session.viewports['Viewport: 1'].makeCurrent()
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
execfile('nodels.py', __main__.__dict__)
#: The model database "/home/nidish/Documents/Academics/RESEARCH/INTRED_STUDY/ABAQUS_MODELS/HOLEPLATE/ABQCONS/MATEX/../HOLEPLATE_ABQC.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: Done 1
#: Done 2
#: Done 3
#: Done 4
#: Done 5
#: Done 6
#: Done 7
#: Done 8
#: Done 9
#: Done 10
#: Done 11
#: Done 12
#: Done 13
#: Done 14
#: Done 15
#: Done 16
#: Done 17
#: Done 18
#: Done 19
#: Done 20
#: Done 21
#: Done 22
#: Done 23
#: Done 24
#: Done 25
#: Done 26
#: Done 27
#: Done 28
#: Done 29
#: Done 30
#: Done 31
#: Done 32
#: Done 33
#: Done 34
#: Done 35
#: Done 36
#: Done 37
#: Done 38
#: Done 39
#: Done 40
#: Done 41
#: Done 42
#: Done 43
#: Done 44
#: Done 45
#: Done 46
#: Done 47
#: Done 48
#: Done 49
#: Done 50
#: Done 51
#: Done 52
#: Done 53
#: Done 54
#: Done 55
#: Done 56
#: Done 57
#: Done 58
#: Done 59
#: Done 60
#: Done 61
#: Done 62
#: Done 63
#: Done 64
#: Done 65
#: Done 66
#: Done 67
#: Done 68
#: Done 69
#: Done 70
#: Done 71
#: Done 72
#: Done 73
#: Done 74
#: Done 75
#: Done 76
#: Done 77
#: Done 78
#: Done 79
#: Done 80
#: Done 81
#: Done 82
#: Done 83
#: Done 84
#: Done 85
#: Done 86
#: Done 87
#: Done 88
#: Done 89
#: Done 90
#: Done 91
#: Done 92
#: Done 93
#: Done 94
#: Done 95
#: Done 96
#: Done 97
#: Done 98
#: Done 99
#: Done 100
#: Done 101
#: Done 102
#: Done 103
#: Done 104
#: Done 105
#: Done 106
#: Done 107
#: Done 108
#: Done 109
#: Done 110
#: Done 111
#: Done 112
#: Done 113
#: Done 114
#: Done 115
#: Done 116
#: Done 117
#: Done 118
#: Done 119
#: Done 120
#: Done 121
#: Done 122
#: Done 123
#: Done 124
#: Done 125
#: Done 126
#: Done 127
#: Done 128
#: Done 129
#: Done 130
#: Done 131
#: Done 132
#: Done 133
#: Done 134
#: Done 135
#: Done 136
#: Done 137
#: Done 138
#: Done 139
#: Done 140
#: Done 141
#: Done 142
#: Done 143
#: Done 144
#: Done 145
#: Done 146
#: Done 147
#: Done 148
#: Done 149
#: Done 150
#: Done 151
#: Done 152
#: Done 153
#: Done 154
#: Done 155
#: Done 156
#: Done 157
#: Done 158
#: Done 159
#: Done 160
#: Done 161
#: Done 162
#: Done 163
#: Done 164
#: Done 165
#: Done 166
#: Done 167
#: Done 168
#: Done 169
#: Done 170
#: Done 171
#: Done 172
#: Done 173
#: Done 174
#: Done 175
#: Done 176
#: Done 177
#: Done 178
#: Done 179
#: Done 180
#: Done 181
#: Done 182
#: Done 183
#: Done 184
#: Done 185
#: Done 186
#: Done 187
#: Done 188
#: Done 189
#: Done 190
#: Done 191
#: Done 192
#: Done 193
#: Done 194
#: Done 195
#: Done 196
#: Done 197
#: Done 198
#: Done 199
#: Done 200
#: Done 201
#: Done 202
#: Done 203
#: Done 204
#: Done 205
#: Done 206
#: Done 207
#: Done 208
#: Done 209
#: Done 210
#: Done 211
#: Done 212
#: Done 213
#: Done 214
#: Done 215
#: Done 216
#: Done 217
#: Done 218
#: Done 219
#: Done 220
#: Done 221
#: Done 222
#: Done 223
#: Done 224
#: Done 225
#: Done 226
#: Done 227
#: Done 228
#: Done 229
#: Done 230
#: Done 231
#: Done 232
#: Done 233
#: Done 234
#: Done 235
#: Done 236
#: Done 237
#: Done 238
#: Done 239
#: Done 240
#: Done 241
#: Done 242
#: Done 243
#: Done 244
#: Done 245
#: Done 246
#: Done 247
#: Done 248
#: Done 249
#: Done 250
#: Done 251
#: Done 252
#: Done 253
#: Done 254
#: Done 255
#: Done 256
#: Done 257
#: Done 258
#: Done 259
#: Done 260
#: Done 261
#: Done 262
#: Done 263
#: Done 264
#: Done 265
#: Done 266
#: Done 267
#: Done 268
#: Done 269
#: Done 270
#: Done 271
#: Done 272
#: Done 273
#: Done 274
#: Done 275
#: Done 276
#: Done 277
#: Done 278
#: Done 279
#: Done 280
#: Done 281
#: Done 282
#: Done 283
#: Done 284
#: Done 285
#: Done 286
#: Done 287
#: Done 288
#: Done 289
#: Done 290
#: Done 291
#: Done 292
#: Done 293
#: Done 294
#: Done 295
#: Done 296
#: Done 297
#: Done 298
#: Done 299
#: Done 300
#: Done 301
#: Done 302
#: Done 303
#: Done 304
#: Done 305
#: Done 306
#: Done 307
#: Done 308
#: Done 309
#: Done 310
#: Done 311
#: Done 312
#: Done 313
#: Done 314
#: Done 315
#: Done 316
#: Done 317
#: Done 318
#: Done 319
#: Done 320
#: Done 321
#: Done 322
#: Done 323
#: Done 324
#: Done 325
#: Done 326
#: Done 327
#: Done 328
#: Done 329
#: Done 330
#: Done 331
#: Done 332
#: Done 333
#: Done 334
#: Done 335
#: Done 336
#: Done 337
#: Done 338
#: Done 339
#: Done 340
#: Done 341
#: Done 342
#: Done 343
#: Done 344
#: Done 345
#: Done 346
#: Done 347
#: Done 348
#: Done 349
#: Done 350
#: Done 351
#: Done 352
#: Done 353
#: Done 354
#: Done 355
#: Done 356
#: Done 357
#: Done 358
#: Done 359
#: Done 360
#: Done 361
#: Done 362
#: Done 363
#: Done 364
#: Done 365
#: Done 366
#: Done 367
#: Done 368
#: Done 369
#: Done 370
#: Done 371
#: Done 372
#: Done 373
#: Done 374
#: Done 375
#: Done 376
#: Done 377
#: Done 378
#: Done 379
#: Done 380
#: Done 381
#: Done 382
#: Done 383
#: Done 384
#: Done 385
#: Done 386
#: Done 387
#: Done 388
#: Done 389
#: Done 390
#: Done 391
#: Done 392
#: Done 393
#: Done 394
#: Done 395
#: Done 396
#: Done 397
#: Done 398
#: Done 399
#: Done 400
#: Done 401
#: Done 402
#: Done 403
#: Done 404
#: Done 405
#: Done 406
#: Done 407
#: Done 408
#: Done 409
#: Done 410
#: Done 411
#: Done 412
#: Done 413
#: Done 414
#: Done 415
#: Done 416
#: Done 417
#: Done 418
#: Done 419
#: Done 420
#: Done 421
#: Done 422
#: Done 423
#: Done 424
#: Done 425
#: Done 426
#: Done 427
#: Done 428
#: Done 429
#: Done 430
#: Done 431
#: Done 432
#: Done 433
#: Done 434
#: Done 435
#: Done 436
#: Done 437
#: Done 438
#: Done 439
#: Done 440
#: Done 441
#: Done 442
#: Done 443
#: Done 444
#: Done 445
#: Done 446
#: Done 447
#: Done 448
#: Done 449
#: Done 450
#: Done 451
#: Done 452
#: Done 453
#: Done 454
#: Done 455
#: Done 456
#: Done 457
#: Done 458
#: Done 459
#: Done 460
#: Done 461
#: Done 462
#: Done 463
#: Done 464
#: Done 465
#: Done 466
#: Done 467
#: Done 468
#: Done 469
#: Done 470
#: Done 471
#: Done 472
#: Done 473
#: Done 474
#: Done 475
#: Done 476
#: Done 477
#: Done 478
#: Done 479
#: Done 480
#: Done 481
#: Done 482
#: Done 483
#: Done 484
#: Done 485
#: Done 486
#: Done 487
#: Done 488
#: Done 489
#: Done 490
#: Done 491
#: Done 492
#: Done 493
#: Done 494
#: Done 495
#: Done 496
#: Done 497
#: Done 498
#: Done 499
#: Done 500
#: Done 501
#: Done 502
#: Done 503
#: Done 504
#: Done 505
#: Done 506
#: Done 507
#: Done 508
#: Done 509
#: Done 510
#: Done 511
#: Done 512
#: Done 513
#: Done 514
#: Done 515
#: Done 516
#: Done 517
#: Done 518
#: Done 519
#: Done 520
#: Done 521
#: Done 522
#: Done 523
#: Done 524
#: Done 525
#: Done 526
#: Done 527
#: Done 528
#: Done 529
#: Done 530
#: Done 531
#: Done 532
#: Done 533
#: Done 534
#: Done 535
#: Done 536
#: Done 537
#: Done 538
#: Done 539
#: Done 540
#: Done 541
#: Done 542
#: Done 543
#: Done 544
#: Done 545
#: Done 546
#: Done 547
#: Done 548
#: Done 549
#: Done 550
#: Done 551
#: Done 552
#: Done 553
#: Done 554
#: Done 555
#: Done 556
#: Done 557
#: Done 558
#: Done 559
#: Done 560
#: Done 561
#: Done 562
#: Done 563
#: Done 564
#: Done 565
#: Done 566
#: Done 567
#: Done 568
#: Done 569
#: Done 570
#: Done 571
#: Done 572
#: Done 573
#: Done 574
#: Done 575
#: Done 576
#: Done 577
#: Done 578
#: Done 579
#: Done 580
#: Done 581
#: Done 582
#: Done 583
#: Done 584
#: Done 585
#: Done 586
#: Done 587
#: Done 588
print 'RT script done'
#: RT script done

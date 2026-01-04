# Segmenttaion

- another memory management technique
- divided into logical parts called segments instead of fixed sized

## Example

- I am having a book: chapters, sections, Index
- Each part having diffrent size  but their meanings
- Code Segment, Data Segment, Stack Segment in process

**What is Segment?**

- A logical unit of program
- Variable in size
- find it by segment number

- In Segmentation  CPU Generate Logical Address
    - Logical Address = < Segment number, Offset>
    - eg. <2, 400>
- Maintains Segment Table
- Converts into Physical Address

In Side Segment table
- SegmentNO      Base Add(Starting Phy Add)      Limit(Segment Size)
- 0              1000                                   500
- 1              3000                                   1000
- 2              5000                                   700

**Physical Address**
- 5000+400 = 5400

**Disadvantage**
- External Framentation
- complex memory allocation
- compaction needed
- slower than paging
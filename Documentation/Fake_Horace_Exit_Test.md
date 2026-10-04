# Branch-specific handover closing response

Never-met-Horace branch now uses the requested two-page Boy response:

> Another happy client, who I'm sure isn't about to betray us.

> Come on [dog's current name], let's go to that fine drinking establishment at a leisurely pace.

The existing "Okay... Horace never laughed like that. Come on, [dog]!" text
remains unchanged and is displayed only when the Horace-met flag is set.
Both responses retain the Boy theme at Y=18 and acknowledged page endings.
All preceding test-build fixes are included.

The scene's original five-byte Boy opener/display at $D6C22A calls the new
branch helper at $F7F380. It tests the native Horace-met flag ($22D9 bit 0),
shows the existing text for the met branch or the new text for the unmet
branch, then returns to the original close and scene continuation. Movement,
transfer, payment, villain dialogue and fight setup are untouched.

The added raw text is at $FA605E. Its pointer uses blank, unowned padding at
$D1FFD9 (SHOW TEXT byte offset $2FD9, logical ID 4083). This is an additional
native pointer, separate from the 3,002 existing primary entries; no existing
dialogue ID is repurposed. The native decoder confirms both pointer operands
and branch destinations. Pointer round-trip and text payload are validated
explicitly in addition to the standard primary-table audit.

ROM: `Build/Secret_of_Evermore_Casual_Run_v1.40_Fake_Horace_Exit_Test.sfc`.
Source: `Build/Secret_of_Evermore_Casual_Run_v1.40_Fake_Horace_Exit_Test.asm`.
Rebuild: `Build/build_fake_horace_exit_test.py <clean-USA-ROM>`.
SHA-256: `1102b85b9e46c883d36b126aab0b407f035e86c94d73859016dfb8c533357fb2`.

Checks passed: preceding-build reconstruction, blank/unowned allocations,
restricted ROM differences, zero source overlaps, 3,002 primary pointers,
additional pointer round-trip, exact requested wording, dynamic dog token
($82), two input waits ($86), and native branch decoding. Gameplay validation
is pending. Replay from before the closing response. Published/default release
remains v1.40.

#!/usr/bin/env python3
"""
Merge Claude settings.local.json files from multiple directories.

This script finds all .claude/settings.local.json files in a given directory,
extracts their "allow" permissions lists, merges them, and writes the result
to a new settings.local.json file.
"""

import json
import os
import sys
import argparse
from pathlib import Path
from typing import Set, List, Dict, Any


def find_settings_files(root_dir: Path) -> List[Path]:
    """
    Find all .claude/settings.local.json files in the given directory tree.
    Uses glob pattern for recursive search.

    Args:
        root_dir: Root directory to search in

    Returns:
        List of Path objects for found settings files
    """
    # Use glob pattern to recursively find all settings.local.json files
    # **/.claude/settings.local.json will match at any depth
    settings_files = list(root_dir.glob("**/.claude/settings.local.json"))

    # Sort for consistent output
    settings_files.sort()

    return settings_files


def extract_allow_permissions(file_path: Path) -> Set[str]:
    """
    Extract the "allow" permissions list from a settings.local.json file.

    Args:
        file_path: Path to the settings.local.json file

    Returns:
        Set of allowed permission strings
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        permissions = data.get("permissions", {})
        allow_list = permissions.get("allow", [])

        return set(allow_list)

    except json.JSONDecodeError as e:
        print(f"⚠️  Error parsing JSON in {file_path}: {e}", file=sys.stderr)
        return set()
    except Exception as e:
        print(f"⚠️  Error reading {file_path}: {e}", file=sys.stderr)
        return set()


def merge_permissions(settings_files: List[Path], root_dir: Path) -> Set[str]:
    """
    Merge all allow permissions from multiple settings files.

    Args:
        settings_files: List of settings file paths
        root_dir: Root directory for relative path display

    Returns:
        Set of all unique allowed permissions
    """
    all_permissions = set()

    for file_path in settings_files:
        permissions = extract_allow_permissions(file_path)
        if permissions:
            # Try to show relative path from root_dir, otherwise show absolute path
            try:
                display_path = file_path.relative_to(root_dir)
            except ValueError:
                # If file is not under root_dir, show absolute path
                display_path = file_path

            print(f"  📄 Found {len(permissions)} permissions in: {display_path}")
            all_permissions.update(permissions)

    return all_permissions


def update_settings_file(output_path: Path, permissions: Set[str]) -> None:
    """
    Update the settings.json file with merged permissions.
    Preserves existing configuration and merges with existing permissions.allow field.

    Args:
        output_path: Path where to write the output file
        permissions: Set of allowed permissions to add
    """
    try:
        # Check if the file exists and read existing content
        existing_settings = {}
        existing_allow = set()

        if output_path.exists():
            try:
                with open(output_path, "r", encoding="utf-8") as f:
                    content = f.read()

                # Try to parse JSON directly first
                try:
                    existing_settings = json.loads(content)
                except json.JSONDecodeError:
                    # If that fails, try to fix common issues like trailing commas
                    import re

                    # Remove trailing commas before ] or }
                    fixed_content = re.sub(r",\s*([}\]])", r"\1", content)
                    existing_settings = json.loads(fixed_content)
                    print(
                        f"⚠️  Fixed JSON formatting issues (trailing commas) in: {output_path}"
                    )

                print(f"📖 Reading existing settings from: {output_path}")

                # Extract existing allow permissions
                if (
                    "permissions" in existing_settings
                    and "allow" in existing_settings["permissions"]
                ):
                    existing_allow = set(existing_settings["permissions"]["allow"])
                    print(
                        f"  📋 Found {len(existing_allow)} existing allowed permissions"
                    )

            except (json.JSONDecodeError, Exception) as e:
                print(
                    f"⚠️  Warning: Could not parse existing file: {e}", file=sys.stderr
                )
                print(
                    f"  Will preserve other settings but reset permissions...",
                    file=sys.stderr,
                )

        # Ensure permissions structure exists
        if "permissions" not in existing_settings:
            existing_settings["permissions"] = {}

        # Merge existing and new permissions, removing duplicates
        merged_allow = existing_allow.union(permissions)

        # Update the allow list with sorted permissions
        existing_settings["permissions"]["allow"] = sorted(list(merged_allow))

        # Preserve deny and ask if they don't exist
        if "deny" not in existing_settings["permissions"]:
            existing_settings["permissions"]["deny"] = []
        if "ask" not in existing_settings["permissions"]:
            existing_settings["permissions"]["ask"] = []

        # Write the updated settings
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(existing_settings, f, indent=2, ensure_ascii=False)
            f.write("\n")  # Add newline at end of file

        # Report what was added
        new_permissions = permissions - existing_allow
        if new_permissions:
            print(f"\n🆕 Added {len(new_permissions)} new permissions")
        else:
            print(f"\n✔️  No new permissions to add (all already exist)")

        print(f"✅ Successfully updated settings in: {output_path}")
        print(f"   Total unique permissions: {len(merged_allow)}")

    except Exception as e:
        print(f"❌ Error writing output file: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    """Main function to run the merge process."""
    parser = argparse.ArgumentParser(
        description="Merge Claude settings.local.json files from multiple directories"
    )
    parser.add_argument(
        "directory",
        nargs="?",
        default=".",
        help="Directory to search for settings files (default: current directory)",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="conf/.claude/settings.json",
        help="Output file path (default: conf/.claude/settings.json)",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Show verbose output including all found permissions",
    )

    args = parser.parse_args()

    # Convert to Path objects
    root_dir = Path(args.directory).resolve()
    output_path = Path(args.output).resolve()

    # Validate input directory
    if not root_dir.exists():
        print(f"❌ Error: Directory '{root_dir}' does not exist", file=sys.stderr)
        sys.exit(1)

    if not root_dir.is_dir():
        print(f"❌ Error: '{root_dir}' is not a directory", file=sys.stderr)
        sys.exit(1)

    print(f"🔍 Searching for .claude/settings.local.json files in: {root_dir}")
    print("-" * 60)

    # Find all settings files
    settings_files = find_settings_files(root_dir)

    if not settings_files:
        print("⚠️  No .claude/settings.local.json files found")
        sys.exit(0)

    print(f"📁 Found {len(settings_files)} settings file(s):")

    # Merge permissions
    merged_permissions = merge_permissions(settings_files, root_dir)

    if not merged_permissions:
        print("\n⚠️  No permissions found to merge")
        sys.exit(0)

    print(f"\n📊 Total unique permissions found: {len(merged_permissions)}")

    if args.verbose:
        print("\n📋 Merged permissions list:")
        for perm in sorted(merged_permissions):
            print(f"  • {perm}")

    # Update the settings file with merged permissions
    update_settings_file(output_path, merged_permissions)

    # Print summary
    print("\n📈 Summary:")
    print(f"  • Files processed: {len(settings_files)}")
    print(f"  • Unique permissions: {len(merged_permissions)}")
    print(f"  • Output file: {output_path}")


if __name__ == "__main__":
    main()

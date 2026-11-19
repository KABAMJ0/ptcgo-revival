from ptcgo.game.data_utils import PokemonCardDef, Attack
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import snipe_attack
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.support_common import remove_self_from_play

_EXTRA_TYPES = (PokemonTypes.FIRE.value, PokemonTypes.WATER.value,
                PokemonTypes.LIGHTNING.value)


def _has_extra_triplet(ctx) -> bool:
    """1 extra Fire, Water AND Lightning Energy, each on its own unit.

    The Compendium rules a lone Rainbow Energy insufficient even though it
    provides every type at once: one unit can only cover one of the three
    requirements, so the match here gives each type a distinct Energy card."""
    pool = [{t for t in _EXTRA_TYPES if energy_provides_type(energy, t)}
            for energy in ctx.attached_energies(ctx.source)]

    def cover(index, used) -> bool:
        if index == len(_EXTRA_TYPES):
            return True
        for slot, provided in enumerate(pool):
            if slot in used or _EXTRA_TYPES[index] not in provided:
                continue
            used.add(slot)
            if cover(index + 1, used):
                return True
            used.discard(slot)
        return False

    return cover(0, set())


async def _sky_legends_gx(ctx):
    """Shuffle this Pokemon and all cards attached to it into your deck; with
    the extra Fire, Water and Lightning Energy attached, also 110 to 3 of your
    opponent's Pokemon."""
    if _has_extra_triplet(ctx):
        await snipe_attack(110, pool="any", count=3, prompt=(
            "Choose 3 of your opponent's Pokémon to take 110 damage"))(ctx)
    await remove_self_from_play(destination="deck")(ctx)


card = PokemonCardDef(
    guid="7b5f383e-6650-59c3-9de1-d12c6720a666",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MoltresZapdosArticunoGX.Name",
    display_name="Moltres & Zapdos & Articuno-GX",
    searchable_by=["Moltres & Zapdos & Articuno-GX", "Basic", "TAG TEAM", "GX", "MoltresZapdosArticunoGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=69,
    set_code="HF",
    rarity=Rarities.RareRainbow,
    hp=300,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=144,
    abilities=[
        Attack(
            title="Trinity Burn",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=210,
        ),
        Attack(
            title="Sky Legends-GX",
            game_text="Shuffle this Pok\u00e9mon and all cards attached to it into your deck. If this Pok\u00e9mon has at least 1 extra Fire, Water, and Lightning Energy attached to it (in addition to this attack's cost), this attack does 110 damage to 3 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_sky_legends_gx,
        ),
    ],
)
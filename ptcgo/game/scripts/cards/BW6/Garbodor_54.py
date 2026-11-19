from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import has_tool
from ptcgo.game.card_effects.passives_common import ability_lock_passive


def _garbotoxin_lock(pokemon, carrier):
    """Every Pokemon in play loses its Abilities while Garbodor holds a Tool;
    Garbotoxin itself is the printed exception, so the carrier is skipped.

    "in each player's hand, and in each player's discard pile" is not enforced:
    out-of-zone abilities (usable_from) are offered by legal_actions without
    consulting ability locks, and that lives in the shared library."""
    return pokemon is not carrier and has_tool(carrier)


card = PokemonCardDef(
    guid="64ecb03e-1f25-503c-a41d-0449303784ac",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Garbodor.Name",
    display_name="Garbodor",
    searchable_by=["Garbodor", "Stage 1", "Garbodor"],
    subtypes=["Stage 1"],
    collector_number=54,
    set_code="BW6",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Trubbish.Name",
    family_id=568,
    abilities=[
        Ability(
            title="Garbotoxin",
            game_text="If this Pok\u00e9mon has a Pok\u00e9mon Tool card attached to it, each Pok\u00e9mon in play, in each player's hand, and in each player's discard pile has no Abilities (except for Garbotoxin).",
            passive=ability_lock_passive(_garbotoxin_lock),
        ),
        Attack(
            title="Sludge Toss",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)

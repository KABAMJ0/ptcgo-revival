from ptcgo.game.card_effects.attacks_common import (
    damage_per, discard_defender_tools_then_damage,
)
from ptcgo.game.data_utils import PokemonCardDef, Attack
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.trainers import named_one_of

_RATTATA = named_one_of("Rattata")


def _benched_rattata_counters(ctx) -> int:
    """Damage counters on all of your Benched Rattata."""
    total = 0
    for pokemon in ctx.my_bench():
        if _RATTATA(pokemon):
            total += max(0, (ctx.max_hp(pokemon)
                             - pokemon.get_attribute(AttrID.HP, 0)) // 10)
    return total


card = PokemonCardDef(
    guid="eb9314e1-7287-5998-85b3-a9b3515e397e",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raticate.Name",
    display_name="Raticate",
    searchable_by=["Raticate", "Stage 1", "Raticate"],
    subtypes=["Stage 1"],
    collector_number=61,
    set_code="ME3",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rattata.Name",
    family_id=19,
    abilities=[
        Attack(
            title="Scrape Off",
            game_text="Before doing damage, discard all Pok\u00e9mon Tools from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=discard_defender_tools_then_damage(),
        ),
        Attack(
            title="Retaliatory Incisors",
            game_text="This attack does 40 damage for each damage counter on all of your Benched Rattata.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="x",
            effect=damage_per(_benched_rattata_counters, 40),
        ),
    ],
)
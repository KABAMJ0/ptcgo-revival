from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, def_for
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import (
    count_bench,
    damage_per,
    snipe_attack,
)


def _is_passimian(pokemon) -> bool:
    definition = def_for(getattr(pokemon, "archetype_id", None) or "")
    return getattr(definition, "display_name", None) == "Passimian"

card = PokemonCardDef(
    guid="1cf199c4-157d-511d-a13e-3514108792e7",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Passimian.Name",
    display_name="Passimian",
    searchable_by=["Passimian", "Basic", "Passimian"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=766,
    abilities=[
        Attack(
            title="Fling",
            game_text="This attack does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1},
            effect=snipe_attack(30, count=1),
        ),
        Attack(
            title="Team Play",
            game_text="This attack does 30 more damage for each of your Benched Passimian.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=damage_per(count_bench("mine", _is_passimian), 30, base=10),
        ),
    ],
)
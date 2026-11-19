from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import damage_per, damage_counters_on
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="915dfd2e-5f71-5a23-81e1-f1de51e1eb24",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Remoraid.Name",
    display_name="Remoraid",
    searchable_by=["Remoraid", "Basic", "Remoraid"],
    subtypes=["Basic"],
    collector_number=33,
    set_code="SV9",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=223,
    abilities=[
        Attack(
            title="Flail",
            game_text="This attack does 10 damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator="x",
            effect=damage_per(damage_counters_on("self"), 10, base=0),
        ),
        Attack(
            title="Rain Splash",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.card_effects.attacks_common import damage_counters_on, damage_per
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="a143f3c9-2134-5783-88ef-716d9369b982",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Duraludon.Name",
    display_name="Duraludon",
    searchable_by=["Duraludon", "Basic", "Duraludon"],
    subtypes=["Basic"],
    collector_number=106,
    set_code="SV7",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=884,
    abilities=[
        Attack(
            title="Hammer In",
            cost={PokemonTypes.METAL: 1},
            damage=30,
        ),
        Attack(
            title="Raging Hammer",
            game_text="This attack does 10 more damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=damage_per(damage_counters_on("self"), per=10, base=80),
        ),
    ],
)
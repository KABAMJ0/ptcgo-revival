from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import damage_per, damage_counters_on
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ca74d604-db83-5b3f-8359-27b39705dea2",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Duraludon.Name",
    display_name="Duraludon",
    searchable_by=["Duraludon", "Basic", "Duraludon"],
    subtypes=["Basic"],
    collector_number=69,
    set_code="SV8PT5",
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
            effect=damage_per(damage_counters_on("self"), 10, base=80),
        ),
    ],
)
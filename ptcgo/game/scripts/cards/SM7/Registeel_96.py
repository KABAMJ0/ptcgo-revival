from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="25435822-4b51-5a8e-a431-fad35991f19a",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Registeel.Name",
    display_name="Registeel",
    searchable_by=["Registeel", "Basic", "Registeel"],
    subtypes=["Basic"],
    collector_number=96,
    set_code="SM7",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=379,
    abilities=[
        Ability(
            title="Exoskeleton",
            game_text="This Pok\u00e9mon takes 20 less damage from attacks (after applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Silver Fist",
            game_text="If your opponent's Active Pok\u00e9mon has an Ability, this attack does 60 more damage.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)